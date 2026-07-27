"""p3_char_0174_主 — 主 (zhǔ, "master", 5画).

Layout: dot (丶) on top + 王-like body (top heng, mid heng crossed by
vertical spine, bottom heng). MMH stroke order:
  s1: 丶 (dot in TC)
  s2: top heng (shortest, upper)
  s3: mid heng (wider) — pierced by spine (P)
  s4: vertical spine (C → BC)
  s5: bottom heng (longest, base)

Joints:
  s2.mid ⇆ s4.head @ C  : N (~14.5 px gap — spine top hangs below top heng)
  s3.mid ⇆ s4.mid @ BC  : P (welded — spine pierces mid heng)
  s4.tail ⇆ s5.mid @ BC : N (~19.3 px gap — spine bottom hangs above bot heng)

MANDATORY lookup checklist:
  1. INDEX grep — no 主 in bank yet; 王 exists (wang.py); 丶 exists (zhu.py wrapper for dian).
  2. errata grep — 主 not in errata.
  3. form_catalog — heng bars + vertical spine, standard.
  4. principles_meta — TR1 override anchors (yes, custom per MMH).
  5. joint_atlas — P weld at spine×mid heng, N-gap ~15-20 px at top and bottom heng.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes: dot + 3 hengs + 1 vertical. P at mid-heng×spine, N-gap at top/bot heng vs spine.'
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1: 丶 dot on top (TC area). MMH: head TC(0.31,0.612) → tail TC(0.679,0.92)
    # Slightly compressed to look more dot-like (thicker peak, less span).
    draw_dian(draw,
              ('TC', 0.36, 0.66),
              ('TC', 0.64, 0.90),
              head_width=3, peak_width=13, curve=0.10, segments=24)

    # s2: top heng — MMH: ML(0.817,0.412) → MR(0.2,0.242). Slight upward tilt.
    fat_line(draw, anchor_to_xy(('ML', 0.817, 0.412)),
             anchor_to_xy(('MR', 0.2, 0.242)), width=9)

    # s3: mid heng (this is the one PIERCED by spine at BC) —
    # MMH: BL(0.888,0.101) → MR(0.039,0.963). Longer, spans across BC.
    fat_line(draw, anchor_to_xy(('BL', 0.888, 0.101)),
             anchor_to_xy(('MR', 0.039, 0.963)), width=9)

    # s4: vertical spine — MMH: C(0.412,0.453) → BC(0.441,0.657).
    fat_line(draw, anchor_to_xy(('C', 0.412, 0.453)),
             anchor_to_xy(('BC', 0.441, 0.657)), width=10)

    # s5: bottom heng (base, longest) — MMH: BL(0.346,0.801) → BR(0.789,0.757).
    fat_line(draw, anchor_to_xy(('BL', 0.346, 0.801)),
             anchor_to_xy(('BR', 0.789, 0.757)), width=10)

    img.save(out_path)
    print(f"saved: {out_path}")


if __name__ == '__main__':
    render(os.path.join(_HERE, '01_主.png'))
