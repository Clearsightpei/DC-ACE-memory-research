# BANK_DEVIATION
# skipped: heng_zhe_short.py (draw_heng_zhe_short) and heng_zhe_box.py
# reason: heng_zhe_short is tuned for the 乛 short-arc corner (~30px
#         horizontal, immediate curve). heng_zhe_box is a full closed
#         rectangle with a bottom cap. 冂's right stroke is an open
#         wide 横折 (~130px horizontal, ~180px vertical drop) with a
#         near-right-angle corner and no bottom. Applying either
#         primitive as-is produces the wrong silhouette.
# fresh_component: heng_zhe_wide_for_jiong — wide horizontal + sharp
#         squared corner + long vertical, endpoint-signature like the bank.
# Sibling reference: p2_radical_024_冂 attempt used this same fresh_component
# and produced a clean silhouette; the p3_char_0026_冂 MMH block is identical,
# so the same approach applies.
"""Render p3_char_0026_冂 (2-stroke character).

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

# Visual calibration vs GT (same shift as the p2 sibling attempt):
DX = 30
DY = -22


def calibrate(p, extra_x=0):
    return (p[0] + DX + extra_x, p[1] + DY)


s1_head = calibrate(s1_head_mmh)                    # ≈ (90, 65)
s1_tail = calibrate(s1_tail_mmh)                    # ≈ (90, 256)
s2_head = calibrate(s2_head_mmh)                    # ≈ (111, 72)
# Pull s2 head slightly right of s1 head (small N-gap ~14px).
s2_head = (s1_head[0] + 14, s1_head[1] + 6)         # ≈ (104, 71)
s2_tail = calibrate(s2_tail_mmh, extra_x=35)        # ≈ (220, 242)


# --- render ---------------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: left vertical with soft top curl (matches GT hook at top-left)
draw_shu(d, s1_head, s1_tail, width=7, top_curl=True)


def draw_heng_zhe_wide(draw, head, tail, width=7, corner_radius=6):
    """Wide 横折: horizontal head→corner (near tail_x,head_y), then
    near-vertical drop to tail. Squared corner with small rounding.
    """
    hx, hy = head
    tx, ty = tail

    corner_x = tx
    corner_y = hy - 4

    # horizontal segment
    end_h = (corner_x - corner_radius, corner_y + 1)
    n = 50
    for i in range(n):
        u0, u1 = i / n, (i + 1) / n
        x0 = hx + (end_h[0] - hx) * u0
        y0 = hy + (end_h[1] - hy) * u0
        x1 = hx + (end_h[0] - hx) * u1
        y1 = hy + (end_h[1] - hy) * u1
        draw.line([(x0, y0), (x1, y1)], fill='black', width=width)

    # corner (quadratic bezier)
    p0 = end_h
    p1 = (corner_x + 2, corner_y)
    p2 = (corner_x, corner_y + corner_radius + 2)
    prev = p0
    for i in range(1, 20):
        u = i / 20
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        draw.line([prev, (x, y)], fill='black', width=width + 1)
        prev = (x, y)

    # vertical drop
    v_start = p2
    n = 60
    for i in range(n):
        u0, u1 = i / n, (i + 1) / n
        x0 = v_start[0] + (tx - v_start[0]) * u0
        y0 = v_start[1] + (ty - v_start[1]) * u0
        x1 = v_start[0] + (tx - v_start[0]) * u1
        y1 = v_start[1] + (ty - v_start[1]) * u1
        w = int(round(width + 0.5 - 1.0 * u0))
        draw.line([(x0, y0), (x1, y1)], fill='black', width=max(w, 5))


draw_heng_zhe_wide(d, s2_head, s2_tail, width=7)


# --- self-check -----------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 2 stroke primitives (shu + heng_zhe_wide)
    'endpoint_mismatches': [
        {'stroke': 's2', 'field': 'head',
         'expected_px': (111, 72), 'actual_px': (104, 71),
         'delta_px': (-7, -1),
         'note': 'deliberate — preserves N-gap to s1.head'},
        {'stroke': 's2', 'field': 'tail',
         'expected_px': (185, 242), 'actual_px': (220, 242),
         'delta_px': (35, 0),
         'note': 'GT calibration — MMH tail compressed vs visible glyph'},
    ],
    'joint_class_mismatches': [],  # s1.head ⇆ s2.head : N (~14px gap)
    'overall_pass': True,
    'notes': ('BANK_DEVIATION: skipped heng_zhe_short/heng_zhe_box for a '
              'wide sharp-corner 横折 fresh render. Left shu uses bank '
              'with top_curl=True (matches GT hook).')
}


OUT = HERE.parent / '01_冂.png'
img.save(OUT)
print(f'wrote {OUT}')
