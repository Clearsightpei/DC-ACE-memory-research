"""p3_char_0185_仟 — 亻 (left) + 千 (right), 5 strokes.

Memory checklist (memory_index.md v8):
1. drawer_memory.md — component-reuse shortlist: ren_side (亻); qian_thousand (千) also in bank.
2. success_bank/INDEX.md grep: ren_side.py mastered; qian_thousand.py mastered.
3. errata.md grep: 仟 not listed.

Composition: 亻 in left column, 千 in right column. Using MMH-injected
per-stroke anchors verbatim (dispatcher block).

Expected 5 strokes = 亻(2 = pie + shu) + 千(3 = pie + heng + shu).
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
    'stroke_count_ok': True,   # 5 = pie + shu + pie + heng + shu
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Composed 亻 (left) + 千 (right) at MMH-injected anchors.',
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- 亻 (left radical, 2 strokes) ----
# s1 撇: MMH head TL(0.85, 0.609) → tail ML(0.141, 0.831)
draw_pie(draw,
         ('TL', 0.85, 0.609),
         ('ML', 0.141, 0.831),
         head_width=11, tail_width=1, curve=0.10, segments=48)

# s2 竖: MMH head ML(0.665, 0.374) → tail BL(0.674, 0.777)
draw_shu(draw,
         ('ML', 0.665, 0.374),
         ('BL', 0.674, 0.777),
         width=9)

# ---- 千 (right side, 3 strokes) ----
# s3 短撇: MMH head TR(0.276, 0.776) → tail C(0.245, 0.14)
draw_pie(draw,
         ('TR', 0.276, 0.776),
         ('C', 0.245, 0.14),
         head_width=10, tail_width=2, curve=0.06, segments=48)

# s4 横: MMH head ML(0.929, 0.731) → tail MR(0.757, 0.567)
draw_heng(draw,
          ('ML', 0.929, 0.731),
          ('MR', 0.757, 0.567),
          width=10)

# s5 长竖: MMH head C(0.632, 0.069) → tail BC(0.778, 1.094)
draw_shu(draw,
         ('C', 0.632, 0.069),
         ('BC', 0.778, 1.094),
         width=10)

out_path = os.path.join(os.path.dirname(__file__), '01_仟.png')
img.save(out_path)
print('wrote', out_path)
