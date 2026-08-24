# BANK_DEVIATION
# skipped: (no 禾 or 尔 bank primitive exists)
# reason: 称 = 禾 (grain, left) + 尔 (right); neither component has a
#   bank entry, and inline hand-render at MMH-thin ink matches the GT
#   silhouette more directly than heavy transformations of unrelated
#   primitives (e.g. bank chars whose top-pie/heng/shu geometry is
#   calligraphic-thick).
# fresh_component: he_grain_for_LR_left, er_you_for_LR_right

"""称 (cheng) — inline PIL render, MMH-thin widths ~4-5px, L-R split.

Left  = 禾 (grain radical): top-pie + heng + shu + long-pie + right-dot.
Right = 尔: top-pie + wide-heng + inner short-pie + inner right-slant +
        central shu-gou + two flanking dots.
"""

from PIL import Image, ImageDraw

W = H = 300
INK = 4  # MMH-thin per P12
img = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(img)


def line(p0, p1, width=INK):
    d.line([p0, p1], fill=0, width=width)


def dot(cx, cy, r=3):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=0)


def tapered(p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = w0 + (w1 - w0) * t0
        d.line([(xa, ya), (xb, yb)], fill=0, width=max(1, int(round(w))))


def curved_pie(p0, p1, bow=0.15, w_head=6, w_tail=2, steps=40):
    """Quadratic bezier with taper (head thicker, tail thin)."""
    x0, y0 = p0
    x1, y1 = p1
    mx = (x0 + x1) / 2
    my = (y0 + y1) / 2
    dx = x1 - x0
    dy = y1 - y0
    # perpendicular offset (bow to the LEFT of travel for 撇)
    px = -dy
    py = dx
    L = (px * px + py * py) ** 0.5 or 1
    cx = mx + px / L * bow * ((dx * dx + dy * dy) ** 0.5)
    cy = my + py / L * bow * ((dx * dx + dy * dy) ** 0.5)
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t * t * y1
        w = w_head + (w_tail - w_head) * t
        d.line([prev, (x, y)], fill=0, width=max(1, int(round(w))))
        prev = (x, y)


# ---------------------------------------------------------------
# 禾 (left half) — occupies x ~ 30..140
# ---------------------------------------------------------------
# top short 撇 (small perch)
curved_pie((100, 65), (78, 92), bow=0.20, w_head=5, w_tail=2)
# heng — spans left component width
tapered((45, 108), (135, 105), w0=3, w1=5)
# central shu (vertical) down to bottom
line((90, 108), (90, 260), width=4)
# long 撇 sweeping to lower-left
curved_pie((90, 155), (38, 225), bow=0.18, w_head=6, w_tail=2)
# right dot (na shortened as dot in radical form on the left)
tapered((92, 158), (135, 210), w0=2, w1=6)

# ---------------------------------------------------------------
# 尔 (right half) — occupies x ~ 155..275
# ---------------------------------------------------------------
# top small 撇 (perched)
curved_pie((215, 60), (192, 92), bow=0.20, w_head=5, w_tail=2)
# top heng — wide across right side
tapered((160, 108), (270, 105), w0=3, w1=5)
# left inner descending pie from heng — reaches lower-left region
curved_pie((178, 108), (158, 175), bow=0.16, w_head=5, w_tail=2)
# right inner descending slant from heng — na-like sweep
tapered((250, 108), (272, 180), w0=3, w1=6)
# central shu-gou (vertical with left hook), starts just under heng
line((215, 115), (215, 260), width=4)
# hook at bottom of shu-gou (short tick to lower-left)
tapered((215, 260), (200, 268), w0=4, w1=2)
# left inner dot (compact, leaning down-left)
tapered((198, 175), (188, 200), w0=5, w1=2)
# right inner dot (compact, leaning down-right)
tapered((233, 175), (245, 205), w0=5, w1=2)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G3_coords/attempts/p3_char_0553_称/01_称.png"
)
