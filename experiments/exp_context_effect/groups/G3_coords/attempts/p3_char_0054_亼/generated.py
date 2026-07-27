"""p3_char_0054_亼 — 亼 (ji) = 人-like roof (X-crossing at apex) + 一 (heng) below.

Approach:
- Roof: 人-family X-crossing (u_pie=0.0, kiss at apex). Use variant_pie +
  variant_na with kiss_apex to guarantee shared apex pixel.
- Bottom: single 一 heng, spanning canvas mid-width.
- GT is MMH-style (thin uniform lines). Per P12 candidate: use thin widths
  (w_head ~4, w_tail ~2) instead of calligraphic brush profile.
"""
import os, sys
from PIL import Image, ImageDraw

HELPERS = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                       "..", "..", "success_bank", "code"))
sys.path.insert(0, HELPERS)
from _shared_helpers import (variant_pie, variant_na, kiss_apex,
                             tapered_line, to_px)

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
draw = ImageDraw.Draw(img)

# ---- Roof (人-style X-crossing at apex) ----
# Math coords: center (150,150), +y up.
# GT apex is at roughly PIL(148,80) -> math(-2, +70)
# Pie tail lands lower-left near PIL(70,205) -> math(-80, -55)
# Na tail lands lower-right near PIL(230,200) -> math(+80, -50)
pie_head = (-2, +75)
pie_tail = (-90, -50)
na_tail  = (+90, -45)

# Kiss at apex (both heads share pie_head pixel)
pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                        u_pie=0.0, bow_pie=-6.0)

# Thin uniform widths per P12 (GT is MMH-style, thin lines).
variant_pie(draw, head=pie_h, tail=pie_tail,
            bow_perp=-6.0, w_head=4.0, w_tail=2.0)
variant_na(draw, head=na_h, tail=na_tail,
           bow_perp=+6.0, w_head=3.0, w_belly=4.0,
           w_tail=2.0, belly_u=0.7)

# ---- Bottom heng 一 ----
# GT heng roughly PIL(80,240)->(220,238) -> math(-70,-90) to (+70,-88)
heng_left  = (-70, -95)
heng_right = (+70, -93)
tapered_line(draw, heng_left, heng_right, w0=3, w1=3, n=32)

out = os.path.join(os.path.dirname(__file__), "01_亼.png")
img.save(out)
print(f"Wrote {out}")
