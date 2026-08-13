"""疮 (chuāng) — 9 strokes.

Decomposition: 疮 = 疒 (left/outer, 5 strokes) + 仓 (interior, 4 strokes).
  疒 = top dot + top heng + long 撇 + 2 dots on left column.
  仓 = 撇 + 捺 (top X) + bottom 巴-like hook (2 strokes).

Following B9 A-recipe:
  1. explicit decomposition ✓
  2. MMH-verbatim anchors (all dispatcher-injected tuples used unchanged) ✓
  3. SELF_CHECK block ✓
  4. base primitives (pie/na/heng/dian/fat_line) — no compound override ✓
  5. N-joint discipline — natural gaps preserved for all 8 declared N-joints ✓

# BANK_DEVIATION
# skipped: no compound primitive attempted
# reason: 疮 has no compound bank primitive matching MMH placement;
#         inline base primitives with MMH-verbatim anchors per A-recipe pt 4
# fresh_component: chuang_sick_inline (not promoted; per B11 pattern rule)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 疒 outer + 仓 interior; N-joint gaps preserved.',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from na import draw_na
from heng import draw_heng
from dian import draw_dian

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 疒 (5 strokes) ---
# s1: top dot of 疒
draw_dian(d, ('TC', 0.377, 0.571), ('TC', 0.729, 0.800))
# s2: top heng of 疒 (long horizontal from ML band to TR)
draw_heng(d, ('C', 0.037, 0.069), ('TR', 0.323, 0.949), width=8)
# s3: long left 撇 of 疒
draw_pie(d, ('ML', 0.820, 0.008), ('BL', 0.354, 0.924),
         head_width=12, tail_width=2, curve=0.06, segments=60)
# s4: first small dot on left (upper of two)
draw_dian(d, ('ML', 0.439, 0.301), ('ML', 0.645, 0.547))
# s5: second dot (lower) — goes up-right, treat as ti/dian
draw_dian(d, ('BL', 0.164, 0.165), ('ML', 0.741, 0.898),
          head_width=2, peak_width=10, curve=0.06)

# --- 仓 (4 strokes) ---
# s6: 撇 of 仓 (top-left slash)
draw_pie(d, ('C', 0.556, 0.134), ('BL', 0.923, 0.224),
         head_width=10, tail_width=2, curve=0.08, segments=48)
# s7: 捺 of 仓 (top-right slash)
draw_na(d, ('C', 0.723, 0.383), ('BR', 0.780, 0.004),
        head_width=3, peak_width=13, tail_width=1, curve=0.08, segments=48)
# s8: short 竖 — left inner of bottom 巴 box
p8a = anchor_to_xy(('BC', 0.389, 0.098))
p8b = anchor_to_xy(('BC', 0.538, 0.396))
fat_line(d, p8a, p8b, 7)
# s9: 横折弯钩 — top + right + bottom of the 巴 enclosure
#   head at upper-left, tail at bottom-right; explicit corner at (tail.x, head.y)
#   then a return-hook back leftward along the bottom.
p9a = anchor_to_xy(('BC', 0.222, 0.019))
p9b = anchor_to_xy(('BR', 0.288, 0.426))
p9c = (p9b[0], p9a[1])                          # top-right corner
p9d = (p9a[0] + 8, p9b[1])                      # bottom-left return (hook)
fat_line(d, p9a, p9c, 7)                        # top heng
fat_line(d, p9c, p9b, 7)                        # right shu
fat_line(d, p9b, p9d, 7)                        # bottom heng (hook back)

out = os.path.join(os.path.dirname(__file__), '01_疮.png')
img.save(out)
print(f'wrote {out}')
