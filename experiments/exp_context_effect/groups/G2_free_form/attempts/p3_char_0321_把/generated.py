"""
p3_char_0321_把 — 扌 (hand radical) + 巴

# SIGNATURE CHECK (from sibling family 巴/也/己):
#   巴 body MUST have:
#     - middle 横 FLOATS on BOTH sides (does not touch left 竖 nor right side)
#     - bottom is 竖弯钩 SWEEP (curve going down then right then hook UP-LEFT),
#       NOT a geometric 冂 box (this is the errata failure mode for 也/巴 family).
#   TIER-0 hook rule: all hook flicks go UP-and-LEFT (~-105° to -120°).

# Structure:
#   Left: 扌 (raise-hand radical) — 3 strokes
#     1. 短横 (short horizontal, slight upward tilt)
#     2. 长竖钩 (long vertical, hook flicks UP-LEFT at bottom)
#     3. 提 (rising tick from lower-left up through the 竖)
#   Right: 巴 — 4 strokes
#     4. 竖 (left vertical of 巴, short — top portion only)
#     5. 横折 (top horizontal + right side down)
#     6. 横 (middle, FLOATS both sides)
#     7. 竖弯钩 (bottom horizontal sweep + hook UP-LEFT)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
INK = 8


def line(p0, p1, w=INK):
    d.line([p0, p1], fill=BLACK, width=w)
    r = w // 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ---- Left: 扌 (x=40..130, y=105..265) — modeled on B6 PASS p3_180_打 ----
# 1. 短横
line((45, 145), (128, 132))
# 2. 长竖钩
line((100, 118), (100, 255))
line((100, 255), (82, 240))  # hook UP-LEFT
# 3. 提
line((48, 215), (128, 188))


# ---- Right: 巴 (x=155..275, y=115..260) ----
# 4. 竖 (short left vertical of 巴 — top portion, drawn slightly slanted in)
line((160, 122), (162, 200))

# 5. 横折 (top horizontal, then folds down forming right side)
line((160, 122), (258, 126))         # top 横 (slight upward tilt)
line((258, 126), (256, 215))         # right vertical

# 6. 横 middle — FLOATS clearly on BOTH sides
line((180, 172), (238, 174))

# 7. 竖弯钩 — continuous bottom sweep (curved, not right-angled)
#    Sample points along an arc from bottom of left 竖 sweeping right and up
import math
# arc center approx (200, 200), radius ~50, sweep from ~180° to ~-10°
cx, cy = 205, 205
rx, ry = 55, 45
prev = None
for t_deg in range(180, 355, 8):
    t = math.radians(t_deg)
    x = cx + rx * math.cos(t)
    y = cy - ry * math.sin(t)  # negative because want lower half
    # Actually we want the lower arc: y = cy + ry*sin(t) for t in 180..360
    y = cy + ry * math.sin(math.radians(t_deg - 180))
    pt = (x, y)
    if prev is not None:
        line(prev, pt)
    prev = pt
# hook flick UP-LEFT from the arc's right end
end = prev
line(end, (end[0] - 18, end[1] - 18))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0321_把/01_把.png")
