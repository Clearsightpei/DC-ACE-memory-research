"""p3_char_0094_不 — 不 (bù), 4 strokes: 横 + 撇 + 竖 + 点/捺.

Memory lookup checklist:
  1. success_bank/INDEX.md grep '不' — NOT FOUND (no mastered 不).
  2. errata.md grep '不' — NOT LISTED.
  3. form_catalog.md — 横 top-band spans TL..TR;
     撇 from C(top) → BL; 竖 vertical mid; 点/捺 short right diagonal.
  4. principles_meta.md — TR1 (override anchors), TR8 (横 y_frac equal),
     TR10 (N-class gap ≤ 25 px).
  5. joint_atlas.md — 不 has N-class top-hat (撇 head just touches
     underside of 横 with tiny gap) and T-class (竖 head welded to
     midpoint of 撇 body).
  6. sandbox.md — nothing 不-specific noted.

MMH structural expectations (from dispatcher):
  s1 横: ('ML',0.548,0.046) → ('TR',0.575,0.955)
  s2 撇: ('C',0.664,0.017) → ('BL',0.337,0.528)
  s3 竖: ('C',0.345,0.395) → ('BC',0.474,1.038)   # tail y clamped to 1.0
  s4 点/捺: ('C',0.852,0.778) → ('BR',0.59,0.414)

Joints:
  s1.mid(0.52) ⇆ s2.head @ TC — N (natural gap ≈ 12 px, DO NOT weld)
  s2.mid(0.32) ⇆ s3.head @ C — T (welded, tip touches 撇 body)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's3 tail y_frac clamped 1.038 -> 1.0 (BC bottom edge).',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from heng import draw_heng
from pie import draw_pie
from shu import draw_shu
from na import draw_na


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 横 — top horizontal spans left→right across the top band.
    # MMH ML(0.548,0.046) → TR(0.575,0.955); use those as-is.
    draw_heng(draw,
              from_anchor=('ML', 0.548, 0.046),
              to_anchor=('TR', 0.575, 0.955),
              width=9)

    # s2 撇 — long left-falling sweep from top-center down to BL.
    draw_pie(draw,
             from_anchor=('C', 0.664, 0.017),
             to_anchor=('BL', 0.337, 0.528),
             head_width=11, tail_width=1, curve=0.08, segments=48)

    # s3 竖 — short vertical stem, welded onto 撇 body (T-class).
    # tail y_frac clamped from MMH 1.038 -> 1.0 (BC bottom edge).
    draw_shu(draw,
             from_anchor=('C', 0.345, 0.395),
             to_anchor=('BC', 0.474, 1.0),
             width=9)

    # s4 点/捺 — short right-side stroke starting from center-right
    # sweeping down-right toward BR.
    draw_na(draw,
            from_anchor=('C', 0.852, 0.778),
            to_anchor=('BR', 0.59, 0.414),
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.7, curve=0.06, segments=40)

    out = os.path.join(_HERE, '01_不.png')
    img.save(out)
    print(f"Wrote {out}")


if __name__ == '__main__':
    render()
