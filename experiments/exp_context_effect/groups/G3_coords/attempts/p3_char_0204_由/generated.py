"""
由 (yóu) — 5 strokes. Not a retry; main attempt.

Decomposition from GT PNG:
  1. 竖 — short vertical protruding upward from the top-center of the box.
  2. 竖 — left side of box (口).
  3. 横折 — top of box + right side of box (one continuous stroke).
  4. 横 — middle horizontal crossbar inside the box.
  5. 横 — bottom of box.

G3 v8: writing fresh; bank primitives are reference only. The GT
shows a slightly narrower-than-tall 口 (~90 wide × 130 tall) centered
in the lower canvas, with a ~50px vertical tail rising from the top
center. Uniform ~5px strokes matching MMH thin-line style.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6  # line width — matches GT calligraphic weight roughly

# Box geometry
box_left   = 100
box_right  = 200
box_top    = 110
box_bot    = 245

# Central vertical protrusion (goes UP from box top)
tail_top   = 55
mid_x      = (box_left + box_right) // 2  # 150

# Stroke 1: 竖 (top vertical protrusion) — from tail_top down to just past box_top
d.line([(mid_x, tail_top), (mid_x, box_top + 2)], fill=INK, width=LW)

# Stroke 2: 竖 (left side of box)
d.line([(box_left, box_top), (box_left, box_bot)], fill=INK, width=LW)

# Stroke 3: 横折 (top + right side of box). Draw as one polyline.
d.line([(box_left, box_top), (box_right, box_top), (box_right, box_bot)],
       fill=INK, width=LW, joint="curve")

# Stroke 4: 横 (middle horizontal inside box)
mid_y = (box_top + box_bot) // 2
d.line([(box_left, mid_y), (box_right, mid_y)], fill=INK, width=LW)

# Stroke 5: 横 (bottom of box)
d.line([(box_left, box_bot), (box_right, box_bot)], fill=INK, width=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_由.png"))
print("wrote", os.path.join(out_dir, "01_由.png"))
