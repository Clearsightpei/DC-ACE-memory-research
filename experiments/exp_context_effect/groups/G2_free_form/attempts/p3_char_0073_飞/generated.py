"""
飞 (fly) — 3 strokes:
  1) 横斜钩 (heng-xie-gou): short horizontal from left, then long diagonal
     down-right, curving into a vertical that ends with an upward flick.
  2) 撇 (pie): short slash from upper-middle down-left, sitting inside the hook.
  3) 点 (dian): short small stroke at right of the 撇.

Rendered with PIL at 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def brush_line(pts, width=8):
    """Draw a poly-line as connected round brush segments."""
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        draw.line([(x0, y0), (x1, y1)], fill="black", width=width)
    for x, y in pts:
        r = width / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def taper_line(p0, p1, w0, w1, steps=30):
    """Straight taper from p0(w0) → p1(w1)."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        r = max(0.5, w / 2)
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def bezier(p0, p1, p2, p3, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (
            (1 - t) ** 3 * p0[0]
            + 3 * (1 - t) ** 2 * t * p1[0]
            + 3 * (1 - t) * t ** 2 * p2[0]
            + t ** 3 * p3[0]
        )
        y = (
            (1 - t) ** 3 * p0[1]
            + 3 * (1 - t) ** 2 * t * p1[1]
            + 3 * (1 - t) * t ** 2 * p2[1]
            + t ** 3 * p3[1]
        )
        pts.append((x, y))
    return pts


def stamp(pts, w0, w1):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        w = w0 + (w1 - w0) * t
        r = max(0.5, w / 2)
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


# ---- Stroke 1: 横斜钩 -------------------------------------------------
# Short horizontal from the left, then long swooping curve down-right
# ending in a near-vertical tail with an upward hook.
#
# From GT: horizontal starts around (55,110), moves right to a shoulder
# near (150,95), then dives down-right in a smooth curve, becoming
# vertical near (215,245), with a small hook flicking up-left.

# 1a) short 横 (with a slight rise as it goes right)
taper_line((50, 120), (150, 100), 9, 10, steps=40)

# 1b) curved diagonal from shoulder swooping down, transitioning to
#     near-vertical on the right side (mimicking GT's straightening tail)
curve1 = bezier((150, 100), (215, 145), (220, 220), (215, 260), steps=80)
stamp(curve1, 10, 9)

# 1c) short rightward/upward tick at the bottom end of the curve
taper_line((215, 260), (223, 250), 9, 3, steps=20)

# ---- Stroke 2: 撇 -----------------------------------------------------
# Short 撇 inside the hook, upper-mid, slashing down-left.
taper_line((178, 150), (155, 185), 9, 3, steps=30)

# ---- Stroke 3: 点 / short stroke -------------------------------------
# Small stroke to the right of the 撇 (short down-left dot/tick).
taper_line((193, 165), (183, 183), 6, 3, steps=20)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0073_飞/01_飞.png"
)
