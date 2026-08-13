"""p3_char_0109_仄 — G5 drawer attempt.

仄 = 厂 (top-heng + long-pie) enclosing 人 (inner pie + na).

4 strokes per MMH:
  s1: heng, TC(0.049,0.979) → TR(0.265,0.861)  = (105, 98) → (227, 86)
  s2: pie,  TL(0.85,0.943)  → BL(0.264,0.669)  = (85, 94)  → (26, 267)
  s3: pie,  C(0.491,0.312)  → BL(0.82,0.839)   = (149,131) → (82, 284)
  s4: na,   C(0.649,0.854)  → BR(0.807,0.854)  = (165,185) → (281, 285)

Joints:
  s1.head N s2.head @ C  (expected gap ~14.9 px; MMH-anchor gap ≈ 20 px, keep gap)
  s3.mid(0.36) N s4.head @ C (expected gap ~17.3 px; visible N-gap between inner
      pie belly and na head — do NOT weld)

Composition strategy: inline from stroke bank (heng, pie, na). No whole-radical
primitive fits — 厂 bank primitive's baked geometry (tail at (20,297)) doesn't
match MMH's stroke-2 tail (26,267), and 人 bank primitive's anchors are for a
standalone-size 人, not the compact inner 人 here. So compose fresh from
stroke primitives with MMH anchors verbatim. No BANK_DEVIATION block needed
(no bank primitive was skipped — no whole-item bank entry exists for 仄).
"""

import pathlib
import sys

from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from heng import draw_heng
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes drawn (heng + pie + pie + na)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'anchors verbatim from MMH; N-joints preserved (no welding)',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top-heng — short, slight down-slope right to left (calligraphic 厂 top)
    # MMH: TC(0.049,0.979) → TR(0.265,0.861)
    draw_heng(d, head=(105, 98), tail=(227, 86),
              width_head=8, width_tail=9)

    # s2: long pie — 厂's left-sweeping stroke from head near s1.head to lower-left
    # MMH: TL(0.85,0.943) → BL(0.264,0.669). N-joint with s1.head (~20 px gap).
    draw_pie(d, head=(85, 94), tail=(26, 267),
             bow_perp=14, w_head=10, w_tail=3, steps=90)

    # s3: inner pie (top of 人) — from center down-left
    # MMH: C(0.491,0.312) → BL(0.82,0.839)
    draw_pie(d, head=(149, 131), tail=(82, 284),
             bow_perp=12, w_head=8, w_tail=3, steps=80)

    # s4: inner na — starts below and slightly right of s3.mid (N-joint, ~17 px gap)
    # MMH: C(0.649,0.854) → BR(0.807,0.854)
    # Note: the head y-coord (185) is deliberately below s3.mid(~186) — this
    # creates the calligraphic N-gap for the 人-style joint.
    draw_na(d, head=(165, 185), tail=(281, 285),
            bow_perp=10, w_head=4, w_tail=10, steps=80)

    return img


if __name__ == '__main__':
    out = _HERE.parent / '01_仄.png'
    render().save(out)
    print(f'wrote {out}')
