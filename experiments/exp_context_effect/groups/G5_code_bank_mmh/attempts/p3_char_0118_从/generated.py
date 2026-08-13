# BANK_DEVIATION
# skipped: ren.py (whole-radical primitive with ox/oy/scale API)
# reason: 从 is two 人 side-by-side with distinct sizes (left 人 smaller/compressed,
#         right 人 larger) and specific MMH endpoints that don't match ren.py's fixed
#         internal proportions. Composing via stroke-level pie.py + na.py primitives
#         with per-stroke MMH endpoints preserves the correct asymmetry.
# fresh_component: cong_two_ren_asymmetric (composed inline, not promoted here)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,      # 4 strokes: pie L, na L, pie R, na R
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 3 joints are N (natural gaps preserved)
    'overall_pass': None,
    'notes': 'Inlined pie/na for both 人 halves; left 人 compressed (short na), right 人 full.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- Stroke 1: left 人 pie ---
# MMH head ('TL', 0.753, 0.949) -> (75.3, 94.9)
# MMH tail ('BL', 0.158, 0.868) -> (15.8, 286.8)
draw_pie(d, head=(75.3, 94.9), tail=(15.8, 286.8),
         bow_perp=14, w_head=8, w_tail=3)

# --- Stroke 2: left 人 na (short — this 人 is compressed to leave room for right 人)
# MMH head ('BL', 0.932, 0.057) -> (93.2, 205.7)
# MMH tail ('BC', 0.298, 0.52)  -> (129.8, 252.0)
# Short na: shallower bow, moderate taper.
draw_na(d, head=(93.2, 205.7), tail=(129.8, 252.0),
        bow_perp=6, w_head=3, w_tail=8)

# --- Stroke 3: right 人 pie ---
# MMH head ('TC', 0.737, 0.773) -> (173.7, 77.3)
# MMH tail ('BC', 0.072, 0.938) -> (107.2, 293.8)
draw_pie(d, head=(173.7, 77.3), tail=(107.2, 293.8),
         bow_perp=14, w_head=8, w_tail=3)

# --- Stroke 4: right 人 na ---
# MMH head ('C',  0.904, 0.948) -> (190.4, 194.8)
# MMH tail ('BR', 0.903, 0.889) -> (290.3, 288.9)
draw_na(d, head=(190.4, 194.8), tail=(290.3, 288.9),
        bow_perp=12, w_head=4, w_tail=11)

out = os.path.join(os.path.dirname(__file__), '01_从.png')
img.save(out)
print('Wrote', out)
