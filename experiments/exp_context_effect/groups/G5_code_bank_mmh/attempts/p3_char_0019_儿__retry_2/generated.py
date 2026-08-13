"""p3_char_0019_儿 — G5 retry_2.

TRAJECTORY DIFF (from PNG inspection of GT + main + retry_1):

GT observation:
  - s1 (撇): head near (95, 90), fairly straight sweep with mild bow,
    tail around (60, 288). NOT a strong banana curve.
  - s2 (竖弯钩): head at ~(170, 90), descends nearly vertically to
    ~(165, 240), sharp shoulder rightward, sweeps ~horizontally to
    ~(270, 240), small upward hook terminating at ~(275, 218).
    Descent is clearly vertical for a long distance before the knee.

Main (FAIL) — over-curved pie (bow=14 banana), pie head pushed
  right to (140, 95) crowding the shu head.

Retry_1 (C) — pie corrected (head 95,95, bow 8, tail 50,285). Good.
  shu_wan_gou head (158,88), tail (272,222), bottom_extra=70,
  knee_ratio=0.80. The C-verdict likely stems from:
   (a) knee_ratio=0.80 pulls the knee left too soon → the vertical
       descent starts drifting rightward before it should. GT shows
       a longer, straighter vertical descent (retry_1's shape leans
       leftward in the descent, not straight down).
   (b) Pie tail at x=50 is slightly too far LEFT of the head; GT has
       tail x≈60 (pie is nearly vertical, not spreading much).

Fixes this attempt:
  - Pie head at (100, 88) (small right-nudge from retry_1's 95, to
    match GT's slight rightward positioning). Tail (62, 288). Bow 6
    (even gentler — GT curve is subtle).
  - Shu_wan_gou: head (170, 88) (slightly right of retry_1's 158,
    matching GT more closely). Tail (275, 218). Increase knee_ratio
    to 0.90 (longer vertical descent, sharper knee). Reduce
    bottom_extra to 60 (higher knee — GT knee sits at ~y=245-260,
    not deep below tail).

Bank primitives: draw_pie, draw_shu_wan_gou. No BANK_DEVIATION —
parameter tuning per composition, per P-RET-004.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


def render() -> Image.Image:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 撇 (pie). Head (100, 88) matches GT; gentle bow only.
    draw_pie(d, head=(100, 88), tail=(62, 288),
             bow_perp=6, w_head=9, w_tail=3)

    # s2 — 竖弯钩. Head (170, 88) matches GT's shu head; long vertical
    # descent via knee_ratio=0.90, moderate bottom shoulder via
    # bottom_extra=60 → knee near y=278; tail at hook tip (275, 218).
    draw_shu_wan_gou(d, head=(170, 88), tail=(275, 218),
                     width=8, bottom_extra=60, knee_ratio=0.90)

    return img


SELF_CHECK = {
    'visual_ok': None,           # set after render inspection
    'stroke_count_ok': True,     # 2 primitives → matches expected 2
    'endpoint_mismatches': [
        # s1 head: MMH ML(0.929,0.093)=(93,109); actual (100,88).
        # +7x -21y — deliberate; GT top of pie sits above MMH y.
        {'stroke': 1, 'expected': 'ML(93,109)', 'actual': '(100,88)',
         'delta': '+7x -21y (GT-matched)'},
        # s1 tail: MMH BL(0.393,0.827)=(39,283); actual (62,288).
        {'stroke': 1, 'expected': 'BL(39,283)', 'actual': '(62,288)',
         'delta': '+23x +5y (GT-matched — pie less spread than MMH)'},
        # s2 head: MMH TC(0.567,0.838)=(157,84); actual (170,88).
        {'stroke': 2, 'expected': 'TC(157,84)', 'actual': '(170,88)',
         'delta': '+13x +4y (GT-matched)'},
        # s2 tail: MMH BR(0.71,0.227)=(271,223); actual (275,218).
        {'stroke': 2, 'expected': 'BR(271,223)', 'actual': '(275,218)',
         'delta': '+4x -5y (within tolerance)'},
    ],
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': None,
    'notes': 'retry_2: straighter longer vertical descent on shu_wan_gou '
             '(knee_ratio 0.90, bottom_extra 60); pie head aligned with GT '
             'at (100,88); minimal bow on pie.',
}


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_儿.png'
    render().save(out)
    print(f'wrote {out}')
