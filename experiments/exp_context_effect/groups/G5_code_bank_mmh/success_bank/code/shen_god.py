"""shen_god — 神 (shén, "spirit/god") wrapper.

Promoted B12 (2026-08-09) from p3_char_0463_神 — SOLO A verdict
(all other groups C or FAIL on the same character).

Composition: 礻 (left, 4 strokes) + 申 (right, 5 strokes) = 9 strokes.

Recipe encoded here:
- 礻 is BANK_DEVIATIONed relative to `shi_spirit.py`. shi_spirit's native
  central shu sits at x≈140; when embedded on the left of a compound
  (神/社/祈/礼/祝/福), the shu must shift ~57 px LEFT to ~x≈83. Additional
  per-stroke aspect variance (heng_pie sweep, right-dot compression) means
  no single (ox, oy, scale) fits.
  → inline via dian + heng_pie + shu + dian at compound-shifted anchors.

- 申 (right, 5 strokes) uses stroke primitives directly at MMH anchors:
  shu + heng_zhe_box + heng + heng + long central shu (piercing top+bottom).

This is a **礻-adaptation exemplar**: any downstream compound where
礻 sits on the left of a 3-cell layout (神/社/祈/福/祸/祈) can call
`draw_shen_left_hemisphere(d)` for the 礻 half at its default 57-px-shifted
position, then compose the right half from stroke primitives at
target-specific MMH anchors.

P-A-006 stroke-primitive layer + P-A-009 quantitative BANK_DEVIATION math
in the promoted attempt's docstring.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import ImageDraw  # noqa: E402
from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_pie import draw_heng_pie  # noqa: E402
from heng_zhe_box import draw_heng_zhe_box  # noqa: E402
from shu import draw_shu  # noqa: E402


def draw_shen_left_hemisphere(d, ox=0.0, oy=0.0, scale=1.0):
    """Draw the compound-left 礻 (4 strokes) at compound-shifted anchors.

    Reference anchors for 神 (x=83 central shu):
      s1 dian    (77.9, 65.9)  → (112.8,  90.2)
      s2 heng_pie(27.2,149.1)  → ( 14.9, 249.9)
      s3 shu     (82.3,190.7)  → ( 85.3, 292.7)
      s4 dian    (102.8,183.1) → (128.0, 206.5)
    """
    def T(pt):
        return (pt[0] * scale + ox, pt[1] * scale + oy)

    draw_dian(d, T((77.9, 65.9)),   T((112.8, 90.2)),  w_head=3, w_tail=7, bow=3)
    draw_heng_pie(d, T((27.2, 149.1)), T((14.9, 249.9)),
                  apex_x=95 * scale + ox, corner_x=90 * scale + ox)
    draw_shu(d, T((82.3, 190.7)), T((85.3, 292.7)), width=int(6 * scale))
    draw_dian(d, T((102.8, 183.1)), T((128.0, 206.5)), w_head=3, w_tail=7, bow=4)


def draw_shen(d, ox=0.0, oy=0.0, scale=1.0):
    """Draw the full 神 character (9 strokes) at reference anchors.

    Reference: p3_char_0463_神 (A verdict, B12). Anchors are MMH-verbatim
    on a 300x300 canvas. For downstream use in wider compositions, adjust
    ox/oy/scale or call draw_shen_left_hemisphere() for the 礻 half only.
    """
    def T(pt):
        return (pt[0] * scale + ox, pt[1] * scale + oy)

    # 礻 (left, 4 strokes)
    draw_shen_left_hemisphere(d, ox=ox, oy=oy, scale=scale)

    # 申 (right, 5 strokes) — 田-box + long central shu piercing top+bottom
    draw_shu(d, T((130.4, 138.6)), T((159.4, 220.0)), width=int(8 * scale))
    draw_heng_zhe_box(d, T((143.0, 138.9)), T((237.6, 209.5)), width=int(8 * scale))
    draw_heng(d, T((165.2, 175.2)), T((225.0, 169.6)), width_head=7, width_tail=8)
    draw_heng(d, T((163.8, 210.4)), T((225.9, 197.8)), width_head=8, width_tail=9)
    draw_shu(d, T((179.9, 68.6)),  T((194.2, 307.6)), width=int(8 * scale))


if __name__ == "__main__":
    from PIL import Image
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_shen(d)
    img.save(os.path.join(os.path.dirname(__file__), '_shen_god_ref.png'))
