"""
Render 串 (chuan4) — two 口 boxes vertically stacked, pierced by a
central 丨 that starts above the top box and extends below the bottom
box as a tail.

Structure (7 strokes total per MMH decomposition):
  - top 口: 竖 (left), 横折 (top+right), 横 (bottom)
  - bottom 口: 竖 (left), 横折 (top+right), 横 (bottom)
  - central 丨: one long vertical piercing through both boxes

Layout in 300x300 canvas:
  - Central vertical axis at x=150.
  - Top box roughly y=55..135, width ~90.
  - Bottom box roughly y=145..225, width ~90.
  - Vertical starts at y~30 and ends at y~275 (long tail below).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # base line width for brush

def stroke(pts, width=LW):
    """Draw a polyline with rounded joints via successive line segments."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=width)
    # dab endpoints to hide seams
    for p in pts:
        r = width // 2
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=BLACK)

# --- geometry ---
cx = 150

# top box
tb_left  = 105
tb_right = 195
tb_top   = 55
tb_bot   = 138

# bottom box
bb_left  = 105
bb_right = 195
bb_top   = 152
bb_bot   = 232

# central vertical (long, pierces both, tail below)
v_top = 28
v_bot = 278

# --- draw top 口 ---
# left 竖 (top-left down)
stroke([(tb_left, tb_top), (tb_left, tb_bot)])
# 横折 (top horizontal + right vertical)
stroke([(tb_left, tb_top), (tb_right, tb_top), (tb_right, tb_bot)])
# bottom 横
stroke([(tb_left, tb_bot), (tb_right, tb_bot)])

# --- draw bottom 口 ---
stroke([(bb_left, bb_top), (bb_left, bb_bot)])
stroke([(bb_left, bb_top), (bb_right, bb_top), (bb_right, bb_bot)])
stroke([(bb_left, bb_bot), (bb_right, bb_bot)])

# --- central vertical (drawn last so it dominates) ---
stroke([(cx, v_top), (cx, v_bot)], width=LW+1)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0296_串/01_串.png"
img.save(out)
print("wrote", out)
