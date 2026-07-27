"""p3_char_0231_会 — G3 attempt.

会 = 人 (roof) + 云-like body (一 + 厶-with-dot-like).

Structure from GT decomposition:
  Stroke 1: 撇 — from apex top-center down-left to lower-left area.
  Stroke 2: 捺 — from apex top-center down-right, thickening.
  Stroke 3: 横 — mid horizontal (top of 云 body).
  Stroke 4: 撇 — short pie starting mid-left going down-left.
  Stroke 5: 折 — from top of pie going right then down-left (厶 curl).
  Stroke 6: 点 — small dian inside the 厶.

Inline PIL rendering (v8 signature freedom — no bank primitive imports
needed; GT shape trumps abstraction per B5 lesson).
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(p1, p2, w=5):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(points, w=5):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=BLACK, width=w)

# --- Roof 人 (large, spans most of canvas) ---
apex = (150, 50)
# 撇: apex down-left, curving out to lower-left corner
poly([apex, (115, 100), (80, 150), (40, 195)], w=6)
# 捺: apex down-right, thickening to lower-right corner
poly([apex, (185, 100), (225, 150), (265, 195)], w=7)

# small hook / 顿笔 at apex
line((148, 40), (156, 55), w=4)

# --- 横 (mid horizontal inside the 人 roof) ---
line((70, 190), (235, 188), w=6)

# --- Second 横 (below, top edge of 厶) ---
line((95, 225), (210, 223), w=6)

# --- 厶 shape (bottom) ---
# stroke: 撇 short — goes from upper-left corner of ㄙ down-left
poly([(105, 230), (90, 260), (75, 280)], w=5)

# stroke: 折 curl — from same start going right along top then down and back left
poly([(105, 230), (200, 232), (175, 275), (130, 280)], w=5)

# stroke: 点 (small dot inside ㄙ, right side)
poly([(195, 255), (215, 278)], w=6)

# ensure output dir & save
out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_会.png")
img.save(out_path)
print(f"Saved {out_path}")
