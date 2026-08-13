"""
疟 (yao / nue) — sickness-radical 疒 + 丆-like enclosure.

Structure (from GT):
  - 疒 radical wraps top+left:
      1. small dot near top-center-left
      2. long horizontal (top bar) starting a bit left of center
      3. long left-falling 撇 from top bar's left end down to bottom-left
      4-5. two short slant strokes (like 冫) on the left side of the
           enclosed region
  - Interior (right-of-center, mid-height): small 丆-like shape —
      6. short horizontal
      7. short vertical drop with slight hook / turn
  - Optional bottom stroke closing the interior.
"""
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 6  # base ink width


def line(p0, p1, w=W):
    d.line([p0, p1], fill=BLACK, width=w)


def dab(cx, cy, r=4):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLACK)


def stroke_poly(points, w=W):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=BLACK, width=w)
    for (x, y) in points:
        dab(x, y, r=w // 2)


# --- 疒 outer shell ------------------------------------------------

# 1) top dot (小点), slightly left of horizontal's start
stroke_poly([(112, 55), (122, 68)], w=7)

# 2) top horizontal — long, running rightward to the right edge
stroke_poly([(108, 78), (240, 78)], w=6)

# 3) long left-falling 撇 — from left end of horizontal down-left to
#    bottom-left of canvas, gently curving.
stroke_poly([
    (108, 78),
    (98, 120),
    (85, 170),
    (70, 220),
    (55, 265),
], w=7)

# 4) upper short slant on the left (冫 upper) — small tick pointing
#    inward-down
stroke_poly([(95, 125), (115, 140)], w=6)

# 5) lower short slant on the left (冫 lower)
stroke_poly([(78, 175), (100, 195)], w=6)

# --- Interior — 尸/丆-like shape, right of center ------------------

# 6) inner top horizontal, then bending down on the right (one stroke,
#    a 横折 — like the top of 尸)
stroke_poly([
    (130, 155),
    (245, 155),
    (245, 210),
    (240, 245),
], w=6)

# 7) inner bottom horizontal (base bar) — long, closes the enclosure
stroke_poly([(130, 245), (245, 245)], w=6)

# 8) inner short vertical on the left (short — like the small tick
#    inside 尸/丆)
stroke_poly([(155, 200), (155, 245)], w=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0380_疟/01_疟.png")
print("saved 01_疟.png")
