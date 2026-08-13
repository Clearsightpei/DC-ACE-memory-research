"""p3_char_0091_乡 — G5 attempt (revision 1).

Structural plan: 3 strokes = 2× 撇折 (pie_zhe) + 1× long 撇 (pie).

Sibling: 幺-family (纟, 幺, 么). 乡 differs by ending in a long descending
pie rather than a ti or dian.

Revision note: initial render used MMH cell-fraction endpoints literally, which
gave near-vertical short strokes (MMH medians for 幺-family often only cover the
central portion of pie_zhe compound strokes). Overrode to match the GT silhouette:
each of the top two strokes starts upper-right and sweeps down-left with clear
bow, then flicks right at the corner. s3 is the dominant long pie sweeping to
lower-left. MMH cascade positions preserved (top→middle→bottom, right-side entry).

# BANK_DEVIATION
# skipped: none (used pie_zhe + pie as-is)
# but: MMH endpoints overridden per drawer_memory § MMH anchor calibration notes
#       (MMH gives medial segment only for 幺-family compound strokes;
#        head extended upper-right, tail extended past corner for zhe flick)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 primitives, matches MMH expected 3
    'endpoint_mismatches': [
        {'stroke': 1, 'expected_head_cell': 'TC', 'actual_head_cell': 'TC',
         'note': 'head shifted right and up ~15px for visible pie diagonal'},
        {'stroke': 2, 'expected_head_cell': 'C',  'actual_head_cell': 'C',
         'note': 'head shifted right ~10px, tail extended for zhe flick'},
        {'stroke': 3, 'expected_head_cell': 'C',  'actual_head_cell': 'C',
         'note': 'tail extended past BL bound to y=305 for full sweep'},
    ],
    'joint_class_mismatches': [],  # both N joints preserved as small gaps
    'overall_pass': True,
    'notes': ('Overrode MMH per drawer_memory MMH-calibration section: '
              'the near-vertical medians expand into visible upper-right→lower-left '
              'pie shape in the GT silhouette. Cascade positions preserved.'),
}

import sys, pathlib
from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from pie_zhe import draw_pie_zhe
from pie import draw_pie

img = Image.new('L', (300, 300), 255)
d = ImageDraw.Draw(img)

# s1 — top 撇折 (small, upper-center)
draw_pie_zhe(d,
             head=(160, 65),
             corner=(120, 118),
             tail=(158, 115),
             pie_bow=8, zhe_bow=1,
             w_head=6, w_corner=4, w_tail=3, steps=70)

# s2 — middle 撇折 (medium)
draw_pie_zhe(d,
             head=(180, 130),
             corner=(115, 195),
             tail=(160, 192),
             pie_bow=10, zhe_bow=1,
             w_head=7, w_corner=5, w_tail=3, steps=80)

# s3 — long 撇 sweeping down-left (dominant)
draw_pie(d,
         head=(200, 205),
         tail=(50, 300),
         bow_perp=18, w_head=9, w_tail=3, steps=90)

out_png = _HERE.parent / '01_乡.png'
img.save(str(out_png))
print(f'wrote {out_png}')
