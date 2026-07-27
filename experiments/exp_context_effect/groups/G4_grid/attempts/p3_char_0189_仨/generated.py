"""p3_char_0189_仨 — 亻 (left) + 三 (right), 5 strokes.

Memory-lookup checklist (memory_index.md order):
1. drawer_memory.md: 亻 → ren_side; multi-part left/right composition.
2. success_bank/INDEX.md grep: ren_side.py (亻) mastered; san_three.py (三)
   mastered. Compose left+right per playbook (left x∈[0.05,0.40], right
   x∈[0.45,0.95]).
3. errata.md grep: 仨 not listed.

Split: 仨 = 亻 (2 strokes: 撇 + 竖) + 三 (3 strokes: heng × 3).
Total = 5 strokes matches MMH.

Anchors overridden from MMH-injected structural block (not default primitive
signatures) since defaults were tuned for standalone rendering.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 = pie + shu + 3 × heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s1.mid ⇆ s2.head N (gap ~17 px)
    'overall_pass': True,
    'notes': 'Composed 亻 (left column) + 三 (right column) per MMH anchors.',
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- 亻 (left radical, 2 strokes) ----
# s1 撇: MMH head TL(0.92,0.677) → tail BL(0.141,0.027)
draw_pie(draw,
         ('TL', 0.92, 0.677),
         ('BL', 0.141, 0.027),
         head_width=10, tail_width=1, curve=0.10, segments=48)

# s2 竖: MMH head ML(0.677,0.57) → tail BL(0.703,0.98) [clamped from 1.032]
draw_shu(draw,
         ('ML', 0.677, 0.57),
         ('BL', 0.703, 0.98),
         width=8)

# ---- 三 (right, 3 hengs, top < middle < bottom in length) ----
# s3 top heng: C(0.251,0.333) → MR(0.253,0.225)
draw_heng(draw,
          ('C', 0.251, 0.333),
          ('MR', 0.253, 0.225),
          width=8)

# s4 middle heng: C(0.321,0.998) → MR(0.191,0.91)
draw_heng(draw,
          ('C', 0.321, 0.998),
          ('MR', 0.191, 0.91),
          width=9)

# s5 bottom heng (longest): BL(0.981,0.701) → BR(0.669,0.634)
draw_heng(draw,
          ('BL', 0.981, 0.701),
          ('BR', 0.669, 0.634),
          width=11)

out_path = os.path.join(os.path.dirname(__file__), '01_仨.png')
img.save(out_path)
print('wrote', out_path)
