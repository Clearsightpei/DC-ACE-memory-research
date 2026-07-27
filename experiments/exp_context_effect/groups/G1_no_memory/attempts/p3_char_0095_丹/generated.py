"""G1 render for 丹 (p3_char_0095) — PIL, 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

# 丹 has 4 strokes:
# 1) 撇 (left curved down-stroke) — starts upper-middle, curves down-left
# 2) 横折钩 (top and right side with hook at bottom-left)
# 3) 点 (dot inside)
# 4) 一 (long horizontal through middle)

# Stroke 1: 撇 — from around (145, 60) curving down to (75, 265)
pts_pie = [(150, 55), (140, 90), (125, 130), (108, 175), (92, 220), (78, 260)]
line(pts_pie, width=6)

# Stroke 2: 横折钩 — top horizontal from (145,60) across to (215,68), then down right side to (215,255), hook left
pts_hz = [(148, 62), (180, 60), (210, 65), (218, 75), (220, 120), (220, 170), (218, 220), (212, 250), (198, 262), (180, 258)]
line(pts_hz, width=6)

# Stroke 3: 点 (dot) — small stroke inside upper area
pts_dot = [(150, 130), (165, 145)]
line(pts_dot, width=7)

# Stroke 4: 一 (long horizontal through middle) — extends slightly beyond both sides
pts_heng = [(40, 175), (100, 172), (180, 172), (255, 175)]
line(pts_heng, width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_丹.png")
img.save(out_path)
print(f"Saved {out_path}")
