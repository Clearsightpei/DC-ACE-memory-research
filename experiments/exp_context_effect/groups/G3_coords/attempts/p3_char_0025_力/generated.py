"""力 (li, 'power') — 2 strokes: 横折钩 + 撇.

Fully inlined coord composition for G3 (numeric-coord memory format).
Drawn against the clean GT (regenerated). Prior attempt used the frozen
heng_zhe_gou primitive which is too rectangular for 力 — the GT shows
a shorter top-horizontal, a curved (bowed-out-right) vertical, and a
long sweeping 撇 that starts above/at the horizontal and reaches near
the bottom-left corner.
"""
from PIL import Image, ImageDraw

CANVAS = 300
OUT = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0025_力/01_力.png"


def to_px(ox, oy):
    """Math coords (+y up, center origin) -> PIL px."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def tapered_line(draw, x0, y0, x1, y1, w0, w1, steps=24):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * (u0 + u1) / 2)))
        pa = to_px(xa, ya)
        pb = to_px(xb, yb)
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


def tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    """Quadratic bezier with linear taper w0->w1."""
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        pt = to_px(bx, by)
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w)
            r = w / 2
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Stroke 1: 横折钩 (horizontal + bowed-down vertical + tiny hook)
# GT: top-horizontal is fairly short (~60 wide), slightly slanting up-right;
# then turns down and curves out-right slightly; ends with small hook.

# --- 横 (short horizontal top): from x=-15..58, y ~55 (slight slant up)
h_x0, h_y0 = -18, 50
h_x1, h_y1 = 58, 60
tapered_line(draw, h_x0, h_y0, h_x1, h_y1, w0=6, w1=9, steps=20)

# Corner joint (small filled circle)
cx, cy = to_px(h_x1, h_y1)
r = 5
draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

# --- 竖 (curved vertical, bowed out to the right slightly), ends at (~50, -80)
v_end_x, v_end_y = 48, -80
# Quadratic bezier: start at corner, control pulled right for gentle bow
ctrl_x = 60
ctrl_y = -15
tapered_bezier(draw, (h_x1, h_y1), (ctrl_x, ctrl_y), (v_end_x, v_end_y),
               w0=9, w1=7, steps=50)

# --- 钩 (small hook at bottom, pointing up-and-left)
hook_end_x, hook_end_y = v_end_x - 18, v_end_y + 16
tapered_line(draw, v_end_x, v_end_y, hook_end_x, hook_end_y, w0=8, w1=1, steps=14)

# Stroke 2: 撇 (long sweeping left-falling stroke)
# GT: head at ~top of horizontal (slightly above), sweeps down-left across
# the horizontal, curves out to bottom-left corner.
# Head at (~5, 75) — above the 横 slightly; tail at (~-105, -115) near bottom-left.
pie_head = (10, 95)   # above the 横 so 撇 crosses through it
pie_tail = (-115, -115)
# Control point pulled to left of chord to bow the sweep
pie_ctrl = ((pie_head[0] + pie_tail[0]) / 2 - 25,
            (pie_head[1] + pie_tail[1]) / 2 + 10)
tapered_bezier(draw, pie_head, pie_ctrl, pie_tail, w0=9, w1=1, steps=70)

img.save(OUT)
print("saved", OUT)
