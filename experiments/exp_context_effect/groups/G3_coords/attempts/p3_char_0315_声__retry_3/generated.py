# BANK_DEVIATION
# skipped: shi_male.py, shi_radical.py
# reason: prior R1/R2 stacked-bank composition drifted (missing 士 middle 竖,
#   cramped 尸 envelope, mis-proportioned box). Inlining fresh with explicit
#   column widths + y-band hints per B12 errata guidance.
# fresh_component: sheng_inline_R3

# TRAJECTORY DIFF (p3_char_0315_声 retry_3)
# GT (声): from top:
#   (1) short top 横 (~x 115-205, y 78)
#   (2) tiny 竖 hanging below top-heng center (~x 163, y 70-95)
#   (3) long middle 横 (~x 55-245, y 128) -- the 士 lower / envelope top
#   (4) long 撇 curving down-left from below middle-heng-left (~x 78, y 132)
#       to bottom-left (~x 40, y 275)
#   (5) 横折 top of small right box (~x 115 -> 218, then down to y 225)
#   (6) short 竖 left side of box (~x 115, y 158-225)
#   (7) bottom 横 of box (~x 115-218, y 225)
# R1 FAIL: missing top 横 span; box too small; no 竖 in 士
# R2 FAIL: still no 士 middle 竖; box hovering, box top merged with middle heng
# R3 fixes:
#   * add the small 竖 of 士 hanging from top-heng
#   * make top-heng properly short (~90px) not overlapping middle heng
#   * make middle heng LONG (~190px) — the envelope top
#   * box below middle heng: wider (~100px x 70px), left edge closed
#   * long 撇 starts from below-left of middle heng, curves outward

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

def line(x1, y1, x2, y2, w=4):
    d.line([(x1, y1), (x2, y2)], fill='black', width=w)

def polyline(pts, w=4):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill='black', width=w)

# --- Stroke 1: top 横 (short, slight upward tilt to right, tiny hook end) ---
polyline([(118, 80), (160, 77), (205, 75), (207, 82)], w=4)

# --- Stroke 2: 士 middle 竖 (short vertical below top-heng center) ---
line(163, 73, 163, 100, w=4)

# --- Stroke 3: middle long 横 (envelope top) ---
polyline([(55, 132), (150, 128), (245, 126)], w=5)

# --- Stroke 4: long 撇 (curve from below middle-heng-left down to bottom-left) ---
pie_pts = []
for i in range(30):
    t = i / 29.0
    # start (78, 138) -> end (35, 278)
    x = 78 - t * 43
    y = 138 + t * 140
    # curve outward (bow to the left in the lower half)
    bow = 12 * (t * (1 - t) * 4) * -1  # negative = leftward bow
    x += bow
    pie_pts.append((x, y))
polyline(pie_pts, w=5)

# --- Stroke 5: 横折 (top and right side of the small box) ---
# horizontal from ~(108,152) to (208,150), then turn down to (210,215)
polyline([(108, 152), (160, 150), (208, 148), (210, 180), (210, 215)], w=4)

# --- Stroke 6: short 竖 (left side of the box) ---
line(108, 152, 108, 215, w=4)

# --- Stroke 7: bottom 横 of the box ---
polyline([(108, 216), (160, 215), (210, 216)], w=4)

img.save('/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0315_声__retry_3/01_声.png')
print("wrote 01_声.png")
