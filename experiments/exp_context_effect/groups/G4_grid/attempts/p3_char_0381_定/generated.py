"""定 (dìng) — 8 strokes.

Decomposition: 定 = 宀 (top roof, 3 strokes: 点 + 点 + 横钩)
             + 疋-like bottom (5 strokes: 横 + 竖 + 短横 + 撇 + 捺).

MMH-verbatim anchors (A-recipe point 2). Base primitives over compound
primitives (A-recipe point 4) — mian.py's defaults do not match MMH
placement here (MMH puts the roof higher and narrower than mian's
defaults), so we inline dian+heng_gou with MMH anchors instead.

Joints (all N-class per dispatcher — leave the natural gap, do NOT weld):
  s2.mid ⇆ s3.head @ ML  (roof left corner)
  s3.tail ⇆ s4.tail @ C  (roof hook tip near top-横 of 疋)
  s4.mid ⇆ s5.head @ C   (top-横 to 竖)
  s5.mid ⇆ s6.head @ BC  (竖 to short-横)
  s5.tail ⇆ s8.mid @ BC  (竖 tail near 捺 body)
  s7.head ⇆ s8.head @ BL (撇 and 捺 origins near each other, not welded)
"""
import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from dian import draw_dian
from heng_gou import draw_heng_gou
from heng import draw_heng
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; roof inlined (dian+dian+heng_gou); '
             'bottom 疋 inlined (heng+shu+heng+pie+na); all N-joints '
             'left as natural gaps.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- 宀 roof (3 strokes) ----
# s1: top 点 (rounded press above the roof).
draw_dian(d,
          ('TC', 0.277, 0.53),
          ('TC', 0.591, 0.794),
          head_width=2, peak_width=9, curve=0.10, segments=24)

# s2: left 点 (vertical dot at top-left corner of roof).
draw_dian(d,
          ('ML', 0.671, 0.058),
          ('ML', 0.571, 0.644),
          head_width=2, peak_width=8, curve=0.06, segments=24)

# s3: 横钩 (top horizontal of roof + down-left hook at right end).
# MMH gives head+tail of the horizontal body; extend a short hook tip
# below-left of the shoulder (down-left flick, canonical heng_gou form).
_sh = ('MR', 0.033, 0.362)   # shoulder = MMH tail of s3
_tip = ('MR', -0.10, 0.75)   # hook tip: down-left of shoulder
draw_heng_gou(d,
              ('ML', 0.797, 0.236),
              _sh,
              _tip,
              head_w=6, mid_w=5, shoulder_w=11, tip_w=2)

# ---- 疋-like bottom (5 strokes) ----
# s4: short 横 (top horizontal of 疋).
draw_heng(d,
          ('ML', 0.99, 0.611),
          ('C', 0.84, 0.5),
          width=7)

# s5: 竖-like short vertical dropping down from center.
draw_heng(d,
          ('C', 0.333, 0.693),
          ('BC', 0.485, 0.555),
          width=7)

# s6: short 横 mid-bottom band.
draw_heng(d,
          ('BC', 0.538, 0.112),
          ('BR', 0.001, 0.021),
          width=8)

# s7: 撇 sweeping down-left across bottom-left region.
draw_pie(d,
         ('ML', 0.876, 0.983),
         ('BL', 0.375, 0.895),
         head_width=10, tail_width=1, curve=0.08, segments=48)

# s8: 捺 sweeping down-right, long base sweep.
draw_na(d,
        ('BC', 0.008, 0.276),
        ('BR', 0.774, 0.947),
        head_width=3, peak_width=14, tail_width=1,
        peak_t=0.8, curve=0.10, segments=48)

img.save(os.path.join(_HERE, '01_定.png'))
print('OK 定 8 strokes')
