"""纟 (sī, silk radical, 3 strokes) — G4 drawer, first attempt.

Lookup checklist:
  1. success_bank grep for 纟: not present.
  2. errata grep 纟: p2_radical_070_纟 FAIL — fix idea: "compact both
     撇折 (~<60 px each), stack tightly along a single column, pivots
     in same column; s3 提 head directly under s2 tail, sweeping
     up-right. Model after yao_small.py (幺)." I follow this literally.
  3. form_catalog: 撇折 in stacked-radical context → compact, low-shoulder.
  4. principles_meta TR1: OVERRIDE anchors (never default). TR9: 纟 is
     a LEFT-position radical here rendered STANDALONE — expand y-span
     to fill the frame; keep x compact (tall thin body).
  5. joint_atlas: N-class joints (2 total per MMH block) — leave small
     visible gaps (~11 px), do NOT weld.

Composition (from MMH-derived structural expectations block):
  s1 — 撇折 (top loop)  head TC(0.354,0.762) → tail C(0.444,0.731)
  s2 — 撇折 (mid loop)  head C (0.679,0.304) → tail BC(0.761,0.153)
  s3 — 提 (bottom)      head BL(0.914,0.795) → tail BC(0.872,0.435)

For each 撇折 we add a pivot anchor down-left of the tail (MMH gives
only 2 endpoints; the elbow is implicit). Placed roughly at the
tail's y and ~30 px left, matching yao_small convention.

Joint spec:
  s1.tail ⇆ s2.mid(0.32) @ C   — N (~12 px gap, do NOT weld)
  s2.tail ⇆ s3.mid @ BC        — N (implicit, small gap)
"""

import os
import sys
from PIL import Image, ImageDraw

# Import shared primitives from the success_bank code dir.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy  # noqa: E402
from pie_zhe import draw_pie_zhe  # noqa: E402
from ti import draw_ti            # noqa: E402


SELF_CHECK = {
    'visual_ok': False,
    'stroke_count_ok': True,   # 3 strokes = 3 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': False,
    'notes': ('first render: s1 and s2 merged into one long staircase — '
              'the two 撇折 loops must read as separate stacked pieces. '
              'Revised: shortened both 撇折 sweeps + tighter pivot placement '
              'so top loop is compact around y~80-130 and middle loop lives '
              'around y~150-210, giving the ~11 px N-gap MMH expects.'),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- s1: 撇折 (top loop) — very compact ---------------------------
    # MMH: head TC(0.354, 0.762) → tail C(0.444, 0.731)
    # Pivot placed just below the head so the 撇 sweep is short (~30 px),
    # then the heng runs right to tail. Keeps the whole loop < ~65 px tall.
    s1_head  = ('TC', 0.354, 0.762)
    s1_pivot = ('C',  0.20,  0.68)
    s1_tail  = ('C',  0.444, 0.731)
    draw_pie_zhe(draw, s1_head, s1_pivot, s1_tail,
                 pie_head_w=7, pie_tip_w=3, heng_w=5, shoulder=3)

    # ---- s2: 撇折 (mid loop) — compact --------------------------------
    # MMH: head C(0.679, 0.304) → tail BC(0.761, 0.153).  Head starts
    # ~11 px right and below s1's tail (N-gap). Pivot down-left of tail.
    s2_head  = ('C',  0.679, 0.304)
    s2_pivot = ('BC', 0.40,  0.10)
    s2_tail  = ('BC', 0.761, 0.153)
    draw_pie_zhe(draw, s2_head, s2_pivot, s2_tail,
                 pie_head_w=9, pie_tip_w=4, heng_w=6, shoulder=4)

    # ---- s3: 提 (bottom rising flick) ---------------------------------
    # MMH: head BL(0.914, 0.795) → tail BC(0.872, 0.435).
    s3_head = ('BL', 0.914, 0.795)
    s3_tail = ('BC', 0.872, 0.435)
    draw_ti(draw, s3_head, s3_tail,
            head_width=11, tail_width=2, curve=0.08, segments=48)

    out = os.path.join(_HERE, '01_纟.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
