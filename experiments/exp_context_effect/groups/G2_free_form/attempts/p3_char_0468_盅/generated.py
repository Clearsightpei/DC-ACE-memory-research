"""
p3_char_0468_盅 — G2 free-form

Composition: 中 (top) + 皿 (bottom), vertical stack.
- Top: 中 compressed into the upper ~half of the canvas.
  Its central axis passes THROUGH the box but stops just above 皿
  (does NOT hang down into the bowl).
- Bottom: 皿 (bowl) occupies the lower ~half, with a long bottom
  一 that extends beyond the box on both sides.

Consulted memory:
- form_catalog "囗/口 as pure box" — 3-stroke box for 中's frame.
- form_catalog "竖 as central axis for 中" — long central vertical.
- Prior successful renders: p3_char_0100_中, p3_char_0195_皿.
- TIER-0 F: apply calligraphic weight — but this character is all
  straight strokes (no 撇/捺/hook), so shoulder-dab at 折 joints is
  the primary lift.
- radical_position_rules: for top-bottom compounds, top component
  is compressed vertically; bottom sits below with its own footprint.

Stroke count: 4 (中) + 5 (皿) = 9 strokes.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6

def line(p0, p1, width=LW):
    d.line([p0, p1], fill=INK, width=width)

def dab(p, r):
    d.ellipse([(p[0] - r, p[1] - r), (p[0] + r, p[1] + r)], fill=INK)

# ============================================================
# TOP: 中 — compressed into upper half (y ~ 20 to 145)
# ============================================================
# Box a bit wider than tall, centered
top_box_L = 110
top_box_R = 200
top_box_T = 45
top_box_B = 125
top_cx = (top_box_L + top_box_R) // 2  # 155

# Central axis: protrudes above and just below the box (short, does
# NOT hang into 皿)
axis_top = 20
axis_bot = 148   # just above 皿 (which starts around y=155)

# Stroke 1: left 竖 of box
line((top_box_L, top_box_T), (top_box_L, top_box_B), width=LW)

# Stroke 2: 横折 (top + right wall)
line((top_box_L, top_box_T), (top_box_R, top_box_T), width=LW)
# shoulder dab
dab((top_box_R, top_box_T), LW // 2 + 1)
line((top_box_R, top_box_T), (top_box_R, top_box_B), width=LW)

# Stroke 3: bottom 一 of box
line((top_box_L, top_box_B), (top_box_R, top_box_B), width=LW)

# Stroke 4: central axis
line((top_cx, axis_top), (top_cx, axis_bot), width=LW)
r = LW // 2 + 1
dab((top_cx, axis_top), r)
dab((top_cx, axis_bot), r)

# ============================================================
# BOTTOM: 皿 — occupies lower half (y ~ 155 to 265)
# ============================================================
# Box wider than tall
bot_box_L = 80
bot_box_R = 220
bot_box_T = 165
bot_box_B = 250
bot_bar_L = 45
bot_bar_R = 258
bot_bar_Y = 262

# Stroke 5: 竖 — left outer vertical, slight inward lean at top
line((bot_box_L + 5, bot_box_T), (bot_box_L - 2, bot_box_B), width=LW)

# Stroke 6: 竖折 — top horizontal + right vertical
line((bot_box_L + 5, bot_box_T), (bot_box_R - 5, bot_box_T - 3), width=LW)
# shoulder dab
dab((bot_box_R - 5, bot_box_T - 3), LW // 2 + 1)
line((bot_box_R - 5, bot_box_T - 3), (bot_box_R + 2, bot_box_B), width=LW)

# Stroke 7: 竖 — inner-left short vertical
inner_L_x = bot_box_L + 42
line((inner_L_x, bot_box_T + 12), (inner_L_x, bot_box_B), width=LW - 1)

# Stroke 8: 竖 — inner-right short vertical
inner_R_x = bot_box_R - 42
line((inner_R_x, bot_box_T + 12), (inner_R_x + 2, bot_box_B), width=LW - 1)

# Stroke 9: 一 — long bottom horizontal extending beyond box on both sides
line((bot_bar_L, bot_bar_Y - 1), (bot_bar_R, bot_bar_Y + 1), width=LW + 1)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0468_盅/01_盅.png"
img.save(out)
print(f"wrote {out}")
