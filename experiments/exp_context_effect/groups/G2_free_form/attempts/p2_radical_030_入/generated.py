"""Render 入 (2-stroke radical) to 300x300 PNG using PIL brush-dabs.

入 has two strokes that MEET at the top (unlike 八 where they are separate):
  1. 撇 (pie) — starts at the peak (top-center), throws down-and-left,
     thick→thin, gentle bow.
  2. 捺 (na) — starts on the 撇 body (a short way down from the peak, not
     at the peak itself — this is 入's signature vs 人), runs down-and-
     right, thin→thick, ending in a broad flat foot.

Looking at GT: the peak is near (150, 80). The 撇 sweeps down-left to
about (75, 235). The 捺 head attaches to the 撇 body around (155, 105)
(a bit below the peak) and runs to about (235, 220), with a broad foot.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(P0, P1, P2, r_start, r_end, steps=400, ease=1.0):
    """Quadratic Bezier stroke with tapered brush-dabs."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * P0[0] + 2 * u * t * P1[0] + t * t * P2[0]
        y = u * u * P0[1] + 2 * u * t * P1[1] + t * t * P2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---- Stroke 1: 撇 (pie) starting at the peak ----
# Peak sits high-center-slightly-right. Sweeps down-and-left with a
# gentle rightward bow (control point toward interior). Scale up for
# standalone canvas — fill more of the frame.
P0 = (155, 55)       # peak, top
P2 = (55, 255)       # tip, lower-left
P1 = (110, 155)      # control gives gentle bow (belly toward lower-left)
# Modest start 顿 press for standalone (r=8)
dab(P0[0], P0[1], 8)
bezier_stroke(P0, P1, P2, r_start=9, r_end=2.5, steps=500, ease=1.2)

# ---- Stroke 2: 捺 (na) attaching to the 撇 body just below the peak ----
# Key 入 signature: the 捺 starts a little way DOWN the 撇, not at the
# peak itself. This is what makes 入 read as 入 and not 人. Attach
# just slightly below the peak (~25 px down along the 撇).
Q0 = (145, 90)       # head on 撇 body (slightly below peak)
Q2 = (255, 245)      # tail, lower-right (foot)
Q1 = (185, 155)      # control giving belly on lower-left
# thin start, thickens toward foot (捺 signature)
bezier_stroke(Q0, Q1, Q2, r_start=3.5, r_end=11, steps=500, ease=0.9)
# Joining dab at attach point to hide the seam onto the 撇 body
dab(Q0[0], Q0[1], 6.5)
# terminal broad foot press
dab(Q2[0], Q2[1], 12)
# slight extension of the foot to give a broader flat terminal
for i in range(22):
    t = i / 22
    x = Q2[0] + t * 8
    y = Q2[1] + t * 2
    dab(x, y, 11 - t * 3)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_030_入/01_入.png"
)
print("wrote 01_入.png")
