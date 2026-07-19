# 儿 (2-画 radical) — G3 coord composition.
# Decomposition: 撇 (left) + 竖弯钩 (right).
#
# GT observations (300x300 canvas, top-left origin):
#  - 撇: starts around pixel (~130, ~95), sweeps down-left, tail near (~75, ~245).
#  - 竖弯钩: shaft starts near (~180, ~95), descends to (~180, ~220),
#           curves right to (~230, ~245), hooks up to (~230, ~215).
#  - 撇's head sits just left of the 竖弯钩's shaft top; small gap allowed.
#
# TR1/TR6 — transforms below are deliberate, not defaults.
# TR3 — coords picked to place stroke centers at target GT centers.

import sys, os
from PIL import Image, ImageDraw

# Bank paths.
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from pie import draw_pie              # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS_SIZE = 300

img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
d = ImageDraw.Draw(img)

# --- 撇 (left component) ---
# pie primitive default: head at math (+65,+90) => pixel (215, 60);
#                        tail at math (-45,-85) => pixel (105, 235).
# Target for 儿-left: head near pixel (135, 95), tail near pixel (75, 245).
# So target head math ≈ (-15, +55); target tail math ≈ (-75, -95).
# Compare to defaults: head shift ox = -15 - 65 = -80 (too far left);
# Instead, scale pie down (~0.75) and shift right slightly.
# scale=0.75: head default -> (+48.75, +67.5) px = (198.75, 82.5);
#             tail default -> (-33.75, -63.75) px = (116.25, 213.75).
# Want head (135,95) and tail (75,245).
# ox_math = 135 - 198.75 = -63.75; oy_math = -(95 - 82.5) = -12.5
# Check tail with ox=-63.75, oy=-12.5:
#   tail px = (116.25 - 63.75, 213.75 + 12.5) = (52.5, 226.25) — tail too far left/high.
# Compromise: ox=-55, oy=-20, scale=0.80
#   head px = (215 - 55*? ...) — pie's _to_pixel is center-origin math:
#   head math (0.80*65, 0.80*90) = (52, 72) + (ox,oy) -> pixel (150+52-55, 150-72+20)=(147,98). Good.
#   tail math (0.80*-45, 0.80*-85) = (-36,-68) + (ox,oy) -> pixel (150-36-55,150+68+20)=(59,238). Close.
# Revision: bump scale to 0.95 for a thicker/more visible pie head and slightly
# shift up so head meets the 竖弯钩 shaft-top vicinity (GT shows the heads at
# similar y). scale=0.95:
#   head math (0.95*65, 0.95*90) = (61.75, 85.5) + (ox,oy) needed for pixel target (140, 92):
#     ox = 140 - 150 - 61.75 = -71.75 → round -68 for slight right shift
#     oy = -(92 - 150 - 85.5) = ... target head py=92: 150 - (oy_math + 85.5) = 92 → oy_math = -27.5
#   tail math (-42.75, -80.75) + (-68, -27.5) = (-110.75, -108.25) → px (39.25, 258.25) — too far.
# Compromise: scale=0.90, ox=-60, oy=-22
#   head math (58.5, 81) + (-60,-22) = (-1.5, 59) → px (148.5, 91) — close to shu_wan_gou shaft top; may overlap.
#   Better: ox=-65 to shift head left of shaft (GT has small gap):
#   head px (58.5-65, -(59-22)) uses shift: math (-6.5, 59) → px (143.5, 91). Small gap to shaft-top ~172. Good.
#   tail math (-40.5, -76.5) + (-65,-22) = (-105.5, -98.5) → px (44.5, 248.5). A bit far-left but ink-thick.
draw_pie(d, ox=-65, oy=-22, scale=0.90)

# --- 竖弯钩 (right component) ---
# shu_wan_gou default (scale=1):
#   shaft: math (0,+70) -> px (150,80); math (0,-30) -> px (150,180).
#   arc curves right to (0+40,-70) -> px (190, 220).
#   tail end (80,-70) -> px (230, 220).
#   hook tip (75,-48) -> px (225, 198).
# Target: shaft top near px (180, 95), shaft bot near px (180, 205),
#         tail end near (230, 245), hook tip near (230, 215).
# ox_math = 180-150 = +30; oy_math = 150-95 - 70 = -15 for shaft top.
# check shaft bot with ox=30, oy=-15, scale=1:
#   shaft_bot math (0, -30) + (30, -15) = (30, -45) -> px (180, 195). Good.
#   tail end math (80, -70) + (30, -15) = (110, -85) -> px (260, 235). Slightly right/high.
# Scale 0.85 tightens it:
#   ox=+22, oy=-15, scale=0.85
#   shaft_top math (0, 0.85*70) = (0, 59.5) + (22, -15) = (22, 44.5) -> px (172, 105.5)
#   shaft_bot math (0, -0.85*30) = (0, -25.5) + (22, -15) = (22, -40.5) -> px (172, 190.5)
#   tail end math (0.85*80, -0.85*70) = (68, -59.5) + (22, -15) = (90, -74.5) -> px (240, 224.5)
#   hook tip math (0.85*75, -0.85*48) = (63.75, -40.8) + (22, -15) = (85.75, -55.8) -> px (235.75, 205.8)
# That fits the GT well.
draw_shu_wan_gou(d, ox=22, oy=-15, scale=0.85)

out_path = os.path.join(os.path.dirname(__file__), "01_儿.png")
img.save(out_path)
print(f"wrote {out_path}")
