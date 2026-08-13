"""
佝 (gōu) — 7 strokes: 亻 (撇 + 竖) + 句 (撇 + 横折钩 wrapping 口).

Composition (from GT):
  Left: 亻 in narrow left column (~x 40-100).
  Right: 句 in wider right column (~x 110-280).
    - 勹 outer: 撇 top-left + 横折钩 wrapping right & down with hook flick up-left.
    - 口 inside: three strokes (竖, 横折, 横 sealing bottom).

Hook flicks: 横折钩 terminal flicks UP-and-LEFT (per TIER-0 rule B).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 7

def stroke(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

def dab(cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=INK)

# ---------- 亻 (person radical, left) ----------
# Stroke 1: 撇 — apex near (78, 55), curves down-left to (42, 190)
apex_x, apex_y = 80, 55
stroke([(apex_x, apex_y), (70, 100), (58, 140), (42, 190)], width=8)
dab(apex_x, apex_y, 4)

# Stroke 2: 竖 — from just below apex straight down to (75, 250)
stroke([(apex_x - 2, apex_y + 30), (apex_x - 5, 250)], width=8)

# ---------- 句 (right, 勹 wrapping 口) ----------
# Stroke 3: 撇 (top-left of 勹) — apex ~(145, 45), sweeps down-left to (105, 155)
stroke([(148, 45), (135, 85), (122, 120), (108, 158)], width=8)
dab(148, 45, 4)

# Stroke 4: 横折钩 — starts near (148, 58), goes right to (255, 55),
# folds down to (245, 260), then hooks UP-and-LEFT.
# Segment 4a: 横 top (slight upward slant to right)
stroke([(148, 60), (200, 56), (256, 54)], width=8)
# Segment 4b: 折 corner going down
stroke([(256, 54), (256, 130), (250, 210), (245, 260)], width=8)
# Segment 4c: 钩 hook flick up-and-left (~-110°)
stroke([(245, 260), (232, 245)], width=8)

# ---------- 口 (inside 句, lower-middle area) ----------
# Positioned inside the 勹 pocket: roughly x 135-220, y 155-225
# Stroke 5: 竖 (left side of 口) — from (140, 160) down to (138, 225)
stroke([(140, 160), (139, 225)], width=6)

# Stroke 6: 横折 (top + right side of 口) — from (138, 160) right to (222, 158),
# then down to (222, 225)
stroke([(138, 160), (180, 158), (222, 158)], width=6)
stroke([(222, 158), (223, 192), (222, 225)], width=6)

# Stroke 7: 横 (bottom of 口, sealing) — from (138, 225) to (222, 225)
stroke([(138, 225), (180, 226), (222, 225)], width=6)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0344_佝/01_佝.png"
img.save(out)
print(f"Saved {out}")
