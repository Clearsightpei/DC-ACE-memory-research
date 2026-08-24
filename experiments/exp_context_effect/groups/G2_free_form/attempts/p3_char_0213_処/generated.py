"""Render 処 at 300x300.

Revised: extend right leg of 几 further right/down; put dot-tick and
horizontal at top; make 夂 sweep tail run to bottom-left.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def line_taper(p0, p1, r0, r1, n=60):
    for i in range(n + 1):
        t = i / n
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

def bezier_taper(p0, p1, p2, r0, r1, n=120):
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

# ---- Top short tick (dot going down-right) ----
line_taper((110, 55), (128, 78), 3.0, 2.0)

# ---- Horizontal top (short, slight slope) ----
line_taper((85, 88), (150, 90), 3.5, 3.0)

# ---- Left 撇 of 夂 sweeping down-left to bottom ----
bezier_taper((140, 78), (95, 175), (45, 265), 5.5, 1.5)

# ---- Inner right diagonal (捺-like) inside 夂 body ----
line_taper((115, 130), (160, 175), 3.0, 2.5)

# ---- 几 left leg: starts high near top-right, sweeps down/curves left ----
bezier_taper((160, 85), (145, 175), (115, 265), 5.5, 2.0)

# ---- 几 top horizontal (short) ----
line_taper((160, 85), (220, 82), 4.0, 3.5)

# ---- 几 right leg 横折弯钩: comes down and sweeps out to lower-right ----
bezier_taper((220, 82), (215, 210), (285, 275), 4.5, 2.5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0213_処/01_処.png")
print("saved")
