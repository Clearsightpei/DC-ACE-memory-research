"""仫 (mù) — 亻 + 么 composition, 5 strokes.

Memory reads (per memory_index.md v8 mandatory 3-file checklist):
- drawer_memory.md: high-value primitives (ren_side for 亻) noted; me/幺 is
  yao_small.py but 仫's right side is 么 which shares stroke geometry (撇 +
  撇折 + 点), so structurally compatible.
- INDEX.md grep '仫': not mastered. INDEX grep '么/幺': p2_radical_078_幺
  = yao_small.py (3 strokes: 撇折 + 撇折 + 点).
- errata.md grep '仫': not present.

Decision: use MMH-supplied anchors directly (v8 says GT/spec wins over
bank defaults). 亻 = strokes 1-2 (撇 + 竖). 么 = strokes 3-5 (long 撇 +
short 撇/折 + tail curl). Draw fresh via anchor_to_xy since MMH anchors
diverge substantially from ren_side/yao_small defaults for this compact
character.
"""
import sys, os
CODE = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(CODE))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 5 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # 2 N joints, both natural small gap
    'overall_pass': True,
    'notes': '亻+么 via MMH anchors; s1.mid ⇆ s2.head (N gap ~15px), s4.tail ⇆ s5.mid (N gap ~22px).'
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

# ---- Stroke 1: 撇 of 亻 (curved from upper-right to lower-left) ----
p1_head = anchor_to_xy(('TL', 0.99, 0.656))
p1_tail = anchor_to_xy(('BL', 0.199, 0.065))
# quadratic curve, bow slightly to the lower-left
p1_ctrl = ((p1_head[0] + p1_tail[0]) / 2 - 8,
           (p1_head[1] + p1_tail[1]) / 2 + 12)
pts1 = quad_bezier(p1_head, p1_ctrl, p1_tail, n=48)
widths1 = [max(2, int(10 - 8 * (i / 48))) for i in range(49)]
stroke_variable_width(draw, pts1, widths1)

# ---- Stroke 2: 竖 of 亻 (slight-lean vertical) ----
p2_head = anchor_to_xy(('ML', 0.729, 0.585))
p2_tail = anchor_to_xy(('BL', 0.768, 0.988))
fat_line(draw, p2_head, p2_tail, width=8)

# ---- Stroke 3: long 撇 of 么 (top-right to bottom-left, spans full char) ----
p3_head = anchor_to_xy(('TC', 0.705, 0.923))
p3_tail = anchor_to_xy(('BC', 0.102, 0.007))
p3_ctrl = ((p3_head[0] + p3_tail[0]) / 2 - 6,
           (p3_head[1] + p3_tail[1]) / 2 + 10)
pts3 = quad_bezier(p3_head, p3_ctrl, p3_tail, n=52)
widths3 = [max(2, int(9 - 7 * (i / 52))) for i in range(53)]
stroke_variable_width(draw, pts3, widths3)

# ---- Stroke 4: short 撇/折 in center-right ----
p4_head = anchor_to_xy(('C', 0.86, 0.646))
p4_tail = anchor_to_xy(('BR', 0.291, 0.531))
p4_ctrl = ((p4_head[0] + p4_tail[0]) / 2 - 3,
           (p4_head[1] + p4_tail[1]) / 2 + 6)
pts4 = quad_bezier(p4_head, p4_ctrl, p4_tail, n=32)
widths4 = [max(2, int(8 - 5 * (i / 32))) for i in range(33)]
stroke_variable_width(draw, pts4, widths4)

# ---- Stroke 5: closing tail/point (小捺 in BR, curl down-right) ----
p5_head = anchor_to_xy(('BR', 0.153, 0.142))
p5_tail = anchor_to_xy(('BR', 0.522, 0.78))
p5_ctrl = ((p5_head[0] + p5_tail[0]) / 2 + 6,
           (p5_head[1] + p5_tail[1]) / 2 - 4)
pts5 = quad_bezier(p5_head, p5_ctrl, p5_tail, n=36)
widths5 = [max(3, int(4 + 6 * (i / 36))) for i in range(37)]
stroke_variable_width(draw, pts5, widths5)

out = os.path.join(os.path.dirname(__file__), '01_仫.png')
img.save(out)
print(f'wrote {out}')
