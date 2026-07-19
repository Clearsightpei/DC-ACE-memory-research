"""Deterministic structural judge for DC-ACE (run_7 prototype).

Per the project plan: CV cannot decide whether a character is calligraphically
"good", but it CAN decide deterministic structural questions:

  - Does the render have the right number of strokes?
  - Does it have the right number of connected components AFTER applying
    brush-radius topology tolerance? (i.e. small N-class gaps don't break
    connectivity, but a missing stroke or two strokes overlapping into one
    blob do break it)
  - Does the skeleton have the right number of true crossings (P-class joints)?
  - Do rendered stroke endpoints fall in the cell they were declared in?

These are mechanical checks. They do NOT score brushwork, 顿笔 strength,
hook visibility, or other aesthetic dimensions — those go to an LLM
annotator (separate, informational, NEVER gates).

Usage:
    from structural_judge import judge_cycle
    result = judge_cycle('runs/run_6/attempts/cycle_32/',
                         'runs/run_6/task_briefs/cycle_32_dataset.json')
    # result['verdict'] in {'PASS', 'FAIL'}
    # result['checks'] = dict of per-check pass/fail + numeric details

Calibration (later step): the brush_radius and tolerance dials below are
seeded with reasonable defaults. The calibration workflow renders ~80
chars, the user judges them by eye, and a sweep over these dials picks
the values that maximize user-agreement.
"""

import json
import os
import re
import sys
import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.morphology import skeletonize
from skimage.draw import line as sk_line

# Add tools dir to path so we can use the existing anchor/cell helper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anchor import xy_to_cell, CELLS
from joint_detector import find_joints, get_medians, mmh_to_canvas
from classify_joints import classify


# ─── Tunable thresholds (calibration targets) ──────────────────────────
BRUSH_RADIUS_PX = 8         # dilation radius for topology-tolerant cc count
MIN_INK_PIXELS = 200        # below = render is essentially empty
P_JOINT_TOLERANCE = 2       # |actual_junctions - expected_P_joints| <= this
ENDPOINT_TOLERANCE = 4      # |actual_endpoints - expected_endpoints| <= this
COMPONENT_TOLERANCE = 0     # must match exactly (after topology dilation)
IOU_THRESHOLD = 0.40        # topology-IoU between render and MMH GT (unused in v1)
GT_RECALL_THRESHOLD = 0.20      # min fraction of dilated-GT covered by render
GT_PRECISION_THRESHOLD = 0.40   # min fraction of render inside dilated-GT
ANCHOR_INK_RADIUS = 25          # px — declared anchor must have ink within
ANCHOR_MIN_COVERAGE = 0.75      # fraction of anchors that must have ink nearby
TRACE_TOLERANCE_PX = 12         # dilation radius for "stroke path has ink"
TRACE_PER_STROKE_MIN = 0.50     # min fraction of one stroke's path covered
TRACE_FRAC_STROKES = 0.80       # min fraction of strokes with sufficient trace


# ─── Image / topology primitives ───────────────────────────────────────

def to_binary(png_path, threshold=128):
    """Load PNG -> binary ink mask (1 = ink, 0 = bg)."""
    img = Image.open(png_path).convert('L')
    arr = np.array(img)
    return (arr < threshold).astype(np.uint8)


def connected_components_tolerant(binary, brush_radius=BRUSH_RADIUS_PX):
    """Count connected components after dilating by brush_radius.

    Two strokes whose visible ink is within ~brush_radius px of each other
    will register as one component. Larger gaps (e.g. a fully detached
    stroke per 八) stay as separate components.
    """
    if binary.sum() == 0:
        return 0
    dilated = ndimage.binary_dilation(binary, iterations=brush_radius)
    _, n = ndimage.label(dilated)
    return n


def skeleton_topology(binary):
    """Skeletonize + count 1-neighbor (endpoints) and 3+-neighbor (junctions) pixels."""
    if binary.sum() == 0:
        return 0, 0
    skel = skeletonize(binary > 0)
    if skel.sum() == 0:
        return 0, 0
    # 8-connectivity neighbor count
    kernel = np.ones((3, 3), dtype=int); kernel[1, 1] = 0
    neighbor_count = ndimage.convolve(skel.astype(int), kernel, mode='constant')
    on = skel.astype(bool)
    endpoints = int(((neighbor_count == 1) & on).sum())
    junctions = int(((neighbor_count >= 3) & on).sum())
    return junctions, endpoints


def gt_coverage(render_binary, gt_binary, brush_radius=BRUSH_RADIUS_PX):
    """How much of the (dilated) GT shape is covered by the render?

    Returns recall = |render ∩ dilated_gt| / |dilated_gt|.

    This is asymmetric on purpose: a render with EXTRA ink in the right
    places (e.g. thick brushwork over thin GT centerlines like 又, 牛)
    still gets recall close to 1. A render with ink in the WRONG places
    (e.g. broken 里 c30 — only covers part of where 里's strokes should
    be) gets low recall.
    """
    gt_dilated = ndimage.binary_dilation(gt_binary, iterations=brush_radius)
    inter = int(np.logical_and(render_binary, gt_dilated).sum())
    denom = int(gt_dilated.sum())
    return inter / denom if denom > 0 else 0.0


def gt_precision(render_binary, gt_binary, brush_radius=BRUSH_RADIUS_PX):
    """How much of the render is inside the (dilated) GT shape?

    Returns precision = |render ∩ dilated_gt| / |render|.

    A correct character: most ink is in or near the GT skeleton → high.
    A broken character placing ink in random wrong regions → low.
    """
    gt_dilated = ndimage.binary_dilation(gt_binary, iterations=brush_radius)
    inter = int(np.logical_and(render_binary, gt_dilated).sum())
    denom = int(render_binary.sum())
    return inter / denom if denom > 0 else 0.0


def anchor_to_canvas_px(anchor, canvas_w=800, canvas_h=600):
    """Convert a (cell, x_frac, y_frac) anchor to canvas pixel (px, py).
    Canvas convention: origin top-left, y grows DOWN.
    Math convention (anchor.CELLS): origin center, y grows UP.
    """
    if not (isinstance(anchor, (list, tuple)) and len(anchor) == 3):
        return None
    cell, xf, yf = anchor[0], anchor[1], anchor[2]
    if cell not in CELLS:
        return None
    xl, xr, yt, yb = CELLS[cell]
    tx = xl + xf * (xr - xl)
    ty = yt + yf * (yb - yt)
    cx, cy = canvas_w // 2, canvas_h // 2
    return int(cx + tx), int(cy - ty)


def anchor_coverage(binary, declared_anchors, radius=ANCHOR_INK_RADIUS,
                    canvas_w=800, canvas_h=600):
    """For each declared anchor point, check if any ink falls within `radius`.

    Returns (fraction_with_ink_nearby, count_total, count_missing).

    Strong signal: a broken render concentrated in one canvas region will
    miss many anchors that point elsewhere on the grid. A correct render
    will have ink near every declared anchor.
    """
    if not declared_anchors:
        return 1.0, 0, 0
    covered = 0
    missing_anchors = []
    for a in declared_anchors:
        pxpy = anchor_to_canvas_px(a, canvas_w, canvas_h)
        if pxpy is None:
            continue
        px, py = pxpy
        x0 = max(0, px - radius); x1 = min(canvas_w, px + radius)
        y0 = max(0, py - radius); y1 = min(canvas_h, py + radius)
        if x1 <= x0 or y1 <= y0:
            missing_anchors.append(a); continue
        region = binary[y0:y1, x0:x1]
        if int(region.sum()) > 0:
            covered += 1
        else:
            missing_anchors.append(a)
    total = len(declared_anchors)
    return covered / total if total else 1.0, total, missing_anchors


def canvas_math_to_pixel(canvas_x, canvas_y, w=800, h=600):
    """Math-coords (origin center, y-up) -> image pixel (origin top-left, y-down)."""
    return int(round(canvas_x + w / 2)), int(round(h / 2 - canvas_y))


def rasterize_stroke_path(canvas_pts, canvas_w=800, canvas_h=600):
    """Given a polyline of canvas math-coord points, return a binary mask
    of the line connecting them (one-pixel-wide skeleton)."""
    mask = np.zeros((canvas_h, canvas_w), dtype=np.uint8)
    if not canvas_pts:
        return mask
    px = [canvas_math_to_pixel(x, y, canvas_w, canvas_h) for x, y in canvas_pts]
    for (x0, y0), (x1, y1) in zip(px[:-1], px[1:]):
        x0 = np.clip(x0, 0, canvas_w - 1)
        y0 = np.clip(y0, 0, canvas_h - 1)
        x1 = np.clip(x1, 0, canvas_w - 1)
        y1 = np.clip(y1, 0, canvas_h - 1)
        rr, cc = sk_line(int(y0), int(x0), int(y1), int(x1))
        rr = np.clip(rr, 0, canvas_h - 1)
        cc = np.clip(cc, 0, canvas_w - 1)
        mask[rr, cc] = 1
    return mask


def stroke_trace_coverage(render_binary, char, tolerance=TRACE_TOLERANCE_PX):
    """For each MMH stroke of `char`, compute the fraction of its expected
    path that has ink within `tolerance` px in the render.

    Returns: list of per-stroke coverages (one float per stroke), plus the
    aggregate fraction-of-strokes-well-covered.
    """
    medians = get_medians(char)
    h, w = render_binary.shape
    dilated = ndimage.binary_dilation(render_binary.astype(bool), iterations=tolerance)
    coverages = []
    for stroke in medians:
        canvas_pts = [mmh_to_canvas(*p) for p in stroke]
        path = rasterize_stroke_path(canvas_pts, canvas_w=w, canvas_h=h)
        path_total = int(path.sum())
        if path_total == 0:
            coverages.append(1.0)  # degenerate — count as covered
            continue
        covered = int(np.logical_and(path > 0, dilated).sum())
        coverages.append(covered / path_total)
    return coverages


def cells_having_ink(binary, min_pixels=30, canvas_w=800, canvas_h=600):
    """Return the set of 米字格 cell names whose region has ≥ min_pixels of ink.

    The character region is the central 300×300 of the 800×600 canvas
    (anchor.CELLS coords). Each cell is 100×100 in turtle math-coords,
    which maps to 100×100 in canvas pixels at this scale.
    """
    cx, cy = canvas_w // 2, canvas_h // 2
    have = set()
    for cell, (xl, xr, yt, yb) in CELLS.items():
        # turtle math: y_top is larger; canvas pixel y is flipped
        px_left = cx + xl
        px_right = cx + xr
        # math y_top (larger) maps to smaller canvas y; math y_bot (smaller) maps to larger canvas y
        px_top = cy - yt
        px_bot = cy - yb
        px_left = max(0, int(px_left)); px_right = min(canvas_w, int(px_right))
        px_top = max(0, int(px_top));   px_bot = min(canvas_h, int(px_bot))
        if px_right <= px_left or px_bot <= px_top:
            continue
        region = binary[px_top:px_bot, px_left:px_right]
        if int(region.sum()) >= min_pixels:
            have.add(cell)
    return have


def stroke_call_count(generated_py_path):
    """Count top-level draw_<prim>(t, ...) calls inside task_01()."""
    if not os.path.exists(generated_py_path):
        return None
    code = open(generated_py_path).read()
    m = re.search(r'def task_01\([^)]*\):(.*?)def main', code, re.DOTALL)
    if not m:
        return None
    body = m.group(1)
    # Match top-level (4-space-indented) draw calls only
    return len(re.findall(r'^    draw_\w+\(', body, re.MULTILINE))


# ─── Expected-topology prediction from MMH brief ───────────────────────

def expected_component_count(n_strokes, joints):
    """Union-find: each stroke is a node, each joint merges two strokes
    into one component. Returns the number of groups after all merges."""
    parent = list(range(n_strokes + 1))   # 1-indexed
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[ra] = rb
    for j in joints:
        sa = j.get('stroke_a'); sb = j.get('stroke_b')
        if sa is None or sb is None: continue
        if 1 <= sa <= n_strokes and 1 <= sb <= n_strokes:
            union(sa, sb)
    roots = {find(i) for i in range(1, n_strokes + 1)}
    return len(roots)


def expected_p_joints(joints):
    """Count joints classified as Piercing (= true skeleton crossings)."""
    return sum(1 for j in joints if j.get('class') == 'P')


def expected_endpoints(n_strokes, joints):
    """Each stroke has 2 ends. Each joint absorbs participating endpoints
    if the joint touches a head (frac < 0.15) or tail (frac > 0.85)."""
    free_ends = 2 * n_strokes
    for j in joints:
        la = j.get('label_a', ''); lb = j.get('label_b', '')
        if la in ('head', 'tail'): free_ends -= 1
        if lb in ('head', 'tail'): free_ends -= 1
    return max(0, free_ends)


# ─── The judge ─────────────────────────────────────────────────────────

def judge_cycle(cycle_dir, brief_path,
                brush_radius=BRUSH_RADIUS_PX,
                verbose=False):
    """Apply deterministic structural checks to one cycle's render.

    Returns:
        dict with keys: char, png_path, checks (per-gate dict), verdict
        ('PASS' / 'FAIL' / 'FAIL_NO_RENDER'), fail_reasons (list of strings).
    """
    if not os.path.exists(brief_path):
        return {'verdict': 'FAIL_NO_BRIEF', 'cycle_dir': cycle_dir,
                'brief_path': brief_path}
    brief = json.load(open(brief_path))
    spec = brief['characters'][0]
    char = spec['character']
    n_strokes_expected = spec['mmh_stroke_count']

    # Derive joints from MMH directly — DON'T trust brief joint indices.
    # Old briefs (c32-c52) had off-by-one stroke_a/stroke_b serialization.
    # MMH is the ground truth for topology.
    joints_raw = find_joints(char)
    joints = []
    for j in joints_raw:
        joints.append({
            'stroke_a': j['stroke_a'], 'label_a': j['label_a'],
            'stroke_b': j['stroke_b'], 'label_b': j['label_b'],
            'cell': j['cell'], 'dist_mmh': j['dist_mmh'],
            'class': classify(j),
        })

    png_path = os.path.join(cycle_dir, f'01_{char}.png')
    gen_path = os.path.join(cycle_dir, 'generated.py')

    checks = {}
    fail_reasons = []

    # --- Check 1: stroke call count ---
    actual_calls = stroke_call_count(gen_path)
    checks['stroke_count'] = {
        'actual': actual_calls, 'expected': n_strokes_expected,
        'pass': actual_calls == n_strokes_expected
    }
    if not checks['stroke_count']['pass']:
        fail_reasons.append(
            f'stroke_count mismatch: {actual_calls} calls vs MMH {n_strokes_expected}'
        )

    # --- Load render ---
    if not os.path.exists(png_path):
        return {'char': char, 'verdict': 'FAIL_NO_RENDER',
                'cycle_dir': cycle_dir, 'checks': checks,
                'fail_reasons': ['no rendered PNG']}
    binary = to_binary(png_path)
    ink = int(binary.sum())
    checks['ink_pixels'] = {'value': ink, 'min': MIN_INK_PIXELS,
                            'pass': ink >= MIN_INK_PIXELS}
    if not checks['ink_pixels']['pass']:
        fail_reasons.append(f'render essentially empty ({ink} ink px)')
        return {'char': char, 'verdict': 'FAIL_EMPTY',
                'cycle_dir': cycle_dir, 'checks': checks,
                'fail_reasons': fail_reasons}

    # --- Check 2: connected components (topology-tolerant) ---
    actual_cc = connected_components_tolerant(binary, brush_radius)
    expected_cc = expected_component_count(n_strokes_expected, joints)
    cc_diff = abs(actual_cc - expected_cc)
    checks['components'] = {
        'actual': actual_cc, 'expected': expected_cc,
        'diff': cc_diff, 'tolerance': COMPONENT_TOLERANCE,
        'brush_radius': brush_radius,
        'pass': cc_diff <= COMPONENT_TOLERANCE
    }
    if not checks['components']['pass']:
        fail_reasons.append(
            f'connected components: got {actual_cc}, expected {expected_cc} '
            f'(brush_radius={brush_radius})'
        )

    # --- Check 3: skeleton topology (junctions ~ P joints, endpoints) ---
    junctions, endpoints = skeleton_topology(binary)
    exp_p = expected_p_joints(joints)
    exp_endpoints = expected_endpoints(n_strokes_expected, joints)
    checks['skeleton_junctions'] = {
        'actual': junctions, 'expected_P_joints': exp_p,
        'diff': abs(junctions - exp_p), 'tolerance': P_JOINT_TOLERANCE,
        'pass': abs(junctions - exp_p) <= P_JOINT_TOLERANCE
    }
    checks['skeleton_endpoints'] = {
        'actual': endpoints, 'expected': exp_endpoints,
        'diff': abs(endpoints - exp_endpoints), 'tolerance': ENDPOINT_TOLERANCE,
        'pass': abs(endpoints - exp_endpoints) <= ENDPOINT_TOLERANCE
    }
    # NOTE: skeleton junctions and endpoints are INFORMATIONAL ONLY for v1.
    # Brush dunbi / 垂露 blobs create many false junctions in the skeleton.

    # --- Check 4: IoU vs MMH ground truth (topology-tolerant) ---
    # The render and the MMH GT are both dilated by brush_radius, then
    # intersection-over-union is computed. Catches placement errors that
    # pass component-count by coincidence (broken 里 c30 has right CC
    # count because the strokes blur into one blob — but the blob is in
    # the wrong region of the canvas vs the GT).
    gt_path = os.path.join(os.path.dirname(cycle_dir), '..',
                           'ground_truths',
                           os.path.basename(cycle_dir),
                           f'01_{char}.png')
    if os.path.exists(gt_path):
        gt_binary = to_binary(gt_path)
        recall = gt_coverage(binary, gt_binary, brush_radius)
        precision = gt_precision(binary, gt_binary, brush_radius)
        checks['gt_recall'] = {
            'value': round(recall, 3),
            'threshold': GT_RECALL_THRESHOLD,
            'pass': recall >= GT_RECALL_THRESHOLD
        }
        checks['gt_precision'] = {
            'value': round(precision, 3),
            'threshold': GT_PRECISION_THRESHOLD,
            'pass': precision >= GT_PRECISION_THRESHOLD
        }
        if not checks['gt_recall']['pass']:
            fail_reasons.append(
                f'GT recall {recall:.2f} < {GT_RECALL_THRESHOLD} '
                f'(strokes missing from expected positions)'
            )
        if not checks['gt_precision']['pass']:
            fail_reasons.append(
                f'GT precision {precision:.2f} < {GT_PRECISION_THRESHOLD} '
                f'(ink in wrong canvas regions)'
            )
    else:
        checks['gt_recall'] = {'value': None, 'pass': True,
                               'note': 'no GT — skipped'}
        checks['gt_precision'] = {'value': None, 'pass': True,
                                  'note': 'no GT — skipped'}

    # --- Final verdict: stroke_count + components + GT recall + GT precision ---
    must_pass = ['stroke_count', 'components', 'gt_recall', 'gt_precision']
    verdict = 'PASS' if all(checks[k]['pass'] for k in must_pass) else 'FAIL'

    result = {
        'char': char,
        'cycle_dir': cycle_dir,
        'png_path': png_path,
        'checks': checks,
        'fail_reasons': fail_reasons,
        'verdict': verdict,
    }
    if verbose:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


# ─── CLI / test harness ────────────────────────────────────────────────

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: structural_judge.py <cycle_dir> <brief_path>')
        sys.exit(1)
    r = judge_cycle(sys.argv[1], sys.argv[2], verbose=True)
    sys.exit(0 if r.get('verdict') == 'PASS' else 1)
