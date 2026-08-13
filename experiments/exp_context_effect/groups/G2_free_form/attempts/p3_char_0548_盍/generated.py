"""Render 盍 (cover/lid) — 10 strokes.

Decomposition: 去 (top) + 皿 (bottom).
  去 = 士 (3 strokes: 横, 竖, 横) + 厶 (2 strokes: 撇折, 点)
  皿 = 5 strokes (see p3_char_0195_皿 for reused pattern)

Layout on 300x300:
  士 rows: y ~ 40..85
  厶:      y ~ 88..145
  皿 box:  y ~ 155..255 (bottom bar at y=258)

Components MUST touch (TIER-0 H): 皿's top edge sits just under 厶's point.

SIGNATURE CHECK: 士 = top-横 LONGER than bottom-横 (士, not 土).
  Here the middle-横 is the LONG one under the top-短横; this is 士.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6

def line(p0, p1, width=LW):
    d.line([p0, p1], fill=INK, width=width)

def dab(cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=INK)

# --- 士 (top) ---
# Stroke 1: 横 (top, shorter but here reading as top of 士 -- draw longer
# following GT which shows top horizontal wider than in 土)
line((100, 48), (200, 45), width=LW)
# Stroke 2: 竖 (vertical center)
line((150, 45), (150, 92), width=LW)
# Stroke 3: 横 (middle, longer bar of 士 -- extends widest)
line((80, 90), (220, 88), width=LW + 1)

# --- 厶 (middle) ---
# Stroke 4: 撇折 — 撇 down-left, then 折/提 sweeping up-right
# 撇 part (bowed slightly)
pts_pie = [(165, 100), (150, 122), (128, 148)]
for i in range(len(pts_pie) - 1):
    line(pts_pie[i], pts_pie[i + 1], width=LW)
# shoulder dab at fold
dab(128, 148, 4)
# 折 (提) sweeping up-right
line((128, 148), (178, 140), width=LW)

# Stroke 5: 点 (teardrop on lower-right of 厶, closes the mouth)
for k, r in enumerate([3.0, 4.0, 5.0, 4.0]):
    dab(184 + k * 2, 138 + k * 4, r)

# --- 皿 (bottom) ---
BOX_L, BOX_R = 75, 225
BOX_T, BOX_B = 160, 245

# Stroke 6: 竖 — left outer vertical (slight inward lean at top)
line((BOX_L + 8, BOX_T + 5), (BOX_L, BOX_B), width=LW)
# Stroke 7: 竖折 — top horizontal + right vertical
line((BOX_L + 8, BOX_T + 5), (BOX_R - 7, BOX_T), width=LW)
line((BOX_R - 7, BOX_T), (BOX_R, BOX_B), width=LW)
# Stroke 8: inner-left short 竖
line((120, BOX_T + 15), (120, BOX_B), width=LW - 1)
# Stroke 9: inner-right short 竖
line((180, BOX_T + 15), (183, BOX_B), width=LW - 1)
# Stroke 10: long bottom 一 extending past both sides
line((45, 258), (260, 255), width=LW + 1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0548_盍/01_盍.png")
print("Wrote 01_盍.png")
