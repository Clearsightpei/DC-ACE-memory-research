# p2_radical_016_刂 — 刂 (dao pang, "knife" radical, 2 strokes)
# Composition:
#   Stroke 1 (left): short 竖 — upper portion of canvas, left of center
#   Stroke 2 (right): 竖钩 — taller shaft, hook flicks up-left at bottom
#
# GT analysis (300x300):
#   Left 短竖: x ~ 125, y from ~100 (top) to ~180 (bot) => length ~80 px
#     Standalone shu is 200 px; so scale ~ 0.40 for length.
#     In math coords (center 150,150; +y up): center at (ox=-25, oy=+10),
#     half_len = 40 => scale = 40/100 = 0.40.
#   Right 竖钩: x ~ 180, y from ~80 (top) to ~230 (bot) => shaft ~150 px
#     Standalone shu_gou has shaft length 180 px (half_len=90); so scale ~ 0.83.
#     Center of shaft in math coords: (ox=+30, oy=+5) approximately
#     (canvas y 80->math +70, canvas y 230->math -80; center math +y = -5).
#
# TR1/TR6: Every primitive call is deliberately placed, transform recorded.
# TR2: 刂 is a right-radical form; components scaled down from standalone.
# TR7 mental check:
#   - Left shu: pixels (125,110) to (125,190). Upper-left slot. OK.
#   - Right shu_gou shaft: (180, 75) to (180, 235). Hook flicks to ~(160, 213).
#   - Canvas 300x300, margins ok, both strokes vertically parallel.

import sys, os
from PIL import Image, ImageDraw

# Import bank primitives
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from shu import draw_shu
from shu_gou import draw_shu_gou

W = H = 300
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)

# Revision 1: GT sits slightly right-of-center. Shift both strokes +8 px right.
# Also nudge left stub down a hair to better match GT vertical placement.
#
# Stroke 1: left short 竖
# Target: canvas x=133, y 110..185 -> math center (-17, +12), half_len=37 -> scale 0.37
draw_shu(d, ox=-17.0, oy=+12.0, scale=0.37)

# Stroke 2: right 竖钩
# Target: canvas x=188, shaft y 75..235 -> math center (+38, -5), half_len=80 -> scale ≈ 0.89
draw_shu_gou(d, ox=+38.0, oy=-5.0, scale=0.89)

out = os.path.join(os.path.dirname(__file__), "01_刂.png")
img.save(out)
print(f"wrote {out}")
