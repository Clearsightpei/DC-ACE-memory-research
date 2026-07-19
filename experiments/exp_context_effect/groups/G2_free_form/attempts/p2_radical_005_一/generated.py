"""
p2_radical_005_一  — the 一 radical (1画部首).

The GT PNG shows a horizontal stroke that:
- sits slightly below vertical midline (roughly y ~ 175 in a 300 canvas)
- has a subtle downward-then-up-tilt profile (very slight); overall reads as
  a near-uniform 横 with mild 顿 presses at both ends and a very slight
  upward end lift on the right.
- spans ~70% of the canvas width (not full-bleed), centered horizontally.

Proven Phase-1 recipe for 横 (from drawer_memory): left→right uniform brush
dabs, r ~ 5, 顿-dab (r+2) at both ends, with a small end-press. Since this
is a standalone RADICAL, per the "standalone vs compound scale-up" note,
we keep the 顿 press modest (r+1 rather than r+2) to avoid balloon-heads.

Renders black ink on 300x300 white, using PIL brush-dab technique.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- 一: horizontal stroke ---
# Anchors from GT observation: starts left-of-center at y ~180, ends right
# of center at y ~172 (very slight up-tilt to the right — canonical 横).
# Widen span a touch to match GT reach.
x0, y0 = 50, 183
x1, y1 = 250, 170

# Body: thinner uniform radius. Prior 6.5 read as heavy vs GT; drop to 5.0
# to match GT's slimmer 横 profile.
steps = 460
r_body = 5.0
for i in range(steps + 1):
    t = i / steps
    x = x0 + (x1 - x0) * t
    y = y0 + (y1 - y0) * t
    dab(x, y, r_body)

# End presses: keep VERY subtle — memory warns that r+2 becomes a visible
# ball at standalone scale. Use r+0.5 at start, r+1 at right terminal
# (canonical 横 has a slightly heavier end 顿).
dab(x0, y0, r_body + 0.5)
dab(x1, y1, r_body + 1.0)

img.save("01_一.png")
