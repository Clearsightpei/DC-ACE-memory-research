"""
仂 = 亻 (LEFT, tall-narrow 40% width; 撇 + 竖) + 力 (RIGHT; 横折钩 + body-crossing 撇)

Memory consulted:
- form_catalog "撇 as left-position radical component (亻...)": SHORTER ~80-110 px,
  steep 70-80 deg, throws down-left from ~x=130 to x=70-90.
- form_catalog char-role table row 亻: LEFT tall-narrow 40% width.
- form_catalog char-role table row 力: 横折钩 + body-crossing 撇.
- form_catalog "撇 as body-crossing diagonal (刀, 力, 匕)": LONG (~150-180 px),
  MUST cross the 横折 top with tip visibly ABOVE crossing line.

Layout (300x300 canvas):
  亻 occupies roughly x=45..115 (tall column, 40% of char zone)
  力 occupies roughly x=130..255

Stroke plan (4 strokes total):
  亻:
    1. 撇: from (95, 60) down-left to (55, 200), gentle bow
    2. 竖: from (95, 90) straight down to (95, 260)
  力:
    3. 横折钩: 横 from (150, 100) to (240, 100); fold down to (230, 235);
              hook flick up-left ending at (215, 220)
    4. 撇 body-crossing: from (215, 70) down-left through the 横 at ~(195, 100),
       curving down-left to (140, 275) — top visibly ABOVE the 横.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(pts, width_start=10, width_end=10, steps=None):
    """Draw a variable-width polyline by stamping ellipses along it."""
    if steps is None:
        steps = 80
    n = len(pts)
    if n < 2:
        return
    # walk along segment sequence with parameter t in [0, n-1]
    total_len = 0
    seg_lens = []
    for i in range(n - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        L = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        seg_lens.append(L)
        total_len += L
    for s in range(steps + 1):
        t = s / steps  # 0..1
        target = t * total_len
        acc = 0
        for i, L in enumerate(seg_lens):
            if acc + L >= target or i == len(seg_lens) - 1:
                local = 0 if L == 0 else (target - acc) / L
                x0, y0 = pts[i]
                x1, y1 = pts[i + 1]
                x = x0 + (x1 - x0) * local
                y = y0 + (y1 - y0) * local
                break
            acc += L
        w = width_start + (width_end - width_start) * t
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def straight(p0, p1, w0=10, w1=10, steps=None):
    if steps is None:
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        steps = max(30, int((dx * dx + dy * dy) ** 0.5))
    brush_line([p0, p1], w0, w1, steps)


# --------------------------------------------------------------
# 亻 (left)
# --------------------------------------------------------------

# Stroke 1: 撇 — starts near top with slight 顿 (thicker), tapers to a point
# Path: (95, 60) → gentle down-left curve → (55, 200)
pie_pts = [
    (95, 58),
    (92, 90),
    (85, 125),
    (75, 160),
    (63, 190),
    (52, 210),
]
brush_line(pie_pts, width_start=11, width_end=3, steps=120)

# Stroke 2: 竖 — from meeting point of 撇 (about 30% down the 撇) straight down
# Start point sits ON the 撇 around y=95, then goes straight down to y=265
shu_x = 95
straight((shu_x, 92), (shu_x, 265), w0=11, w1=10, steps=180)

# --------------------------------------------------------------
# 力 (right)
# --------------------------------------------------------------

# Stroke 3: 横折钩
# 横 part: (150, 100) → (240, 100), slight upward tilt at end
heng_pts = [
    (150, 105),
    (180, 102),
    (210, 100),
    (238, 98),
]
brush_line(heng_pts, width_start=9, width_end=11, steps=120)

# 折 part: (238, 98) → down to (232, 235); slight lean left
zhe_pts = [
    (240, 98),
    (238, 130),
    (235, 170),
    (232, 210),
    (230, 238),
]
brush_line(zhe_pts, width_start=13, width_end=11, steps=140)

# 钩 flick: at bottom, kick up-left, more pronounced
gou_pts = [
    (230, 238),
    (218, 230),
    (205, 218),
]
brush_line(gou_pts, width_start=11, width_end=2, steps=70)

# Stroke 4: body-crossing 撇 of 力
# Must START above the 横 (y < 100) and END lower-left.
# Cross-point through the 横 around x=205. Extend further down-left to match GT.
pie2_pts = [
    (218, 62),
    (213, 85),
    (205, 110),
    (188, 150),
    (170, 195),
    (152, 235),
    (132, 278),
]
brush_line(pie2_pts, width_start=11, width_end=2, steps=200)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0105_仂/01_仂.png"
)
