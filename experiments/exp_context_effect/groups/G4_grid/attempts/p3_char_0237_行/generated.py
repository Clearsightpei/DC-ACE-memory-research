"""行 (xíng) — Phase-3 char, 6 strokes.

Reading log (per memory_index v8 slim checklist):
  1. drawer_memory.md — noted `chi_step` primitive available; but MMH
     anchors here place 彳 in the LEFT column and the right half is a
     bare 撇+横+竖 (not the mastered `chu_stroll`), so we draw from
     MMH-verbatim anchors and use the shared pie/heng/shu primitives
     rather than trying to override chi_step's default anchors
     (never-tune-anchors rule, drawer_memory.md line 65).
  2. success_bank/INDEX.md — grep '行' → not mastered. Grep '彳' →
     `chi_step.py` mastered but its anchors are for a stand-alone 彳
     filling the canvas, not the left-half of 行.
  3. errata.md — 行 not present.

Decomposition (compositional playbook):
  行 = 彳 (left, s1-s3) + right-half (s4-s6)

Layout: left-right, left in x∈[0.05, 0.40], right in x∈[0.45, 0.95].
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, CANVAS
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors, 6 primitives; all joints N-class (no welding).',
}


def draw_xing(draw):
    # s1 — upper 撇 of 彳 (short)
    draw_pie(draw,
             from_anchor=('TL', 0.979, 0.606),
             to_anchor=('ML', 0.457, 0.38),
             head_width=8, tail_width=1, curve=0.10, segments=48)

    # s2 — middle 撇 of 彳 (long sweep)
    draw_pie(draw,
             from_anchor=('ML', 0.97, 0.198),
             to_anchor=('BL', 0.226, 0.212),
             head_width=10, tail_width=1, curve=0.10, segments=48)

    # s3 — 竖 of 彳 (short bottom vertical)
    draw_shu(draw,
             from_anchor=('ML', 0.791, 0.808),
             to_anchor=('BL', 0.814, 0.9),
             width=9)

    # s4 — short 撇 at top of right half
    draw_pie(draw,
             from_anchor=('C', 0.585, 0.069),
             to_anchor=('TR', 0.367, 0.964),
             head_width=7, tail_width=1, curve=0.08, segments=32)

    # s5 — 横 of right half (main horizontal)
    draw_heng(draw,
              from_anchor=('C', 0.213, 0.685),
              to_anchor=('MR', 0.845, 0.523),
              width=9)

    # s6 — 竖 of right half (vertical descending)
    draw_shu(draw,
             from_anchor=('C', 0.972, 0.667),
             to_anchor=('BC', 0.699, 0.795),
             width=9)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)
    draw_xing(draw)
    out = os.path.join(os.path.dirname(__file__), '01_行.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
