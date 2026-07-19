"""
Render 歹 (radical 090, 4画) via PIL brush-dabs on 300x300 white canvas.

Decomposition (4 strokes, per canonical MMH ordering):
  1. 横 — long top horizontal, slight up-tilt.
  2. 撇 — throws from below the 横 (upper-middle) down to lower-left.
  3. 横折钩 (or 横折) — top-short-横 + shoulder + curved 竖 forming right
     wall; belly on the LEFT (concave toward the right), so the tail
     curls inward like the right side of 夕.
  4. 点 — small teardrop dot inside the body area (mid-lower-right).

Revision notes vs pass 1:
  - Reduced top-横 endpoint 顿 dabs (r=7 -> r=6) so they don't read as knobs.
  - Flipped stroke-3 belly direction: now concave-right (belly on LEFT),
    matching 夕's characteristic right-wall curl.
  - Shrunk the 点 and moved it toward center per GT.
  - Scaled the whole radical to fill more vertical extent.

Coordinates in image-coords (y grows DOWN).
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=400, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---------- Stroke 1: 横 (top horizontal, long, slight up-tilt) ----------
h_x0, h_y0 = 35, 78
h_x1, h_y1 = 270, 64
dab(h_x0, h_y0, 6)  # modest 顿笔 start
line_taper(h_x0, h_y0, h_x1, h_y1, 5, 5, steps=300)
dab(h_x1, h_y1, 6)  # modest terminal press

# ---------- Stroke 2: 撇 (upper-middle -> lower-left) ----------
# Starts just below the 横, roughly center-left; long throw to lower-left.
p_p0 = (130, 78)
p_p2 = (40, 260)
p_p1 = (105, 160)  # gentle rightward bow (control pulled interior)
dab(p_p0[0], p_p0[1], 8)  # 顿笔 dab at start
bezier_taper(p_p0, p_p1, p_p2, r0=8, r1=1.5, steps=400, ease=1.15)

# ---------- Stroke 3: 横折 + inward-curling tail ----------
# Short 横 rightward, shoulder dab, then a curving 竖-tail with belly on
# LEFT (concave right) — the tail curls inward-left forming 夕's right wall.
sh_x0, sh_y0 = 145, 110
sh_x1, sh_y1 = 240, 100   # short 横, slightly up-tilted
line_taper(sh_x0, sh_y0, sh_x1, sh_y1, 5, 5.5, steps=200)
dab(sh_x1, sh_y1, 8)  # shoulder 顿 dab

# Curved descent: belly on left (concave-right). P0=shoulder end,
# P2=lower area (~x=150), control pulled to the LEFT to make belly-left.
d_p0 = (sh_x1, sh_y1)
d_p2 = (150, 275)
d_p1 = (170, 195)  # control pulled left of P0->P2 chord = belly on LEFT
bezier_taper(d_p0, d_p1, d_p2, r0=7, r1=1.3, steps=400, ease=1.15)

# ---------- Stroke 4: 点 (small teardrop inside body) ----------
# Compact dot placed in mid-body area under the shoulder.
dot_x0, dot_y0 = 170, 155
dot_x1, dot_y1 = 195, 185
line_taper(dot_x0, dot_y0, dot_x1, dot_y1, 2, 6, steps=150)
dab(dot_x1, dot_y1, 6)  # terminal press

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_090_歹/01_歹.png"
img.save(out_path)
print(f"saved {out_path}")
