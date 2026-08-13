# BANK_DEVIATION
# skipped: (no pie-zhe / 撇折 bank primitive exists) — stroke 1 of 厶 is 撇折 (pie sweeping down-left then bending into a heng going right).
# reason: bank has pie.py and heng.py separately, but no combined pie-zhe path with an interior pivot. Rather than call pie+heng as two disconnected primitives (which would leave a visible gap at the corner and mis-report stroke count), stroke 1 is inlined as one continuous path with a smooth pivot near the bottom-left corner.
# fresh_component: pie_zhe_for_si (撇折 with interior pivot at the bottom-left)
#
# For stroke 2 (dian/short-na from mid to lower-right), I use the na bank primitive with adjusted widths since it's a short taper-widening slant.

import sys, pathlib
BANK = pathlib.Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from na import draw_na


def _bezier(p0, p1, p2, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def draw_pie_zhe(draw, head, pivot, tail,
                 pie_bow=18, heng_bow=-4,
                 w_head=8, w_pivot=6, w_tail=6, steps=80):
    """Inlined pie-zhe (撇折).
    head  = top of the pie (upper-mid)
    pivot = corner at bottom-left
    tail  = end of the heng along the bottom
    pie_bow: perpendicular bow of the pie segment (positive = arches right of travel)
    heng_bow: perpendicular bow of the bottom heng segment (negative = slight rise)
    """
    # pie segment
    hx, hy = head
    px, py = pivot
    mx, my = (hx + px) / 2, (hy + py) / 2
    dx, dy = px - hx, py - hy
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    perpx, perpy = -dy / length, dx / length
    cx, cy = mx + perpx * pie_bow, my + perpy * pie_bow
    pts1 = _bezier(head, (cx, cy), pivot, steps=steps)
    n1 = len(pts1)
    for i, (x, y) in enumerate(pts1):
        t = i / (n1 - 1)
        r = w_head + (w_pivot - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')

    # heng segment from pivot to tail (slight upward-arch)
    tx, ty = tail
    mx2, my2 = (px + tx) / 2, (py + ty) / 2
    dx2, dy2 = tx - px, ty - py
    length2 = (dx2 * dx2 + dy2 * dy2) ** 0.5 or 1.0
    perpx2, perpy2 = -dy2 / length2, dx2 / length2
    cx2, cy2 = mx2 + perpx2 * heng_bow, my2 + perpy2 * heng_bow
    pts2 = _bezier(pivot, (cx2, cy2), tail, steps=steps)
    n2 = len(pts2)
    for i, (x, y) in enumerate(pts2):
        t = i / (n2 - 1)
        r = w_pivot + (w_tail - w_pivot) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # -------- Stroke 1: 撇折 (pie-zhe) --------
    # MMH endpoints: head @ ('C', 0.368, 0.002) ≈ (137, 100)
    #                tail @ ('BR', 0.13, 0.379) ≈ (213, 238)
    # The visible glyph shows a pie descending to a corner at bottom-LEFT
    # (around x=60, y=260), then a heng rising slightly rightward to the
    # tail. MMH only stores endpoint anchors, so the interior pivot is
    # inferred from the GT silhouette.
    s1_head = (137, 100)
    s1_pivot = (60, 258)
    s1_tail = (213, 238)
    draw_pie_zhe(d, s1_head, s1_pivot, s1_tail,
                 pie_bow=20, heng_bow=-3,
                 w_head=8, w_pivot=6, w_tail=5)

    # -------- Stroke 2: 点/短捺 (dian / short na) --------
    # MMH: head @ ('C', 0.866, 0.863) ≈ (187, 186)
    #      tail @ ('BR', 0.402, 0.687) ≈ (240, 269)
    s2_head = (187, 186)
    s2_tail = (240, 269)
    draw_na(d, s2_head, s2_tail, bow_perp=6, w_head=3, w_tail=9, steps=60)

    out = pathlib.Path(__file__).parent / '01_厶.png'
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': None,          # to be set after render + inspection
    'stroke_count_ok': True,    # 2 stroke calls (pie-zhe as one continuous path + na)
    'endpoint_mismatches': [],  # s1 head (137,100)=C(0.37,0.00) match; s1 tail (213,238)=BR(0.13,0.38) match
                                # s2 head (187,186)=C(0.87,0.86) match; s2 tail (240,269)=BR(0.40,0.69) match
    'joint_class_mismatches': [],  # expected N (gap ~22px) between s1.tail(213,238) and s2.mid(~223,242) — natural gap preserved
    'overall_pass': None,
    'notes': 'Bank had no pie-zhe primitive; stroke 1 inlined via draw_pie_zhe helper. Bank pie+heng could have been called separately but would leave a corner gap and inflate stroke count.'
}


if __name__ == '__main__':
    print(render())
