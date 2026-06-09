"""捺 — atomic 捺 (na, right-diagonal sweep with flat closing kick) — 斜捺 variant.

Tags: tag:atomic-stroke tag:捺 tag:斜捺 tag:flat-kick-tail tag:two-segment tag:楷书 tag:PIL-renderer
Component-of: 八, 人, 入, 大, 木, 火, 之 ... (any char with a 捺 stroke)
Mastered: run_5 cycle 5 (verified inside 八/人/入 c5).
Vision identity: PASSED.

This is the two-segment stitched pattern (§1.5 reborn for PIL):
- Segment A: main sweep, thin head (5) → 8 → 14 → 18 toward the tail.
- Segment B: short flat kick (出锋), width 18 → hold 16 (25%) → release 3.

The kick is its own brushed Bezier extending from the main-sweep tail roughly
horizontally to the right (slight downward dip then leveling off).

Reuse interface:
    from na import draw_na
    draw_na(pil_draw, head_x=<upper_left_x>, head_y=<upper_left_y>,
            tail_x=<lower_right_x>, tail_y=<lower_right_y>,
            scale=1.0, kick_len_frac=0.22)

`kick_len_frac` is the kick length as a fraction of the main-sweep chord length.
"""

from heng import brushed_bezier  # reuse §1.0 primitive


def w_profile_na_main(s):
    """Thin head 5 → 8 → 14 → 18 (heavy toward the tail)."""
    if s <= 0.25:
        t = s / 0.25
        return 5.0 + (8.0 - 5.0) * t
    elif s <= 0.70:
        t = (s - 0.25) / 0.45
        return 8.0 + (14.0 - 8.0) * t
    else:
        t = (s - 0.70) / 0.30
        return 14.0 + (18.0 - 14.0) * t


def w_profile_na_kick(s):
    """Press 18 → hold 16 (to 50%) → release to 3."""
    if s <= 0.25:
        return 18.0
    elif s <= 0.50:
        t = (s - 0.25) / 0.25
        return 18.0 + (16.0 - 18.0) * t
    else:
        t = (s - 0.50) / 0.50
        return 16.0 + (3.0 - 16.0) * t


def draw_na(pil_draw, head_x, head_y, tail_x, tail_y, scale=1.0, kick_len_frac=0.22):
    """Draw a 捺 with main sweep + flat closing kick.

    Main sweep bows toward the lower-left side of the chord (gentle belly).
    Kick extends from the main-sweep tail roughly horizontally to the right.
    """
    dx = tail_x - head_x
    dy = tail_y - head_y
    chord_len = (dx * dx + dy * dy) ** 0.5
    bow = 0.08 * chord_len
    # Perpendicular toward the "lower-left" side of the chord (negative math-y offset):
    px_u = dy / chord_len
    py_u = -dx / chord_len
    P0 = (head_x, head_y)
    P1 = (head_x + dx * 0.30 + px_u * bow * 0.5, head_y + dy * 0.30 + py_u * bow * 0.5)
    P2 = (head_x + dx * 0.65 + px_u * bow, head_y + dy * 0.65 + py_u * bow)
    P3 = (tail_x, tail_y)
    brushed_bezier(pil_draw, P0, P1, P2, P3, w_profile_na_main, samples=260)

    # Flat kick: short segment extending from tail to the right.
    kick_dx = chord_len * kick_len_frac
    kick_dy = -chord_len * 0.02
    K0 = (tail_x, tail_y)
    K1 = (tail_x + kick_dx * 0.35, tail_y + kick_dy * 0.5)
    K2 = (tail_x + kick_dx * 0.70, tail_y + kick_dy * 0.9)
    K3 = (tail_x + kick_dx, tail_y + kick_dy)
    brushed_bezier(pil_draw, K0, K1, K2, K3, w_profile_na_kick, samples=140)
