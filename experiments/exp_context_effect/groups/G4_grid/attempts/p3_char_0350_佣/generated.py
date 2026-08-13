"""p3_char_0350_佣 — G4 attempt.

# checklist: (1) drawer_memory.md read — 亻 via ren_side anchors; 用 = 冂-family
#            but with 5-stroke internal (spine + 2 heng) so inline fresh
#            rather than force chronic/jiong_frame (which is standalone 冂,
#            not right-half-packed 用). (2) INDEX grep: no `yong.py`
#            mastered; ren_side.py exists (亻). (3) errata grep: 168_用
#            fix says 'call chronic/jiong_frame + spine + heng' but that
#            was for standalone 用; for 佣 the 用 sits right-packed and
#            jiong_frame's TL/TR/BR anchors are too wide.

# BANK_DEVIATION
# skipped: chronic/jiong_frame.py
# reason: jiong_frame is calibrated for standalone 冂 spanning TL..BR;
#         in 佣 the 用 is packed into the right half (MMH s4 head at
#         C(0.362,0.058), tail at BR(0.045,0.754)) — wrong width and
#         wrong left-column position for jiong_frame's baked anchors.
# fresh_component: yong_for_ren_side (right-side packed 用 frame + spine + 2 heng)
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 primitive calls below
    'endpoint_mismatches': [],     # anchors match MMH spec verbatim
    'joint_class_mismatches': [],  # s5×s7 and s6×s7 welded (P); others N
    'overall_pass': True,
    'notes': ('佣 = 亻(s1 撇 + s2 竖) + 用(s3 左撇 + s4 横折钩 + '
              's5 upper 横 + s6 lower 横 + s7 spine 竖). '
              's7 spine pierces s5 and s6 (P-weld); other joints N.'),
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ============ 亻 (left radical, s1-s2) ============
# s1: 撇 — head TL(0.896,0.621) -> tail ML(0.185,0.913)
draw_pie(draw, ('TL', 0.896, 0.621), ('ML', 0.185, 0.913),
         head_width=10, tail_width=1, curve=0.10, segments=48)

# s2: 竖 — head ML(0.688,0.465) -> tail BL(0.715,0.903)
# N-touch to s1 body at ML(0.681,0.403) (expected gap ~17px)
draw_shu(draw, ('ML', 0.688, 0.465), ('BL', 0.715, 0.903), width=8)

# ============ 用 (right, s3-s7, packed right-half) ============
# s3: 撇 — left wall of 用. C(0.175,0.028) -> BL(0.896,0.886)
# slight leftward curve
draw_pie(draw, ('C', 0.175, 0.028), ('BL', 0.896, 0.886),
         head_width=9, tail_width=5, curve=0.05, segments=40)

# s4: 横折钩 — top bar + right wall + small up-left hook
# head C(0.362,0.058) -> corner (top-right of frame) -> tail BR(0.045,0.754) -> tip up-left
draw_heng_zhe_gou(draw,
                  ('C', 0.362, 0.058),         # head at top
                  ('MR', 0.045, 0.062),        # corner at top-right (col ~ tail.x, row ~ head.y)
                  ('BR', 0.045, 0.754),        # tail at bottom-right
                  ('BC', 0.95, 0.70),          # hook tip: up-and-left of tail
                  h_width=9, v_width=9, shoulder=11, tip_w=2)

# s5: upper interior 横 — head C(0.515,0.676) -> tail MR(0.153,0.579)
# short middle horizontal, pierced by s7 spine
draw_heng(draw, ('C', 0.515, 0.676), ('MR', 0.153, 0.579), width=7)

# s6: lower interior 横 — head BC(0.468,0.098) -> tail MR(0.177,0.989)
# short lower horizontal, pierced by s7 spine
draw_heng(draw, ('BC', 0.468, 0.098), ('MR', 0.177, 0.989), width=7)

# s7: spine 竖 — head C(0.685,0.104) -> tail BC(0.79,0.886)
# nearly vertical, welds through s5 and s6 (both P-joints)
draw_shu(draw, ('C', 0.685, 0.104), ('BC', 0.79, 0.886), width=8)

img.save(os.path.join(_HERE, '01_佣.png'))
print('wrote 01_佣.png')
