"""
刈 (yì) — 4 strokes, left-right composition.
Left: 乂 (撇 + 捺 crossing near middle).
Right: 刂 radical — short 竖 (left) + 竖钩 (right, hook up-and-left).

Consulted:
- form_catalog.md "乂 as body-cross" — 撇+捺 crossing near vertical middle.
- form_catalog.md "刂 RIGHT" — two verticals; right is 亅 (竖钩), left is 短竖.
- memory_index TIER-0 hook rule — 竖钩 flicks UP-and-slightly-LEFT (~-100° to -110°).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=6):
    d.line([p0, p1], fill="black", width=w)

def bezier(pts, steps=80, w=6):
    # quadratic bezier
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = None
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        if prev is not None:
            d.line([prev, (x, y)], fill="black", width=w)
        prev = (x, y)

# --- Left half: 乂 ---
# Left half spans roughly x=35..165, y=70..270.
# 撇 (piě) — from upper-right to lower-left, with gentle rightward bow
# Start ~(140, 75), curve through (105, 170), end ~(45, 268).
bezier([(140, 75), (108, 170), (45, 268)], w=6)

# 捺 (nà) — from upper-left to lower-right, gentle curve
# Start ~(60, 85), curve through (100, 175), end ~(175, 268).
bezier([(60, 85), (100, 175), (175, 268)], w=6)

# --- Right half: 刂 ---
# Right half spans roughly x=200..265.
# 短竖 (short left vertical) — starts a bit below the top, ends around 3/4 down.
line((208, 105), (210, 225), w=6)

# 竖钩 (right vertical with hook) — taller, from near top to bottom, with hook up-left
# Main body:
line((258, 75), (260, 258), w=6)
# Hook: from bottom terminal, flick UP-and-LEFT (~-110°)
# Terminal at (260, 258); flick to about (238, 245).
line((260, 258), (238, 245), w=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0137_刈/01_刈.png")
