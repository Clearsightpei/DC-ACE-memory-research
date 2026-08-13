"""
采 (pick/gather) — 爫 (claw) on top + 木 (tree) below.
8 strokes total:
  Top 爫: 撇 (left slant) + 3 short vertical dots + a small horizontal shoulder
  Bottom 木: 横, 竖, 撇, 捺
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(pts, width=9):
    d.line(pts, fill=BLACK, width=width, joint="curve")


def taper(p0, p1, w0, w1, steps=80):
    # Approximate a tapered stroke by drawing overlapping circles.
    (x0, y0), (x1, y1) = p0, p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = (w0 + (w1 - w0) * t) / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def curve(pts, width=9, steps=40):
    # Simple polyline treated as a smooth curve.
    for i in range(len(pts) - 1):
        line([pts[i], pts[i + 1]], width=width)


# --- 爫 top (approx y=40..115) ---
# Left downward slant (long 撇-ish)
taper((110, 55), (85, 115), 6, 11)
# Short horizontal shoulder / top hint
line([(120, 55), (185, 60)], width=8)
# Right side down-hook (short 竖 with slight curve)
taper((190, 60), (180, 115), 10, 6)
# Three short vertical marks in the middle-bottom of 爫
taper((125, 90), (127, 118), 6, 9)
taper((150, 90), (152, 118), 6, 9)

# --- 木 bottom (approx y=140..270) ---
# 横 (long horizontal)
line([(50, 155), (250, 155)], width=9)
# 竖 (central vertical, extends down)
taper((150, 130), (150, 275), 8, 9)
# 撇 (left flare from just below 横)
taper((150, 170), (60, 265), 10, 5)
# 捺 (right flare from just below 横)
taper((150, 170), (250, 265), 6, 12)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0413_采/01_采.png")
print("saved")
