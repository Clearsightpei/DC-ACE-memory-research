"""G1 render of 畜 (chù). Layout top-to-bottom: 亠 + 玄 middle + 田."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(x1, y1, x2, y2, w=4):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

def poly(pts, w=4):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=w)

# --- Top: 亠 (dot + long horizontal) ---
# slanted dot
line(152, 25, 162, 45, 5)
# long horizontal (wide)
line(50, 72, 250, 68, 4)

# --- Middle: 玄 (亠 style: short horizontal + 幺) ---
# short horizontal
line(115, 100, 185, 98, 4)

# 幺 top loop: small curved triangle
# down-stroke into loop
poly([(150, 100), (140, 118)], 4)
poly([(140, 118), (128, 128), (140, 138), (158, 132), (160, 120), (148, 116)], 4)

# 幺 bottom loop (slightly larger)
poly([(140, 138), (125, 148), (128, 162), (148, 165), (165, 158), (168, 145), (155, 138)], 4)

# tiny dot at bottom-right of 幺
line(170, 162, 178, 172, 4)

# --- Bottom: 田 (rectangle with internal cross) ---
left, right = 80, 220
top, bot = 180, 275

# top horizontal
line(left, top, right, top, 4)
# left vertical
line(left, top, left, bot, 4)
# right vertical (slight hook feel: extend a hair)
line(right, top, right, bot, 4)
# bottom horizontal
line(left, bot, right, bot, 4)

# internal vertical
mid_x = (left + right) // 2
line(mid_x, top, mid_x, bot, 4)
# internal horizontal
mid_y = (top + bot) // 2
line(left, mid_y, right, mid_y, 4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0506_畜/01_畜.png")
print("saved")
