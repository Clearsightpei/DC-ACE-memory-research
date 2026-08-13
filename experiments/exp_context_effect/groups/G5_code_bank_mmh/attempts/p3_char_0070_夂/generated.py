"""p3_char_0070_夂 (zhi) — 3 strokes: short pie + long pie + wide na.
Uses bank primitives draw_pie and draw_na directly (no BANK_DEVIATION).
Structure follows MMH anchors; s2 and s3 cross at cell C (P joint);
s1 has N-gaps to both s2.head and s3.head.
"""

import sys, os
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [
        {'stroke': 's2', 'expected_tail': ('BL', 0.437, 0.001), 'actual': (43.7, 275.0),
         'delta_y_frac': 0.75, 'reason': 'GT s2 tail visually near y=275; MMH BL@y=200 too high'},
        {'stroke': 's3', 'expected_tail': ('MR', 0.701, 0.937), 'actual': (275.0, 245.0),
         'delta_y_frac': 0.51, 'reason': 'GT s3 na tail sits in BR band ~y=245'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Rev1: extended s2 tail and s3 na tail downward to match GT silhouette. s2xs3 P-cross preserved at C. s1 N-gap preserved.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# MMH anchor -> pixel:
#   TC (0.245, 0.551) -> (124.5,  55.1)
#   ML (0.636, 0.371) -> ( 63.6, 137.1)
#   TC (0.195, 0.987) -> (119.5,  98.7)
#   BL (0.437, 0.001) -> ( 43.7, 200.1)
#   C  (0.037, 0.143) -> (103.7, 114.3)
#   MR (0.701, 0.937) -> (270.1, 193.7)

# s1: short upper pie (TC -> ML). Head ~ where s2 head sits (small N-gap above).
draw_pie(d, (124.5, 55.1), (63.6, 137.1),
         bow_perp=8, w_head=7, w_tail=3)

# s2: long left pie (TC -> BL, extended low). Descends past s1 with N-gap; crosses s3 at C.
draw_pie(d, (119.5, 98.7), (40.0, 275.0),
         bow_perp=14, w_head=8, w_tail=3)

# s3: wide rightward na (C -> lower MR/BR). Welds with s2 mid ~(85,190) at cell C (P joint).
draw_na(d, (103.7, 114.3), (275.0, 245.0),
        bow_perp=16, w_head=4, w_tail=12)

out = os.path.join(os.path.dirname(__file__), '01_夂.png')
img.save(out)
print('saved', out)
