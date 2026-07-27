# p3_char_0060_卂 — first attempt.
# 卂 (xun) decomposed from GT PNG inspection:
#   1) Top 横 — wide horizontal spanning most of upper region.
#   2) 竖折折钩 — starts as a short 横 in the middle-left, drops as a
#      tall right-side vertical, curves and hooks up at bottom-left
#      (envelope of the character).
#   3) Small 撇 crossing through the middle 横 from upper-mid down-left.
#
# Reference frame: math coords, +y up, center of 300x300 canvas at (0,0).
# Rendering: pure PIL via a small Turtle-like wrapper `t` with .line/.ellipse.

import math
import os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


class Canvas:
    def __init__(self):
        self.img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
        self.d = ImageDraw.Draw(self.img)

    def line(self, pts, fill=(0, 0, 0), width=1):
        self.d.line(pts, fill=fill, width=width)

    def ellipse(self, box, fill=(0, 0, 0)):
        self.d.ellipse(box, fill=fill)


def to_px(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


# ----- stroke 1: top 横 -----
def draw_top_heng(t):
    thickness = 11
    x_left, y_left = to_px(-105, 75)
    x_right, y_right = to_px(105, 75)
    t.line([(x_left, y_left), (x_right, y_right)], fill=(0, 0, 0), width=thickness)


# ----- stroke 2: 横折弯钩-like envelope -----
# Top horizontal cap around y = 15, from x = -70 to x = 95.
# Right vertical from (95, 15) down to about (95, -75).
# Curve/hook: from (95, -75) sweeps left-and-slightly-up ending near (-30, -95),
# then a small tick up.
def draw_envelope(t):
    """Middle 横 (short, left half) + right descending curve with hook up.
    Matches GT: an open (not closed) shape — the middle 横 does NOT touch
    the right curve on the right; the right curve descends and curls
    back left-then-up as a hook."""
    thickness = 10
    # Middle short 横 — from left-side to about center
    a = to_px(-95, -5)
    b = to_px(10, -5)
    t.line([a, b], fill=(0, 0, 0), width=thickness)
    # Right descending curve with hook (like 乚/竖弯钩 form).
    # Head at top-right, drops down and curls left-then-up.
    x0, y0 = 55.0, 40.0     # top of the right curve (above middle 横 level)
    x1, y1 = -50.0, -90.0   # bottom-left end (hook base)
    # Two-segment bezier via one control point pulling right-down.
    mx, my = 90.0, -70.0
    n = 50
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = to_px(bx, by)
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=thickness)
        prev = (px, py)
    # Small upward hook (tapered) at the end
    hook_base = to_px(-50, -90)
    hook_tip = to_px(-62, -68)
    n_seg = 8
    for i in range(n_seg):
        u0 = i / n_seg
        u1 = (i + 1) / n_seg
        p0 = (hook_base[0] + u0 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u0 * (hook_tip[1] - hook_base[1]))
        p1 = (hook_base[0] + u1 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u1 * (hook_tip[1] - hook_base[1]))
        w = max(1, int(round((thickness - 2) * (1 - (u0 + u1) / 2) + 2)))
        t.line([p0, p1], fill=(0, 0, 0), width=w)


# ----- stroke 3: 撇 through the middle -----
# Starts thick at upper-right of middle band, tapers down-left past
# the envelope shaft to below the middle 横.
def draw_pie(t):
    x0, y0 = 15.0, 25.0     # thick head near top of middle band
    x1, y1 = -70.0, -40.0   # thin tail lower-left, below middle 横
    mx = (x0 + x1) / 2.0 - 5.0
    my = (y0 + y1) / 2.0 + 5.0
    n_segments = 50
    w_head = 9.0
    w_tail = 1.0
    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = to_px(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def main():
    t = Canvas()
    draw_top_heng(t)
    draw_envelope(t)
    draw_pie(t)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_卂.png")
    t.img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
