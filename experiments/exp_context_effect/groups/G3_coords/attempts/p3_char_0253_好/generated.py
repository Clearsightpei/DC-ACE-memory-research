# p3_char_0253_好 (hǎo) — L-R compound: 女 (left) + 子 (right).
# Revision 2 after visual diff:
#   - 女's 撇点: shorten the dot bounce so V-shape reads clearly
#   - 长撇: start higher-right, sweep through V nadir
#   - 子: strengthen 横撇 top, bow 弯钩 more, keep crossbar

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)

def polyline(pts, w=LW):
    d.line(pts, fill=INK, width=w, joint="curve")

def bezier(p0, p1, p2, p3, w=LW, n=48):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    d.line(pts, fill=INK, width=w, joint="curve")

# ============================================================
# LEFT HALF: 女 (nǚ) — 3 strokes, x≈25..155, y≈85..270
# ============================================================
# Stroke 1: 撇点 — V-shape. Pie down-left, then short 点 rebound up-right.
#   Pie: (100,85) -> (48,205); Dot rebound: (48,205) -> (95,180)
bezier((100, 85), (85, 130), (65, 172), (48, 205), w=LW)
line((48, 205), (98, 178), w=LW+1)

# Stroke 2: 长撇 — long crossing pie from top-right sweeping down-left.
bezier((158, 118), (118, 168), (75, 220), (22, 272), w=LW)

# Stroke 3: 横 — horizontal crossbar at mid-height.
line((28, 205), (162, 202), w=LW)

# ============================================================
# RIGHT HALF: 子 (zǐ) — 3 strokes, x≈165..292, y≈90..270
# ============================================================
# Stroke 1: 横撇 — clear heng then diagonal down-left.
polyline([(178, 115), (262, 110), (215, 155)], w=LW)

# Stroke 2: 弯钩 — bowed descender, more pronounced curve, small hook.
bezier((248, 108), (245, 165), (218, 215), (203, 258), w=LW)
line((203, 258), (188, 250), w=LW)  # hook tip

# Stroke 3: 横 — long horizontal crossbar.
line((168, 195), (290, 192), w=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0253_好/01_好.png")
