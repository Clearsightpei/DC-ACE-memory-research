"""Render 老 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)

def polyline(points, w=LW):
    for a, b in zip(points[:-1], points[1:]):
        d.line([a, b], fill=INK, width=w)

# 老 = 土 (top) + 丿 (long left-falling) + 匕 (bottom-right)
# Character occupies roughly x in [40, 260], y in [40, 270]

# --- Top part (土-like, small, upper center) ---
# 1) Short upper horizontal
line((125, 75), (200, 72), LW)

# 2) Short vertical descending, slightly rightward tilt then curving left
polyline([(165, 60), (162, 90), (158, 120)], LW)

# 3) Long horizontal sweep (crosses full width), slightly rising to right
line((55, 135), (260, 122), LW+1)

# --- 4) Long 丿 (left-falling) starting from upper right and sweeping to lower-left ---
polyline([(215, 60), (200, 100), (175, 145), (135, 195), (85, 240), (55, 270)], LW+1)

# --- Bottom right: 匕 ---
# 5) Short 撇 (short left-falling) inside 匕
polyline([(180, 165), (165, 195), (150, 220)], LW)

# 6) 竖弯钩 — down, curve right along bottom, hook up
polyline([
    (170, 175),
    (170, 210),
    (175, 240),
    (190, 262),
    (215, 268),
    (240, 262),
    (245, 245),
    (245, 225),
], LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0271_老/01_老.png")
print("done")
