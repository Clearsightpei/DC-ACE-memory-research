# BANK_DEVIATION
# skipped: (no fitting bank entry — 乘 is a 10-stroke compound with
#   an unusual layout: pie-top + long heng + left/right pairs of small
#   heng strokes + central shu-gou + spreading pie/na at bottom)
# reason: no bank primitive covers this composition; inline fresh
#   render matching GT stroke-by-stroke.
# fresh_component: cheng_char_inline
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=5):
    d.line([p0, p1], fill="black", width=w)

def poly(pts, w=5):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- Stroke 1: short 撇 at top ----
poly([(150, 40), (135, 55)], w=5)

# ---- Stroke 2: long 横 (upper horizontal crossbar) ----
# spans wide, slightly rising
poly([(60, 78), (240, 72)], w=5)

# ---- Stroke 3: central 竖 with slight hook (main vertical) ----
poly([(150, 55), (150, 245), (140, 255)], w=6)

# ---- Left inner ヨ-like: two horizontals + connecting slant ----
# Stroke 4: upper-left short heng
poly([(72, 118), (140, 115)], w=5)
# Stroke 5: lower-left short heng (a bit lower/longer)
poly([(60, 160), (140, 155)], w=5)
# Stroke 6: left slanting pie down-left connecting them
poly([(85, 110), (55, 175)], w=5)

# ---- Right inner mirror: two horizontals + curved hook ----
# Stroke 7: upper-right short heng
poly([(160, 115), (228, 118)], w=5)
# Stroke 8: lower-right short heng
poly([(160, 155), (238, 160)], w=5)
# Stroke 9: right curved 乙-like: short slant then horizontal then hook up
poly([(215, 100), (218, 130), (215, 165), (240, 178), (245, 165)], w=5)

# ---- Middle horizontal across center (belt of 乘) ----
poly([(50, 185), (250, 180)], w=5)

# ---- Bottom 撇 (long left-spreading) ----
poly([(150, 185), (55, 275)], w=5)
# ---- Bottom 捺 (long right-spreading) ----
poly([(150, 185), (255, 275)], w=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0514_乘/01_乘.png")
