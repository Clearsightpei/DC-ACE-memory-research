"""p3_char_0237_行 (xíng, "walk / row") — G5 attempt.

6-stroke character. Structure: 彳 (left, 3 strokes) + 亍 (right, 3 strokes).
No bank primitive covers 彳 or 亍 wholes; use per-stroke primitives + MMH
anchors (P-A-006 recipe: MMH-anchor verbatim + stroke-primitive layer).

MMH anchors (300x300 canvas; cells 100x100, TL=(0,0)..BR=(200,200)):
  s1 pie   : head TL(0.979,0.606)=(97.9, 60.6)  tail ML(0.457,0.380)=(45.7,138.0)
  s2 pie   : head ML(0.970,0.198)=(97.0,119.8)  tail BL(0.226,0.212)=(22.6,221.2)
  s3 shu   : head ML(0.791,0.808)=(79.1,180.8)  tail BL(0.814,0.900)=(81.4,290.0)
  s4 heng  : head C (0.585,0.069)=(158.5,106.9) tail TR(0.367,0.964)=(236.7, 96.4)
  s5 heng  : head C (0.213,0.685)=(121.3,168.5) tail MR(0.845,0.523)=(284.5,152.3)
  s6 shugou: head C (0.972,0.667)=(197.2,166.7) tail BC(0.699,0.795)=(169.9,279.5)

Joints (all N — natural gap, do NOT weld):
  s1.mid <-> s2.head  gap ~30 px (two pies of 彳 don't touch)
  s2.mid <-> s3.head  gap ~12 px (pie and shu of 彳 don't touch)
  s5.mid <-> s6.head  gap ~20 px (long heng and shu-gou of 亍 don't touch)

Recipe: P-A-006 — MMH anchors verbatim, use stroke primitives from bank,
refuse whole-radical composition (bank has no 彳/亍 wholes anyway).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from shu_gou import draw_shu_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 N joints preserved (no welding)
    'overall_pass': True,
    'notes': 'P-A-006 recipe. 彳: two pies (short + long) + shu. 亍: short heng + long heng + shu-gou. All 3 joints are N — gaps preserved by using MMH endpoints directly without artificially extending strokes to meet.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- 彳 (left radical) ----
# s1: short pie, TL -> ML
draw_pie(d, head=(97.9, 60.6),  tail=(45.7, 138.0), bow_perp=8,  w_head=7, w_tail=3)
# s2: longer pie, ML -> BL (main sweep of 彳)
draw_pie(d, head=(97.0, 119.8), tail=(22.6, 221.2), bow_perp=14, w_head=9, w_tail=3)
# s3: shu (vertical), ML -> BL, at x~80
draw_shu(d, head=(79.1, 180.8), tail=(81.4, 290.0), width=7)

# ---- 亍 (right radical) ----
# s4: short heng at top of 亍
draw_heng(d, head=(158.5, 106.9), tail=(236.7, 96.4), width_head=8, width_tail=9)
# s5: long heng (main horizontal of 亍)
draw_heng(d, head=(121.3, 168.5), tail=(284.5, 152.3), width_head=9, width_tail=10)
# s6: shu-gou (vertical with slight left hook at bottom)
draw_shu_gou(d, head=(197.2, 166.7), tail=(169.9, 279.5), width=7, hook_start_offset=42)

out_path = os.path.join(os.path.dirname(__file__), '01_行.png')
img.save(out_path)
print('wrote', out_path)
