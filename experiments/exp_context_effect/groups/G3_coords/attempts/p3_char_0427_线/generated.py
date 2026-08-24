# BANK_DEVIATION
# skipped: si_zi_pang.py
# reason: si_zi_pang's (ox, oy, scale) params are unused (baked coords, always centered) — cannot slot into L-R composition as the left radical; must inline fresh.
# fresh_component: si_zi_pang_left_for_LR (compact 纟 shifted into left column)
#
# 线 = 纟 (silk radical, left) + 戋 (right, 5 strokes: two 横 stacked + long 斜钩 + short 撇 upper-right)
# L-R aspect: left ~35% width, right ~65% width. Both extend nearly full height.

from PIL import Image, ImageDraw

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
d = ImageDraw.Draw(img)


def to_px(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=40, head_ramp=0.1):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = to_px(bx, by)
        if u < head_ramp:
            w = w_head
        else:
            w = w_head + (w_tail - w_head) * ((u - head_ramp) / (1 - head_ramp))
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


def tapered_line(draw, p0, p1, w_head, w_tail, n=30):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        pt = to_px(x, y)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


# ---- LEFT: 纟 (silk radical) — compact, shifted to left column ----
# two small 撇折 hooks stacked + long 提 spanning bottom-left

def draw_pie_zhe_hook(cx, cy, size, ink=5):
    # descending 撇 stroke
    p0 = (cx + size * 0.55, cy + size * 1.15)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1, (p0[1] + p2[1]) / 2 - size * 0.1)
    tapered_bezier(d, p0, p1, p2, w_head=ink, w_tail=max(2, ink - 2), n=30)
    # rightward hook
    h0 = (cx, cy)
    h2 = (cx + size * 1.5, cy + size * 0.5)
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.1)
    tapered_bezier(d, h0, h1, h2, w_head=ink + 1, w_tail=1.5, n=40, head_ramp=0.05)


# left column: x ~ -105 to -35, taller
draw_pie_zhe_hook(cx=-80, cy=60, size=22, ink=5)   # upper 撇折
draw_pie_zhe_hook(cx=-82, cy=10, size=24, ink=5)   # middle 撇折
# 提 (rising stroke) bottom of 纟
p0 = (-105, -50)
p2 = (-30, -25)
p1 = ((p0[0] + p2[0]) / 2 - 3, (p0[1] + p2[1]) / 2 - 6)
tapered_bezier(d, p0, p1, p2, w_head=11, w_tail=1.5, n=60, head_ramp=0.08)


# ---- RIGHT: 戋 (5 strokes) ----
# stroke order: 1) upper short 横, 2) middle short 横, 3) long 斜钩 diagonal, 4) short 撇 upper-right dot-like

# 1) upper 横 — short, upper area
tapered_line(d, (0, 50), (55, 55), w_head=4, w_tail=6, n=20)

# 2) middle 横 — slightly longer/lower
tapered_line(d, (-10, 15), (60, 20), w_head=4, w_tail=6, n=20)

# 3) 斜钩 — long diagonal from upper-mid down to lower-right, with slight upward hook tip
xk0 = (-20, 65)
xk2 = (70, -100)  # bottom-right endpoint
tapered_bezier(d, xk0, (20, -20), xk2, w_head=6, w_tail=8, n=60, head_ramp=0.05)
# small hook at bottom-right (upward flick, shorter and up-right)
tapered_line(d, (70, -100), (95, -85), w_head=7, w_tail=1, n=15)

# 4) 撇 upper-right — small diagonal from upper-right down-left, short
tapered_line(d, (90, 80), (68, 55), w_head=6, w_tail=2, n=15)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0427_线/01_线.png")
print("saved")
