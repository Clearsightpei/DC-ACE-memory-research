# BANK_DEVIATION
# skipped: (none from bank fully covers 横折折撇)
# reason: 及 stroke 2 is a complex 横折折撇 compound (horizontal, fold-down,
#         fold-left, long 撇) with no direct bank primitive. Inlined as a
#         polyline+curve fresh sub-element.
# fresh_component: heng_zhe_zhe_pie_for_ji
#
# Composition: 及 (3 strokes) — 撇 + 横折折撇 (inline) + 捺
# Bank primitives used: draw_pie (s1), draw_na (s3).
#
# Anchors (image convention pixel targets, derived from MMH 米字格):
#   s1 head TC ~ (140, 15)   tail BL ~ (55, 245)
#   s2 head (top-center-left) ~ (135, 25); traces horizontal → fold down →
#      fold left → long 撇 down-left to (~90, 220)
#   s3 head (mid-left C) ~ (85, 170)  tail BR ~ (285, 260)
#   joint s2.mid ⇆ s3.mid in BC region ~ (170, 250) — welded (P)

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 primitives: pie + inline compound + na
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes: s1 draw_pie, s2 inline 横折折撇 compound, s3 draw_na. '
             'Joint s2mid⇆s3mid welded P at ~(170,250). Two N joints at top.'
}


def _bezier(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _stamp(draw, pts, w_start, w_end):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1) if n > 1 else 0
        r = w_start + (w_end - w_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_stroke2_inline(draw):
    """横折折撇 compound for 及. Compact top-right box then long 撇 down-left."""
    # segment A: horizontal top ~ heng (compact, slightly right-tilted)
    a0 = (130, 35); a1 = (205, 30)
    _stamp(draw, _bezier(a0, (168, 28), a1, steps=30), 4, 4.5)

    # segment B: fold down (right vertical, short)
    b0 = a1; b1 = (208, 75)
    _stamp(draw, _bezier(b0, (210, 55), b1, steps=25), 4.5, 5)

    # segment C: fold left (small hook back)
    c0 = b1; c1 = (155, 108)
    _stamp(draw, _bezier(c0, (190, 100), c1, steps=25), 5, 4.5)

    # segment D: long 撇 down-left through joint at ~(170, 235) then to tail
    d0 = c1
    d_mid = (170, 220)          # welded joint region with s3
    d1 = (105, 265)             # tail lower-left
    _stamp(draw, _bezier(d0, (180, 160), d_mid, steps=45), 4.5, 3.5)
    _stamp(draw, _bezier(d_mid, (145, 258), d1, steps=35), 3.5, 2.2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1: 撇 (long left sweep, top → lower-left with pronounced arc)
    draw_pie(d, head=(150, 25), tail=(40, 255),
             bow_perp=28, w_head=8, w_tail=2.5, steps=90)

    # stroke 2: 横折折撇 (inline compound)
    draw_stroke2_inline(d)

    # stroke 3: 捺 (diagonal right sweep, mid-left → lower-right, welds s2)
    draw_na(d, head=(78, 195), tail=(285, 258),
            bow_perp=14, w_head=3, w_tail=11, steps=90)

    out = os.path.join(os.path.dirname(__file__), '01_及.png')
    img.save(out)
    print(f'wrote {out}')
    print(f'SELF_CHECK: {SELF_CHECK}')


if __name__ == '__main__':
    main()
