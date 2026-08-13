# 佥 (qiān) — decomposition inferred from GT:
#   - Top: wide 人 roof (撇 + 捺 from apex near top-center),
#          arms spread wide, bottoming near y~205 at x~40 and x~260
#   - Under apex: short 横 in the upper-middle band (inside the roof)
#   - Below that: two small chevron pairs (从 miniature) sitting under the 一
#   - Bottom: long 横 spanning near full width
# Rendering fresh via PIL — proportions widened after first-pass self-check
# vs GT (roof was too steep/narrow; now spreads to canvas edges).

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(p0, p1, w=5):
    d.line([p0, p1], fill=BLACK, width=w)

def bezier(p0, p1, p2, w=5, steps=60):
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        line(prev, (x, y), w=w)
        prev = (x, y)

# --- Top big 人 (roof) — wider than first pass ---
apex = (150, 40)
# 撇 — sweep down-left, mild outward bow
bezier(apex, (95, 130), (40, 210), w=5)
# 捺 — sweep down-right, mild outward bow, tail slightly thicker
bezier(apex, (205, 130), (260, 210), w=5)

# --- Short 横 inside upper (the "一" closing 亼) ---
line((115, 150), (185, 150), w=4)

# --- Two small chevrons under the 一 (从 miniature) ---
# left small 人
line((110, 195), (85, 235), w=4)   # small 撇
line((110, 195), (140, 235), w=4)  # small 捺
# right small 人
line((190, 195), (165, 235), w=4)  # small 撇
line((190, 195), (220, 235), w=4)  # small 捺

# --- Bottom long 横 (spans wide) ---
line((45, 268), (255, 268), w=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0352_佥/01_佥.png")
