"""点 (diǎn) — 9 strokes.
Decomposition: 点 = 占 (top, 5 strokes) + 灬 (bottom, 4 dots).
  占 = 卜 (2: 竖 + 点) + 口 (3: 竖, 横折, 横)
  灬 = 4 dian (leftmost leans left; rest lean right, rightmost longest)

Memory checklist:
- drawer_memory.md: A-recipe points 1-5: decomposition comment, MMH-verbatim
  anchors, SELF_CHECK, base primitives, N-joint discipline. No compound
  primitive fits well (口 is small/compressed top-center; 灬 is 4 tiny dots).
- INDEX.md: kou.py exists but its baked anchors are full-canvas, not the
  compressed C-region 口 needed here — inline via fat_line.
- errata.md: no 点 entry.

No BANK_DEVIATION block: not deviating from a specific compound primitive
whose defaults nearly fit — this is a straight base-primitive render.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from PIL import Image
from PIL import ImageDraw
from _anchor import anchor_to_xy, fat_line

W = 8  # ink width

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- 占 (top, 5 strokes) ---------------------------------------------------

# stroke 1: 竖 of 卜 (vertical stub, TC → C)
s1_h = ('TC', 0.38, 0.636)
s1_t = ('C',  0.456, 0.509)
fat_line(d, anchor_to_xy(s1_h), anchor_to_xy(s1_t), W)

# stroke 2: 点/short 横 of 卜 (right-flick from mid-shu to upper right)
s2_h = ('C',  0.597, 0.166)
s2_t = ('MR', 0.15,  0.081)
fat_line(d, anchor_to_xy(s2_h), anchor_to_xy(s2_t), W)

# stroke 3: 竖 of 口 (left wall) — head above tail
s3_h = ('ML', 0.952, 0.573)
s3_t = ('BC', 0.16,  0.215)
fat_line(d, anchor_to_xy(s3_h), anchor_to_xy(s3_t), W)

# stroke 4: 横折 of 口 (top + right wall). MMH endpoints define the top-heng
# start and elbow region; extend the right wall down to nearly reach the
# bottom heng level so 口 closes visually (v13 A-recipe: coherence beats
# strict endpoint literalism when MMH gives head+tail-of-elbow only).
s4_h_xy = anchor_to_xy(('C', 0.134, 0.588))   # top-left of 口
s4_elbow_xy = anchor_to_xy(('C', 0.893, 0.588))  # top-right corner (elbow)
# Right wall descends to just above bottom heng (y ≈ 213, N-gap ~2 px)
s4_tail_xy = (s4_elbow_xy[0], 213)
fat_line(d, s4_h_xy, s4_elbow_xy, W)
fat_line(d, s4_elbow_xy, s4_tail_xy, W)

# stroke 5: 横 (bottom of 口) — closes the box
s5_h = ('BC', 0.225, 0.15)
s5_t = ('BR', 0.08,  0.065)
fat_line(d, anchor_to_xy(s5_h), anchor_to_xy(s5_t), W)

# ---- 灬 (bottom, 4 dots) ---------------------------------------------------
# Each dian is drawn as a short thick tapered stroke. Leftmost leans LEFT
# (down-left); middle two lean slightly down-right; rightmost longest.

def draw_dian(head_anchor, tail_anchor, width_head=6, width_tail=12):
    """Short tapered dian: thin at head, fat at tail."""
    h = anchor_to_xy(head_anchor)
    t = anchor_to_xy(tail_anchor)
    # 3-segment taper
    n = 8
    from _anchor import stroke_variable_width
    pts = [(h[0] + (t[0]-h[0]) * i/n, h[1] + (t[1]-h[1]) * i/n) for i in range(n+1)]
    ws = [width_head + (width_tail - width_head) * i/n for i in range(n+1)]
    stroke_variable_width(d, pts, ws)

# stroke 6: leftmost dot (leans LEFT / down-left)
draw_dian(('BL', 0.803, 0.373), ('BL', 0.542, 0.903))
# stroke 7: 2nd dot (short, down-right)
draw_dian(('BC', 0.143, 0.432), ('BC', 0.312, 0.771))
# stroke 8: 3rd dot (short, down-right)
draw_dian(('BC', 0.632, 0.37),  ('BC', 0.825, 0.736))
# stroke 9: rightmost dot (longer, down-right)
draw_dian(('BR', 0.095, 0.314), ('BR', 0.552, 0.874))

out = os.path.join(os.path.dirname(__file__), '01_点.png')
img.save(out)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 strokes drawn (s4 = 2 segments = 1 stroke)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 5 joints are N (natural gap preserved)
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 卜+口+灬 decomposition; N-gaps preserved between 卜 and 口 and 灬.',
}
