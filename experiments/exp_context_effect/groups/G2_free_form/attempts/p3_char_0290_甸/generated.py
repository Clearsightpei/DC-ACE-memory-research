"""
甸 (diàn) — 7 strokes: 勹 (wrap) enclosing 田 (field).

Revision: first attempt had 撇 disconnected floating high, and 田 stuck
out beneath the wrap. Move 撇 down to meet the shoulder; shrink 田 and
lift it so wrap actually encloses it; tighten hook.

Stroke order:
  1) 撇 — top-left short flick (shoulder of 勹).
  2) 横折钩 — 横 shoulder + long right-side curved 竖, hook UP-LEFT.
  3-7) 田 interior: 竖 / 横折 / 横 / 竖 / 横.

Hook rule (TIER-0-B): 横折钩 flick UP-and-LEFT (~-105°..-120°), never DOWN.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=7):
    d.line(points, fill=BLACK, width=width, joint="curve")
    for (x, y) in [points[0], points[-1]]:
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def bezier(p0, p1, p2, n=48):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


# ---------- 勹 wrap ----------

# Stroke 1: top-left 撇 — short steep, ends at the shoulder-height so
# the 横 starts near where this ends.
s1 = bezier((128, 55), (115, 72), (100, 90))
stroke(s1, width=6)

# Stroke 2: 横折钩
# 横 (top horizontal) — starts near 撇 tail, extends to right shoulder
stroke([(102, 82), (222, 72)], width=7)
# shoulder + long descending curve, bowing slightly right
descend = bezier((222, 72), (222, 175), (185, 245))
stroke(descend, width=7)
# hook flick UP-and-LEFT
stroke([(185, 245), (162, 228)], width=7)


# ---------- 田 (field) inside the wrap ----------
# Contained: x in [115, 195], y in [120, 225]
LEFT = 115
RIGHT = 195
TOP = 120
BOT = 225
MIDX = (LEFT + RIGHT) // 2
MIDY = (TOP + BOT) // 2

# Stroke 3: 竖 — left side
stroke([(LEFT, TOP), (LEFT, BOT)], width=6)

# Stroke 4: 横折 — top horizontal + right vertical
stroke([(LEFT, TOP), (RIGHT, TOP)], width=6)
stroke([(RIGHT, TOP), (RIGHT, BOT)], width=6)

# Stroke 5: 横 — middle horizontal
stroke([(LEFT, MIDY), (RIGHT, MIDY)], width=6)

# Stroke 6: 竖 — central vertical
stroke([(MIDX, TOP), (MIDX, BOT)], width=6)

# Stroke 7: 横 — bottom horizontal
stroke([(LEFT, BOT), (RIGHT, BOT)], width=6)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0290_甸/01_甸.png"
)
print("wrote 01_甸.png")
