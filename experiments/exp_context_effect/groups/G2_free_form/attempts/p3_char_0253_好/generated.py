"""
p3_char_0253_好  (好 = 女 + 子)

Layout: 女 occupies left ~45% of canvas, 子 occupies right ~55%.
好 is a left-right compound; 女 is compressed narrow on the left,
子 uses the right side with its horizontal extending well left
into the 女 area (like the GT shows a long middle 横 extending
across both components).

女 strokes (3):
  1. 撇点 (piedian): down-left diagonal then reflex down-right
  2. 撇: down-left diagonal from top
  3. 横: long horizontal crossing at middle

子 strokes (3):
  1. 横撇 (heng-pie): horizontal top then sharp down-left hook
  2. 竖钩: long vertical descending, hook up-left at bottom
  3. 横 (long): horizontal across middle (crosses into 女 area)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=7):
    d.line(pts, fill=INK, width=width, joint="curve")
    # dab ends for calligraphic feel
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse([x - width / 2, y - width / 2, x + width / 2, y + width / 2], fill=INK)


# ---------- 女 (left) ----------
# 女 sits in left region ~ x in [30, 140], y in [50, 260]

# Stroke 1: 撇点 — down-left slope from top-center of 女, then reflex right-down
# Start high-right of 女, sweep down-left, elbow, sweep down-right (dot)
stroke([(95, 65), (75, 130), (55, 190)], width=7)         # first pie down-left
stroke([(55, 190), (95, 240)], width=7)                    # dian back down-right

# Stroke 2: 撇 — from upper-right of 女 down-left through center to bottom-left
stroke([(115, 90), (95, 160), (60, 245)], width=7)

# Stroke 3: 横 — long horizontal crossing 女 (goes slightly upward like GT)
stroke([(30, 175), (145, 165)], width=7)


# ---------- 子 (right) ----------
# 子 sits in right region ~ x in [150, 280], y in [55, 275]

# Stroke 1: 横撇 — horizontal top then sharp diagonal down-left
stroke([(160, 80), (250, 75)], width=7)                   # top heng
stroke([(250, 75), (240, 95), (200, 130)], width=7)       # pie down-left

# Stroke 2: 竖钩 — vertical down center-right of 子, hook up-left at bottom
stroke([(215, 105), (215, 250)], width=7)                 # vertical
stroke([(215, 250), (200, 245), (185, 240)], width=7)     # hook up-left

# Stroke 3: 横 — long horizontal across the middle of 子, extends left into 女 area
stroke([(145, 165), (275, 170)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0253_好/01_好.png")
print("saved")
