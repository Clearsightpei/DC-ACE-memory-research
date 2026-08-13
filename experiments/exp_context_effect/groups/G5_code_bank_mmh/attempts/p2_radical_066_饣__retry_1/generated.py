# TRAJECTORY DIFF for p2_radical_066_饣 (retry_1)
#
# Main attempt (C verdict) — visual gaps:
#   1. Stroke 2 (top short hook): rendered as a curving line with a tiny
#      down-left flick — reads more as a comma than as a proper 横钩
#      (short horizontal into a sharp down-tick). Also placed too far
#      right/down of the visible dot in the GT (~x=145, y=112 in GT vs
#      148,132 attempt).
#   2. Stroke 3 (竖提): the "shu" body did not have a distinct corner
#      before the ti — it curved smoothly, so the reader loses the L-shape
#      that gives 饣 its lower silhouette. Also the tail did not flick
#      up-right cleanly (still angled slightly down).
#   3. Overall proportion: the bottom half was too small; the ti tail
#      needs to reach into BC-right, not stop near the C/BC boundary.
#
# Retry fixes (from errata.md hint + visual inspection):
#   - Use draw_pie from bank for stroke 1 (unchanged; it was OK).
#   - For stroke 2, render an inline **横钩** with clear geometry: short
#     horizontal from head, sharp corner, small down-left hook tip. NOT a
#     smooth arc.
#   - For stroke 3, follow errata: draw shu (vertical) from head to the
#     corner, then draw_ti from the corner to the up-right tail. This
#     gives the L-corner + rising-tail signature that 竖提 needs.
#   - Move the corner of the 竖提 further DOWN so the vertical portion
#     is dominant; extend the ti to reach x>200 (BC cell right side).
#
# BANK_DEVIATION
# used: pie.py (stroke 1, as before), shu.py + ti.py (composed for stroke 3).
# skipped: none — stroke 2 inlined because there is no 横钩 primitive
#          (would be a candidate for future promotion after PASS).
# replaced: stroke 2 inline (fresh — small heng + terminal down-tick).
# reason: 饣's stroke 2 is a compact 横钩 with sharp geometry; no bank
#         primitive currently matches. Stroke 3 now composes shu+ti to
#         give the clear L-corner the previous attempt lacked.
# fresh_component: heng_gou_short_for_饣

SELF_CHECK = {
    'visual_ok': None,           # to fill after render
    'stroke_count_ok': True,     # 3 strokes: pie, heng-gou, shu+ti (composed as 竖提)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # both joints are N-class (natural gap, not welded)
    'overall_pass': None,
    'notes': 'Stroke 3 uses shu+ti composed so corner is explicit; stroke 2 is inline 横钩 with sharp down-tick.'
}

import sys
import pathlib
from PIL import Image, ImageDraw

BANK_DIR = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK_DIR))

from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402
from ti import draw_ti    # noqa: E402


def draw_heng_gou_short(draw, head, corner, hook_tip, width=6):
    """Short 横钩: near-horizontal from head to corner, then small
    downward hook tip. Corner is sharp (not smoothed)."""
    # Segment A: head → corner (near-horizontal), slight downward drift
    n = 30
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        x0 = head[0] + (corner[0] - head[0]) * t0
        y0 = head[1] + (corner[1] - head[1]) * t0
        x1 = head[0] + (corner[0] - head[0]) * t1
        y1 = head[1] + (corner[1] - head[1]) * t1
        # taper slightly thicker toward corner
        w = width + 1 * t0
        draw.line([(x0, y0), (x1, y1)], fill='black', width=max(1, int(round(w))))
    # Sharp corner cap
    r = width // 2 + 1
    draw.ellipse([corner[0] - r, corner[1] - r, corner[0] + r, corner[1] + r], fill='black')
    # Segment B: corner → hook_tip (short down-left), tapered tip
    m = 20
    for i in range(m):
        t0, t1 = i / m, (i + 1) / m
        x0 = corner[0] + (hook_tip[0] - corner[0]) * t0
        y0 = corner[1] + (hook_tip[1] - corner[1]) * t0
        x1 = corner[0] + (hook_tip[0] - corner[0]) * t1
        y1 = corner[1] + (hook_tip[1] - corner[1]) * t1
        w = width - 3 * t0
        draw.line([(x0, y0), (x1, y1)], fill='black', width=max(1, int(round(w))))


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---------- Stroke 1: 撇 (pie) ----------
    # MMH head TC(0.447, 0.671) → tail ML(0.803, 0.995)
    # TC cell: x∈[100,200], y∈[0,100]  → head (144.7, 67.1)
    # ML cell: x∈[0,100],   y∈[100,200] → tail (80.3, 199.5)
    draw_pie(draw, head=(145, 67), tail=(78, 205),
             bow_perp=14, w_head=9, w_tail=3, steps=90)

    # ---------- Stroke 2: 横钩 (short top hook) ----------
    # MMH head C(0.43, 0.356) → tail C(0.752, 0.714)
    # C cell x∈[100,200], y∈[100,200] → head (143, 135.6), tail (175.2, 171.4)
    # Reshape as horizontal-then-downtick: head at MMH head-position,
    # corner near MMH-tail (top-right of the C cell), then hook tip
    # drops down-left from corner. Nudged up ~5 px to sit closer to
    # the GT's small dot which reads higher than the MMH midpoint suggests.
    heng_head = (146, 130)
    heng_corner = (180, 130)   # short horizontal → hard corner
    heng_hook_tip = (170, 152) # small down-left tick (hook)
    draw_heng_gou_short(draw, heng_head, heng_corner, heng_hook_tip, width=6)

    # ---------- Stroke 3: 竖提 (shu + ti, composed) ----------
    # MMH head C(0.392, 0.673) → tail BC(0.901, 0.388)
    # head (139.2, 167.3), tail (190.1, 238.8)
    # Compose: shu from head DOWN to corner (near lower part of C),
    # then ti from corner UP-RIGHT to tail (into BC-right).
    shu_head = (146, 170)
    shu_corner = (146, 232)    # corner sits at the bottom of the vertical
    draw_shu(draw, head=shu_head, tail=shu_corner, width=6)
    # ti rises from corner up-right to tail. MMH tail is at (190, 239)
    # but for a proper 竖提, the ti should end HIGHER than the corner —
    # so lift the tail Y up to ~215 (still within BC's upper band).
    ti_tail = (210, 215)
    draw_ti(draw, head=shu_corner, tail=ti_tail, w_head=8, w_tail=2)

    out = pathlib.Path(__file__).parent / '01_饣.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
