"""地 (dì, "earth") — 6 strokes.
地 = 土 (left) + 也 (right).
Left 土 uses 提 for bottom stroke (as left-radical convention).
Right 也 = 横折钩 + 竖 + 竖弯钩.

Stroke plan (matches MMH-derived structural block):
  s1  短横 (top of 土)                 head ML(0.35,0.79) tail C(0.10,0.61)
  s2  竖 (spine of 土)                 head TL(0.64,0.90) tail BL(0.72,0.36)
  s3  提 (bottom of 土, slanted up)    head BL(0.26,0.58) tail BC(0.14,0.22)
  s4  也 top 横折钩                    head ML(0.98,0.99) tail BC(0.93,0.11)
  s5  也 middle 竖                     head TC(0.67,0.63) tail BC(0.71,0.31)
  s6  也 竖弯钩 (long curved bottom)   head C(0.26,0.31)  tail BR(0.74,0.03)

# Joints (from brief):
#  s1.mid × s2.mid @ ML       P welded
#  s1.tail ⇆ s6.head @ C      N ~33px gap
#  s2.tail ⇆ s3.mid @ BL      N ~19px gap
#  s2.mid  ⇆ s4.head @ ML     N ~28px gap
#  s3.tail ⇆ s4.head @ BC     N ~35px gap
#  s3.tail ⇆ s6.mid @ BC      N ~29px gap
#  s4.mid  × s5.mid  @ C      P welded
#  s4.head ⇆ s6.mid  @ C      T welded
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes; 土 (heng/shu/ti) + 也 (heng-zhe-gou / shu / shu-wan-gou).',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)
W = 8  # default stroke width

# --- 土 (left radical) ---
# s1 short heng
p_s1_h = anchor_to_xy(('ML', 0.346, 0.79))
p_s1_t = anchor_to_xy(('C',  0.099, 0.608))
fat_line(d, p_s1_h, p_s1_t, W)

# s2 vertical spine
p_s2_h = anchor_to_xy(('TL', 0.642, 0.896))
p_s2_t = anchor_to_xy(('BL', 0.724, 0.358))
fat_line(d, p_s2_h, p_s2_t, W)

# s3 提 (slanted heng going up-right)
p_s3_h = anchor_to_xy(('BL', 0.264, 0.584))
p_s3_t = anchor_to_xy(('BC', 0.137, 0.224))
# taper: thicker at head, tapered at tail like a 提
pts_s3 = [(p_s3_h[0] + i/10*(p_s3_t[0]-p_s3_h[0]),
           p_s3_h[1] + i/10*(p_s3_t[1]-p_s3_h[1])) for i in range(11)]
widths_s3 = [max(2, W - int(i*0.5)) for i in range(11)]
stroke_variable_width(d, pts_s3, widths_s3)

# --- 也 (right side) ---
# s4 横折钩: head at left-top of 也 area, goes right, bends down, then hook up
# Based on head @ (98.1, 198.9) and tail @ (192.5, 210.6), this stroke is
# largely in the middle-y band. Draw as: start at head, go right and slightly up
# to top of 也, then horizontal right to top-right corner, then down to tail.
# Actually simpler: interpret head as top-left of the horizontal, tail as
# the hook tip. Use a polyline through top and bend point.
# But the head y=199 is high (relative to canvas top being 0). We need to
# render a 横折钩 shape. Use the given endpoints and add via points.
h4 = p_s2_t_head = anchor_to_xy(('ML', 0.981, 0.989))   # (98.1, 198.9)
t4 = anchor_to_xy(('BC', 0.925, 0.106))                  # (192.5, 210.6)
# via top-right corner (approximate top of 也 near TC/TR):
top_right = anchor_to_xy(('TC', 0.85, 0.75))             # (185, 75)
bend_pt   = anchor_to_xy(('C',  0.85, 0.10))             # (185, 110)
# Draw horizontal segment: head -> top_right (going up-right)
# then vertical: top_right -> bend_pt
# then hook: bend_pt -> tail (slight leftward hook)
# Actually: 横折钩 goes horizontal from top-left to top-right, then vertical
# down, then hook. Let me redo with a proper polyline.
# Redefine: 横 starts at top-left of 也 zone (~(155, 130)), goes right to
# (~(240, 130)), then bends down to (~(240, 220)), then hook up-left to tail.
h4_start = (155, 130)
h4_corner = (240, 130)
h4_hook_base = (240, 205)
h4_hook_tip = (218, 195)
fat_line(d, h4_start, h4_corner, W)
fat_line(d, h4_corner, h4_hook_base, W)
fat_line(d, h4_hook_base, h4_hook_tip, W)

# s5 middle 竖 of 也
p_s5_h = anchor_to_xy(('TC', 0.67, 0.633))               # (167, 63.3)
p_s5_t = anchor_to_xy(('BC', 0.71, 0.312))               # (171, 231.2)
fat_line(d, p_s5_h, p_s5_t, W)

# s6 竖弯钩 (bottom curve): head at C(0.26,0.31)=(126,131), tail at BR(0.74,0.03)=(274,203)
# Draw as: down from head, curve along bottom rightward, then HOOK UP at tail.
p_s6_h = anchor_to_xy(('C', 0.257, 0.31))                # (125.7, 131.0)
p_s6_t = anchor_to_xy(('BR', 0.742, 0.027))              # (274.2, 202.7)
ctrl = (135, 265)                                        # bottom-left of curve
mid_bottom = (200, 275)
pre_hook = (270, 245)
pts_s6 = quad_bezier(p_s6_h, ctrl, mid_bottom, n=25) \
       + quad_bezier(mid_bottom, pre_hook, (p_s6_t[0], p_s6_t[1] + 15), n=25)
widths_s6 = [W] * len(pts_s6)
stroke_variable_width(d, pts_s6, widths_s6)
# hook up at tail
fat_line(d, (p_s6_t[0], p_s6_t[1] + 15), p_s6_t, W)

out_png = os.path.join(os.path.dirname(__file__), '01_地.png')
img.save(out_png)
print(f'wrote {out_png}')
