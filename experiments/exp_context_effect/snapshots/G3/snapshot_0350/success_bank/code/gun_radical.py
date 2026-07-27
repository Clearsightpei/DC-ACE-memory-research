# gun_radical.py — 丨 (gun) radical, 1 stroke.
# Bootstrap batch (position 33) — human PASSed the coord render.
#
# The PASSing render (attempts/p2_radical_001_丨/generated.py) is NOT a
# plain shu — it has a rightward-scooping head (~10 px arc) followed by
# a straight vertical descent, at thickness ~10 (vs shu's default 12).
# Recorded verbatim from the passing attempt.

from PIL import ImageDraw  # noqa: F401 (documents expected `t` type)

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def draw_gun_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw 丨 radical: rightward-scooping head + straight vertical shaft.

    Canonical unit: head arc spans math (-6,+85)→(+4,+60), shaft (+4,+60)→(+4,-100).
    Thickness 10 px. (ox, oy, scale) offset and scale everything from that.
    """
    thickness = max(1, int(round(10 * scale)))
    head_pts = [
        _to_pixel(ox + (-6) * scale, oy + 85 * scale),
        _to_pixel(ox + (-3) * scale, oy + 80 * scale),
        _to_pixel(ox + 0 * scale,    oy + 74 * scale),
        _to_pixel(ox + 3 * scale,    oy + 68 * scale),
        _to_pixel(ox + 4 * scale,    oy + 60 * scale),
    ]
    shaft_top = _to_pixel(ox + 4 * scale, oy + 60 * scale)
    shaft_bot = _to_pixel(ox + 4 * scale, oy + (-100) * scale)

    t.line(head_pts, fill=(0, 0, 0), width=thickness, joint="curve")
    t.line([shaft_top, shaft_bot], fill=(0, 0, 0), width=thickness)
    r = thickness / 2
    hx, hy = head_pts[0]
    t.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))
    bx, by = shaft_bot
    t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
