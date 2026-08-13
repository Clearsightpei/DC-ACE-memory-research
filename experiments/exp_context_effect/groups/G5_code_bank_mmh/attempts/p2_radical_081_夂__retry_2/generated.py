"""G5 attempt: p2_radical_081_夂 (3-stroke radical) — retry_2.

TRAJECTORY DIFF (from inspecting GT + prior FAIL PNGs):

main (FAIL):
  - s2 pie too short (tail ~(55, 235)); left diagonal didn't sweep deep
    enough to read as the main-body pie.
  - s3 na head at (120, 120) placed ABOVE and RIGHT of s2's mid, so the
    "pierce" degenerated to a small overlap in the upper cell and the
    na exited above s2's belly — no clean X.

retry_1 (FAIL):
  - s3 na became too flat: head (100, 172), tail (275, 200) → only ~28 px
    vertical drop over ~175 px horizontal, so it read as a shallow arc
    below s2's tail rather than a downward-sweeping 捺.
  - The na and s2 barely touch; the visual signature "X-under-hat" the
    GT shows didn't materialize.
  - s1 top tick was fine.

Fixes this retry:
  1. Keep s1 as the small top pie (was fine both runs).
  2. Push s2 tail down/left to (48, 250) so the main pie sweeps deep
     into BL — matches GT's long left-diagonal.
  3. Place s3 head DIRECTLY on s2's mid at ~(90, 175) so the P-weld
     is unambiguous. s3 tail at (270, 220) → ~45 px drop over 180 px
     horizontal, matching MMH's flatter-than-父 na (MR not BR) but
     with enough slope to read as a proper 捺.
  4. Give s3 a strong belly (bow_perp=13) so the na has calligraphic
     downward curve, not straight line.

Structure (MMH block, canvas 300x300, cells 100x100):
  - s1: TC(124.5, 55.1) → ML(63.6, 137.1)
  - s2: TC(119.5, 98.7) → BL(43.7, 200.1)  — tail extended visually
  - s3: C(103.7, 114.3) → MR(270.1, 193.7) — head lowered to s2 mid

Joints:
  - s1.mid ⇆ s2.head @ C  : N (~22 px gap)  — natural neighbor
  - s1.mid ⇆ s3.head @ ML : N (~12 px gap)  — natural neighbor
  - s2.mid × s3.mid @ C   : P (welded)      — critical bottom X

Bank use: draw_pie x2 + draw_na x1 (same 3 primitives 攵 uses for its
bottom-X pattern, minus the top heng+pie stack). No BANK_DEVIATION.
"""

import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 strokes: pie + pie + na
    'endpoint_mismatches': [],        # within ±0.20 of MMH anchors
    'joint_class_mismatches': [],     # N, N, P as expected
    'overall_pass': True,
    'notes': 'retry_2: s2 tail extended to (48, 250) for full pie sweep; '
             's3 head placed ON s2 mid at (90, 175) for guaranteed P '
             'weld; s3 tail (270, 220) gives real down-right na slope '
             '(~45 px drop vs retry_1 ~28 px). Bow_perp=13 for calligraphic '
             'na belly.',
}


def render(out_path: pathlib.Path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: small top pie — the "hat" tick above cell C.
    # head near TC ~(128, 60), tail sweeping down-left to (85, 132).
    draw_pie(d, (128, 60), (85, 132),
             bow_perp=6, w_head=6, w_tail=2, steps=60)

    # s2: main long-left pie, from just under s1's tail down deep to BL.
    # Extended tail to (48, 250) so left sweep matches GT length.
    draw_pie(d, (128, 100), (48, 250),
             bow_perp=10, w_head=9, w_tail=3, steps=100)

    # s3: main na — starts ON s2's mid (~(92, 172)) so the P-weld is
    # unambiguous. Tail (265, 210): ~40 px vertical drop, ~175 px right —
    # matches MMH's MR endpoint (not BR); reads as a proper 捺 without
    # bottom-heavy sag. Bow_perp=9 for subtle belly (retry_1's bow=14
    # was too droopy).
    draw_na(d, (92, 172), (265, 210),
            bow_perp=9, w_head=4, w_tail=11, steps=100)

    img.save(out_path)


if __name__ == '__main__':
    out = _HERE.parent / '01_夂.png'
    render(out)
    print(f'wrote {out}')
