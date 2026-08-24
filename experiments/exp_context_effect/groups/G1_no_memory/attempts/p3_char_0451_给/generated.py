"""G1 render of 给 (gěi) — 纟 (silk radical) on left, 合 on right."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 4

def poly(pts, w=LW):
    d.line(pts, fill="black", width=w, joint="curve")

# ---------- Left: 纟 (silk radical) ----------
# Top 撇折 — small down-left slant then fold to lower-right
poly([(90, 55), (70, 78), (95, 92)])
# Middle 撇折 — larger version
poly([(80, 100), (55, 130), (95, 148)])
# 提 — rising horizontal from lower-left to upper-right (at bottom)
poly([(45, 220), (120, 205)])
# Three small dots along the 提 tail (small strokes)
poly([(60, 195), (70, 210)])
poly([(80, 195), (90, 210)])
poly([(100, 195), (110, 210)])

# ---------- Right: 合 ----------
# 人 top: peak around (200,55) — 撇 left, 捺 right
poly([(200, 55), (155, 115)])   # 撇
poly([(200, 55), (250, 115)])   # 捺
# 一 middle horizontal (wider than the peak base)
poly([(150, 145), (255, 140)])
# 口 bottom
poly([(175, 180), (245, 180)])  # top
poly([(175, 180), (175, 235)])  # left
poly([(245, 180), (245, 235)])  # right
poly([(175, 235), (245, 235)])  # bottom

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0451_给/01_给.png")
