"""G5 drawer attempt — p2_radical_085_贝 (bèi — shell/cowrie, 4 strokes).

Decomposition (from GT + injected MMH structural block):
  s1: 竖 (left vertical of top box)          — shu, head (93,79) → tail (101,232)
  s2: 横折 (top + right, boxy corner)         — heng_zhe_box, TL≈(101,80), BR≈(201,231)
  s3: 撇 (long down-left leg)                 — pie, head (136,108) → tail (60,299)
  s4: 点/短捺 (right leg)                     — dian, head (171,243) → tail (229,290)

Joint expectation from brief:
  s1.head ⇆ s2.head @ TC — class N (neighbor, ~14.7 px gap). Confirmed:
  s1.head=(93,79), s2.head=(111,80) → gap ~18 px. Do NOT weld.

Bank usage: uses draw_shu, draw_heng_zhe_box, draw_pie, draw_dian. No BANK_DEVIATION.
"""

import sys
import pathlib
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve()
GROUP_ROOT = HERE.parents[2]
sys.path.insert(0, str(GROUP_ROOT / 'success_bank' / 'code'))

from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,       # v2 render inspected: matches GT silhouette
    'stroke_count_ok': True, # 4 primitive calls, matching MMH count=4
    'endpoint_mismatches': [
        {'stroke': 4, 'expected_tail_y': 303.5, 'actual_tail_y': 288,
         'delta': 15.5, 'note': 'capped to stay inside canvas'},
    ],
    'joint_class_mismatches': [],  # N-joint gap ~14 px (spec: ~14.7 px)
    'overall_pass': True,
    'notes': 'v2: pie head lowered slightly for visual entry from top of box; '
             's2 top-left pulled to x=110 for correct N-joint gap ~14 px vs s1.head=(95,80).',
}


def render(out_png: pathlib.Path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: left vertical 竖 (soft top head → straight descent)
    draw_shu(d, head=(95, 80), tail=(101, 232), width=7, top_curl=False)

    # s2: 横折 boxy — top horizontal from (~110, 80) right to (~205, 80),
    # then vertical drop to (~205, 232). N-gap ~15 px between s1.head and s2.head.
    draw_heng_zhe_box(d, top_left=(110, 80), bottom_right=(205, 232), width=7)

    # s3: long 撇 sweeping from just inside top of box down to bottom-left corner
    draw_pie(d, head=(148, 115), tail=(55, 295),
             bow_perp=15, w_head=8, w_tail=3, steps=80)

    # s4: right leg — a tapered 点/短捺 sweeping down-right
    draw_dian(d, head=(172, 238), tail=(228, 288),
              w_head=3, w_tail=9, bow=4, steps=48)

    img.save(out_png)


if __name__ == '__main__':
    out = HERE.parent / '01_贝.png'
    render(out)
    print(f'Wrote {out}')
