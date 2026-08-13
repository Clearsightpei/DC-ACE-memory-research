"""
老 (lǎo) — 6 strokes.
Structure: 土-like top (横, 竖, 横) sits atop a long 撇 diagonal;
the bottom-right holds 匕 (短撇 + 竖弯钩).

# SIGNATURE CHECK: 匕 (component) — top stroke is a 撇 (upper-right→lower-left);
# terminal hook flicks UP-and-LEFT. Contrast with 七 whose top is a 横.

Stroke order:
  1. 横         — top horizontal, upper-middle
  2. 竖         — vertical down from center of top 横
  3. 横         — second horizontal (wider), a bit below the first
  4. 撇         — long diagonal from mid-upper-right down to lower-left
  5. 短撇 (匕上) — short flick starting on the long 撇, going lower-left
  6. 竖弯钩     — vertical→right-curve→UP-LEFT hook at bottom-right
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def stroke(points, width=8):
    d.line(points, fill=BLACK, width=width, joint="curve")
    # round dabs
    for x, y in points:
        r = width / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- 1. Top 横 (upper-middle, moderate length) ---
stroke([(115, 85), (195, 80)], width=8)

# --- 2. 竖 (down from center of the top 横) ---
stroke([(155, 80), (155, 160)], width=8)

# --- 3. Second 横 (wide, cuts across) ---
stroke([(45, 148), (265, 142)], width=8)

# --- 4. Long 撇 (starts upper-right, sweeps down to lower-left) ---
pren = [
    (225, 45),
    (215, 80),
    (190, 130),
    (150, 190),
    (100, 240),
    (55, 275),
]
stroke(pren, width=8)

# --- 5. 短撇 (top of 匕) — short flick from around the 撇 line, lower-right area ---
stroke([(185, 175), (160, 205)], width=7)

# --- 6. 竖弯钩 — starts near end of 短撇, down, curves right, hook flicks UP-and-LEFT ---
szwg = [
    (183, 178),
    (183, 220),
    (188, 250),
    (205, 268),
    (230, 272),
    (250, 265),
    (252, 252),  # hook flick UP-and-LEFT
    (243, 245),
]
stroke(szwg, width=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0271_老/01_老.png")
print("saved 01_老.png")
