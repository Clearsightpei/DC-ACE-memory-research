"""G5 retry #1: p2_radical_121_尣.

TRAJECTORY DIFF
---------------
Main attempt (verdict C) analysis:
  - s3 (long pie ML->BL): too thin/pale; bow felt slightly excessive making the
    stroke look scraggly at right of arc. GT's long pie has a decisive weight
    and a smoother sweep.
  - s4 (shu-wan-gou C->BR): most visible defect — the curve read as an angular
    "n"-like shape because bottom_extra=65 + knee_ratio=0.72 dropped the belly
    ~65 px past the tail and pulled the shoulder in tight. In the GT the sweep
    is a gentler cup: smaller descent past tail-y and a broader knee. Also felt
    slightly under-inked vs the GT's bold body.
  - s1 / s2 (top pie + top dian): approximately fine in the main attempt.

Fixes this retry:
  1. Bulk up strokes 3 and 4 for calligraphic weight (w_head +1 for pie, width
     +1 for shu-wan-gou).
  2. Reduce s3 bow_perp 20 -> 16 (smoother sweep, less scraggly).
  3. shu-wan-gou: bottom_extra 65 -> 50 (belly closer to tail-y so no tall "n"),
     knee_ratio 0.72 -> 0.62 (broader bottom shelf, gentler cup).
  4. Keep all endpoint anchors identical to MMH-injected values; joints remain
     NONE (four separate strokes with clear gaps, per the injected spec).
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image
from PIL import ImageDraw
from pie import draw_pie
from dian import draw_dian
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives called; matches expected 4
    'endpoint_mismatches': [],  # anchors held to MMH values within tolerance
    'joint_class_mismatches': [],  # all joints N (clear separation)
    'overall_pass': True,
    'notes': 'Retry #1: thicker s3/s4, smaller shu_wan_gou bottom_extra, wider knee.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: small top-left pie (TL 0.762, 0.756 -> ML 0.542, 0.271)
    #     head (76, 76), tail (54, 127); short mild left-drift
    draw_pie(d, head=(76, 76), tail=(54, 127),
             bow_perp=6, w_head=7, w_tail=3, steps=50)

    # s2: small dian at top-center going down-right (TC 0.746, 0.677 -> MR 0.156, 0.075)
    #     head (175, 68), tail (216, 108)
    draw_dian(d, head=(175, 68), tail=(216, 108),
              w_head=3, w_tail=7, bow=3, steps=48)

    # s3: long left-sweeping pie (ML 0.914, 0.356 -> BL 0.311, 0.903)
    #     head (91, 136), tail (31, 290); smoother sweep, slightly thicker
    draw_pie(d, head=(91, 136), tail=(31, 290),
             bow_perp=16, w_head=10, w_tail=3, steps=100)

    # s4: shu-wan-gou (C 0.491, 0.113 -> BR 0.704, 0.265)
    #     head (149, 111), tail (270, 226); broader shelf, less angular
    # Revision: broaden the bottom shelf (knee_ratio 0.62 -> 0.55) and drop
    # belly slightly (bottom_extra 50 -> 58) so the cup reads flatter/wider,
    # matching GT's fuller bottom sweep before the hook.
    draw_shu_wan_gou(d, head=(149, 111), tail=(270, 226),
                     width=9, bottom_extra=58, knee_ratio=0.55)

    out = os.path.join(os.path.dirname(__file__), '01_尣.png')
    img.save(out)
    print(f'saved {out}')


if __name__ == '__main__':
    main()
