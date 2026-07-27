"""
p3_char_0120_气 — 4-stroke character.

Decomposition (from GT):
  1) 撇 (top short) — starts around (140, 85), throws down-left to (~85, 115).
  2) 横 (upper) — from (~105, 105) rightward to (~215, 100). Slight up-tilt.
  3) 横 (middle) — from (~95, 140) rightward to (~235, 135). Longer, slight up-tilt.
  4) 横折弯钩 — starts as horizontal from (~85, 175), extends right to (~245, 170),
     then turns sharply downward, curves toward bottom-right and finally hooks UP-and-LEFT
     at the terminal (the signature "钩" flicking up).

Not on sibling checklist. No overriding identity bits.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
STROKE_W = 7


def line(p0, p1, w=STROKE_W):
    d.line([p0, p1], fill=INK, width=w)


def polyline(pts, w=STROKE_W):
    d.line(pts, fill=INK, width=w, joint="curve")


def dab(p, r=4):
    x, y = p
    d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# --- Stroke 1: 撇 (short top flick) ---
# starts upper-mid, throws down-left
s1_start = (145, 78)
s1_end = (78, 118)
dab(s1_start, r=5)
polyline([s1_start, (120, 92), (95, 108), s1_end])

# --- Stroke 2: 横 (upper) ---
# From near s1_end area, going right with a slight up-tilt
s2_start = (100, 110)
s2_end = (215, 100)
dab(s2_start, r=4)
polyline([s2_start, (155, 106), s2_end])
dab(s2_end, r=4)

# --- Stroke 3: 横 (middle, longer) ---
s3_start = (90, 148)
s3_end = (235, 138)
dab(s3_start, r=4)
polyline([s3_start, (160, 143), s3_end])
dab(s3_end, r=4)

# --- Stroke 4: 横折弯钩 ---
# Horizontal segment
s4_h_start = (82, 185)
s4_corner = (248, 175)   # right shoulder where it turns down
polyline([s4_h_start, (160, 180), s4_corner], w=STROKE_W)
dab(s4_h_start, r=4)

# From the corner, drop and curve. Longer descent then pronounced up-left hook flick.
curve = [
    s4_corner,
    (252, 210),
    (250, 235),
    (243, 258),
    (228, 275),
    (210, 282),
    (198, 280),
    (192, 272),   # begin hook flick
    (188, 260),   # hook flicks up-and-left
    (185, 248),
]
polyline(curve, w=STROKE_W)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0120_气/01_气.png")
