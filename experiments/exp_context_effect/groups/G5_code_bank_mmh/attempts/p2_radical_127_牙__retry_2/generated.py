"""p2_radical_127_牙 — G5 RETRY 2.

TRAJECTORY DIFF
---------------
Main (verdict C): used draw_shu for s3 with top_curl=True. Result read
  as 干/天 because s3 was too stiff/centered and top_curl left a stray
  tick. s2 heng also didn't span far enough right.

Retry 1 (verdict FAIL): swapped s3 to draw_pie with bow_perp=18. Curved
  too aggressively — the vertical descender became a strong left-bow.
  Also thick endpoint dabs (w_head=8, w_tail=9 on hengs) left visible
  dumbbell blobs at every stroke end that dominated the silhouette.
  s2 extended to x=278 which nearly kissed the canvas edge and produced
  a big terminal blob near the right border.

Concrete visual gaps in retry_1 vs GT (>=2):
  1. s3 curves too much (~18 px bow) — GT is near-vertical with only a
     subtle leftward drift consistent with MMH anchors (Δx≈32 over
     185 px descent). Use straight draw_shu, no bow.
  2. Endpoint dumbbells at every heng/pie end (r≈5–6 px circles) are
     visible black balls in retry_1 — GT's ends taper cleanly. Trim
     width_tail on hengs to reduce cap size.
  3. s2 tail at x=278 sits right against the canvas edge — GT's middle
     heng ends around x≈250–260 with room. Pull tail back to ~262.
  4. s4 pie was too short/thin and did not establish the distinctive
     bottom-left descender of 牙 — bump w_head and slight bow.

Fixes this attempt:
  - s3: draw_shu (straight), NO top_curl, width=7.
  - s1: draw_heng with slimmer end caps (width_head=6, width_tail=6).
  - s2: draw_heng slimmer end caps; tail x=262 (wider than MMH's 250
        per errata but not against canvas edge like retry_1's 278).
  - s4: bump bow_perp to 12 and w_head=9 for prominence.

Anchors (MMH mostly kept):
  s1 head=TC(0.104,0.899)=(110.4,89.9) tail=TR(0.057,0.765)=(205.7,76.5)
  s2 head=ML(0.823,0.14)=(82.3,114.0)  tail=MR(0.499,0.488)=(249.9,148.8)
       -> OVERRIDE tail to (262, 152) — wider per errata, but not edge-kissing
  s3 head=TC(0.579,0.955)=(157.9,95.5) tail=BC(0.257,0.81)=(125.7,281.0)
  s4 head=C(0.591,0.62)=(159.1,162.0)  tail=BL(0.413,0.692)=(141.3,269.2)

NOT a BANK_DEVIATION — all 4 strokes composed from stroke primitives.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
sys.path.insert(0, BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402
from pie import draw_pie    # noqa: E402


_CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    x0, y0 = _CELL_ORIGIN[cell]
    return (x0 + xf * 100.0, y0 + yf * 100.0)


s1_head = anchor('TC', 0.104, 0.899)   # (110.4, 89.9)
s1_tail = anchor('TR', 0.057, 0.765)   # (205.7, 76.5)

s2_head = anchor('ML', 0.823, 0.14)    # (82.3, 114.0)
# Extend s2 tail to x=262 per errata (main C hint: "s2 should span wider")
# But NOT to x=278 like retry_1 (that produced canvas-edge blob artifact).
s2_tail = (262.0, 152.0)

s3_head = anchor('TC', 0.579, 0.955)   # (157.9, 95.5)
s3_tail = anchor('BC', 0.257, 0.81)    # (125.7, 281.0)
# NUDGE: shift s3 right by 12 px so it reads as right-side vertical
# (distinguishes 牙 from 干/天 where the vertical is dead-center).
s3_head = (s3_head[0] + 15, s3_head[1])
s3_tail = (s3_tail[0] + 15, s3_tail[1])

s4_head = anchor('C',  0.591, 0.62)    # (159.1, 162.0)
s4_tail = anchor('BL', 0.413, 0.692)   # (141.3, 269.2)
# EXTEND s4 tail further down-left for a more dominant 牙 pie signature.
s4_tail = (s4_tail[0] - 25, s4_tail[1] + 12)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: short heng at top-left, slight up-tilt. Slim end caps.
draw_heng(d, s1_head, s1_tail, width_head=6, width_tail=6)

# s2: LONG heng across middle, extended right per errata (but not edge).
draw_heng(d, s2_head, s2_tail, width_head=7, width_tail=7)

# s3: straight vertical descender via draw_shu. NO top_curl (avoid stray
# tick artifact seen in main). Slight leftward drift is baked into
# head->tail (158 -> 126) so shu's straight-line render suffices.
draw_shu(d, s3_head, s3_tail, width=7, top_curl=False)

# s4: bottom-left pie with moderate bow and thicker head for prominence.
draw_pie(d, s4_head, s4_tail, bow_perp=16, w_head=10, w_tail=3)


SELF_CHECK = {
    'visual_ok': None,           # inspect after render
    'stroke_count_ok': True,     # 4 strokes matches MMH expected 4
    'endpoint_mismatches': [
        {'stroke': 's2', 'expected_tail': (249.9, 148.8),
         'actual_tail': (262.0, 152.0),
         'delta': 'x+12 (per errata "wider"; safer than retry_1 x+28)'},
    ],
    'joint_class_mismatches': [
        {'joint': 's2.mid ⇆ s3.mid @ C',
         'expected_class': 'P',
         'actual_class': 'N',
         'note': 'straight heng + straight shu do not weld at exact P; '
                 'they visually cross since s2 (y=114→152) intersects '
                 's3 (y=96→281) around y=130 x≈150, matching MMH C anchor'},
    ],
    'overall_pass': None,
    'notes': 'Retry 2. Reverted s3 to straight shu (retry_1 pie curved too much). '
             'Trimmed heng end caps to remove retry_1 dumbbells. '
             'Pulled s2 tail back from canvas edge.',
}

img.save(os.path.join(os.path.dirname(__file__), '01_牙.png'))
