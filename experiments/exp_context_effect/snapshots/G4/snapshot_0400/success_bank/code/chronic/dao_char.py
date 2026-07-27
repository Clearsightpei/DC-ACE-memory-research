"""刀 (dāo, "knife") — 2-stroke, canonical hand-written primitive.

Chronic-cluster item, promoted at position 300 after 3 failed retries.

Baked anchors (do NOT tune):
  s1 = 横折钩 : head shared with s2.head @ ('ML', 0.5, 0.4) [T-weld]
             corner @ ('TR', 0.15, 0.4)      (short top, avoid over-run right)
             tail   @ ('BC', 0.60, 0.60)     (vertical descender centered-ish)
             tip    @ ('BR', 0.30, 0.50)     (hook flick UP-and-LEFT)
  s2 = 撇   : head shared with s1.head @ ('ML', 0.5, 0.4)
             tail   @ ('BL', 0.35, 0.85)     (moderate SW sweep, not too far left)

Joints:
  s1.head ⇆ s2.head  T-weld at ('ML', 0.5, 0.4)   [shared anchor tuple]

Root cause fix: chronic B2-B5 failures all had EITHER hook flicking
wrong OR 撇 sweep too extreme OR 横 too long. This anchor plan is the
B1 retry-1 errata plus the B3 retry-2 proportion fix, applied
verbatim.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..')))

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou


def draw_dao_char(draw, color=(0, 0, 0)):
    # Shared T-weld anchor at upper-mid-left.
    SHARED_HEAD = ('ML', 0.50, 0.40)

    # s1 — 横折钩
    s1_corner = ('TR', 0.15, 0.40)
    s1_tail   = ('BC', 0.60, 0.60)
    s1_tip    = ('BR', 0.30, 0.50)
    draw_heng_zhe_gou(draw, SHARED_HEAD, s1_corner, s1_tail, s1_tip,
                      h_width=9, v_width=9, shoulder=12, tip_w=2,
                      color=color)

    # s2 — 撇
    s2_tail = ('BL', 0.35, 0.85)
    draw_pie(draw, SHARED_HEAD, s2_tail,
             head_width=12, tail_width=1, curve=0.12, segments=56,
             color=color)
