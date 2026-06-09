"""撇 — atomic 撇 (pie, diagonal sweep, tapered tip) — 斜撇 variant.

Tags: tag:atomic-stroke tag:撇 tag:斜撇 tag:tapered-tip tag:楷书 tag:PIL-renderer
Component-of: 八, 人, 入, 大, 木, 千, 才, 不 ... (any char with a 撇 stroke)
Mastered: run_5 cycle 5 (verified inside 八/人 c5 with rubric ≥ 7).
Vision identity: PASSED.

Width profile: heavy head 18 → 14 → 11 → 8 → taper to 3 (the §1.0 floor).
Centerline: cubic Bezier with controls offset on the UPPER side of the chord
(gentle concave-down arc).

Reuse interface:
    from pie import draw_pie
    draw_pie(pil_draw, head_x=<upper_right_x>, head_y=<upper_right_y>,
             tail_x=<lower_left_x>, tail_y=<lower_left_y>, scale=1.0)

Coordinates use math-convention (y-up, origin canvas center).
"""

from heng import brushed_bezier  # reuse §1.0 primitive


def w_profile_pie(s):
    if s <= 0.08:
        return 18.0
    elif s <= 0.20:
        t = (s - 0.08) / 0.12
        return 18.0 + (14.0 - 18.0) * t
    elif s <= 0.50:
        t = (s - 0.20) / 0.30
        return 14.0 + (11.0 - 14.0) * t
    elif s <= 0.75:
        t = (s - 0.50) / 0.25
        return 11.0 + (8.0 - 11.0) * t
    else:
        t = (s - 0.75) / 0.25
        return 8.0 + (3.0 - 8.0) * t


def draw_pie(pil_draw, head_x, head_y, tail_x, tail_y, scale=1.0):
    """Draw a 撇 from (head_x, head_y) to (tail_x, tail_y).

    Control points are offset toward the upper-right of the chord so the
    centerline bows above the straight head-to-tail line (concave-down arc).
    """
    dx = tail_x - head_x
    dy = tail_y - head_y
    chord_len = (dx * dx + dy * dy) ** 0.5
    bow = 0.05 * chord_len
    # Perpendicular pointing to the "above the chord" side (positive math-y offset):
    px_u = dy / chord_len
    py_u = -dx / chord_len
    P0 = (head_x, head_y)
    P1 = (head_x + dx * 0.33 + px_u * bow, head_y + dy * 0.33 + py_u * bow)
    P2 = (head_x + dx * 0.66 + px_u * bow * 0.7, head_y + dy * 0.66 + py_u * bow * 0.7)
    P3 = (tail_x, tail_y)
    brushed_bezier(pil_draw, P0, P1, P2, P3, w_profile_pie, samples=260)
