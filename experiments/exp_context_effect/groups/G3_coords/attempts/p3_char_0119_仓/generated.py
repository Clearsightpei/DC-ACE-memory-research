"""p3_char_0119_仓 — 仓 (cang) = 人-roof + small 横折 tick + 巴-like bottom.

Revised (attempt 2) — bottom-half re-derived to match GT proportions:
- 巴 body is a small oval-ish loop tucked left-of-center
- Right shaft is a 竖弯钩 originating from top of the 巴 body,
  descending well below the body, with small rightward curve at bottom
- Small 横折 tick sits just under the roof apex

GT is MMH-style thin uniform lines.
"""
import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
HELPERS = os.path.abspath(os.path.join(HERE, "..", "..",
                                       "success_bank", "code"))
sys.path.insert(0, HELPERS)
from _shared_helpers import (variant_pie, variant_na, kiss_apex,
                             tapered_line, tapered_bezier, to_px)  # noqa: E402

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
draw = ImageDraw.Draw(img)

# ==== Strokes 1 + 2: 人-roof (撇 + 捺, kiss at apex) ====
pie_head = (+2, +95)
pie_tail = (-105, -50)
na_tail = (+95, -30)

pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                        u_pie=0.0, bow_pie=-8.0)

variant_pie(draw, head=pie_h, tail=pie_tail,
            bow_perp=-8.0, w_head=4.0, w_tail=2.0)
variant_na(draw, head=na_h, tail=na_tail,
           bow_perp=+7.0, w_head=3.0, w_belly=4.0,
           w_tail=2.0, belly_u=0.7)

# ==== Stroke 3: small 横折 tick just under the apex ====
# Very short horizontal then a small downward turn — the "middle mark".
tick_left = (-8, +25)
tick_corner = (+10, +25)
tick_end = (+8, +12)
tapered_line(draw, tick_left, tick_corner, w0=3, w1=3, n=10)
tapered_line(draw, tick_corner, tick_end, w0=3, w1=3, n=8)

# ==== Stroke 4: 巴 body + 竖弯钩 ====
# 巴 body: a small quasi-oval loop, tucked to the LEFT of center,
# roughly occupying math x=[-25,+8], y=[-45,-5].
# Left vertical of loop
loop_tl = (-25, -5)
loop_bl = (-25, -45)
tapered_line(draw, loop_tl, loop_bl, w0=3, w1=3, n=14)
# Bottom of loop (slight upward curve into right side)
loop_br = (+8, -45)
tapered_line(draw, loop_bl, loop_br, w0=3, w1=3, n=14)
# Right side of loop (short, going back up to close top)
loop_tr = (+8, -5)
tapered_line(draw, loop_br, loop_tr, w0=3, w1=3, n=14)
# Top of loop — small horizontal cap
tapered_line(draw, loop_tl, loop_tr, w0=3, w1=3, n=12)

# 竖弯钩: descends from top-right of body downward, then curves right
# with a small rightward hook. Starts higher than loop top, ends below.
shu_top = (+38, +5)
shu_bot = (+38, -75)
tapered_line(draw, shu_top, shu_bot, w0=3, w1=3, n=22)
# Curve rightward at bottom (弯钩)
curve_ctrl = (+45, -92)
curve_end = (+70, -88)
tapered_bezier(draw, shu_bot, curve_ctrl, curve_end,
               w_head=3.0, w_tail=3.0, n=24)

out = os.path.join(HERE, "01_仓.png")
img.save(out)
print(f"Wrote {out}")
