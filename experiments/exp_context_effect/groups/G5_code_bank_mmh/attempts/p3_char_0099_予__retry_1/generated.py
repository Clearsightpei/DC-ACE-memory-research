# TRAJECTORY DIFF (retry 1 of p3_char_0099_予)
#
# main FAIL — visual gaps:
#   1. Top strokes look like two disjoint stacked pieces with a hard
#      right-angle corner. GT shows s1 as one fluid heng-then-pie that
#      sweeps rightward AND downward as a single calligraphic gesture
#      (like the top of 又/子), not a bracket. The horiz_len=75 made s1's
#      horizontal too long and its pie too short/steep.
#   2. Middle heng (s3) has prominent bead-caps at BOTH ends (from
#      heng.py end-cap ellipses) that read as "nail heads" — width=10
#      + r2=6 caps look like beads on 300×300. GT's heng is thinner.
#   3. Vertical hook (s4) is present but the belly is anaemic and the
#      hook flick is small. GT shows a clearly bowed vertical with a
#      long, distinct left flick at the bottom. belly_right=18 too shy.
#   4. Overall vertical extent: FAIL crowds top into y=82-142 (60px)
#      then jumps to horiz at y=170. GT has better spacing top-down.
#
# Fixes this attempt:
#   - Redesign top strokes: s1 = short heng into a longer, more curved
#     pie (heng_pie_compact with narrower horiz + larger bow). s2 same.
#   - Draw s3 heng INLINE with slimmer body (width 7) and softer caps,
#     avoiding heng.py's heavy tail dot. BANK_DEVIATION on heng.
#   - Bump wan_gou belly_right to 28, hook_len to 28, hook_up to 14
#     for a more pronounced sweep-and-flick, matching GT.
#
# BANK_DEVIATION
# skipped: heng.py (for s3)
# reason: heng.py's end-cap ellipses (r=4.5 head, r=6 tail) render as
#   bead-like dots at 300×300 and mask 予's middle horizontal as
#   "dumbbell" rather than a clean stroke. Also heng_pie.py skipped
#   for s1/s2 same reason as main attempt (predates yu, tuned for 又).
# fresh_component: heng_slim (slimmer horizontal without heavy end
#   dabs, better for characters whose middle heng is a light crossbar)

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from wan_gou import draw_wan_gou


def _bezier2(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps):
        t = i / (steps - 1)
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _stamp(draw, pts, w_head, w_tail):
    n = max(len(pts) - 1, 1)
    for i, (x, y) in enumerate(pts):
        t = i / n
        w = w_head * (1 - t) + w_tail * t
        draw.ellipse([x - w, y - w, x + w, y + w], fill='black')


def draw_heng_pie_yu(draw, head, tail, horiz_len, bow_perp=14):
    """Compact heng-pie tuned for 予/矛-family tops.

    Short horizontal from head, then a curved pie sweeping down and
    slightly right-then-left toward tail. Longer/bowier than the main
    attempt's version.
    """
    hx, hy = head
    tx, ty = tail
    corner_x = hx + horiz_len
    corner_y = hy + 3

    # Segment A: short horizontal head -> corner (slim)
    steps_a = 30
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = hx + t * (corner_x - hx)
        by = hy + t * (corner_y - hy)
        w = 4.5 + 1.5 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')

    # Segment B: pie corner -> tail, bows outward (right)
    p0 = (corner_x, corner_y)
    p2 = (tx, ty)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    ctrl = (mx + px * bow_perp, my + py * bow_perp)
    pts = _bezier2(p0, ctrl, p2, steps=60)
    _stamp(draw, pts, 6.5, 1.8)


def draw_heng_slim(draw, head, tail, w_head=5.5, w_tail=6.5):
    """Slim horizontal without heavy bead caps — for light crossbars."""
    hx, hy = head
    tx, ty = tail
    steps = 80
    for i in range(steps):
        t = i / (steps - 1)
        x = hx + t * (tx - hx)
        y = hy + t * (ty - hy)
        w = w_head * (1 - t) + w_tail * t
        draw.ellipse([x - w, y - w, x + w, y + w], fill='black')
    # tiny 顿笔 at the tail — subtle, not a bead
    r = w_tail * 0.55
    draw.ellipse([tx - r, ty - r + 1, tx + r, ty + r + 1], fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: top heng-pie (upper, larger)
    # MMH: head TL(0.894,0.817)=(89.4,81.7), tail C(0.515,0.187)=(151.5,118.7)
    s1_head = (90, 82)
    s1_tail = (152, 119)
    draw_heng_pie_yu(d, s1_head, s1_tail, horiz_len=62, bow_perp=13)

    # ---- Stroke 2: second heng-pie (below s1, smaller)
    # MMH: head C(0.301,0.154)=(130.1,115.4), tail C(0.576,0.415)=(157.6,141.5)
    s2_head = (130, 115)
    s2_tail = (158, 142)
    draw_heng_pie_yu(d, s2_head, s2_tail, horiz_len=30, bow_perp=8)

    # ---- Stroke 3: middle long heng (slim, inlined)
    # MMH: head ML(0.463,0.708)=(46.3,170.8), tail MR(0.197,0.857)=(219.7,185.7)
    s3_head = (46, 171)
    s3_tail = (220, 186)
    draw_heng_slim(d, s3_head, s3_tail, w_head=5.5, w_tail=6.5)

    # ---- Stroke 4: vertical hook (wan_gou) — beefier belly + flick
    # MMH: head C(0.43,0.652)=(143.0,165.2), tail BC(0.081,0.801)=(108.1,280.1)
    s4_head = (143, 165)
    s4_tail = (108, 280)
    draw_wan_gou(d, s4_head, s4_tail,
                 belly_right=28, hook_len=28, hook_up=14,
                 w_head=5, w_body=5.5, w_tail=2)

    out = pathlib.Path(__file__).parent / '01_予.png'
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': None,          # filled after render vs GT
    'stroke_count_ok': True,    # 4 strokes: s1 heng_pie_yu, s2 heng_pie_yu,
                                # s3 heng_slim (inline), s4 wan_gou (bank)
    'endpoint_mismatches': [],  # all coords ≤ 1px from MMH after integer rounding
    'joint_class_mismatches': [], # all three joints implemented as N (natural gaps)
    'overall_pass': None,
    'notes': ('Retry 1 fix set: slimmer heng (no bead caps), longer/bowier '
              'top heng-pies, beefier wan_gou belly + flick. Joints: '
              's1.tail(152,119) ↔ s2 mid(~145,131) ~13px N ✓; '
              's2.tail(158,142) ↔ s3 mid(~133,178) ~40px N (loose but N-class); '
              's3.mid(~110,178) ↔ s4.head(143,165) ~35px N (loose but N-class).')
}


if __name__ == '__main__':
    p = render()
    print(f'wrote {p}')
