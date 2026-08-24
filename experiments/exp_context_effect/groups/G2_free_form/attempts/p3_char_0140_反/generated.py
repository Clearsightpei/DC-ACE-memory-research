"""
反 (fǎn) — 4 strokes: 撇 (long left flick) + 横 (short top bar) +
横撇 (inside 又) + 捺 (inside 又).

Structure per GT (2026-07-24): 反 = 厂-like top-left frame + 又
inside/underneath.
- Stroke 1 (撇): long left-slanting flick from upper-mid (~x=115, y=60)
  down to lower-left (~x=55, y=270). Slight bow, tapered tail.
- Stroke 2 (横): short top horizontal bar, sits to the RIGHT of the
  撇's start; from (~x=115, y=70) to (~x=200, y=65). Very slight
  upward tilt.
- Stroke 3 (横撇 of 又): starts near mid of the 撇 body (~x=95, y=140),
  short 横 to right (~x=180, y=130), then 撇 down-left ending
  (~x=125, y=225).
- Stroke 4 (捺): starts near shoulder of stroke-3 (~x=140, y=175),
  sweeps down-right with broad flat foot ending (~x=255, y=270).

Reuses PIL brush-dab technique from drawer_memory (successful in 又,
支, etc.).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_quad_dabs(p0, p1, p2, r0, r1, steps=500):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# -----------------------------------------------------------------------------
# Stroke 1: 撇 — long left-slanting flick
# -----------------------------------------------------------------------------
# Slight bow, starts thicker at top, tapers at the tail. More pronounced
# leftward curve near the bottom (per GT).
bezier_quad_dabs((118, 55), (75, 155), (48, 275), 5.5, 1.2, steps=500)

# -----------------------------------------------------------------------------
# Stroke 2: 横 — short top horizontal bar sitting to the right of 撇 start
# -----------------------------------------------------------------------------
# Slight upward tilt: left is a bit lower than right.
line_dabs(115, 72, 205, 62, 4.5, 4.5, steps=300)
# right-end 顿笔
dab(205, 62, 5.5)

# -----------------------------------------------------------------------------
# Stroke 3: 横撇 (inside 又) — short 横 + shoulder + 撇 tail
# -----------------------------------------------------------------------------
# 3a. short 横 across mid (raised slightly)
line_dabs(95, 132, 180, 122, 4.2, 4.2, steps=300)
# 3b. shoulder 顿笔
dab(180, 122, 5.5)
# 3c. 撇 tail down-left
bezier_quad_dabs((180, 122), (150, 175), (118, 220), 4.5, 1.5, steps=500)

# -----------------------------------------------------------------------------
# Stroke 4: 捺 (inside 又) — down-right sweep with broad flat foot
# -----------------------------------------------------------------------------
# Starts near shoulder of stroke-3, thin -> thick, ends broad at lower-right.
bezier_quad_dabs((138, 158), (195, 210), (258, 265), 2.0, 7.0, steps=500)
# Broad terminal foot (捺 flat press) with slight rightward extension
for k in range(14):
    dab(258 + k * 0.5, 265 + k * 0.05, 7.0 - k * 0.4)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0140_反/01_反.png"
)
