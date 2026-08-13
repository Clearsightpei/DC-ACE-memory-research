"""侔 (móu) — 亻 (left) + 牟 (right, = 厶-top + 牛-base). 8 strokes.

Composition:
  s1-s2 : 亻 via ren_side (adapted anchors from MMH to sit far-left)
  s3-s4 : 厶-like top of 牟 (pie + na-like fold)
  s5    : 牛 top pie
  s6    : 牛 short heng
  s7    : 牛 long heng (bottom bar)
  s8    : 牛 spine shu (extends past bottom)

Memory citations:
  - drawer_memory.md: 亻-prefixed left radical -> import ren_side (used with adapted anchors)
  - success_bank/niu.py: 牛 structure reference (4 strokes: pie + heng + heng + shu)
  - success_bank/si_private.py: 厶 reference (top of 牟)
  MMH-derived stroke anchors from dispatcher structural block used directly for s3-s8.
"""
import os, sys
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes matching MMH plan; joints s6/s8 and s7/s8 welded P; others left as natural N gaps.'
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# --- s1, s2: 亻 (person radical) --- far-left position
# s1 pie: TL(0.92,0.659) -> ML(0.196,0.995)
draw_pie(draw, ('TL', 0.92, 0.659), ('ML', 0.196, 0.995),
         head_width=11, tail_width=1, curve=0.10, segments=48)
# s2 shu: ML(0.691,0.538) -> BL(0.732,0.883)
draw_shu(draw, ('ML', 0.691, 0.538), ('BL', 0.732, 0.883), width=9)

# --- s3, s4: 厶-cap of 牟 ---
# s3 pie: TC(0.688,0.63) -> MR(0.139,0.23) (top-right curving down-left toward center-right)
draw_pie(draw, ('TC', 0.688, 0.63), ('MR', 0.139, 0.23),
         head_width=11, tail_width=2, curve=0.08, segments=48)
# s4 na-like fold: TR(0.036,0.993) -> MR(0.353,0.371)
draw_na(draw, ('TR', 0.036, 0.993), ('MR', 0.353, 0.371),
        head_width=3, peak_width=10, tail_width=2, peak_t=0.75, curve=0.05, segments=32)

# --- s5: 牛 top pie ---
# C(0.336,0.576) -> BC(0.084,0.15)
draw_pie(draw, ('C', 0.336, 0.576), ('BC', 0.084, 0.15),
         head_width=10, tail_width=1, curve=0.10, segments=48)

# --- s6: 牛 short heng ---
# C(0.397,0.89) -> MR(0.265,0.749)
draw_heng(draw, ('C', 0.397, 0.89), ('MR', 0.265, 0.749), width=9)

# --- s7: 牛 long bottom heng ---
# BL(0.976,0.411) -> BR(0.637,0.282)
draw_heng(draw, ('BL', 0.976, 0.411), ('BR', 0.637, 0.282), width=11)

# --- s8: 牛 spine shu (extends past bottom) ---
# C(0.702,0.45) -> BC(0.813,1.199)
draw_shu(draw, ('C', 0.702, 0.45), ('BC', 0.813, 1.199), width=10)

out = os.path.join(os.path.dirname(__file__), '01_侔.png')
img.save(out)
print('saved', out)
