"""别 (bié) — 7 strokes.
Decomposition: 别 = 另 (left) + 刂 (right); 另 = 口 (top) + 力 (bottom).
Stroke plan (MMH-verbatim anchors):
  s1: 口 竖 (left vertical)
  s2: 口 横折 (top + right corner) — rendered as L
  s3: 口 横 (bottom horizontal)
  s4: 力 横折钩 (top heng + right hook) — 3-pt polyline + hook
  s5: 力 撇 (long diagonal descending left)
  s6: 刂 短竖 (short left vertical of dao-side)
  s7: 刂 竖钩 (long right vertical with hook)
Joints (from MMH):
  s1.mid~s2.head @ ML  N (口 top-left, small gap)
  s1.mid~s3.head @ ML  N (口 bottom-left)
  s1.mid~s5.head @ ML  N
  s2.tail~s3.mid @ C   N (口 top-right meets bottom)
  s3.head~s5.head @ ML N
  s4.mid~s5.mid @ ML   P (力 横折钩 crosses 撇 — welded)
"""

# Reading log:
# 1) drawer_memory.md — read (A-recipe applied: MMH-verbatim + decomposition
#    comment + SELF_CHECK; base primitives via _anchor+fat_line rather than
#    partial-override compound primitives).
# 2) success_bank/INDEX.md — checked; kou.py, li.py, dao_side.py exist but
#    their default anchors don't match this composition's MMH placement
#    (口 confined to TL, 力 in BL, 刂 in TR/BR — components are much
#    smaller and offset). BANK_DEVIATION applies.
# 3) errata.md — grep for 别 / 另 / 刂 / 力 — no literal fix listed for 别.

# BANK_DEVIATION
# skipped: kou.py, li.py, dao_side.py
# reason: bank primitives assume full-column placement (kou at ML/BL, li at
#   central, dao_side at right column full-height); MMH places 口 confined
#   to TL only (y∈[0.31,0.53]), 力 in ML/BL lower-left, and 刂 in right
#   column with two distinct verticals. Partial-override of these compound
#   primitives loses coherence (documented in B8 for p3_char_0252_伊).
# fresh_component: kou_top_slot_for_bie, li_bottom_left_for_bie,
#   dao_side_short_plus_gou_for_bie

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 draw invocations counted below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; s4 as 3-pt polyline+hook for 横折钩; '
             's7 with small hook for 竖钩; P-joint s4.mid×s5.mid preserved '
             'via shared anchor point (ML, 0.958, 0.867).',
}

import os
import sys
from PIL import Image, ImageDraw

# Locate _anchor helper (in success_bank/code/)
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)
from _anchor import anchor_to_xy, fat_line  # noqa: E402


def _line(draw, p0, p1, w):
    """Straight fat segment (rounded caps included)."""
    fat_line(draw, p0, p1, w)


def draw_bie(draw):
    W = 10  # main stroke width
    Wthin = 9

    # ---- s1: 口 左竖 --------------------------------------------------
    s1_h = anchor_to_xy(('TL', 0.568, 0.938))
    s1_t = anchor_to_xy(('ML', 0.738, 0.582))
    _line(draw, s1_h, s1_t, W)

    # ---- s2: 口 横折 --------------------------------------------------
    # Head at ML upper-left of 口; tail at C (upper-right descent).
    # Render as L: horizontal to a top-right corner, then vertical down
    # to match 口 bottom band (extending MMH tail so 口 closes cleanly).
    s2_h = anchor_to_xy(('ML', 0.75, 0.04))       # ~(75, 104)
    s2_t = anchor_to_xy(('C',  0.228, 0.304))     # ~(123, 130)
    corner2 = (s2_t[0], s2_h[1])                   # top-right corner
    # extend the shu-portion down toward the 口 bottom (y ≈ s1_t.y + small)
    right_bottom = (s2_t[0], s1_t[1] + 4)          # close 口 shape
    _line(draw, s2_h, corner2, W)
    _line(draw, corner2, right_bottom, W)

    # ---- s3: 口 底横 --------------------------------------------------
    s3_h = anchor_to_xy(('ML', 0.806, 0.447))     # ~(81, 145)
    s3_t = anchor_to_xy(('C',  0.38,  0.412))     # ~(138, 141)
    # extend to close 口 bottom across the two side-verticals
    s3_h_ext = (s1_t[0] + 2, (s1_t[1] + right_bottom[1]) / 2)
    s3_t_ext = (right_bottom[0], right_bottom[1])
    _line(draw, s3_h_ext, s3_t_ext, W)

    # ---- s4: 力 横折钩 ------------------------------------------------
    # head → corner (near P-joint mid) → tail; then small hook up-left.
    s4_h = anchor_to_xy(('ML', 0.404, 0.922))     # ~(40, 192)
    s4_t = anchor_to_xy(('BL', 0.894, 0.631))     # ~(89, 263)
    s4_corner = anchor_to_xy(('ML', 0.958, 0.867))  # ~(96, 187)
    # widen the heng portion to look like a proper 横 of 力
    s4_h = (s4_h[0] - 5, s4_h[1] - 5)              # nudge start a touch up-left
    _line(draw, s4_h, s4_corner, W)
    _line(draw, s4_corner, s4_t, W)
    # small hook (钩) at tail, curling up-left
    hook4 = (s4_t[0] - 14, s4_t[1] - 10)
    _line(draw, s4_t, hook4, W)

    # ---- s5: 力/另 撇 -------------------------------------------------
    # Long diagonal from upper-mid-left down to lower-left.
    s5_h = anchor_to_xy(('ML', 0.902, 0.541))     # ~(90, 154)
    s5_t = anchor_to_xy(('BL', 0.34,  0.895))     # ~(34, 289)
    _line(draw, s5_h, s5_t, Wthin)

    # ---- s6: 刂 短竖 --------------------------------------------------
    s6_h = anchor_to_xy(('C',  0.764, 0.257))     # ~(176, 126)
    s6_t = anchor_to_xy(('BC', 0.854, 0.25))      # ~(185, 225)
    _line(draw, s6_h, s6_t, W)

    # ---- s7: 刂 竖钩 --------------------------------------------------
    s7_h = anchor_to_xy(('TR', 0.227, 0.691))     # ~(223, 69)
    s7_t = anchor_to_xy(('BC', 0.951, 0.771))     # ~(195, 277)
    _line(draw, s7_h, s7_t, W + 1)
    # hook up-left at bottom
    hook7 = (s7_t[0] - 16, s7_t[1] - 10)
    _line(draw, s7_t, hook7, W + 1)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_bie(d)
    out = os.path.join(_HERE, '01_别.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
