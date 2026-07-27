# p3_char_0097_乌 (wu, crow) — 4 strokes.
# Revision 2: enlarged to fill canvas better, cleaner stroke separation.
#
# Structural decomposition of 乌 from GT:
#   1) 撇 — short slanted dash at top-left ABOVE the head-box
#   2) 横折钩 — top+right of head-box (horizontal then down with small hook)
#   3) 竖折折钩 — the compound body: down-left from head, across, then the
#      big right-side descender curving down to bottom with a hook flick
#   4) 横 — long bottom horizontal across the base
#
# Widths thin/uniform (~5px) to match MMH GT's thin lines (P12).

from PIL import Image, ImageDraw

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
t = ImageDraw.Draw(img)

W = 5


def line(a, b, w=W):
    t.line([a, b], fill=(0, 0, 0), width=w)
    r = w / 2.0
    for p in (a, b):
        t.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))


def qbez(p0, p1, p2, steps=40, w=W):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pt = (x, y)
        if prev is not None:
            line(prev, pt, w=w)
        prev = pt


# --- Stroke 1: 撇 short — slanted mark above head-box, top area ---
line((110, 45), (95, 70), w=W)

# --- Stroke 2: 横折 forming the head/eye box: top horizontal + right ---
# top of head-box: from x=90 to x=180, y around 85
line((90, 90), (185, 85), w=W)
# right side of head-box down to y=140
line((185, 85), (180, 145), w=W)
# bottom of head-box (short horizontal closing back to left)
line((180, 145), (105, 145), w=W)

# --- Stroke 3: main body 竖折折钩 ---
# Left vertical from bottom of head down to bottom of character
line((105, 145), (75, 255), w=W)
# The right-side descender: from top-right of head-box curving out and
# down to bottom-right, ending with an up-hook flick
qbez((185, 85), (240, 170), (235, 250), steps=50, w=W)
# Hook flick at bottom-right curling up-left
qbez((235, 250), (240, 270), (215, 265), steps=25, w=W)

# --- Stroke 4: bottom 横 — long horizontal across base ---
line((55, 260), (225, 258), w=W)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G3_coords/attempts/p3_char_0097_乌/01_乌.png"
)
