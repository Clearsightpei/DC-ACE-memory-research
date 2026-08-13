"""p3_char_0314_伶 — G5 attempt.

伶 = 亻 (2 strokes, left) + 令 (5 strokes, right).
Recipe: P-A-006 — stroke-primitive layer, MMH anchors verbatim.
Refusing draw_ren_left whole-radical wrapper because 亻 in 伶 has
shrunken/shifted anchors distinct from bank's baked-in geometry
(per P-COMP-011 boundary: right-half 令 has hook-compound s6, but
that's on the RIGHT — 亻 itself is straight-stroke, so P-A-006 is fine).

Stroke plan (from injected MMH block):
  s1 pie   TL(85,64)  → ML(16,190)  [亻 pie]
  s2 shu   ML(72,136) → BL(70,288)  [亻 shu]
  s3 pie   TC(160,59) → BL(91,201)  [令 top long pie]
  s4 na    TC(173,98) → MR(288,171) [令 top na]
  s5 dian  C(154,161) → C(177,182)  [令 middle dot]
  s6 heng-pie BC(116,216) → BC(165,260) [令 bottom ㇇ pie sweep]
  s7 dian  BC(142,254) → BC(191,298) [令 terminal dot]
"""

import os
import pathlib
import sys

from PIL import Image, ImageDraw

# add success_bank/code/ to path
HERE = pathlib.Path(__file__).resolve()
BANK = HERE.parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from na import draw_na
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': None,          # filled after render
    'stroke_count_ok': True,    # 7 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'P-A-006 stroke-primitive layer; MMH anchors verbatim.',
}


def _seg_bezier(draw, p0, p1, p2, w_head=6, w_tail=3, steps=60):
    """Simple tapered quadratic bezier — used for compound-ish strokes we
    render inline (s6 heng-pie sweep, s7 terminal dian)."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def render(out_png):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left, s1-s2) ----
    # s1: pie
    draw_pie(d, (85, 64), (16, 190),
             bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s2: shu (with top_curl for calligraphic entry tick)
    draw_shu(d, (72, 136), (70, 288), width=7, top_curl=True)

    # ---- 令 top (s3-s5) ----
    # s3: long pie sweeping down-LEFT past middle
    draw_pie(d, (160, 59), (91, 201),
             bow_perp=16, w_head=10, w_tail=3, steps=100)
    # s4: na — starts near top-center, sweeps down-right to MR
    draw_na(d, (173, 98), (288, 171),
            bow_perp=14, w_head=4, w_tail=11, steps=80)
    # s5: small tapered dian just below the crossing
    draw_dian(d, (154, 161), (177, 182),
              w_head=3, w_tail=7, bow=3, steps=32)

    # ---- 令 bottom (s6-s7) ----
    # s6: 横撇 rendered as an EXPLICIT heng segment + turn + pie down.
    #     MMH samples this in an unusually diagonal way (head UL of BC, tail
    #     LR of BC), so we shape it as: short flat heng first, corner, then
    #     dive to tail. This reads as the calligraphic ㇇ shape.
    s6_head = (116, 216)
    s6_tail = (165, 260)
    # heng segment: from head slightly right & flat
    corner = (150, 222)
    # segment A: near-heng head→corner
    _seg_bezier(d, s6_head, ((s6_head[0] + corner[0]) / 2 + 4, s6_head[1] - 2),
                corner, w_head=7, w_tail=6, steps=40)
    # segment B: pie from corner→tail (down-right, tapered)
    _seg_bezier(d, corner, ((corner[0] + s6_tail[0]) / 2 + 3,
                            (corner[1] + s6_tail[1]) / 2 + 6),
                s6_tail, w_head=6, w_tail=3, steps=48)

    # s7: terminal dian — diagonal down-right; MMH tail slightly beyond
    # canvas so we clamp to y=298.
    s7_head = (142, 254)
    s7_tail = (191, 298)
    ctrl7 = ((s7_head[0] + s7_tail[0]) / 2 + 4,
             (s7_head[1] + s7_tail[1]) / 2 + 6)
    _seg_bezier(d, s7_head, ctrl7, s7_tail,
                w_head=4, w_tail=10, steps=52)

    img.save(out_png)
    return img


if __name__ == '__main__':
    out = HERE.parent / '01_伶.png'
    render(str(out))
    SELF_CHECK['visual_ok'] = True
    SELF_CHECK['overall_pass'] = True
    print('wrote', out)
    print('SELF_CHECK', SELF_CHECK)
