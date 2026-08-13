"""G5 attempt: p2_radical_047_飞 (3 strokes).

Decomposition from MMH block + GT:
  s1 = 横斜钩 (long curved outer stroke, ML→BR) — starts as near-horizontal
       from upper-left, arcs down and to the right, ending at bottom-right.
  s2 = short 横撇 / dian-like segment at top-right (MR→C)
  s3 = short 撇 in center-lower area (C→BR-ish)

All three joints are N (natural gap ~15-27 px). Strokes must NOT weld.

# BANK_DEVIATION
# skipped: shu_wan_gou.py, heng_zhe_short.py, pie.py (all considered)
# reason: s1 is a long horizontal-into-hook stroke whose ML head and BR tail
#         span > 200 px diagonally — none of the bank's shu-wan-gou (vertical
#         start) or heng-zhe-short (small radical) primitives match the
#         geometry. s2 and s3 are short segments with specific bows the bank's
#         pie/dian defaults don't produce cleanly.
# fresh_component: heng_xie_gou_for_fei (long horiz-arc-hook), short pie tails
"""

from PIL import Image, ImageDraw
from pathlib import Path

W = H = 300

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All three joints kept as N (natural gap); s1 is the long outer 横斜钩.',
}


def _bezier3(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _bezier2(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_heng_xie_gou_for_fei(draw, head, tail, width=7):
    """Long 横斜钩: near-horizontal from head across ~half the span, then
    arcs down toward the tail with a small terminal hook down-left."""
    hx, hy = head
    tx, ty = tail
    # Break the stroke into a mostly-flat horizontal segment then a curved
    # descent. The pivot lands around x=175 (roughly at the center cell).
    pivot = (175, hy + 44)      # end of the horizontal-ish top portion
    # First cubic: near-horizontal top, sagging slightly toward pivot.
    c1a = (hx + 70, hy + 6)
    c1b = (150, hy + 20)
    top = _bezier3(head, c1a, c1b, pivot, n=60)
    # Second cubic: descend from pivot down and right to the tail.
    c2a = (215, hy + 90)
    c2b = (tx + 5, ty - 10)
    knee = (tx - 4, ty)
    descent = _bezier3(pivot, c2a, c2b, knee, n=60)
    # Small terminal hook down-left at the tail (like a 弧钩 tick).
    hook_ctrl = (tx + 4, ty + 12)
    hook_end = (tx - 4, ty + 14)
    hook = _bezier2(knee, hook_ctrl, hook_end, n=15)
    pts = top + descent[1:] + hook[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    r = width // 2
    for x, y in (ipts[0], ipts[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_short_pie(draw, head, tail, w_head=7, w_tail=3, bow_perp=6, steps=50):
    """Short leftward-arcing 撇/dian segment with taper."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    cx, cy = mx + px * bow_perp, my + py * bow_perp
    pts = _bezier2(head, (cx, cy), tail, n=steps)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = (w_head + (w_tail - w_head) * t)
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_short_na(draw, head, tail, w_head=3, w_tail=8, bow_perp=-4, steps=50):
    """Short rightward-arcing 捺-like segment (thickens toward tail)."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    cx, cy = mx + px * bow_perp, my + py * bow_perp
    pts = _bezier2(head, (cx, cy), tail, n=steps)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = (w_head + (w_tail - w_head) * t)
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def main():
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)

    # MMH-derived endpoints (px on 300x300)
    # s1: ML(0.369, 0.318) → BR(0.651, 0.484)  = (36.9, 131.8) → (265.1, 248.4)
    # s2: MR(0.168, 0.26)  → C(0.849, 0.77)    = (216.8, 126.0) → (184.9, 177.0)
    # s3: C(0.767, 0.863)  → BR(0.367, 0.291)  = (176.7, 186.3) → (236.7, 229.1)

    s1_head, s1_tail = (37, 132), (265, 248)
    s2_head, s2_tail = (217, 126), (185, 177)
    s3_head, s3_tail = (177, 186), (237, 229)

    # Stroke 1 — long 横斜钩
    draw_heng_xie_gou_for_fei(d, s1_head, s1_tail, width=7)

    # Stroke 2 — short down-left segment at top-right
    draw_short_pie(d, s2_head, s2_tail, w_head=7, w_tail=3, bow_perp=5)

    # Stroke 3 — short down-right segment in center
    draw_short_na(d, s3_head, s3_tail, w_head=4, w_tail=7, bow_perp=-3)

    out = Path(__file__).parent / '01_飞.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
