"""p3_char_0378_疝 — G5 attempt.

疝 = 疒 (sickness radical, 5 strokes) + 山 (mountain, 3 strokes) = 8 strokes.

Following P-A-006 (stroke-primitive layer, refuse whole-radical composition
when sub-component doesn't cleanly match a whole-radical bank at native
aspect). 疒 has no bank primitive; 山 bank primitive (shan_mountain) is
sized for standalone use, but here 山 is squeezed inside 疒 at the
bottom-right — different aspect and position, so we inline with stroke
primitives (P-A-007-v2 hard-check: shan_mountain native scale doesn't fit
this composition).

Per-stroke inline-reasoning trace (P-A-008):
  s1 top dot of 疒 → dian primitive (MMH anchor pair, TC region)
  s2 heng of 疒 → heng primitive (long, across top)
  s3 long pie of 疒 → pie primitive (steep, upper-right to bottom-left)
  s4 inner small dot (upper) → dian primitive (short, ML region)
  s5 inner ti (rising) → ti primitive (BL region)
  s6 middle shu of 山 → shu primitive (tall, C→BC)
  s7 竖折 base of 山 → shu_zhe primitive (L-shape at bottom-right)
  s8 right shu of 山 → shu primitive (MR→BR)

# BANK_DEVIATION
# skipped: shan_mountain.py
# reason: 山 in 疝 is squeezed into bottom-right ~90px wide vs the bank's
#         ~120px standalone layout; positioning + narrow aspect need
#         per-stroke placement from MMH anchors, not the bank's canned coords.
# fresh_component: shan_narrow_for_disease_radical (山 rendered inline via
#         shu + shu_zhe + shu primitives with MMH-anchor endpoints)
"""

import os
import sys
from PIL import Image, ImageDraw

# Add bank code dir to path
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from ti import draw_ti
from shu import draw_shu
from shu_zhe import draw_shu_zhe


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,   # 8 strokes below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'first render; will visually compare with GT after run',
}


def cell(name, xf, yf, cell_w=100):
    """Convert (cell, x_frac, y_frac) to pixel coords in a 300x300 米字格."""
    origins = {
        'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
        'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = origins[name]
    return (ox + xf * cell_w, oy + yf * cell_w)


def draw_shan_disease(draw):
    """Stroke 1: top dot of 疒 — small tapered mark, TC region."""
    # MMH: TC(0.4,0.542) → TC(0.767,0.8). Reduce bow so it reads as a dot,
    # not a curved swoop; also thin the tail.
    draw_dian(draw, cell('TC', 0.4, 0.542), cell('TC', 0.767, 0.8),
              w_head=2, w_tail=6, bow=1)

    # Stroke 2: heng of 疒 — long horizontal across top
    # MMH: C(0.084,0.166) → MR(0.353,0.017). Small N gap from s3 head.
    draw_heng(draw, cell('C', 0.084, 0.166), cell('MR', 0.353, 0.017),
              width_head=8, width_tail=9)

    # Stroke 3: long pie of 疒 — from upper-right area down to BL.
    # MMH tail y=1.064*100+200=306 overshoots the canvas; clamp to 295.
    s3_head = cell('ML', 0.861, 0.084)     # ~ (86.1, 108.4)
    s3_tail_raw = cell('BL', 0.284, 1.064) # ~ (28.4, 306.4)
    s3_tail = (s3_tail_raw[0], min(s3_tail_raw[1], 295))
    draw_pie(draw, s3_head, s3_tail, bow_perp=14, w_head=8, w_tail=3)

    # Stroke 4: inner small dot (upper 冫-like) of 疒
    # MMH: ML(0.431,0.345) → ML(0.618,0.626). Short diagonal — beef up
    # slightly so it's visible.
    draw_dian(draw, cell('ML', 0.431, 0.345), cell('ML', 0.618, 0.626),
              w_head=3, w_tail=7, bow=2)

    # Stroke 5: inner ti (rising) of 疒 at bottom-left
    # MMH: BL(0.182,0.256) → BL(0.732,0.045). Ti (rising) stroke.
    draw_ti(draw, cell('BL', 0.182, 0.256), cell('BL', 0.732, 0.045),
            w_head=8, w_tail=2)

    # Stroke 6: middle shu of 山 — vertical. MMH head y=140 lies inside
    # the 疒 body; nudge head down to y≈165 so it visually reads as the
    # top of 山's middle vertical rather than overlapping the radical.
    s6_head_raw = cell('C', 0.646, 0.403)  # (164.6, 140.3)
    s6_tail = cell('BC', 0.702, 0.408)     # (170.2, 240.8)
    s6_head = (s6_head_raw[0], 168)
    draw_shu(draw, s6_head, s6_tail, width=7)

    # Stroke 7: 竖折 base of 山 — L-shape at bottom-right.
    # Head (110.7, 199.8) — but nudge down to y≈175 so the left side of
    # 山 rises above the horizontal like the GT shows.
    s7_head_raw = cell('C', 0.107, 0.998)  # (110.7, 199.8)
    s7_tail = cell('BR', 0.297, 0.429)     # (229.7, 242.9)
    s7_head = (s7_head_raw[0], 175)
    s7_corner = (s7_head[0] + 2, s7_tail[1] + 3)
    draw_shu_zhe(draw, s7_head, s7_corner, s7_tail, width=7)

    # Stroke 8: right shu of 山 — vertical descending
    # MMH: MR(0.256,0.849) → BR(0.402,0.757). N gap from s7 mid at BR.
    draw_shu(draw, cell('MR', 0.256, 0.849), cell('BR', 0.402, 0.757),
             width=7)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shan_disease(draw)
    out = os.path.join(HERE, '01_疝.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    render()
