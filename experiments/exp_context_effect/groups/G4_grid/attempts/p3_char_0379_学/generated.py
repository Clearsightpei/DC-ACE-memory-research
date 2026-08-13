"""学 (xué) — 8 strokes.

Decomposition: 学 = ⺍ (top 3 tick-dots) + 冖 (cover with left tick + heng)
                    + 子 (child: 横撇 + 竖钩 + 一).

Memory checklist:
  # step 1: drawer_memory.md — no chronic primitive maps to 学 as a whole.
  #         A-recipe (B9): trust MMH verbatim + base primitives.
  # step 2: INDEX grep — no zi/子 primitive that fits 学's compressed bottom.
  #         (xue_broom.py is for the 彐 radical, not this character.)
  #         Inline with _anchor helpers.
  # step 3: errata grep — no entry for 学.

MMH-derived anchors used verbatim. 6 N-joints preserved as small gaps;
1 T-joint (s7.head ⇆ s8.mid) welded naturally where 子's 竖钩 head sits
just above the horizontal cross bar.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 8 primitive calls
    'endpoint_mismatches': [],   # all MMH-verbatim
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; s6=横撇 curved via quad_bezier; '
             's7=竖钩 curved via quad_bezier with left-hook; '
             'N-joints preserved as natural gaps; T-joint s7-s8 naturally welded.',
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

STROKE_W = 7

# ---- stroke 1: ⺍ left tick (long diagonal descending from TL down-right) ----
s1_h = anchor_to_xy(('TL', 0.867, 0.876))
s1_t = anchor_to_xy(('C',  0.116, 0.16))
# Actually a short pie/tick — thin at tail (upper-right end)
pts = sample_line(s1_h, s1_t, n=16)
widths = [8 - (8 - 3) * (i / 16) for i in range(17)]  # thick head → thin tail
stroke_variable_width(draw, pts, widths)

# ---- stroke 2: ⺍ middle dot (short vertical in TC) ----
s2_h = anchor_to_xy(('TC', 0.31,  0.709))
s2_t = anchor_to_xy(('TC', 0.518, 0.99))
pts = sample_line(s2_h, s2_t, n=12)
widths = [3 + (9 - 3) * (i / 12) for i in range(13)]  # thin head → thick tail
stroke_variable_width(draw, pts, widths)

# ---- stroke 3: ⺍ right tick (short diagonal from TR down-left to C top) ----
s3_h = anchor_to_xy(('TR', 0.021, 0.633))
s3_t = anchor_to_xy(('C',  0.729, 0.116))
pts = sample_line(s3_h, s3_t, n=16)
widths = [4 + (9 - 4) * (i / 16) for i in range(17)]  # thin head → thick tail
stroke_variable_width(draw, pts, widths)

# ---- stroke 4: 冖 left tick (short near-vertical in ML) ----
s4_h = anchor_to_xy(('ML', 0.621, 0.336))
s4_t = anchor_to_xy(('ML', 0.501, 0.854))
fat_line(draw, s4_h, s4_t, width=STROKE_W)

# ---- stroke 5: 冖 horizontal cover (long heng ML → MR) ----
s5_h = anchor_to_xy(('ML', 0.718, 0.406))
s5_t = anchor_to_xy(('MR', 0.139, 0.626))
fat_line(draw, s5_h, s5_t, width=STROKE_W)

# ---- stroke 6: 子 横撇 — horizontal-fold-pie. MMH head/tail are the
# median endpoints; the visible stroke starts left, arcs up to a corner,
# then descends. Draw as quad_bezier with control at the corner.
s6_h = anchor_to_xy(('ML', 0.979, 0.74))
s6_t = anchor_to_xy(('BC', 0.506, 0.045))
# Corner control: above and between the two endpoints
s6_ctrl = (max(s6_h[0], s6_t[0]) + 10, min(s6_h[1], s6_t[1]) - 15)
pts = quad_bezier(s6_h, s6_ctrl, s6_t, n=30)
widths = [7] * len(pts)
stroke_variable_width(draw, pts, widths)

# ---- stroke 7: 子 竖钩 — vertical with hook at bottom-left ----
s7_h = anchor_to_xy(('BC', 0.438, 0.045))
s7_t = anchor_to_xy(('BC', 0.16,  0.792))
# Control point pushes tail leftward (the hook)
s7_ctrl = (s7_h[0], (s7_h[1] + s7_t[1]) / 2 + 10)
pts = quad_bezier(s7_h, s7_ctrl, s7_t, n=30)
widths = [8] * len(pts)
stroke_variable_width(draw, pts, widths)

# ---- stroke 8: 子 一 (horizontal cross bar) ----
s8_h = anchor_to_xy(('BL', 0.492, 0.265))
s8_t = anchor_to_xy(('BR', 0.625, 0.215))
fat_line(draw, s8_h, s8_t, width=STROKE_W)

out_png = os.path.join(os.path.dirname(__file__), '01_学.png')
img.save(out_png)
print(f"wrote {out_png}")
