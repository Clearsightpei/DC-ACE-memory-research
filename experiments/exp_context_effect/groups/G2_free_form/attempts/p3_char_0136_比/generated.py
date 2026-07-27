"""
Render 比 (p3_char_0136_比) at 300x300 — revised.

# SIGNATURE CHECK: 比 = 匕 + 匕 (two 匕 side by side).
# Per errata p2_radical_086_比: left half's top is a 提 (rising),
# right half's top is a 撇 (falling). Both have 竖弯钩 with hook
# flicking UP-and-LEFT (TIER-0 B).
# Fixes on revision:
# 1. Top strokes must CROSS the vertical of the 竖弯钩, not float beside it.
# 2. Hooks flick UP-and-LEFT (endpoint y < curve-turn y). Prior attempt
#    had hook endpoints BELOW the base — that reads as DOWN-right flick.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 7

def polyline(pts, w=LW):
    for a, b in zip(pts[:-1], pts[1:]):
        d.line([a, b], fill=BLACK, width=w)

# ---- LEFT 匕 ----
# Stroke 1: 提 (rising left→right) — must CROSS the vertical at x≈95.
# Start lower-left, end upper-right, crossing through x=95.
polyline([(55, 145), (135, 115)])

# Stroke 2: 竖弯钩 — starts high, descends vertically, curves right at bottom,
# then hooks UP-and-LEFT (hook endpoint above curve-turn).
polyline([
    (95, 95),
    (95, 210),
    (100, 225),
    (115, 235),
    (145, 235),   # end of the rightward sweep (base of hook)
])
# Hook flick UP-and-LEFT
polyline([(145, 235), (140, 210)])

# ---- RIGHT 匕 ----
# Stroke 3: 撇 (falling right→left) — must CROSS vertical at x≈200.
# Start upper-right, sweep down-left through x=200.
polyline([(230, 90), (170, 155)])

# Stroke 4: 竖弯钩 — mirror of left one; hook flicks UP-and-LEFT.
polyline([
    (200, 120),
    (200, 215),
    (205, 230),
    (220, 240),
    (250, 240),
])
polyline([(250, 240), (245, 215)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0136_比/01_比.png")
print("wrote 01_比.png (revised)")
