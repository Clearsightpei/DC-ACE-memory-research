# BANK_DEVIATION
# skipped: la_char.py (乚 = turtle-based ya_radical)
# reason: mixing turtle with PIL for a complex character where the 乚
#         needs custom sizing/placement in a L-R layout; inlining PIL
#         gives clean control over the tall right-side hook.
# fresh_component: yi_hook_tall_LR_right (乚 tall hook for L-R right)
#
# 乿 — rare char, roughly composed of:
#   - LEFT: tangled small-strokes cluster (short pie + dots + heng-like
#           strokes stacked, evocative of a variant 幺/糸 top-heavy form)
#   - RIGHT: large tall 乚 hook (竖弯钩) spanning most of the height.
# GT observed: left is dense and taller in mid, right hook is dominant.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def line(p0, p1, w=5):
    d.line([p0, p1], fill=INK, width=w)


def dot(p, r=4):
    d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=INK)


def curve_quad(p0, p1, p2, w=5, steps=40):
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1-t)**2 * p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        line(prev, (x, y), w)
        prev = (x, y)


# ---------- LEFT component (tangled cluster) ----------
# Rough sketch based on GT visual: several short diagonals + horizontals
# The cluster occupies roughly x in [30, 155], y in [55, 265].

# Top row: a short horizontal + short pie
line((45, 75), (105, 70), w=5)              # top short heng
line((110, 60), (145, 90), w=5)             # short down-right stroke

# Second row: 3 short diagonals (like short pies stacked)
line((45, 100), (75, 115), w=4)
line((80, 100), (115, 118), w=4)
line((60, 130), (100, 145), w=4)

# Middle horizontal (spanning)
line((35, 155), (150, 152), w=5)

# Lower cluster: another set of diagonals (like a second 幺)
line((45, 175), (80, 200), w=4)
line((90, 172), (135, 195), w=4)
line((55, 210), (100, 232), w=4)

# Bottom envelope-like curve (small hook to right)
curve_quad((40, 240), (85, 275), (145, 260), w=5)

# ---------- RIGHT component: large 乚 (竖弯钩) ----------
# Starts high on the right, descends as a vertical, curves right at
# bottom, then hooks up to the right.
# vertical portion
line((205, 55), (205, 225), w=6)
# curve at the bottom transitioning to horizontal
curve_quad((205, 225), (215, 260), (260, 265), w=6)
# hook flick up at end
line((260, 265), (272, 245), w=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0578_乿/01_乿.png")
print("wrote 01_乿.png")
