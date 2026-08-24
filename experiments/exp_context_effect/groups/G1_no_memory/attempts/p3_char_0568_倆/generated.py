"""G1 render for 倆 (liǎ) — 亻 + 兩."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width)

# --- 亻 (person radical) left side ---
# Falling stroke (撇)
line([(75, 70), (55, 165)], width=4)
# Vertical (竖)
line([(72, 118), (78, 230)], width=4)

# --- 兩 (right component) ---
# Top horizontal (一)
line([(115, 78), (255, 82)], width=4)

# Left vertical of outer frame (short 竖 going down from top-left area)
line([(130, 78), (130, 100)], width=4)

# Outer frame: left vertical curving
line([(130, 100), (128, 235)], width=4)

# Outer frame: right vertical (横折钩 style — comes down then hooks)
line([(255, 82), (258, 235)], width=4)
# Hook at bottom-right
line([(258, 235), (245, 245)], width=4)

# Inner middle vertical (splits 兩 into two chambers)
line([(192, 100), (192, 235)], width=4)

# Left chamber: 人 shape inside (撇 + 捺 spreading down-outward)
line([(160, 118), (145, 200)], width=3)
line([(165, 118), (180, 200)], width=3)

# Right chamber: 人 shape inside
line([(220, 118), (208, 200)], width=3)
line([(225, 118), (240, 200)], width=3)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0568_倆/01_倆.png")
