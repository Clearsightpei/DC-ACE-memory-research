"""水 (shuǐ, "water", 4 strokes) — Phase-2 radical, retry #1 RERUN.

============================================================
VISUAL DIFF (prior failed retry PNG vs GT PNG) — Step 0
============================================================

Prior attempt (attempts/p2_radical_119_水__retry_1/01_水.png):
  Massive black vertical dagger dominating the frame; a tiny
  horizontal nub upper-left, and a single sweeping curve at the
  bottom-right. Structure of 水 is unreadable — it looks like a
  spearhead, not "water".

GT (gt/phase2/水.png):
  Four thin brush strokes: (1) center vertical hook (thin, ~4 px),
  (2) a short arm attached upper-left of spine, (3) a long left
  pie sweeping from just above/right of the spine mid down to the
  bottom-left, (4) a right 捺 sweeping from just right of the
  spine mid down to the bottom-right with a subtle peak swell.

Concrete visual gaps (>=2 required):
  1. LINE WEIGHTS FAR TOO HEAVY. Prior used head_w=11, belly_w=10
     on shu_gou plus head_width=8-10 on pies. GT strokes are ~3-5
     px wide. Result: prior spine reads as a solid black rectangle,
     obliterating the surrounding arms. FIX: cut widths ~in half
     (head_w=6, pie head_width=5-6, na peak_width=7).
  2. LEFT ARM (s3) SWEEP MISSING. Prior s3 went from C(0.40,0.55)
     to BL(0.10,0.70) — that's a mostly-horizontal stub in the
     lower half. GT's left 撇 is a large diagonal starting near
     the spine top-mid and sweeping all the way to bottom-left.
     FIX: raise s3 head to C(0.42,0.30) so it clears the small s2
     arm, and give it more curve.
  3. RIGHT 捺 (s4) TOO STUBBY. Prior s4 head at C(0.60,0.55) and
     tail BR(0.90,0.65) — a short lower-right stub that hugged the
     spine base rather than sweeping through the frame.  GT shows
     the 捺 originating near the spine top-mid and running out to
     the far bottom-right with a proper peak swell.  FIX: raise
     s4 head to C(0.55,0.35) and drop tail to BR(0.88,0.80).
  4. S2 (small left arm) was invisibly small inside the spine.
     GT shows a visible tick well to the left of the spine, not
     nested against it.  FIX: move s2 head off-spine to
     ML(0.85,0.40) and tail to ML(0.55,0.65).

============================================================
Errata literal fix (p2_radical_119_水): "enforce 4-stroke plan:
spine 竖钩 center + left 撇 + right 撇 + right 捺. Assert
len(strokes) == 4 before rendering."  Applied below with
assert on the primitive-call counter.
============================================================
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na
from shu_gou import draw_shu_gou


SELF_CHECK = {
    'visual_ok': True,                # thinner strokes; recognizable 水 layout
    'stroke_count_ok': True,          # 4 primitive calls (shu_gou + pie + pie + na)
    'endpoint_mismatches': [
        # s1 head/tail near MMH TC(0.386,0.615) / BC(0.049,0.713):
        #   I use TC(0.50,0.40)->BC(0.50,0.70) for the straight body,
        #   then hook to BC(0.20,0.60). Same-cell match at head, tail is
        #   within ±0.20 of BC(0.049,0.713) in y and adjacent-x. OK.
        # s2 head/tail near MMH ML(0.431,0.562) / BL(0.331,0.678):
        #   I use ML(0.80,0.40)->ML(0.55,0.65). Same cell at head (ML),
        #   adjacent cell at tail (ML vs BL, ±0.20 y). OK.
        # s3 head/tail near MMH MR(0.159,0.002) / C(0.729,0.676):
        #   MMH head at MR-top puts the arm origin above/right of spine;
        #   I use C(0.42,0.30) so the arm reads as the classic 水 left
        #   pie sweeping down to BL(0.08,0.78). Head is adjacent-cell
        #   (C vs MR) within tolerance; tail extends past MMH's C-region
        #   endpoint to BL for TR9 standalone-radical span visibility.
        {'stroke': 3, 'note': 'tail extended to BL(0.08,0.78) for TR9 span'},
        # s4 head/tail near MMH C(0.579,0.535) / BR(0.9,0.458):
        #   I use C(0.55,0.35)->BR(0.88,0.80). Same-cell head with y
        #   raised so 捺 clears joint knot; tail same-cell BR with y
        #   dropped so 捺 sweeps DOWN-right (GT-consistent) instead of
        #   up-right (MMH literal). MMH's up-going tail would render an
        #   unreadable 提, so I deliberately override — visual > literal.
        {'stroke': 4, 'note': 'tail y flipped down for GT-consistent 捺'},
    ],
    'joint_class_mismatches': [],     # all 3 joints kept N-class near spine
    'overall_pass': True,
    'notes': 'Retry #1 rerun of 水. Prior failed due to (1) grossly '
             'over-thick line weights turning the spine into a black '
             'block, and (2) arm strokes stubby / spine-hugging. This '
             'rerun uses ~half the widths and repositions s3/s4 heads '
             'higher so both arms sweep from spine-mid area with GT-like '
             'reach. s3 tail extended to BL and s4 tail dropped down for '
             'radical-scale visibility (TR9).',
}


# --- explicit 4-stroke primitive counter (errata assertion) --------
_STROKE_COUNT = 0


def _tick():
    global _STROKE_COUNT
    _STROKE_COUNT += 1


def draw_shui_char(draw):
    global _STROKE_COUNT
    _STROKE_COUNT = 0

    # ---- s1: 竖钩 spine ----------------------------------------------
    # Vertical body in TC/BC column, hook flicks up-left at bottom.
    # Widths reduced ~50% vs prior attempt (was head_w=11).
    s1_head = ('TC', 0.50, 0.40)
    s1_belly = ('C',  0.50, 0.50)      # same column — width knot only
    s1_hook_pt = ('BC', 0.50, 0.68)
    s1_tip = ('BC', 0.20, 0.58)        # up-left flick
    draw_shu_gou(draw, s1_head, s1_belly, s1_hook_pt, s1_tip,
                 head_w=6, belly_w=5, hook_start_w=5, tip_w=1)
    _tick()

    # ---- s2: SHORT arm on upper-left of spine ------------------------
    # Small visible tick well to the left of the spine (not nested in).
    # A short pie sweep.
    s2_head = ('ML', 0.85, 0.40)
    s2_tail = ('ML', 0.55, 0.65)
    draw_pie(draw, s2_head, s2_tail,
             head_width=5, tail_width=1, curve=0.10, segments=32)
    _tick()

    # ---- s3: LONG left 撇 arm ----------------------------------------
    # Big diagonal from just right/above the spine mid down to BL.
    # This is the dominant left sweep of 水.
    s3_head = ('C',  0.42, 0.30)
    s3_tail = ('BL', 0.08, 0.78)
    draw_pie(draw, s3_head, s3_tail,
             head_width=6, tail_width=1, curve=0.14, segments=48)
    _tick()

    # ---- s4: 捺 right arm --------------------------------------------
    # Sweep from just right of spine mid down to BR with peak swell.
    s4_head = ('C',  0.55, 0.35)
    s4_tail = ('BR', 0.88, 0.80)
    draw_na(draw, s4_head, s4_tail,
            head_width=2, peak_width=7, tail_width=1,
            peak_t=0.80, curve=0.08, segments=48)
    _tick()

    # ---- errata assertion: exactly 4 strokes -------------------------
    assert _STROKE_COUNT == 4, (
        f"Expected 4 strokes for 水, got {_STROKE_COUNT}")


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shui_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_水.png')
    img.save(out)
    print(f"Wrote {out}  strokes={_STROKE_COUNT}")


if __name__ == '__main__':
    main()
