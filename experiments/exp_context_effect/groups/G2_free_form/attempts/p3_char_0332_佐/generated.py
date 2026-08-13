"""
佐 (zuǒ) — 7 strokes: 亻 (撇 + 竖) + 左 (横 + 撇 + 工 = 横+竖+横).

Composition (from GT):
  Left: 亻 in narrow left column (~x 40-100).
  Right: 左 in wider right column (~x 100-280).
    - Top: short 横 with long 撇 that sweeps down-left (crosses beyond 亻).
    - Bottom: 工 (short 横 top, short 竖, long 横 bottom).

No sibling-risk targets. No hooks (no 钩 in this character).
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
# Stroke 1: 撇 — apex near (85, 55), curves down-left to (45, 200)
apex_x, apex_y = 88, 55
pie = [(apex_x, apex_y), (78, 100), (65, 145), (48, 200)]
stroke(pie, width=8)
dab(apex_x, apex_y, 4)

# Stroke 2: 竖 — from just below apex straight down to (85, 265)
stroke([(apex_x - 2, apex_y + 30), (apex_x - 4, 265)], width=8)

# ---------- 左 (right, upper 𠂇 + lower 工) ----------
# Stroke 3: 横 (short, upper) — from (135, 90) to (215, 82)
stroke([(135, 92), (170, 88), (218, 82)], width=7)

# Stroke 4: 撇 (long, sweeps down-left) — starts above 横, ends near left-bottom
# but stops shy of the 亻 竖.
pie_long = [(178, 65), (168, 115), (156, 165), (145, 215), (128, 260)]
stroke(pie_long, width=8)
dab(178, 65, 4)

# ---------- 工 (bottom-right, inside 左) ----------
# Stroke 5: 横 (short top of 工) — from (170, 175) to (245, 172)
stroke([(170, 178), (245, 174)], width=6)

# Stroke 6: 竖 (short middle of 工) — from (205, 178) down to (205, 245)
stroke([(206, 180), (205, 245)], width=6)

# Stroke 7: 横 (long bottom of 工) — from (150, 250) to (280, 248)
stroke([(150, 252), (215, 249), (280, 246)], width=7)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0332_佐/01_佐.png"
img.save(out)
print(f"Saved {out}")
