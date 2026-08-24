"""Render 法 as 300x300 PNG."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(pts, width=LW):
    d.line(pts, fill="black", width=width)

# --- Left: 氵 (three-water radical) ---
# top drop (short slanted stroke, upper-left)
line([(60, 90), (78, 108)], width=LW)
# middle drop
line([(50, 130), (68, 148)], width=LW)
# bottom upward tick (提)
line([(55, 200), (85, 180)], width=LW)

# --- Right: 去 ---
# top horizontal (top bar of 土)
line([(130, 95), (245, 100)], width=LW)
# vertical of 土
line([(180, 80), (180, 155)], width=LW)
# middle horizontal (bottom bar of 土, longer)
line([(120, 155), (255, 160)], width=LW)

# 厶 (bottom component): left slanted downstroke (curved feel via two segs)
line([(160, 180), (135, 220)], width=LW)
line([(135, 220), (130, 250)], width=LW)
# horizontal bottom stroke (long)
line([(120, 250), (245, 245)], width=LW)
# right slanted (dot) stroke, top-right descending to meet base
line([(200, 205), (240, 245)], width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0377_法/01_法.png")
