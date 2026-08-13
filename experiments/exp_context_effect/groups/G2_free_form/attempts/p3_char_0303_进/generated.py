"""Render 进 (jin, 7 strokes) at 300x300, PIL brush-dabs, black on white.

进 = 辶 (walking radical, left-and-bottom wrap) + 井 (upper-right).

Stroke plan (per GT gt/phase3/进.png):

  辶 (3 strokes, wraps left+bottom):
    1. 点 dot — small teardrop, upper-left around (95, 60).
    2. 横折折撇 — the zigzag body: short 横 → shoulder → down-left slant
       → shoulder → short 横 → bowed 撇 tail.
    3. 平捺 — long shallow sweep across the bottom from lower-left to
       lower-right, broad flat foot at right end.

  井 (4 strokes, upper-right block):
    4. 横 h1 — short upper horizontal, angled slightly upward.
    5. 横 h2 — longer lower horizontal, slight upward tilt.
    6. 撇 (left vertical, leans slightly left).
    7. 竖 (right vertical, straight down).

Design references GT: 井 sits in x∈[135,265], y∈[50,205]; 辶 body is
compact on the left, x∈[55,140], and its 平捺 sweep runs across bottom.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy)
    if steps is None:
        steps = max(30, int(L * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200, ease=None):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        te = ease(t) if ease else t
        r = r0 + (r1 - r0) * te
        dab(x, y, r)


# ============ 辶 (walking radical) ============

def draw_dot():
    # Small teardrop, upper-left. Oriented slightly down-right.
    p0 = (92, 55)
    p2 = (110, 82)
    p1 = (98, 68)
    steps = 100
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** 1.4
        r = 1.5 + (4.5 - 1.5) * tt
        dab(x, y, r)
    dab(p2[0], p2[1], 4.5)


def draw_body():
    # 横折折撇 zigzag body — compact on left.
    a = (72, 118)
    b = (128, 110)
    c = (95, 148)
    dd = (135, 143)
    tail_tip = (72, 208)
    r_body = 3.5

    dab(a[0], a[1], r_body + 1.2)
    line_dabs(a[0], a[1], b[0], b[1], r_body, r_body)
    dab(b[0], b[1], r_body + 1.2)
    line_dabs(b[0], b[1], c[0], c[1], r_body, r_body)
    dab(c[0], c[1], r_body + 1.2)
    line_dabs(c[0], c[1], dd[0], dd[1], r_body, r_body)
    dab(dd[0], dd[1], r_body + 1.2)
    ctrl = (128, 180)
    bezier_dabs(dd, ctrl, tail_tip, r_body + 0.3, 1.0, steps=240,
                ease=lambda t: t)


def draw_pina():
    # Long shallow 平捺 across bottom; concave-up belly; broad flat foot.
    p0 = (55, 232)
    p2 = (260, 240)
    p1 = (155, 275)  # control pulls DOWN → concave-up belly
    steps = 320
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        if t < 0.85:
            r = 1.5 + (6.5 - 1.5) * (t / 0.85)
        else:
            r = 6.5 - (6.5 - 5.0) * ((t - 0.85) / 0.15)
        dab(x, y, r)
    fx, fy = p2
    for k in range(0, 14):
        dab(fx + k * 0.6, fy + k * 0.15, 5.5 - k * 0.15)
    dab(p0[0], p0[1], 3)


# ============ 井 (upper-right) ============
# Layout: two horizontals crossing two verticals.
# h1 (top) shorter, slightly above; h2 (bottom) longer, near middle.
# Left vertical is a slight 撇 (leans left going down).
# Right vertical is a 竖 (straight).

def draw_h1():
    # Top short horizontal, slight upward tilt (right end higher).
    x0, y0 = 145, 82
    x1, y1 = 250, 72
    steps = 200
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        # Thin start, thicker middle, thin end
        r = 2.8 + 1.2 * math.sin(math.pi * t)
        dab(x, y, r)


def draw_h2():
    # Lower horizontal, longer, gentler upward tilt.
    x0, y0 = 130, 155
    x1, y1 = 270, 148
    steps = 260
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = 3.0 + 1.4 * math.sin(math.pi * t)
        dab(x, y, r)


def draw_left_pie():
    # Left leg — a 撇 that leans left going down.
    p0 = (180, 55)
    p2 = (150, 210)
    p1 = (172, 130)
    bezier_dabs(p0, p1, p2, 3.0, 2.5, steps=240)
    dab(p0[0], p0[1], 3.5)


def draw_right_shu():
    # Right leg — a nearly-straight 竖, very slight lean right at bottom.
    p0 = (230, 60)
    p2 = (238, 215)
    p1 = (235, 138)
    bezier_dabs(p0, p1, p2, 3.2, 3.0, steps=240)
    dab(p0[0], p0[1], 3.8)
    dab(p2[0], p2[1], 3.5)


draw_dot()
draw_body()
draw_h1()
draw_h2()
draw_left_pie()
draw_right_shu()
draw_pina()  # last so it sits on top at bottom

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0303_进/01_进.png"
img.save(out)
print("Saved:", out)
