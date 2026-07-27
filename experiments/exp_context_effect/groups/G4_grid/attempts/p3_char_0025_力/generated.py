"""p3_char_0025_力 — G4 grid-bank attempt (revised vs clean GT).

Character: 力 (lì, 2 strokes)
  s1: 横折钩 (heng_zhe_gou) — horizontal from left, bend down at right,
      curved down-and-slightly-inward, hook flick up-left at bottom.
  s2: 撇 (pie) — sweep from top-center down to lower-left, crossing s1's
      horizontal near cell C.

MMH-declared anchors:
  s1 head ML(0.668, 0.474) → px (66.8, 147.4) — start of 横 at LEFT
  s1 tail BC(0.459, 0.596) → px (145.9, 259.6) — hook TIP (up-left flick)
  s2 head TC(0.4,   0.671) → px (140.0,  67.1) — 起笔 above the 横
  s2 tail BL(0.372, 0.845) → px (37.2, 284.5) — 出锋 lower-left
  joint C(0.446, 0.42)    → px (144.6, 142.0) — P weld (crossing)

Interior corner/hook-base of s1 must be inferred (MMH gives only endpoints).
  s1 corner (折 point): TR(0.15, 0.45) → px (215, 145) — top-right, y matches head
  s1 tail-of-body (hook base): BR(0.15, 0.50) → px (215, 250)
  s1 hook tip:                 BC(0.459, 0.596) — MMH tail (up-left flick)

Anchor plan (TR7):
  s1.head        ML(0.668, 0.474) — head of 横
  s1.corner      TR(0.15, 0.45)   — 折 (top-right)
  s1.tail(body)  BR(0.15, 0.50)   — hook base (bottom of down-curve)
  s1.tip         BC(0.459, 0.596) — MMH-declared hook TIP
  s2.head        TC(0.4, 0.671)
  s2.tail        BL(0.372, 0.845)

TR8 sanity:
  - 横 head ML(0.668,0.474) py=147; corner TR(0.15,0.45) py=145 → level ✓ (2px diff).
  - 竖-drop corner TR(0.15,0.45) px=215; tail(body) BR(0.15,0.50) px=215 → vertical ✓.
  - Hook tail(body) (215,250) → tip (146,260): up-and-LEFT ✓.
  - All fracs in [0,1] ✓.

Joint C (P weld):
  s2 chord (140,67) → (37,285). At y=147 (横 level):
     t = (147-67)/(285-67) = 0.367
     x = 140 - 0.367*(140-37) = 140 - 37.8 = 102.2
  Crossing pixel (102, 147) — sits inside cell C (100-200, 100-200) ✓.
  P (welded): the 撇 physically passes through the horizontal — ink overlaps.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'stroke_count_actual': 2,
    'stroke_count_expected': 2,
    'endpoint_mismatches': [],  # all within same-cell + ±0.20
    'joint_class_mismatches': [],
    'joints_check': [
        {'joint': 'C', 'expected_class': 'P',
         'actual_class': 'P',
         'note': '撇 crosses 横 body at ~(102,147), inside cell C. Welded (ink overlaps).'},
    ],
    'overall_pass': True,
    'notes': 'Rebuilt vs clean GT. MMH endpoints honored (same cell, small deltas). '
             'Interior 折 corner and hook base inferred at TR/BR.',
}

import os, sys
from PIL import Image

# Import bank primitives.
BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from PIL import ImageDraw
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 横折钩
    #   Pulled corner slightly LEFT (px 205 instead of 215) so the horizontal
    #   ends inside the character rather than at the right canvas edge.
    #   Also slightly shortened the vertical drop (BR y_frac 0.50 → 0.45)
    #   to match GT's proportion (hook base sits above canvas bottom-third).
    s1_head   = ('ML', 0.668, 0.474)
    s1_corner = ('TR', 0.05, 0.48)   # ~ (205, 148)
    s1_tail   = ('BR', 0.05, 0.45)   # ~ (205, 245)  hook base
    s1_tip    = ('BC', 0.459, 0.596) # MMH-declared hook tip
    draw_heng_zhe_gou(draw, s1_head, s1_corner, s1_tail, s1_tip,
                      h_width=9, v_width=9, shoulder=13, tip_w=2)

    # s2 — 撇
    s2_head = ('TC', 0.4, 0.671)
    s2_tail = ('BL', 0.372, 0.845)
    draw_pie(draw, s2_head, s2_tail,
             head_width=10, tail_width=1, curve=0.10, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_力.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
