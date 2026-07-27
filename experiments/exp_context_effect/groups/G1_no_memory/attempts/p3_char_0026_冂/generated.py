"""Render 冂 (jiong, 'downbox' radical) at 300x300."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

INK = "black"
W = 6  # stroke width

# 冂 has 2 strokes:
# Stroke 1: Left vertical (竖) - short, starts a bit lower than top,
#           extends slightly below the right side's bottom.
# Stroke 2: Horizontal-turn-vertical (横折钩 or 横折) - top horizontal
#           turns down into the right vertical, with a small left hook at bottom.

# --- Stroke 1: left vertical ---
# GT shows the left vertical starting slightly BELOW the top horizontal
# (i.e., the top horizontal begins slightly above/left of the vertical start)
# and reaches down about the same length or slightly shorter than right side.
left_top = (78, 95)
left_bot = (75, 245)
draw.line([left_top, left_bot], fill=INK, width=W)

# --- Stroke 2: 横折 (horizontal + right vertical) ---
# Top horizontal: starts at upper-left (slightly higher than left vertical top,
# with a tiny down-tick at start typical of 起笔), extends across to the right.
# Then turns down into a vertical, ending with a small hook to the left.

# The top starts with a subtle 顿笔 tick, we approximate with a small
# angled segment then horizontal.
h_start_tick = (72, 88)   # slight left/high starting tick
h_start      = (82, 82)   # after the tick, horizontal begins
h_end        = (228, 84)  # top-right corner
v_end        = (228, 235) # bottom-right (before hook)
hook_end     = (218, 245) # tiny leftward hook at bottom-right

# starting tick (a very short down-right stroke like 顿笔)
draw.line([h_start_tick, h_start], fill=INK, width=W)
# horizontal top
draw.line([h_start, h_end], fill=INK, width=W)
# right vertical (part of 折)
draw.line([h_end, v_end], fill=INK, width=W)
# small hook at the bottom-right
draw.line([v_end, hook_end], fill=INK, width=W)

out_path = os.path.join(os.path.dirname(__file__), "01_冂.png")
img.save(out_path)
print(f"Saved: {out_path}")
