"""弓 (gōng, "bow") — 3-stroke, canonical hand-written primitive.

Chronic-cluster item, promoted at position 300 after 3 failed retries.

Baked anchors (do NOT tune):

  s1 = 横折 (top tier): flat heng right, then straight drop.
     head   @ ('TL', 0.30, 0.20)  (upper-left of top box)
     corner @ ('TR', 0.55, 0.20)  (row-lock with head — TR8 rule 5)
     tail   @ ('MR', 0.55, 0.10)  (col-lock with corner — TR8 rule 6)

  s2 = 横 (middle tier): short flat middle bar.
     head @ ('ML', 0.30, 0.55)
     tail @ ('MR', 0.30, 0.55)   (row-lock)

  s3 = 竖折折钩 (bottom tier): descend → sweep left → hook up-left.
     head    @ ('MR', 0.30, 0.75)  (col-share with s2.tail's x)
     corner1 @ ('BR', 0.30, 0.40)  (short vertical drop, col-lock)
     corner2 @ ('BL', 0.20, 0.40)  (sweep left, row-lock with corner1)
     hook_pt @ ('BL', 0.20, 0.10)  (up-tick from corner2)
     tip     @ ('BL', 0.55, 0.05)  (flick UP-RIGHT into the bowl)

Joints:
  s1.tail ⇆ s2.head : N (~30 px, top→middle tier separator)
  s2.tail ⇆ s3.head : N (~25 px, middle→bottom tier separator)
  s3 hook is internal to the compound stroke.

Root cause fix: chronic B2-B5 弓 failed because tiers ran together OR
bottom bowl inverted. This plan hard-separates the three tiers by
using distinct rows (T, M, B) for s1/s2/s3 heads, and forces
column-shared verticals.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..')))

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from heng import draw_heng
from heng_zhe import draw_heng_zhe


def _shu_zhe_zhe_gou_leftward(draw, head, corner1, corner2, hook_pt, tip,
                              width=9, color=(0, 0, 0)):
    """Custom 竖折折钩 for 弓 whose bottom sweeps LEFT (not right).

    The stock shu_zhe_zhe_gou.py asserts heng goes RIGHT — wrong for 弓.
    """
    p_head    = anchor_to_xy(head)
    p_corner1 = anchor_to_xy(corner1)
    p_corner2 = anchor_to_xy(corner2)
    p_hook_pt = anchor_to_xy(hook_pt)
    p_tip     = anchor_to_xy(tip)

    # vertical descent
    fat_line(draw, p_head, p_corner1, width=width, color=color)
    # leftward heng
    fat_line(draw, p_corner1, p_corner2, width=width, color=color)
    # up-tick vertical
    fat_line(draw, p_corner2, p_hook_pt, width=width, color=color)
    # hook flick up-right
    ctrl = (p_hook_pt[0] + (p_tip[0] - p_hook_pt[0]) * 0.15,
            p_hook_pt[1] + (p_tip[1] - p_hook_pt[1]) * 0.55)
    hook_pts = quad_bezier(p_hook_pt, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [width + (2 - width) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)


def draw_gong_bow(draw, color=(0, 0, 0)):
    # s1 — 横折 top tier
    draw_heng_zhe(draw,
                  ('TL', 0.30, 0.20),
                  ('TR', 0.55, 0.20),
                  ('MR', 0.55, 0.10),
                  h_width=9, v_width=9, shoulder=12, color=color)

    # s2 — 横 middle tier
    draw_heng(draw, ('ML', 0.30, 0.55), ('MR', 0.30, 0.55),
              width=9, color=color)

    # s3 — 竖折折钩 bottom tier (leftward sweep + up-right hook)
    _shu_zhe_zhe_gou_leftward(
        draw,
        ('MR', 0.30, 0.75),
        ('BR', 0.30, 0.40),
        ('BL', 0.20, 0.40),
        ('BL', 0.20, 0.10),
        ('BL', 0.55, 0.05),
        width=9, color=color,
    )
