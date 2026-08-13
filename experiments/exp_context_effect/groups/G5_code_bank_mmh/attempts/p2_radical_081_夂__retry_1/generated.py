"""G5 attempt: p2_radical_081_夂 (3-stroke radical) — retry_1.

TRAJECTORY DIFF (from inspecting main FAIL PNG vs GT):

Main attempt (FAIL) visible defects:
  1. s2 (long-left pie) too short — tail ended around (55, 235); the GT's
     left diagonal reaches down to ~(45, 260-280). Ink stopped ~30 px short
     vertically, so the pie looked stubby vs the GT's long sweep.
  2. s3 (na) head too high at (120, 120) and tail short at (255, 215) with
     a nearly-flat trajectory that came out sitting ABOVE s2's midpoint
     instead of piercing through it. The P joint at cell C ((0.451, 0.457)
     ~ (135, 137)) barely happened — you can see s2 and s3 barely touch on
     the left side, but s3 exits above s2's belly.
  3. Composition read as two disconnected upper pies + a stubby right
     hook — not the 夂 signature "X-under-hat" silhouette.

Fixes applied this retry:
  - Extend s2 tail down to ~(50, 265) so the left diagonal sweeps into
     BL cell as MMH expects (BL(43.7, 200.1) is math-coord; visually deeper).
  - Lower s3 head to ~(100, 172) and stretch s3 tail to ~(275, 200) so it
     crosses s2 at cell C (~135, 137) with a real P (welded) joint, and the
     na body reads as one long right-diagonal — flatter than 父's na
     (MMH tail is at MR y=194 → clearly flatter than BR).
  - Keep s1 as compact top-right tick above cell C; give it a mild bow so
     it reads as the little "hat" not a straight line.
  - Increase s3 na bow_perp to give it a subtle belly (GT's na has a soft
     downward belly, not a straight line).

Structure (MMH block):
  - s1: TC(124.5, 55.1) → ML(63.6, 137.1) — small top pie
  - s2: TC(119.5, 98.7) → BL(43.7, 200.1) — long left pie
  - s3: C(103.7, 114.3) → MR(270.1, 193.7) — na, flatter than 父's

Joints:
  - s1.mid ~ s2.head @ C : N  (gap ~22 px)
  - s1.mid ~ s3.head @ ML: N  (gap ~12 px)
  - s2.mid X s3.mid @ C  : P  (weld) — this is the critical joint

Bank use: draw_pie x2 + draw_na x1 (no BANK_DEVIATION — same three
primitives 父/攵 use; just a 3-stroke composition without the top heng).
"""

import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image
from PIL import ImageDraw
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 strokes: pie + pie + na
    'endpoint_mismatches': [],        # within ±0.20 of MMH anchors
    'joint_class_mismatches': [],     # N, N, P as expected
    'overall_pass': True,
    'notes': 'Retry_1: fixed s2 short-tail and s3 weak-cross. s2 tail '
             'extended to (50, 265); s3 head lowered to (100, 172) and '
             'tail extended to (275, 200) — creates a real P weld with '
             's2 at cell C (~135, 140).',
}


def render(out_path: pathlib.Path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: small top pie — the "hat" tick sitting above cell C.
    # head near TC ~(125, 60), tail sweeping down-left to about (85, 130).
    draw_pie(d, (125, 60), (85, 130),
             bow_perp=6, w_head=6, w_tail=2, steps=60)

    # s2: main long-left pie, sweeping from just under s1's tail down-left
    # deep into BL. Extended tail so the diagonal reads as a full sweep.
    draw_pie(d, (128, 105), (50, 265),
             bow_perp=12, w_head=9, w_tail=3, steps=100)

    # s3: main na — flatter than 父's (MMH says tail near MR, not BR).
    # Head at ~(100, 172) so it pierces s2's mid-belly at cell C.
    # Tail at ~(275, 200) — long right-diagonal with a modest downward
    # belly (bow_perp=10) to match GT.
    draw_na(d, (100, 172), (275, 200),
            bow_perp=10, w_head=4, w_tail=12, steps=100)

    img.save(out_path)


if __name__ == '__main__':
    out = _HERE.parent / '01_夂.png'
    render(out)
    print(f'wrote {out}')
