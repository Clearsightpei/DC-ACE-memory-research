"""Render 刂 (li dao pang) — 2-stroke radical.

Stroke 1: short 竖 on the left (upper-middle vertical).
Stroke 2: taller 竖钩 on the right (long vertical with a small
          left-pointing hook at bottom).
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
WIDTH = 8

# Stroke 1: short left 竖 — upper-middle position, ends around y=170
# Left vertical, slightly slanted (top a hair right of bottom, mimicking GT)
x1_top, y1_top = 118, 85
x1_bot, y1_bot = 112, 175
draw.line([(x1_top, y1_top), (x1_bot, y1_bot)], fill=INK, width=WIDTH)

# Stroke 2: right 竖钩 — long vertical descending, then hook to the left
x2_top, y2_top = 195, 70
x2_bot, y2_bot = 192, 235
draw.line([(x2_top, y2_top), (x2_bot, y2_bot)], fill=INK, width=WIDTH)

# Hook: short flick to the upper-left at the bottom of stroke 2
x_hook_end, y_hook_end = 170, 228
draw.line([(x2_bot, y2_bot), (x_hook_end, y_hook_end)], fill=INK, width=WIDTH)

# Round the endpoints a bit for a calligraphic feel
r = WIDTH // 2
for (x, y) in [(x1_top, y1_top), (x1_bot, y1_bot),
               (x2_top, y2_top), (x2_bot, y2_bot),
               (x_hook_end, y_hook_end)]:
    draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=INK)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0036_刂/01_刂.png"
img.save(out)
print(f"wrote {out}")
