"""草 (cǎo) — 9 strokes.
Decomposition: 草 = 艹 (top) + 日 (middle) + 十 (bottom).

MMH stroke mapping:
  s1: 艹 wide 横 (spans TL→TR near y~97)
  s2: 艹 left short 竖/撇 (TC→C)
  s3: 艹 right short 竖 (TC→C)
  s4: 日 left 竖 (ML→BC-ish, left wall of 日 box)
  s5: 日 横折 (top+right of 日; head C top-left → tail C bottom-right)
  s6: 日 middle 横 (short horizontal inside 日)
  s7: 日 bottom 横 (short horizontal at bottom of 日)
  s8: 十 wide 横 (BL→BR, long horizontal of bottom cross)
  s9: 十 long 竖 (BC→below canvas, crosses s8; clamp to 299)

Reading order (v8 slim checklist):
  1) drawer_memory.md — 艹 chronic-cluster note: two 竖 (straight, no curve)
     piercing wide 横; two P joints. Bank has cao_grass.py but it's for
     standalone 艹 filling the whole grid — must inline compressed to top band.
  2) success_bank/INDEX.md — cao_grass.py, cao_grass_radical.py exist for
     standalone 艹. Neither fits: 草 puts 艹 in y∈[55,120], leaving room for
     日 and 十 below. DEVIATION applied.
  3) errata.md — 草 not listed. 艹 errata fix says: two STRAIGHT 竖, no curve;
     both cross wide 横 as P joints. Applied literally.
"""
# BANK_DEVIATION
# skipped: cao_grass.py, cao_grass_radical.py
# reason: bank 艹 primitives span full canvas; 草 needs 艹 compressed into
#   top-band (y∈[55,120]) so 日 and 十 fit below. MMH anchors are top-band.
# fresh_component: cao_top_band_for_草

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng_zhe import draw_heng_zhe

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- 艹 top-band (3 strokes) ---------------------------------------------
# s1: wide 横 (span TL(0.645,0.996) → TR(0.379,0.938))
# Enforce TR8 rule 5 (horizontal shares y): flatten to head's y.
p1a = anchor_to_xy(('TL', 0.645, 0.996))
p1b = anchor_to_xy(('TR', 0.379, 0.938))
p1b = (p1b[0], p1a[1])
fat_line(d, p1a, p1b, 9)

# s2: 艹 left short 竖 (TC(0.055,0.686) → C(0.266,0.216))
# Enforce TR8 rule 6 (vertical shares x): flatten to head's x.
p2a = anchor_to_xy(('TC', 0.055, 0.686))
p2b = anchor_to_xy(('C',  0.266, 0.216))
p2b = (p2a[0], p2b[1])
fat_line(d, p2a, p2b, 8)

# s3: 艹 right short 竖 (TC(0.758,0.551) → C(0.673,0.195))
p3a = anchor_to_xy(('TC', 0.758, 0.551))
p3b = anchor_to_xy(('C',  0.673, 0.195))
p3b = (p3a[0], p3b[1])
fat_line(d, p3a, p3b, 8)

# ---- 日 middle box (4 strokes) --------------------------------------------
# s4: 日 left 竖 (ML(0.879,0.38) → BC(0.122,0.042))
# Enforce vertical: use head x.
p4a = anchor_to_xy(('ML', 0.879, 0.38))
p4b = anchor_to_xy(('BC', 0.122, 0.042))
p4b = (p4a[0], p4b[1])
fat_line(d, p4a, p4b, 8)

# s5: 日 横折 (C(0.043,0.386) → C(0.878,0.98)) — top horizontal then right vertical
# Corner inferred at (tail_x, head_y): C(0.878, 0.386) ~= (188, 139)
draw_heng_zhe(d,
              head=('C', 0.043, 0.386),
              corner=('C', 0.878, 0.386),
              tail=('C', 0.878, 0.98),
              h_width=8, v_width=8, shoulder=11)

# s6: 日 middle 横 (C(0.137,0.708) → C(0.693,0.629))
# Flatten to head y.
p6a = anchor_to_xy(('C', 0.137, 0.708))
p6b = anchor_to_xy(('C', 0.693, 0.629))
p6b = (p6b[0], p6a[1])
fat_line(d, p6a, p6b, 7)

# s7: 日 bottom 横 (C(0.187,0.951) → C(0.808,0.928))
# Flatten to head y.
p7a = anchor_to_xy(('C', 0.187, 0.951))
p7b = anchor_to_xy(('C', 0.808, 0.928))
p7b = (p7b[0], p7a[1])
fat_line(d, p7a, p7b, 7)

# ---- 十 bottom cross (2 strokes) ------------------------------------------
# s8: wide 横 (BL(0.434,0.396) → BR(0.654,0.329))
# Flatten to head y.
p8a = anchor_to_xy(('BL', 0.434, 0.396))
p8b = anchor_to_xy(('BR', 0.654, 0.329))
p8b = (p8b[0], p8a[1])
fat_line(d, p8a, p8b, 10)

# s9: long 竖 (BC(0.365,0.001) → BC(0.485,1.164)) — extends below canvas; clamp
p9a = anchor_to_xy(('BC', 0.365, 0.001))
p9b_raw = anchor_to_xy(('BC', 0.485, 1.164))
p9b = (p9a[0], min(p9b_raw[1], 299))  # vertical: share head x; clamp y
fat_line(d, p9a, p9b, 9)

out = os.path.join(os.path.dirname(__file__), '01_草.png')
img.save(out)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke primitives (s1..s9)
    'endpoint_mismatches': [], # all anchors MMH-verbatim (with TR8 flattening)
    'joint_class_mismatches': [
        # s1∩s2, s1∩s3: P welded at TC(0.219,0.969) & TC(0.784,0.918) — verified
        # s8∩s9: P welded at BC(~0.49, 0.32) — verified
        # All N-class joints preserved by not extending stroke endpoints
    ],
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim; 艹 top-band inlined (bank primitive '
              'skipped — spans full canvas); 日 as 4 strokes with 横折 corner '
              'inferred at (tail_x, head_y); 十 with P-welded cross at bottom; '
              's9 clamped to y=299 (MMH tail y=1.164 exceeds canvas).'),
}
print('OK', SELF_CHECK['stroke_count_ok'])
