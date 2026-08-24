"""
p3_char_0325_状 — 状 = 爿 (left) + 犬 (right)
7 strokes:
  Left 爿 (3 strokes): 点/短横 top, 竖 (long vertical), 提 (bottom rising)
    - Actually GT shows: short slanted top stroke, vertical drop, short mid horizontal, then bottom
    - Standard 爿: 丶 (top-left dot/short stroke), 一 (short horizontal middle), 丨 (long vertical), 一 (bottom horizontal)
    - Actually 爿 = 4 strokes usually. Let me follow GT: top-left short 撇, vertical 竖, mid short horizontal, bottom long horizontal-提.
  Right 犬 (4 strokes): 一 (横), 丿 (撇), 乀 (捺), 丶 (点 top-right)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# ==== LEFT: 爿 ====
# Top-left short slanted stroke (撇-like)
stroke([(55, 95), (48, 130)], width=6)

# Long vertical (竖) - main spine of 爿
stroke([(70, 75), (65, 260)], width=7)

# Middle short horizontal
stroke([(70, 165), (110, 160)], width=6)

# Bottom long horizontal / 提 rising
stroke([(48, 245), (135, 225)], width=6)

# ==== RIGHT: 犬 (= 大 + 点) ====
# 横 (horizontal top)
stroke([(150, 130), (250, 125)], width=6)

# 撇 (long slanted from above 横 down to bottom-left)
# Starts a bit above the 横, crosses through it, ends bottom-left
stroke([(200, 95), (145, 265)], width=7)

# 捺 (right-down sweeping stroke starting from crossing point)
捺_pts = []
# Start near where 撇 crosses 横 (around x=195, y=130), curve down-right
for t in [i/20 for i in range(21)]:
    x = 190 + 75*t + 10*t*t
    y = 128 + 120*t + 15*t*t
    捺_pts.append((x, y))
stroke(捺_pts, width=7)

# 点 (top-right dot, small slanted mark above/right of 横)
stroke([(240, 95), (255, 115)], width=8)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0325_状/01_状.png"
img.save(out_path)
print(f"Saved {out_path}")
