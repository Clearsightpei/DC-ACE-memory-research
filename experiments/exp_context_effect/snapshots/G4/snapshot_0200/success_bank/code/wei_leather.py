"""p2_radical_123_韦 — 韦 (wéi, "leather", 4画).

Two mid horizontals + bottom compound heng-zhe-gou + centered 竖 spine.

Joints (all P — welded via spine):
  s1.mid ⇆ s4.mid @ C
  s2.mid ⇆ s4.mid @ C
  s3.mid ⇆ s4.mid @ BC
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from heng import draw_heng
from shu import draw_shu


def _heng_zhe_gou_bottom(draw, head, corner, tail, tip, h_width=9, v_width=9, tip_w=2):
    p_h = anchor_to_xy(head); p_c = anchor_to_xy(corner)
    p_t = anchor_to_xy(tail); p_ti = anchor_to_xy(tip)
    fat_line(draw, p_h, p_c, width=h_width)
    fat_line(draw, p_c, p_t, width=v_width)
    pts = quad_bezier(p_t, ((p_t[0]+p_ti[0])/2, p_t[1]), p_ti, segments=24)
    stroke_variable_width(draw, pts, v_width, tip_w)


DEFAULTS = {
    's1_h': ('ML', 0.82, 0.216),  's1_t': ('MR', 0.165, 0.099),
    's2_h': ('ML', 0.841, 0.664), 's2_t': ('MR', 0.101, 0.567),
    's3_h': ('BL', 0.492, 0.153), 's3_c': ('BC', 0.85, 0.20),
    's3_t': ('BC', 0.95, 0.65),   's3_tip': ('BC', 0.55, 0.80),
    's4_h': ('TC', 0.356, 0.58),  's4_t': ('BC', 0.474, 1.103),
}


def draw_wei_leather(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    draw_heng(draw, p['s1_h'], p['s1_t'], width=9)
    draw_heng(draw, p['s2_h'], p['s2_t'], width=9)
    _heng_zhe_gou_bottom(draw, p['s3_h'], p['s3_c'], p['s3_t'], p['s3_tip'])
    draw_shu(draw, p['s4_h'], p['s4_t'], width=10)
