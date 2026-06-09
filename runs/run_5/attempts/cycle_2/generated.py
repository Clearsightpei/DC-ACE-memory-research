"""Cycle 2 — Drawer attempt for 一, 二, 三.

Key fix from sandbox: width profile is entry-press (16) → shaft (11) →
closing-press (19), with the RIGHT END being the heaviest point of the
stroke. This is the 楷书 起笔/行笔/收笔 pattern.

Each 横 is drawn as a smooth cubic Bezier centerline with a per-sample
pensize, plus small angled "feet" at both ends matching the GT visual.

Rendered with PIL directly (drawing small filled circles along each
Bezier sample) rather than turtle.PostScript — equivalent
mathematically (smooth Bezier with per-sample pensize), more reliable
on macOS.
"""

import os
from PIL import Image, ImageDraw

CANVAS_W, CANVAS_H = 800, 600


# ---------------------------------------------------------------------------
# Coordinate system: math-convention (y-up) centered at canvas middle.
# We convert to PIL pixel coords (y-down, origin top-left) in `to_px`.
# ---------------------------------------------------------------------------

def to_px(x, y):
    return (x + CANVAS_W / 2.0, CANVAS_H / 2.0 - y)


# ---------------------------------------------------------------------------
# Brushwork primitives (principle §1.0)
# ---------------------------------------------------------------------------

def bezier_point(s, P0, P1, P2, P3):
    """Cubic Bezier at parameter s in [0,1]."""
    u = 1.0 - s
    x = (u * u * u) * P0[0] + 3 * (u * u) * s * P1[0] + 3 * u * (s * s) * P2[0] + (s * s * s) * P3[0]
    y = (u * u * u) * P0[1] + 3 * (u * u) * s * P1[1] + 3 * u * (s * s) * P2[1] + (s * s * s) * P3[1]
    return x, y


def w_profile_heng(s):
    """Width profile for 楷书 横:
       entry press 16 → shaft 11 → closing press 19.
       Right end (s≈1) is the HEAVIEST point."""
    if s <= 0.10:
        return 16.0
    elif s <= 0.20:
        t = (s - 0.10) / 0.10
        return 16.0 + (11.0 - 16.0) * t
    elif s <= 0.80:
        return 11.0
    elif s <= 0.95:
        t = (s - 0.80) / 0.15
        return 11.0 + (22.0 - 11.0) * t
    else:
        return 22.0


def brushed_bezier(draw, P0, P1, P2, P3, w_profile, samples=220, color=(0, 0, 0)):
    """Walk a cubic Bezier with per-sample pensize.
       Draw a filled circle (disk) at each sample — equivalent to a
       pen-stroke with that radius. Floor max(3, w) per §1.0.
    """
    for i in range(samples + 1):
        s = i / samples
        w = max(3.0, w_profile(s))
        r = w / 2.0
        x, y = bezier_point(s, P0, P1, P2, P3)
        px, py = to_px(x, y)
        draw.ellipse(
            [px - r, py - r, px + r, py + r],
            fill=color,
        )


# ---------------------------------------------------------------------------
# Feet helpers
# ---------------------------------------------------------------------------

def draw_left_foot(draw, ox, oy, scale=1.0):
    """Small angled foot at the LEFT entry of a 横 — slants up-right
       into the body. Drawn at entry-press width (16) throughout."""
    flen = 14.0 * scale
    P0 = (ox - flen * 0.6, oy - flen * 0.7)
    P1 = (ox - flen * 0.4, oy - flen * 0.5)
    P2 = (ox - flen * 0.2, oy - flen * 0.2)
    P3 = (ox, oy)
    brushed_bezier(draw, P0, P1, P2, P3, lambda s: 16.0, samples=80)


def draw_right_foot(draw, ox, oy, scale=1.0):
    """Small angled foot at the RIGHT closing of a 横 — slants down-right.
       Drawn at the CLOSING-PRESS width (19) — does NOT taper."""
    flen = 14.0 * scale
    P0 = (ox, oy)
    P1 = (ox + flen * 0.2, oy - flen * 0.25)
    P2 = (ox + flen * 0.4, oy - flen * 0.5)
    P3 = (ox + flen * 0.6, oy - flen * 0.7)
    brushed_bezier(draw, P0, P1, P2, P3, lambda s: 22.0, samples=80)


# ---------------------------------------------------------------------------
# §2.1 reusable primitive
# ---------------------------------------------------------------------------

def draw_heng(draw, ox, oy, length, scale=1.0):
    """Draw a 楷书 横 centered at (ox, oy) spanning `length` pixels.

    - left foot at entry-press width 16
    - body Bezier with slight upward tilt and gentle bow, width
      profile entry→shaft→closing-press
    - right foot at closing-press width 19 (heaviest point)
    """
    half = length / 2.0
    tilt = 5.0 * scale          # slight upward slant (right higher than left)
    left_x, left_y = ox - half, oy
    right_x, right_y = ox + half, oy + tilt

    bow = 4.0 * scale           # very gentle upward arc (hudu)
    P0 = (left_x, left_y)
    P1 = (left_x + length * 0.30, left_y + bow + tilt * 0.2)
    P2 = (left_x + length * 0.70, right_y + bow * 0.5)
    P3 = (right_x, right_y)

    draw_left_foot(draw, left_x, left_y, scale)
    brushed_bezier(draw, P0, P1, P2, P3, w_profile_heng, samples=220)
    draw_right_foot(draw, right_x, right_y, scale)


# ---------------------------------------------------------------------------
# Characters
# ---------------------------------------------------------------------------

def draw_yi(draw):
    """一 — single horizontal stroke, centered lower-middle."""
    draw_heng(draw, ox=0, oy=-30, length=280, scale=1.0)


def draw_er(draw):
    """二 — two stacked 横: top short, bottom long."""
    draw_heng(draw, ox=0, oy=60, length=190, scale=0.85)
    draw_heng(draw, ox=0, oy=-70, length=280, scale=1.0)


def draw_san(draw):
    """三 — three stacked 横, bottom longest."""
    draw_heng(draw, ox=0, oy=90, length=200, scale=0.85)
    draw_heng(draw, ox=0, oy=0, length=210, scale=0.85)
    draw_heng(draw, ox=0, oy=-90, length=310, scale=1.0)


# ---------------------------------------------------------------------------
# Render driver
# ---------------------------------------------------------------------------

def render_task(draw_fn, out_path):
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), "white")
    draw = ImageDraw.Draw(img)
    draw_fn(draw)
    img.save(out_path, "PNG")


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    render_task(draw_yi, os.path.join(out_dir, "01_一.png"))
    render_task(draw_er, os.path.join(out_dir, "02_二.png"))
    render_task(draw_san, os.path.join(out_dir, "03_三.png"))


if __name__ == "__main__":
    main()
