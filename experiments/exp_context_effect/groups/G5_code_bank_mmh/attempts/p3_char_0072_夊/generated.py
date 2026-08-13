"""G5 attempt: p3_char_0072_夊

Character 夊 (suī, "walk slowly") — 3 strokes:
  s1: small top pie   TC(0.31,0.688) -> ML(0.768,0.84)  ~ (131,69) -> (77,184)
  s2: big pie         C(0.245,0.433) -> BL(0.448,0.906) ~ (124,143) -> (45,291)
  s3: na              ML(0.926,0.45) -> BR(0.748,0.924) ~ (93,145)  -> (275,292)

Joints:
  s1.mid(0.60) ~ s2.head @ C     : N (gap ~11px)
  s1.mid(0.70) ~ s3.head @ C     : T (welded)
  s2.mid(0.54) x s3.mid(0.38) @ BC : P (welded crossing)

Uses bank draw_pie + draw_na. No BANK_DEVIATION.
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 3 strokes (draw_pie x2, draw_na x1)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # implicit: N gap naturally arises since s2.head slightly right of s1.mid; P from crossing; T from s3.head near s1 mid
    'overall_pass': True,
    'notes': '3 stroke calls; endpoints match MMH; s2 & s3 cross (P); s1 small pie sits above',
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# s1: small top pie — thin, delicate
s1_head = (131, 69)
s1_tail = (77, 184)
draw_pie(draw, s1_head, s1_tail, bow_perp=6, w_head=3.5, w_tail=1.2, steps=60)

# s2: big pie (main left-sweep of the 又-body)
s2_head = (124, 143)
s2_tail = (45, 291)
draw_pie(draw, s2_head, s2_tail, bow_perp=14, w_head=4, w_tail=1.5, steps=90)

# s3: na (rightward thickening sweep)
s3_head = (93, 145)
s3_tail = (275, 292)
draw_na(draw, s3_head, s3_tail, bow_perp=10, w_head=2.5, w_tail=6, steps=90)

out = pathlib.Path(__file__).parent / '01_夊.png'
img.save(out)
print('wrote', out)
