"""月 (yuè, moon, 4 strokes) — Phase-2 radical attempt.

Composition:
  s1 — 撇 (left arm sweeping down-left), curved slightly.
  s2 — 横折钩 (top bar + right descending wall + up-left hook flick).
  s3 — inner upper 短横 (short horizontal, upper).
  s4 — inner lower 短横 (short horizontal, lower — sits at the bottom
       of the frame).

Joints (per MMH-derived brief):
  s1.head ⇆ s2.head  → N (small natural gap at top-left, ~15 px).
  s1.mid  ⇆ s3.head  → N (inner-upper bar tucks into the pie body, ~15 px).
  s1.mid  ⇆ s4.head  → N (inner-lower bar tucks into the pie body, ~15 px).

Design notes:
  - Standalone Phase-2 radical → per TR9 expand MMH anchors to fill grid.
  - MMH s2 tail is BC not BR (the right wall curves inward at bottom
    for 月's hook shape) — we still land tail high up in BR to give the
    hook a visible up-left flick per the primitive spec.
  - s3, s4 are short 横 confined to the middle band (row invariant per
    TR8 rule 5): head/tail share the same cell row.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'revision 1: raised the two inner 横 into the upper half of the '
             'frame (closer to GT which stacks them at roughly y_frac 0.42 '
             'and 0.58 within the char region). Tightened right-wall tail '
             'so the hook sits inside the frame.',
}

import sys, os
from PIL import Image, ImageDraw

# Import shared G4 primitives.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy
from pie import draw_pie
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


def draw_yue(draw):
    # --- s1: 撇 (left arm, curved down-left). ---
    # Head near top-center-ish (TR9 span top → BL corner region).
    s1_head = ('TC', 0.45, 0.20)
    s1_tail = ('BL', 0.20, 0.92)
    draw_pie(draw, from_anchor=s1_head, to_anchor=s1_tail,
             head_width=12, tail_width=2, curve=0.09, segments=48)

    # --- s2: 横折钩 (top bar + right wall + up-left hook). ---
    # Head sits just to the right of s1.head, N-gap of ~15 px.
    s2_head = ('TC', 0.60, 0.20)
    s2_corner = ('TR', 0.75, 0.20)
    s2_tail = ('BR', 0.30, 0.90)
    s2_tip = ('BR', 0.02, 0.70)
    draw_heng_zhe_gou(draw, head=s2_head, corner=s2_corner,
                      tail=s2_tail, tip=s2_tip,
                      h_width=10, v_width=10, shoulder=13, tip_w=2)

    # --- s3: inner upper 短横 (row invariant: both share y_frac). ---
    # In the GT the inner bars sit stacked in the upper half of the frame.
    s3_head = ('C', 0.20, 0.28)
    s3_tail = ('C', 0.85, 0.28)
    draw_heng(draw, from_anchor=s3_head, to_anchor=s3_tail, width=8)

    # --- s4: inner lower 短横 (still upper half, just below s3). ---
    s4_head = ('C', 0.20, 0.62)
    s4_tail = ('C', 0.85, 0.62)
    draw_heng(draw, from_anchor=s4_head, to_anchor=s4_tail, width=8)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yue(draw)
    out = os.path.join(_HERE, '01_月.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
