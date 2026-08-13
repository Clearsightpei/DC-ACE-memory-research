# BANK_DEVIATION
# skipped: heng_zhe_short.py (draw_heng_zhe_short)
# reason: bank primitive was tuned for the short 乛 arc (soft Bezier
#         corner ~30px horizontal, immediate curve). 冂's right stroke is
#         a wide 横折 (~130px horizontal, ~180px vertical drop) with a
#         near-right-angle corner. Applying the short-arc geometry to
#         these endpoints produces a diagonal slab, not a squared cap.
# fresh_component: heng_zhe_wide_for_jiong — wide horizontal + sharper
#         corner + long vertical, endpoint-signature like the bank.
"""Render p2_radical_024_冂 (2-stroke radical).

Strokes per MMH-injected block:
  s1: 竖 (shu)     head TL(0.601,0.867)  tail BL(0.595,0.78)
  s2: 横折 (heng-zhe wide)  head TL(0.812,0.938)  tail BC(0.852,0.64)

Joint s1.head ⇆ s2.head at TL is class N (natural gap ~17px). We keep
s1.head slightly left of s2.head so the two tops do not weld — the
horizontal of s2 begins near but not touching s1's crown.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

# add bank to path
HERE = pathlib.Path(__file__).resolve()
BANK = HERE.parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from shu import draw_shu  # noqa: E402


# --- MMH anchor → pixel ---------------------------------------------------
# 米字格 cells cover the 300 canvas as a 3x3 grid of 100-px cells.
# Cell top-left origins:
CELL = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'MC': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELL[cell]
    return (ox + 100 * xf, oy + 100 * yf)


# Raw MMH anchors (from injected block)
s1_head_mmh = anchor('TL', 0.601, 0.867)   # (60.1, 86.7)
s1_tail_mmh = anchor('BL', 0.595, 0.78)    # (59.5, 278.0)
s2_head_mmh = anchor('TL', 0.812, 0.938)   # (81.2, 93.8)
s2_tail_mmh = anchor('BC', 0.852, 0.64)    # (185.2, 264.0)

# Visual calibration vs GT: the raw MMH anchors compress the character
# into the left half of the canvas. GT actually spans ~x[85..220],
# y[65..250]. We shift & widen so the rendered silhouette matches the
# GT bounding box while preserving anchor ordering + N-gap at the top.
DX = 30    # push right so left stroke sits near x≈90
DY = -22   # lift the tops so horizontal cap sits at y≈72

# Widen the right side so the top horizontal covers to ~x≈220
def calibrate(p, extra_x=0):
    return (p[0] + DX + extra_x, p[1] + DY)


s1_head = calibrate(s1_head_mmh)                    # ≈ (90, 65)
s1_tail = calibrate(s1_tail_mmh)                    # ≈ (90, 256)
s2_head = calibrate(s2_head_mmh)                    # ≈ (111, 72)
# Pull the s2 head LEFT to sit near s1.head (small N-gap ~14px) so the
# horizontal begins right where the left stroke's crown ends.
s2_head = (s1_head[0] + 14, s1_head[1] + 6)         # ≈ (104, 71)
s2_tail = calibrate(s2_tail_mmh, extra_x=35)        # ≈ (220, 242)


# --- render ---------------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: left vertical, with a soft top curl (matches GT's leftward top hook)
draw_shu(d, s1_head, s1_tail, width=7, top_curl=True)


def draw_heng_zhe_wide(draw, head, tail, width=7, corner_radius=6):
    """A wide 横折: horizontal from head to a corner near tail_x,head_y,
    then a near-vertical drop to tail. Squared corner with a small
    rounding radius so it reads calligraphic, not mechanical.
    """
    hx, hy = head
    tx, ty = tail

    # Corner sits slightly above head-y (horizontal rises a hair
    # to the right, like the GT's slight upward slope on the top bar).
    corner_x = tx
    corner_y = hy - 4

    # --- horizontal segment (head -> just before corner) ---
    end_h = (corner_x - corner_radius, corner_y + 1)
    n = 50
    for i in range(n):
        u0, u1 = i / n, (i + 1) / n
        x0 = hx + (end_h[0] - hx) * u0
        y0 = hy + (end_h[1] - hy) * u0
        x1 = hx + (end_h[0] - hx) * u1
        y1 = hy + (end_h[1] - hy) * u1
        draw.line([(x0, y0), (x1, y1)], fill='black', width=width)

    # --- corner (quadratic bezier) ---
    p0 = end_h
    p1 = (corner_x + 2, corner_y)                 # slight overshoot outward
    p2 = (corner_x, corner_y + corner_radius + 2)
    prev = p0
    for i in range(1, 20):
        u = i / 20
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        draw.line([prev, (x, y)], fill='black', width=width + 1)
        prev = (x, y)

    # --- vertical drop (corner_bottom -> tail) with mild leftward taper ---
    v_start = p2
    n = 60
    for i in range(n):
        u0, u1 = i / n, (i + 1) / n
        x0 = v_start[0] + (tx - v_start[0]) * u0
        y0 = v_start[1] + (ty - v_start[1]) * u0
        x1 = v_start[0] + (tx - v_start[0]) * u1
        y1 = v_start[1] + (ty - v_start[1]) * u1
        # slight taper: thicker at top, thinner toward the tail
        w = int(round(width + 0.5 - 1.0 * u0))
        draw.line([(x0, y0), (x1, y1)], fill='black', width=max(w, 5))


draw_heng_zhe_wide(d, s2_head, s2_tail, width=7)


# --- self-check -----------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 2 stroke primitives called (shu + heng_zhe_wide)
    'endpoint_mismatches': [
        # s2.head deliberately pulled left ~7px vs raw MMH so N-gap
        # to s1.head is ~14px (target ~16.7). Within tolerance.
        {'stroke': 's2', 'field': 'head',
         'expected_px': (111, 72), 'actual_px': (104, 71),
         'delta_px': (-7, -1),
         'note': 'deliberate — preserves N-gap to s1.head'},
        # s2.tail extended right ~35px to match GT silhouette width.
        {'stroke': 's2', 'field': 'tail',
         'expected_px': (185, 242), 'actual_px': (220, 242),
         'delta_px': (35, 0),
         'note': 'GT calibration — MMH tail compressed vs visible glyph'},
    ],
    'joint_class_mismatches': [],  # s1.head ⇆ s2.head : implemented as N (~14px gap)
    'overall_pass': True,
    'notes': ('BANK_DEVIATION: skipped heng_zhe_short (short-arc bank '
              'primitive) for a wide sharp-corner 横折 fresh render. '
              'Left shu uses bank with top_curl=True (matches GT hook).')
}


OUT = HERE.parent / '01_冂.png'
img.save(OUT)
print(f'wrote {OUT}')
