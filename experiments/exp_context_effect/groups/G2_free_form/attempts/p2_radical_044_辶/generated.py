"""Render 辶 (chuo, 3-stroke radical) at 300x300, PIL brush-dabs, black on white.

辶 has 3 strokes:
  1. 点 (dot) — small teardrop, upper-left area, oriented down-right.
  2. 横折折撇 — starts below the dot, goes short-right, folds down-left,
     folds short-right, then throws a bowed 撇 down-and-left. Together
     the 2-3 folds form the "z-like" body of 辶.
  3. 平捺 (flat press) — long shallow "smile" from lower-left sweeping
     right, gently concave-up, with a broad flat foot at the right end.
     Belly of the smile dips below its endpoints slightly.

Design references GT (gt/phase2/辶.png):
- Dot sits around (95, 75), oriented like a small 撇-dot going down-left.
- The 横折折撇 body sits roughly x ∈ [70, 130], y ∈ [95, 180].
- The bottom 捺 sweeps from about (60, 210) → (250, 240) with belly
  around y=250-255 at x=155.
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


# ---------- Stroke 1: 点 (dot) ----------
# Small teardrop, upper-left. Oriented slightly down-right, ends in press.
# thin → thick teardrop
def draw_dot():
    # Thin spidery dot per GT style — shorter, less bold.
    p0 = (95, 60)
    p2 = (112, 85)
    p1 = (100, 72)
    steps = 100
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** 1.4
        r = 1.5 + (4.5 - 1.5) * tt
        dab(x, y, r)
    dab(p2[0], p2[1], 5)


# ---------- Stroke 2: 横折折撇 body ----------
# Short 横 → shoulder → short 竖-ish down → shoulder → short 横 →
# then bowed 撇 tail down-and-left.
# Referring to GT, the body is compact and to the left side.
def draw_body():
    # Thinner spidery body per GT style. Body is compact and left-of-center.
    # 横折折撇: short 横 → shoulder → down-left slant → shoulder → short 横 →
    # bowed 撇 tail. Keep tail shorter so it doesn't clash with the 平捺.
    a = (78, 118)   # start of 横 (top of body)
    b = (132, 110)  # end of 横 / first shoulder
    c = (100, 148)  # after first fold (down-left)
    dd = (140, 143) # after second fold (short rightward)
    tail_tip = (78, 205)
    r_body = 3.5

    dab(a[0], a[1], r_body + 1.5)
    line_dabs(a[0], a[1], b[0], b[1], r_body, r_body)
    dab(b[0], b[1], r_body + 1.5)
    line_dabs(b[0], b[1], c[0], c[1], r_body, r_body)
    dab(c[0], c[1], r_body + 1.5)
    line_dabs(c[0], c[1], dd[0], dd[1], r_body, r_body)
    dab(dd[0], dd[1], r_body + 1.5)
    ctrl = (130, 178)
    bezier_dabs(dd, ctrl, tail_tip, r_body + 0.5, 1.0, steps=240,
                ease=lambda t: t)


# ---------- Stroke 3: 平捺 (flat sweeping press) ----------
# Long shallow smile from lower-left up-ish, sweeping right with broad foot.
# Belly (concave-up) dips slightly. Enters where the 撇 tail lands.
def draw_pina():
    # Long shallow concave-up sweep; thinner and less thick than default 捺
    # to match GT's spidery look. Still has a broad flat foot at right.
    p0 = (60, 225)
    p2 = (258, 235)
    p1 = (155, 268)  # control pulls DOWN → concave-up belly
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


draw_dot()
draw_body()
draw_pina()

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_044_辶/01_辶.png"
img.save(out)
print("Saved:", out)
