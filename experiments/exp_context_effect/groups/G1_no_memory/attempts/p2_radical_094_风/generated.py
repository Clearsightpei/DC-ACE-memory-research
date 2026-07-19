"""G1 render of 风 (radical, 4 strokes) — revision 1."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

def line(p0, p1, width=LW):
    draw.line([p0, p1], fill=INK, width=width)

def curve(points, width=LW):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=INK, width=width)

# GT: 风 sits roughly (70..240) x (85..250)
# Structure:
#   Stroke 1: 撇 — starts near top-left of frame (~105,95), sweeps down-left ending near (65,245)
#   Stroke 2: 横折弯钩 — top horizontal from (~105,95) rightward to (~230,100),
#             then down curving outward slightly, then back inward with a leftward hook near (~205,240)
#   Stroke 3: 撇 (inner) — from around (145,150) down-left to (~115,235)
#   Stroke 4: 乀-like curved right stroke — from around (150,160) sweeping down-right
#             and curling back left with hook tail near (~200,235)

# Stroke 1: outer 撇
s1 = []
for t in range(0, 25):
    u = t / 24.0
    # subtle curve, sweeps down and left
    x = 108 - 45 * u - 4 * (1 - (2*u - 1) ** 2)
    y = 95 + 155 * u
    s1.append((x, y))
curve(s1)

# Stroke 2a: top horizontal 横 (starts where 撇 begins, ends upper right)
line((108, 95), (228, 100))

# Stroke 2b: right side 弯 - vertical curving outward slightly then inward, ending with hook
s2 = []
for t in range(0, 32):
    u = t / 31.0
    # bulge slightly outward (right) in middle, then curve inward
    # base descent
    x = 228 + 8 * (1 - (2*u - 1) ** 2) - 25 * (u ** 2)
    y = 100 + 140 * u
    s2.append((x, y))
curve(s2)

# Hook 钩 at end of stroke 2 - short flick up-left
hook_start = s2[-1]
line(hook_start, (hook_start[0] - 20, hook_start[1] - 15))

# Stroke 3: inner 撇 (short, from upper middle going down-left)
s3 = []
for t in range(0, 20):
    u = t / 19.0
    x = 148 - 38 * u - 3 * (1 - (2*u - 1) ** 2)
    y = 145 + 95 * u
    s3.append((x, y))
curve(s3)

# Stroke 4: inner 乀 / right-curving stroke with hook tail
# Starts near top-middle where stroke 3 starts, sweeps down and right, ends with small hook
s4 = []
for t in range(0, 26):
    u = t / 25.0
    # gentle S-curve going down-right
    x = 152 + 55 * u + 5 * (u ** 2)
    y = 152 + 80 * u + 10 * (u ** 2)
    s4.append((x, y))
curve(s4)
# small hook back to the right/up at end
tail = s4[-1]
line(tail, (tail[0] + 10, tail[1] - 8))

out_path = os.path.join(os.path.dirname(__file__), "01_风.png")
img.save(out_path)
print(f"wrote {out_path}")
