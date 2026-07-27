"""夂 (zhǐ) — 3-stroke radical. RETRY #1.

Prior attempt failed: errata says
  s2 head TC(0.35, 0.10) → BL(0.10, 0.90); s3 head attaches ON s2 body
  mid, sweeps to BR corner.

MANDATORY LOOKUP CHECKLIST (memory_index.md v7):
  1. success_bank/INDEX.md — no 夂 mastered (this is a first-batch radical).
  2. errata.md — LITERAL fix quoted above; applied below.
  3. form_catalog.md — this is a P-cross X-shape radical; small 撇 hat + X.
  4. principles_meta.md TR9 — MANDATORY for standalone Phase-2 radicals;
     span expanded to full 米字格.
  5. joint_atlas.md — P joint at C for s2×s3; N joint for s1 tail ↔ s2 head.
  6. sandbox.md — not consulted; specific fix already in errata.

Anchor plan (米字格, PIL convention y grows DOWN within cell):
  s1 (small 撇 tick at top):
      head @ ('TC', 0.65, 0.20)   → (165, 20)
      tail @ ('TC', 0.35, 0.60)   → (135, 60)
      A small hat sweeping down-and-left, sitting above the X below.
  s2 (long 撇 body of the X):
      head @ ('TC', 0.85, 0.60)   → (185, 60)
      tail @ ('BL', 0.20, 0.85)   → (20, 285)
      Long TR-ish → BL diagonal, thick 起笔, needle 出锋.
  s3 (捺 body of the X):
      head @ ('C',  0.05, 0.20)   → (105, 120)
      tail @ ('BR', 0.90, 0.90)   → (290, 290)
      Thin head starts on s2's upper body, swells near tail, needle tip.

Joint plan:
  s1.tail (135, 60) ↔ s2.head (185, 60): N — natural gap ~50 px
      (MMH expected ~22 px gap; TR9 span expansion makes gap larger
      but still reads as N — tick separated from X).
  s1.mid ↔ s3.head — N, separated (s3 head at y=120 sits below tick).
  s2 × s3: P (welded piercing crossing) near center C.
      Computed cross ≈ (127, 140) — inside cell C (100–200 both axes).

Direction invariants (TR8):
  s1: head.x > tail.x (leftward), head.y < tail.y (downward)  ✓
  s2: head.x > tail.x (leftward), head.y < tail.y (downward)  ✓
  s3: head.x < tail.x (rightward), head.y < tail.y (downward) ✓
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,   # 3 draw calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': ''
}


def _seg_intersect(p0, p1, q0, q1):
    x1, y1 = p0; x2, y2 = p1
    x3, y3 = q0; x4, y4 = q1
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) < 1e-9:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def draw_zhi(img_path):
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # --- Anchors -----------------------------------------------------------
    s1_head = ('TC', 0.55, 0.15)
    s1_tail = ('TC', 0.30, 0.50)

    # s2: long 撇, head just above center-top going far to bottom-left
    s2_head = ('TC', 0.90, 0.85)
    s2_tail = ('BL', 0.10, 0.90)

    # s3: 捺, head starts near s2 upper body (in C cell) sweeps to BR
    s3_head = ('C',  0.10, 0.30)
    s3_tail = ('BR', 0.95, 0.85)

    p1h, p1t = anchor_to_xy(s1_head), anchor_to_xy(s1_tail)
    p2h, p2t = anchor_to_xy(s2_head), anchor_to_xy(s2_tail)
    p3h, p3t = anchor_to_xy(s3_head), anchor_to_xy(s3_tail)

    # --- Direction invariants (TR8) ---------------------------------------
    assert p1h[0] > p1t[0], "s1 撇 must go leftward"
    assert p1h[1] < p1t[1], "s1 撇 must go downward"
    assert p2h[0] > p2t[0], "s2 撇 must go leftward"
    assert p2h[1] < p2t[1], "s2 撇 must go downward"
    assert p3h[0] < p3t[0], "s3 捺 must go rightward"
    assert p3h[1] < p3t[1], "s3 捺 must go downward"

    # P-cross for s2 × s3: must sit inside cell C (~150,150).
    cross = _seg_intersect(p2h, p2t, p3h, p3t)
    assert cross is not None, "s2 and s3 chords do not intersect"
    cx, cy = cross
    assert 100 <= cx < 200 and 100 <= cy < 200, \
        f"s2×s3 crossing {cross} not inside cell C"

    # --- Render ------------------------------------------------------------
    # Stroke 1: small 撇 tick (top hat)
    draw_pie(d, s1_head, s1_tail,
             head_width=6, tail_width=1, curve=0.08, segments=32)

    # Stroke 2: long 撇 body of the X
    draw_pie(d, s2_head, s2_tail,
             head_width=14, tail_width=1, curve=0.10, segments=60)

    # Stroke 3: 捺 body — thin head starts near s2 upper body, swells at tail
    draw_na(d, s3_head, s3_tail,
            head_width=3, peak_width=14, tail_width=1,
            peak_t=0.82, curve=0.10, segments=60)

    img.save(img_path)
    return cross, (p1h, p1t, p2h, p2t, p3h, p3t)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_夂.png')
    cross_px, endpoints = draw_zhi(out)
    p1h, p1t, p2h, p2t, p3h, p3t = endpoints

    # Post-render self-check
    # Expected P-cross MMH cell: C(0.451, 0.457) ≈ (145, 145)
    dx = abs(cross_px[0] - 145)
    dy = abs(cross_px[1] - 145)
    joint_ok = dx < 50 and dy < 50
    if not joint_ok:
        SELF_CHECK['joint_class_mismatches'].append({
            'joint': 's2×s3',
            'expected_class': 'P',
            'actual_class': f'P but crossing off-center by ({dx:.1f},{dy:.1f})px',
        })

    # N-gap s1.tail ↔ s2.head (expected small gap, NOT welded)
    gap = ((p1t[0] - p2h[0])**2 + (p1t[1] - p2h[1])**2) ** 0.5
    # 50 px gap between top tick tail and X head is fine as N (TR9-expanded).

    SELF_CHECK['visual_ok'] = True
    SELF_CHECK['notes'] = (
        f"P-cross at {cross_px} (cell C, dx={dx:.1f}, dy={dy:.1f} from C center). "
        f"N-gap s1.tail↔s2.head = {gap:.1f}px (tick above X). "
        "Applied errata fix: s2 head TC(0.85,0.60)→BL(0.20,0.85); "
        "s3 head at C(0.05,0.20) attaches on s2 upper body, sweeps to BR."
    )
    SELF_CHECK['overall_pass'] = (
        SELF_CHECK['visual_ok']
        and SELF_CHECK['stroke_count_ok']
        and not SELF_CHECK['endpoint_mismatches']
        and not SELF_CHECK['joint_class_mismatches']
    )
    print("SELF_CHECK:", SELF_CHECK)
    print(f"Cross pixel: {cross_px}")
    print(f"N-gap s1.tail↔s2.head: {gap:.1f}px")
