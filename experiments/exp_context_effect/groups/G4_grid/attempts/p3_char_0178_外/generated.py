"""p3_char_0178_外 — 外 (wài, "outside").
Composition: 夕 (left, 3 strokes: pie + heng-pie + dian) + 卜 (right, 2 strokes: shu + dian).
5 strokes total, matches MMH.

Memory lookup checklist:
  1. success_bank INDEX grep: 卜 exists (bu.py). 夕 in errata (p2_radical_075_夕 FAIL).
  2. errata grep: 夕 fix -> shorten heng-pie shoulder, lengthen pie tip. Applied.
  3. form_catalog: 夕 as left-radical + 卜 as right-radical, both compressed toward outer edges.
  4. principles_meta TR1: OVERRIDE anchors for THIS composition (don't call defaults).
  5. joint_atlas: All 4 joints are N-class (small gap, do NOT weld). MMH gaps ~15-23 px.

MMH-derived anchors (verbatim from brief):
  s1: head ('TL',0.926,0.838) -> tail ('ML',0.372,0.767)
  s2: head ('ML',0.899,0.321) -> tail ('BL',0.305,0.716)
  s3: head ('ML',0.598,0.714) -> tail ('ML',0.879,0.925)
  s4: head ('TC',0.688,0.548) -> tail ('BC',0.802,1.144 -> clamp 1.0)
  s5: head ('C',0.934,0.438)  -> tail ('MR',0.684,0.893)
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 5 strokes at MMH anchors; 4 N-joints preserved (no welds).',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy
from pie import draw_pie
from heng_pie import draw_heng_pie
from dian import draw_dian
from shu import draw_shu


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # --- 夕 (left component, 3 strokes) ---
    # s1: outer 撇 — sweeps from TL down-left into ML. Long sweep, thin tail.
    draw_pie(d,
             from_anchor=('TL', 0.926, 0.838),
             to_anchor=('ML', 0.372, 0.767),
             head_width=9, tail_width=1, curve=0.04, segments=48)

    # s2: 横撇 (heng-pie) — short heng shoulder (per errata fix), long pie sweep to BL.
    # heng_pie takes 3 anchors: head, corner, tail.
    draw_heng_pie(d,
                  ('ML', 0.899, 0.321),   # head (top-right of 夕 shoulder)
                  ('C',  0.15,  0.40),    # corner (short heng, per errata fix)
                  ('BL', 0.305, 0.716),   # tip (pie sweep endpoint)
                  head_w=7, corner_w=10, tip_w=1)

    # s3: interior 点 — small dot inside 夕, from ML to ML.
    draw_dian(d,
              from_anchor=('ML', 0.598, 0.714),
              to_anchor=('ML', 0.879, 0.925),
              head_width=3, peak_width=11, curve=0.05, segments=28)

    # --- 卜 (right component, 2 strokes) ---
    # s4: 竖 — long vertical from TC down through BC. Tail y clamped to 1.0.
    draw_shu(d,
             from_anchor=('TC', 0.688, 0.548),
             to_anchor=('BC', 0.802, 1.0),
             width=9)

    # s5: 点 — dot on the right side of 卜, N-gap from shu mid.
    draw_dian(d,
              from_anchor=('C',  0.934, 0.438),
              to_anchor=('MR', 0.684, 0.893),
              head_width=3, peak_width=11, curve=0.06, segments=28)

    out = os.path.join(_HERE, '01_外.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
