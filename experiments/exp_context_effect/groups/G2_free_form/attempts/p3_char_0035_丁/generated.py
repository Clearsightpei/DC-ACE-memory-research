"""
丁 (dīng) — 2 strokes: 横 (horizontal top), then 竖钩 (vertical with left hook).
GT shows a wide top 横 spanning most of the width, and a 竖 dropping from
just right of center, ending with a left-pointing hook at the bottom.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 9  # main stroke width

def dab(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# --- Stroke 1: 横 (top horizontal) ---
# Spans ~x=45..255, at y ~= 95. Slight downward-then-up smile so it feels brushed.
y_top = 95
x1, x2 = 45, 255
# start dab (顿)
dab(x1, y_top - 2, r=7)
# subtle arc: sample a few points
pts = []
for i in range(21):
    t = i / 20
    x = x1 + (x2 - x1) * t
    # very slight sag then flat
    y = y_top + 2 * (0.5 - abs(t - 0.5)) * 1.0
    pts.append((x, y))
d.line(pts, fill=BLACK, width=LW)
# ending 顿 dab
dab(x2, y_top - 2, r=7)

# --- Stroke 2: 竖钩 (vertical stem with hook to the left at bottom) ---
# Starts near the middle of the top 横 (slightly right of center),
# drops vertically, then hooks up-and-left.
x_stem = 150
y_stem_top = y_top + 4       # begins just under the horizontal
y_stem_bot = 240              # bottom before hook
# small starting shoulder dab (顿 at top of 竖)
dab(x_stem, y_stem_top + 2, r=6)
# vertical, very slight lean (calligraphic)
stem_pts = []
for i in range(21):
    t = i / 20
    x = x_stem + 0 * t         # keep straight
    y = y_stem_top + (y_stem_bot - y_stem_top) * t
    stem_pts.append((x, y))
d.line(stem_pts, fill=BLACK, width=LW)

# Hook: from (x_stem, y_stem_bot) curve down-left then flick up-left
hook_pts = []
# small arc: go slightly down and left, then sweep up-left
hx0, hy0 = x_stem, y_stem_bot
# control-ish: curve outward
for i in range(15):
    t = i / 14
    # quadratic-ish path: bottom curves left and up
    x = hx0 - 22 * t
    y = hy0 + 8 * (1 - (1 - t) ** 2) - 18 * t
    hook_pts.append((x, y))
d.line(hook_pts, fill=BLACK, width=LW)
# taper the hook tip
tip_x, tip_y = hook_pts[-1]
dab(tip_x, tip_y, r=4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0035_丁/01_丁.png")
