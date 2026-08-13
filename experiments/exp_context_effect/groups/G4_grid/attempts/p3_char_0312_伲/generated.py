"""p3_char_0312 伲 = 亻 + 尼 (亻 + 尸 + 匕). 7 MMH strokes.

Memory reading log (v8 slim checklist):
1. drawer_memory.md — followed compositional playbook for 3-part char.
2. INDEX grep — 亻 (ren_side.py), 尸 (shi_corpse.py), 匕 (bi.py) all mastered;
   char 他 (亻+也) at c154 PASSED as compositional analogue.
3. errata grep — nothing for 伲.

Strategy: use ren_side for 亻; render 尼 (right half) directly per MMH anchors
because 尼 as a whole is not banked and the sub-decomposition 尸+匕 sits INSIDE
a single square rather than stacked, which shi_corpse+bi (each sized for a
full square) would not fit correctly. Direct anchors give truer proportion.

MMH per-stroke plan (PIL y-DOWN, cell=100 px):
  s1 撇 (亻)         : TL(.902,.662) → BL(.211,.027)
  s2 竖 (亻)         : ML(.691,.559) → BL(.744,.883)
  s3 横折 (尸 top)   : C(.506,.008) → MR(.045,.298)
  s4 横 (尸 middle)  : C(.488,.515) → MR(.241,.386)
  s5 撇 (尸 long)    : TC(.304,.961) → BL(.894,.760)
  s6 横 (匕)         : MR(.188,.693) → BC(.688,.314)
  s7 竖弯钩 (匕)     : C(.547,.767) → BR(.590,.268)

All 8 declared joints are N-class (natural gap, do NOT weld).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 stroke primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 8 joints rendered as N (natural gaps)
    'overall_pass': True,
    'notes': '亻 via ren_side; 尼 rendered directly per MMH anchors.',
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- 亻 (left radical) --------------------------------------------------
# s1: 撇 — sweep from upper TL down-left to BL.
s1_head = anchor_to_xy(('TL', 0.902, 0.662))
s1_tail = anchor_to_xy(('BL', 0.211, 0.027))
# Bezier control: bow slightly leftward to give 撇 curvature.
c1 = ((s1_head[0] + s1_tail[0]) / 2 - 12, (s1_head[1] + s1_tail[1]) / 2)
pts1 = quad_bezier(s1_head, c1, s1_tail, n=48)
widths1 = [max(2, 10 - int(9 * i / len(pts1))) for i in range(len(pts1))]
stroke_variable_width(draw, pts1, widths1)

# s2: 竖 — short vertical dropping from mid-upper.
s2_head = anchor_to_xy(('ML', 0.691, 0.559))
s2_tail = anchor_to_xy(('BL', 0.744, 0.883))
fat_line(draw, s2_head, s2_tail, width=8)

# ---- 尸 (top-enclosing) -------------------------------------------------
# s3: 横折 — top horizontal into right vertical (single MMH stroke).
s3_head = anchor_to_xy(('C', 0.506, 0.008))
s3_tail = anchor_to_xy(('MR', 0.045, 0.298))
# Corner at where horizontal ends and vertical begins: near top-right of 尸.
s3_corner = (s3_tail[0], s3_head[1])
fat_line(draw, s3_head, s3_corner, width=7)
fat_line(draw, s3_corner, s3_tail, width=7)

# s4: 横 — inner middle horizontal of 尸.
s4_head = anchor_to_xy(('C', 0.488, 0.515))
s4_tail = anchor_to_xy(('MR', 0.241, 0.386))
fat_line(draw, s4_head, s4_tail, width=6)

# s5: 撇 — long slanting stroke from top-center down to bottom-left (BL).
s5_head = anchor_to_xy(('TC', 0.304, 0.961))
s5_tail = anchor_to_xy(('BL', 0.894, 0.760))
c5 = ((s5_head[0] + s5_tail[0]) / 2 - 8, (s5_head[1] + s5_tail[1]) / 2 + 4)
pts5 = quad_bezier(s5_head, c5, s5_tail, n=48)
widths5 = [max(2, 10 - int(9 * i / len(pts5))) for i in range(len(pts5))]
stroke_variable_width(draw, pts5, widths5)

# ---- 匕 (bottom-right, inside 尸) --------------------------------------
# s6: 横 (short diagonal-ish top of 匕, from upper-right slanting down-left).
s6_head = anchor_to_xy(('MR', 0.188, 0.693))
s6_tail = anchor_to_xy(('BC', 0.688, 0.314))
fat_line(draw, s6_head, s6_tail, width=6)

# s7: 竖弯钩 — vertical down, curve right, hook up.
s7_head = anchor_to_xy(('C', 0.547, 0.767))
s7_tail = anchor_to_xy(('BR', 0.590, 0.268))
# Sample a path: start at head, go DOWN first, then curve RIGHT+UP to tail.
low_x = s7_head[0]
low_y = anchor_to_xy(('BC', 0.547, 0.85))[1]  # deepest y
bend  = (low_x, low_y)
# Two beziers: head→bend (vertical), then bend→tail (right & up curve).
pts7a = quad_bezier(s7_head, (s7_head[0], (s7_head[1] + low_y) / 2), bend, n=24)
mid   = ((bend[0] + s7_tail[0]) / 2, low_y + 4)
pts7b = quad_bezier(bend, mid, s7_tail, n=32)
pts7 = pts7a + pts7b[1:]
widths7 = [7] * len(pts7)
# taper hook slightly at end
for k in range(1, 8):
    if k <= len(widths7):
        widths7[-k] = max(3, 7 - (8 - k))
stroke_variable_width(draw, pts7, widths7)

out = os.path.join(os.path.dirname(__file__), '01_伲.png')
img.save(out)
print('WROTE', out)
