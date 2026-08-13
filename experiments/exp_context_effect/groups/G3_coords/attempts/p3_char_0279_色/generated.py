# p3_char_0279_色 — G3 attempt (revision 1)
# 色 = ⺈ (top hat) + 巴-like body. 6 strokes, thin uniform lines per GT.
# Rev1 fixes: bigger 撇, more prominent envelope sweep + upward hook,
# character centered slightly lower.

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 4


def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)


def poly(points, w=LW):
    d.line(points, fill=INK, width=w, joint="curve")


# --- Stroke 1: 撇 (top-left of ⺈ hat, slanting down-left) ---
poly([(150, 55), (132, 78), (108, 100)], w=LW)

# --- Stroke 2: 横折钩 (top hat horizontal then down + tiny left hook) ---
poly([
    (140, 62),
    (208, 64),
    (212, 68),
    (212, 138),
    (204, 143),
], w=LW)

# --- Stroke 3: 横 (middle crossbar) ---
line((98, 140), (215, 140))

# --- Stroke 4: 竖 (left vertical of body) ---
line((102, 140), (102, 232))

# --- Stroke 5: 横 (inner middle bar of body) ---
line((106, 188), (210, 188))

# --- Stroke 6: 竖弯钩 (right down, curve right along bottom, hook up) ---
poly([
    (212, 140),
    (212, 218),
    (210, 235),
    (222, 250),
    (250, 254),
    (270, 248),
    (274, 236),
    (272, 224),
], w=LW)


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_色.png")
img.save(out)
print("saved", out)
