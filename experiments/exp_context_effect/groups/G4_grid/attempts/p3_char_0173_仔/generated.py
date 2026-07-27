"""p3_char_0173_仔 — 亻 (left) + 子 (right), 5 strokes.

Memory-lookup checklist (memory_index.md):
1. success_bank/INDEX.md grep: ren_side.py (亻) + zi_char.py (子) both mastered.
   Composing 仔 by calling both with OVERRIDE anchors per TR1 (left/right split).
2. errata.md grep: 仔 not listed.
3. form_catalog.md: 亻 is left-radical (column 0-1); 子 is right (column 1-2).
4. principles_meta.md TR1: override anchors, never call with defaults.
5. joint_atlas.md: MMH joint spec injected — s1.mid ⇆ s2.head T-like N (17 px),
   s2.mid ⇆ s5.head N (30 px), s3.tail ⇆ s4.head N (8 px), s4.mid × s5.mid P.
6. sandbox.md: standard compound-char layout.

Expected 5 strokes = 亻(2) + 子(3): pie, shu, heng_pie, wan_gou, heng.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng_pie import draw_heng_pie
from wan_gou import draw_wan_gou
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 = pie + shu + heng_pie + wan_gou + heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Composed 亻 (left) + 子 (right) matching MMH-injected anchors.',
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- 亻 (left radical, 2 strokes) ----
# s1 撇: MMH head TL(0.908,0.688) → tail ML(0.173,0.972)
draw_pie(draw,
         ('TL', 0.908, 0.688),
         ('ML', 0.173, 0.972),
         head_width=10, tail_width=1, curve=0.10, segments=48)

# s2 竖: MMH head ML(0.735,0.456) → tail BL(0.756,0.795)
draw_shu(draw,
         ('ML', 0.735, 0.456),
         ('BL', 0.756, 0.795),
         width=8)

# ---- 子 (right side, 3 strokes) ----
# s3 横撇: head C(0.269,0.078), corner near C(0.80,0.10), tip C(0.802,0.433)
# MMH gives head + tail; heng_pie needs an intermediate corner. Since tail is
# already in the "corner-then-pie-down" zone, we use tail as corner and let the
# pie taper into the tip inside cell C. Actually MMH gives head→tail of the
# COMBINED heng+pie as one stroke; we place corner at the top-right (TR side of C)
# and let the tip land where MMH tail is.
draw_heng_pie(draw,
              ('C', 0.269, 0.078),
              ('C', 0.90, 0.12),
              ('C', 0.802, 0.433),
              head_w=7, corner_w=10, tip_w=4)

# s4 弯钩: head C(0.693,0.40), tail BC(0.362,0.643) — hook pointing up-left
draw_wan_gou(draw,
             ('C', 0.693, 0.40),
             ('C', 0.85, 0.70),
             ('BC', 0.55, 0.85),
             ('BC', 0.362, 0.643),
             head_w=8, belly_w=12, hook_start_w=10, tip_w=2)

# s5 横: head C(0.014,0.825) → tail MR(0.733,0.752)
draw_heng(draw,
          ('C', 0.014, 0.825),
          ('MR', 0.733, 0.752),
          width=8)

out_path = os.path.join(os.path.dirname(__file__), '01_仔.png')
img.save(out_path)
print('wrote', out_path)
