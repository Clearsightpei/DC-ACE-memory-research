"""
冯 (píng) — 冫 (left, two dots) + 马 (right).
Layout: 冫 occupies left ~28%, 马 occupies right ~65%.
马 = 横折 (top box top+right side), 竖折折钩 (middle body sweeping down with UP-LEFT flick),
     横 (long horizontal crossing through mid).
Hook family rule: 横折弯钩 terminal flicks UP-and-LEFT, not down.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def stroke(pts, width=7):
    d.line(pts, fill=BLACK, width=width, joint="curve")
    for x, y in pts:
        d.ellipse([x - width / 2, y - width / 2, x + width / 2, y + width / 2], fill=BLACK)


def dot(p1, p2, width=8):
    stroke([p1, p2], width=width)


# --- 冫 (left) ---
# top dot: small slanting stroke going down-right
dot((55, 100), (75, 118), width=9)
# 提: rising stroke bottom-left going up-right
stroke([(48, 200), (95, 178)], width=8)

# --- 马 (right) ---
# Occupies roughly x=110..255, y=75..245
# Stroke 1: 横折 — top horizontal then turn down (top of box + right side of top box)
# Top: horizontal from (125,100) to (215,95), then down to (208,145)
stroke([(125, 100), (215, 95), (210, 145)], width=8)

# Stroke 2: 竖折折钩 — starts as vertical left of body, folds right, folds down, ends in hook
# Hook must flick UP-and-LEFT prominently (per TIER-0 rule).
stroke([
    (128, 100),
    (128, 155),
    (218, 150),
    (225, 200),
    (222, 235),
], width=8)
# Hook flick — separate segment for a crisp UP-and-LEFT terminal
stroke([(222, 235), (195, 218)], width=8)

# Stroke 3: 横 — long horizontal crossing through mid, extends slightly past left edge of body
stroke([(110, 190), (240, 187)], width=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0211_冯/01_冯.png")
