# 丫 (ya) — 3 strokes: left 撇 + right 短捺/点, meeting at a fork; then 竖 down.
# GT is MMH-style (thin uniform lines). Use thin widths per P12.
import sys, os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from _shared_helpers import variant_pie, variant_na, tapered_line, to_px  # noqa

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
draw = ImageDraw.Draw(img)

# --- Geometry (math coords, center=150,150, +y up) ---
# The fork (meeting apex) sits roughly at center-line horizontally,
# a bit above middle vertically (GT shows apex around y ~ +5 to +10).
apex = (0, 0)  # fork point

# Left 撇: head upper-left, tail at apex; short, slight downward curl.
pie_head = (-55, +55)
pie_tail = apex

# Right stroke: short 短捺/点 mirroring pie, head upper-right, tail at apex.
na_head = (+55, +55)
na_tail = apex

# 竖 (vertical): from apex straight down.
shu_top = apex
shu_bot = (0, -110)

# --- Render ---
# Thin uniform widths per P12 (MMH-style GT).
variant_pie(draw, head=pie_head, tail=pie_tail,
            bow_perp=-4.0, w_head=4.0, w_tail=2.0)
# Right stroke: use variant_pie mirrored (thin uniform, slight curl)
variant_pie(draw, head=na_head, tail=na_tail,
            bow_perp=+4.0, w_head=4.0, w_tail=2.0)
# Vertical shu
tapered_line(draw, shu_top, shu_bot, w0=4.0, w1=4.0)

out = os.path.join(HERE, "01_丫.png")
img.save(out)
print(f"wrote {out}")
