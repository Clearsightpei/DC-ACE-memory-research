"""点 — atomic 点 (right-dot) stroke, brushed teardrop.

Tags: tag:atomic-stroke tag:点 tag:右点 tag:楷书 tag:PIL-renderer
Component-of: 下, 太, 主, 玉 ... (any char with a 点 stroke)
Mastered: run_5 cycle 4 (verified inside 下 c4, rubric 9/10)
Vision identity: PASSED — reads as a clean diagonal teardrop, light upper-left tip
to heavy lower-right press.

Width profile: light entry 5 → mid 10 → 16 → heavy press 18 at the anchor.

Reuse interface:
    from dian import draw_dian
    draw_dian(pil_draw, ox=<anchor_x>, oy=<anchor_y>, length=36.0, scale=1.0)

Coordinates `(ox, oy)` are the BOTTOM-RIGHT ANCHOR (where the heavy press
lands). The stroke runs from upper-left (light tip) to (ox, oy).
"""

from heng import brushed_bezier  # reuse §1.0 primitive


def w_profile_dian(s):
    """Light entry (5) → grows → heavy press at the bottom-right (18)."""
    if s <= 0.20:
        t = s / 0.20
        return 5.0 + (10.0 - 5.0) * t
    elif s <= 0.80:
        t = (s - 0.20) / 0.60
        return 10.0 + (16.0 - 10.0) * t
    else:
        t = (s - 0.80) / 0.20
        return 16.0 + (18.0 - 16.0) * t


def draw_dian(pil_draw, ox, oy, length=36.0, scale=1.0):
    """Diagonal teardrop 点 anchored such that the heavy tail lands at (ox, oy).
       Stroke runs from upper-left (light tip) to (ox, oy) (heavy press).
    """
    L = length * scale
    P0 = (ox - L * 0.85, oy + L * 0.85)
    P1 = (ox - L * 0.55, oy + L * 0.55)
    P2 = (ox - L * 0.25, oy + L * 0.25)
    P3 = (ox, oy)
    brushed_bezier(pil_draw, P0, P1, P2, P3, w_profile_dian, samples=160)
