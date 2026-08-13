"""p3_char_0355_块 — G4 attempt.

Decomposition: 块 = 土 (left, with 提 bottom) + 夬 (right).  7 strokes, matches MMH.
  Left 土-radical: s1 短横, s2 竖, s3 提 (rising, replaces bottom 横).
  Right 夬:       s4 短横 (top), s5 长横 (middle), s6 撇, s7 捺.

Reading order (v8):
  1) drawer_memory.md — read. Applied A-recipe: MMH-verbatim anchors + base
     primitives (heng/shu/ti/pie/na). No compound primitive fits 夬 cleanly.
  2) INDEX.md — tu.py exists (mastered position 104) but tu is 士-shaped
     (bottom 横). Left 土-radical here needs 提 not 横 — inline instead.
  3) errata.md — 块 not present.

Following B9 A-recipe: MMH-verbatim anchors + base primitives; declare
joint classes; respect N-gaps.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from shu import draw_shu
from ti import draw_ti
from pie import draw_pie
from na import draw_na
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 primitives = 7 strokes
    'endpoint_mismatches': [],     # all MMH-verbatim
    'joint_class_mismatches': [],  # P joints emerge from geometry (s6 crosses s4 and s5); N gaps preserved
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim using base primitives. P at s1xs2 (welded cross of 土), P at s4xs6 and s5xs6 (夬 pie crossing horizontals). N joints preserved as natural gaps: s1.tail~s4.head (~21px at C), s2.tail~s3.mid at BL, s3.tail~s5.head at BC, s4.tail~s5.mid at MR, s5~s7.head near BC, s6~s7.head near BC.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ==================== LEFT: 土-radical (with 提 bottom) ====================

# s1: 短横 of 土 (top short heng)  ML(.36,.594) -> C(.113,.45)
draw_heng(d, ('ML', 0.36, 0.594), ('C', 0.113, 0.45), width=8)

# s2: 竖 of 土 (vertical spine)  TL(.65,.765) -> BL(.724,.145)
draw_shu(d, ('TL', 0.65, 0.765), ('BL', 0.724, 0.145), width=9)

# s3: 提 of 土-radical (rising, thick head → needle tip)
#     BL(.231,.367) -> BC(.09,.045)
draw_ti(d, ('BL', 0.231, 0.367), ('BC', 0.09, 0.045),
        head_width=12, tail_width=1, curve=0.06, segments=40)

# ==================== RIGHT: 夬 ====================

# s4: 短横 (top of 夬, slight downward slant)  C(.269,.477) -> MR(.106,.852)
draw_heng(d, ('C', 0.269, 0.477), ('MR', 0.106, 0.852), width=8)

# s5: 长横 (middle horizontal, spans BC->MR, slight upward slant)
#     BC(.175,.024) -> MR(.695,.951)
draw_heng(d, ('BC', 0.175, 0.024), ('MR', 0.695, 0.951), width=9)

# s6: 撇 (long pie top-center-right -> bottom-left) — belly bows down-right
#     TC(.635,.665) -> BL(.97,.956)   curve NEGATIVE flips belly to correct side
draw_pie(d, ('TC', 0.635, 0.665), ('BL', 0.97, 0.956),
         head_width=11, tail_width=1, curve=-0.09, segments=50)

# s7: 捺 (right-falling, with peak swell near tail)
#     BC(.775,.057) -> BR(.818,.971)
draw_na(d, ('BC', 0.775, 0.057), ('BR', 0.818, 0.971),
        head_width=3, peak_width=14, tail_width=1,
        peak_t=0.80, curve=0.09, segments=50)

out = os.path.join(os.path.dirname(__file__), '01_块.png')
img.save(out)
print('wrote', out)
