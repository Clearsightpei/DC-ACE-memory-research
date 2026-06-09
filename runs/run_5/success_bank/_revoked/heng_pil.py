"""横 — atomic horizontal stroke (楷书 brushwork primitive).

Tags: tag:atomic-stroke tag:heng tag:楷书 tag:PIL-renderer
Component-of: 一, 二, 三 (and any character with a 横 stroke)
Mastered: run_5 cycle 2, rubric 7/10 (dunbi=2 hudu=1 taper=1 proportion=2 overall=1)
Vision identity: PASSED (curator confirmed each cycle-2 attempt unambiguously
reads as the target character, no plausible alternate reading).

Width profile: entry-press 16 → shaft 11 → closing-press 22 (right end is
the HEAVIEST point of the stroke, per 楷书 收笔). The closing-press was
empirically pushed from the c1-target value of 19 up to 22 to make the
right-end visibly heavier than the left-end entry press.

Renderer: PIL (`draw.ellipse` per sample). The Drawer switched from
turtle+PostScript because the PS export was fragile on macOS.
Mathematically equivalent: same cubic Bezier centerline, same per-sample
`max(3, w(s))` width floor, same 220-sample count.

Reuse interface (run_5 PIL flavor):
    from heng import draw_heng
    draw_heng(pil_draw, ox=<center_x>, oy=<center_y>, length=<px>, scale=1.0)

The `pil_draw` argument is a `PIL.ImageDraw.Draw` object. Coordinates use
math-convention (y-up, origin canvas center); `to_px` translates to PIL
pixel space.
"""

from PIL import ImageDraw  # noqa: F401  (declares the interface dep)

CANVAS_W, CANVAS_H = 800, 600


def to_px(x, y):
    return (x + CANVAS_W / 2.0, CANVAS_H / 2.0 - y)


def bezier_point(s, P0, P1, P2, P3):
    u = 1.0 - s
    x = (u**3) * P0[0] + 3 * (u**2) * s * P1[0] + 3 * u * (s**2) * P2[0] + (s**3) * P3[0]
    y = (u**3) * P0[1] + 3 * (u**2) * s * P1[1] + 3 * u * (s**2) * P2[1] + (s**3) * P3[1]
    return x, y


def w_profile_heng(s):
    """entry press 16 → shaft 11 → closing press 22. Right end is heaviest."""
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
    """Walk a cubic Bezier and stamp a filled disk at each sample.
       Floor max(3, w) per §1.0 (run_5 invariant).
    """
    for i in range(samples + 1):
        s = i / samples
        w = max(3.0, w_profile(s))
        r = w / 2.0
        x, y = bezier_point(s, P0, P1, P2, P3)
        px, py = to_px(x, y)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=color)


def draw_left_foot(draw, ox, oy, scale=1.0):
    """Small angled foot at the LEFT entry of a 横 — slants up-right.
       Drawn at constant entry-press width 16."""
    flen = 14.0 * scale
    P0 = (ox - flen * 0.6, oy - flen * 0.7)
    P1 = (ox - flen * 0.4, oy - flen * 0.5)
    P2 = (ox - flen * 0.2, oy - flen * 0.2)
    P3 = (ox, oy)
    brushed_bezier(draw, P0, P1, P2, P3, lambda s: 16.0, samples=80)


def draw_right_foot(draw, ox, oy, scale=1.0):
    """Small angled foot at the RIGHT closing of a 横 — slants down-right.
       Drawn at constant CLOSING-press width 22 — does NOT taper."""
    flen = 14.0 * scale
    P0 = (ox, oy)
    P1 = (ox + flen * 0.2, oy - flen * 0.25)
    P2 = (ox + flen * 0.4, oy - flen * 0.5)
    P3 = (ox + flen * 0.6, oy - flen * 0.7)
    brushed_bezier(draw, P0, P1, P2, P3, lambda s: 22.0, samples=80)


def draw_heng(draw, ox, oy, length, scale=1.0):
    """Draw a 楷书 横 centered at (ox, oy) spanning `length` pixels.

    - left foot at entry-press width 16
    - body Bezier with slight upward tilt and gentle bow
    - right foot at closing-press width 22 (heaviest point)
    """
    half = length / 2.0
    tilt = 5.0 * scale
    left_x, left_y = ox - half, oy
    right_x, right_y = ox + half, oy + tilt

    bow = 4.0 * scale
    P0 = (left_x, left_y)
    P1 = (left_x + length * 0.30, left_y + bow + tilt * 0.2)
    P2 = (left_x + length * 0.70, right_y + bow * 0.5)
    P3 = (right_x, right_y)

    draw_left_foot(draw, left_x, left_y, scale)
    brushed_bezier(draw, P0, P1, P2, P3, w_profile_heng, samples=220)
    draw_right_foot(draw, right_x, right_y, scale)
