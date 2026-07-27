# p3_char_0117_仑 — 仑 (lún), 4 strokes:
#   Top: 人-roof (撇 + 捺, kiss at apex).
#   Bottom: 匕 = 撇 + 竖弯钩 (a short leftward 撇 crossed by an L-shaped
#           down-then-right stroke ending with a small upturn hook).
#
# Reading gt/phase3/仑.png: the top 人 spans wide; apex at top-center
# around y=+85. The bottom 匕 sits under the apex — its 撇 starts inside
# the 人, curves down-left. The 竖弯钩 begins slightly right of 撇's
# start, goes down, then bends right and terminates with a small hook.
#
# Approach:
#   Stroke 1 (撇 of 人): variant_pie, thin uniform (P12 — MMH thin).
#   Stroke 2 (捺 of 人): variant_na, thin uniform.
#   Stroke 3 (撇 of 匕): variant_pie, short, mid-height.
#   Stroke 4 (竖弯钩): inline as two tapered_line segments (vertical
#     down, then horizontal right) plus a tiny upturn hook.
# kiss_apex used for the 人 apex (u_pie=0.0 style).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, kiss_apex, tapered_line, tapered_bezier,
)


def draw_lun_char(draw, ox=0, oy=0, scale=1.0):
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    # ---- TOP 人-roof ----
    pie_head = P(0, +95)
    pie_tail = P(-95, -20)
    na_tail = P(+95, -25)
    pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                            u_pie=0.0, bow_pie=-6.0)
    variant_pie(draw, head=pie_h, tail=pie_tail,
                bow_perp=-6.0, w_head=3.5, w_tail=2.0)
    variant_na(draw, head=na_h, tail=na_tail,
               bow_perp=+6.0, w_head=2.5, w_belly=3.5,
               w_tail=2.0, belly_u=0.75)

    # ---- BOTTOM 匕 ----
    # Stroke 3: 撇 of 匕 — longer and clearly visible. Starts high inside
    # the 人 (near +25), sweeps down-left to about (-45, -60).
    variant_pie(draw, head=P(+5, +25), tail=P(-50, -65),
                bow_perp=-5.0, w_head=3.0, w_tail=2.0)

    # Stroke 4: 竖弯钩 — starts on stroke 3's shaft (around its midpoint),
    # goes down vertically, bends right in a rounded elbow, ends with a
    # small upturn hook. Keep horizontal short (匕 is narrow).
    # Vertical portion:
    tapered_line(draw, P(-20, -15), P(-20, -70), w0=3.0, w1=3.0, n=20)
    # Rounded elbow into horizontal:
    tapered_bezier(draw,
                   P(-20, -70),
                   P(-20, -88),   # control: continues down
                   P(+5, -88),    # bend rightward
                   w_head=3.0, w_tail=3.0, n=24)
    # Short horizontal continuation:
    tapered_line(draw, P(+5, -88), P(+30, -85), w0=3.0, w1=3.0, n=14)
    # Small upturn hook at terminal:
    tapered_line(draw, P(+30, -85), P(+33, -75), w0=3.0, w1=2.0, n=6)


def main():
    W, H = 300, 300
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_lun_char(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_仑.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
