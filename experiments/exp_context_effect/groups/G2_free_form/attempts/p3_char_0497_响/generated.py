"""
p3_char_0497_响 — G2 attempt
Character: 响 (xiǎng, "sound"). 9 strokes.
Structure: LR compound. Left = 口 (small, mid-height). Right = 向 (撇 + 冂 + 口).
No sibling-risk labels. 冂 in 向 typically has NO hook (clean 竖) — GT matches.
Components MUST touch (Tier-0 H): left 口 sits close to 向's 冂 (~5 px overlap).

Stroke order (9):
Left 口 (3):
  1. 竖  (left of 口)
  2. 横折 (top + right)
  3. 一  (bottom)
Right 向 (6):
  4. 撇  (top-left flick above 冂)
  5. 竖  (冂 left) — starts high, connects to 撇 base
  6. 横折 (冂 top + right) — clean 竖, no hook
  7. 竖  (inner 口 left)
  8. 横折 (inner 口 top + right)
  9. 一  (inner 口 bottom)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = (0, 0, 0)


def stroke(points, width=7):
    d.line(points, fill=INK, width=width, joint="curve")
    r = width // 2
    for (x, y) in (points[0], points[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# --- Left 口 (small, mid-height) ---
# Positioned around x=42-118, y=125-215 — shifted right so it touches 向's 冂 (Tier-0 H)
lx0, ly0, lx1, ly1 = 42, 125, 118, 212
# 1. 竖 (left)
stroke([(lx0, ly0), (lx0 + 2, ly1)], width=7)
# 2. 横折 (top + right)
stroke([(lx0 - 2, ly0), (lx1, ly0 - 2), (lx1 + 2, ly1)], width=7)
# 3. 一 (bottom)
stroke([(lx0, ly1), (lx1 + 2, ly1)], width=7)

# --- Right 向 (撇 + 冂 + inner 口) ---
# 4. 撇 (top-left, above 冂) — starts high near center, sweeps down-left to top of 冂 left 竖
stroke([(148, 58), (125, 95)], width=8)

# 5. 竖 (冂 left vertical) — begins where 撇 lands, extends down
stroke([(125, 92), (120, 265)], width=8)

# 6. 横折 (冂 top + right vertical) — clean 竖, no hook.
# Top starts a bit right of 撇 base so it visually joins the 撇/竖 corner.
stroke([(132, 78), (270, 72), (274, 265)], width=8)

# --- Inner 口 (of 向) — positioned in lower half of 冂 ---
ix0, iy0, ix1, iy1 = 155, 150, 240, 220
# 7. 竖 (inner left)
stroke([(ix0, iy0), (ix0 + 1, iy1)], width=6)
# 8. 横折 (inner top + right)
stroke([(ix0 - 2, iy0), (ix1, iy0 - 1), (ix1 + 1, iy1)], width=6)
# 9. 一 (inner bottom)
stroke([(ix0, iy1), (ix1 + 1, iy1)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0497_响/01_响.png")
