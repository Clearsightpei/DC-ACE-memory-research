# p1_stroke_13_竖弯 — vertical descending then rightward horizontal
# Coordinate format: numeric offsets (no anchors, no cells, no joints).
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Stroke thickness
TH = 14

# Anchor points (numeric offsets on 300x300 canvas)
# 竖 (vertical): starts near top, descends
x_top = 130
y_top = 55
x_bot = 130
y_bot = 200  # end of vertical segment before turn

# Corner arc region (rounded turn)
turn_cx = 130 + 30   # center of arc, right of vertical line
turn_cy = 200        # aligned with bottom of vertical
arc_r = 30

# 弯 (horizontal to the right, slight upward finish typical of 竖弯)
x_end = 245
y_end = 230

# --- draw vertical segment ---
draw.line([(x_top, y_top), (x_bot, y_bot)], fill="black", width=TH)

# --- draw rounded corner (arc from bottom of vertical, curving right) ---
# arc from angle 180 (leftmost) to 90 (topmost) — quarter turn: down-left to top-right
# We want the ink to smoothly go from vertical (heading down) to horizontal (heading right).
# Use a filled pieslice-like curve via a series of small circles for smooth thickness.
import math
steps = 24
for i in range(steps + 1):
    # sweep from angle=180deg (pointing left of center = bottom of vertical)
    # to angle=270deg (pointing down of center) — actually we want:
    # start where vertical ends: point (x_bot, y_bot) is at angle 180 from (turn_cx, turn_cy)
    # end where horizontal begins: point (turn_cx, turn_cy + arc_r) is at angle 90 (below center)
    # so sweep from 180 -> 90 going clockwise-in-screen = decreasing angle in math coords
    ang_deg = 180 - (i / steps) * 90  # 180 -> 90
    ang = math.radians(ang_deg)
    px = turn_cx + arc_r * math.cos(ang)
    # screen y grows down; we want the arc to dip below turn_cy
    py = turn_cy + arc_r * math.sin(ang) * -1 + arc_r  # shift so arc bulges downward
    # simpler: use PIL-native angle convention (y-down):
    # actually just compute directly for y-down screen:
    ang2 = math.radians(180 + (i / steps) * 90)  # 180 -> 270 in PIL screen coords (going clockwise)
    px = turn_cx + arc_r * math.cos(ang2)
    py = turn_cy + arc_r * math.sin(ang2)
    r = TH // 2
    draw.ellipse([px - r, py - r, px + r, py + r], fill="black")

# --- draw horizontal segment (from end of arc rightward, with slight downward slope) ---
arc_end_x = turn_cx + arc_r * math.cos(math.radians(270))  # = turn_cx
arc_end_y = turn_cy + arc_r * math.sin(math.radians(270))  # = turn_cy - arc_r  (above)
# Actually with sin(270)=-1, arc_end_y = turn_cy - arc_r. That's ABOVE turn_cy, which is wrong direction.
# Recompute: for 竖弯, vertical goes down, then curves to horizontal going right, arc opens up-right.
# The corner is at bottom-right of the vertical: center of arc at (x_bot + arc_r, y_bot).
# Vertical ends at (x_bot, y_bot); that point is at angle 180 from center. Good.
# Horizontal starts at (x_bot + arc_r, y_bot + arc_r); that point is at angle 90 from center (y-down). Good.
# So sweep from 180 to 90 in y-down (which is counterclockwise on screen — but visually clockwise as drawn).
# Redo the loop cleanly:
turn_cx = x_bot + arc_r
turn_cy = y_bot
# clear and redo
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# vertical
draw.line([(x_top, y_top), (x_bot, y_bot)], fill="black", width=TH)

# arc: sweep angle 180deg -> 90deg (y-down system)
for i in range(steps + 1):
    ang = math.radians(180 - (i / steps) * 90)  # 180 -> 90
    px = turn_cx + arc_r * math.cos(ang)
    py = turn_cy + arc_r * math.sin(ang)
    r = TH // 2
    draw.ellipse([px - r, py - r, px + r, py + r], fill="black")

# Wait: at ang=180, cos=-1, sin=0 -> (turn_cx - arc_r, turn_cy) = (x_bot, y_bot). Good.
# At ang=90, cos=0, sin=1 -> (turn_cx, turn_cy + arc_r) = (x_bot + arc_r, y_bot + arc_r). Good.
# The arc dips DOWN and RIGHT — visually the corner of 竖弯. Perfect.

# horizontal segment: from (x_bot + arc_r, y_bot + arc_r) to (x_end, y_end)
h_start_x = x_bot + arc_r
h_start_y = y_bot + arc_r
draw.line([(h_start_x, h_start_y), (x_end, y_end)], fill="black", width=TH)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_13_竖弯/01_竖弯.png")
print("saved")
