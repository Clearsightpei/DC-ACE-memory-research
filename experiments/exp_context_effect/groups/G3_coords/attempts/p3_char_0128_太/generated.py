# p3_char_0128_太 (tài) — 4 strokes: 一 + 丿 + ㇏ + 丶
# Recipe: 大-family X-crossing (u_pie=0.5, crossing on heng crossbar)
# plus a small dian (丶) in the crotch between pie/na tails.
# Refs: form_catalog.md X-crossing family (line 225), wen.py, ji_meet_char.py.
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, variant_dian, kiss_apex, tapered_line,
)

CANVAS = 300


def draw_tai_char(t, ox=0, oy=0, scale=1.0):
    """Draw 太 on the given ImageDraw `t`. ox/oy shift in math coords,
    scale uniform. Bank-callable form."""
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    # -- Stroke 1: 一 (heng crossbar), medium-wide, at upper-mid.
    tapered_line(t, P(-95, +40), P(+95, +37), w0=6, w1=8, n=40)

    # -- Strokes 2 & 3: 丿 (pie) crossing ㇏ (na).
    # Pie starts above heng (right of center) and sweeps down-left to
    # bottom-left. Na starts on the pie where it crosses the heng and
    # sweeps down-right to bottom-right.
    pie_head = P(+30, +85)   # above heng, right of center
    pie_tail = P(-95, -115)  # bottom-left corner
    na_tail = P(+95, -110)   # bottom-right corner
    # Kiss where pie meets heng: pie_head y=+85, pie_tail y=-115, heng y=+37
    # → heng level along pie is at u ≈ (85-37)/(85-(-115)) = 48/200 = 0.24
    pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                            u_pie=0.24, bow_pie=-6.0)
    variant_pie(t, head=pie_h, tail=pie_tail,
                bow_perp=-6.0, w_head=8.0, w_tail=1.0)
    variant_na(t, head=na_h, tail=na_tail,
               bow_perp=+8.0, w_head=2.0, w_belly=12.0,
               w_tail=2.0, belly_u=0.72)

    # -- Stroke 4: 丶 (dian) in the crotch under the crossing, small.
    variant_dian(t, head=P(-8, -55), tail=P(+14, -78),
                 w_head=3.0, w_tail=9.0, bow_perp=-2.0)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_tai_char(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_太.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
