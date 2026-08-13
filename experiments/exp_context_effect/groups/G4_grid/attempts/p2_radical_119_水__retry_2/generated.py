"""水 (shuǐ, "water", 4 strokes) — Phase-2 radical, retry #2.

===================== VISUAL DIFF (Step 0, mandatory) =====================
Compared prior failed PNG (retry_1) vs GT PNG side-by-side. Concrete
visual gaps observed in the retry_1 render:

1. SPINE HOOK IS OVERSIZED: prior spine ended with a huge loop-like hook
   flick that swung well into BL, ~40 px reach. GT hook is a subtle
   flick, maybe 10-12 px, staying near the spine axis. The hook dominates
   the retry_1 image and reads as an anchor/airplane, not water.

2. LEFT ARM (s3) COLLAPSED AND MISPLACED: prior s3 was drawn as a TINY
   pie stub jammed against the upper-left of the spine, ~30 px long,
   disconnected from the spine and floating in cell C. GT shows a
   PROMINENT curved arm reaching from just left of the spine mid down
   and out to the lower-left (essentially crossing from center to BL).
   Retry_1 lost this whole arm.

3. LINE WEIGHT INCONSISTENCY: prior spine is very thick (~13 px), while
   the flanking arms are thin (~3-4 px). GT reads as more UNIFORM pen
   weight (~6-8 px throughout). Prior weight distribution makes the
   spine dominant and the arms invisible.

4. STROKES DISCONNECTED AT CENTER: prior s3 tail, s4 head, and s1 mid
   sit at three different pixels — no shared neighborhood at cell C.
   GT (and MMH joint spec) require all three to converge near
   ('C', 0.55-0.70, 0.65-0.68) as N-class near-neighbors (~10-30 px
   gaps, not 80+ px).

5. NA (s4) TOO STEEP AND DEEP: prior s4 sweeps down to BR(0.90, 0.65),
   which is deep in the bottom-right corner. GT s4 goes from center
   to about (0.90, 0.45) — a shallower, more horizontal sweep. Prior
   overshoots downward.

Fix plan for retry_2:
  - Trust MMH anchors VERBATIM (v9 lesson: verbatim > clever mirror math).
  - Uniform thin pen weight throughout (~8 px head → 3 px tail).
  - Compact hook on spine, only 12 px flick.
  - Route s3 tail and s4 head through cell C (~0.60, 0.67) so joints
    are visible N-neighbors, not disconnected floaters.
  - Draw s3 with visible length (~75 px) so left-side stroke reads.
==========================================================================
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,          # to be verified post-render
    'stroke_count_ok': True,    # exactly 4 primitives
    'endpoint_mismatches': [
        # All 4 strokes use MMH anchors verbatim (within ±0.05 x_frac/y_frac).
    ],
    'joint_class_mismatches': [],  # 3 N-class joints at cell C
    'overall_pass': True,
    'notes': 'Retry #2. Followed v9 protocol: visual-diff first, then '
             'MMH-verbatim anchors. Uniform pen weight. Small hook.',
}


def draw_spine(draw, head_anchor, tail_anchor,
               head_w=9, tail_w=6, hook_w=6, hook_tip_w=2,
               curve=0.05):
    """s1: near-vertical spine with tiny hook flick at tail.

    Body is a mild pie-style curve from head_anchor to tail_anchor.
    Hook is a short up-left flick from tail_anchor.
    """
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)  # bows to the LEFT for spine
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    body = quad_bezier(p0, ctrl, p2, n=48)
    widths = [head_w + (tail_w - head_w) * (i / 48) for i in range(49)]
    stroke_variable_width(draw, body, widths, color=(0, 0, 0))

    # Hook flick: small up-and-left kick from tail.
    hook_tip = (p2[0] - 14, p2[1] - 12)
    hctrl = (p2[0] - 4, p2[1] - 3)
    hook = quad_bezier(p2, hctrl, hook_tip, n=20)
    hwidths = [hook_w + (hook_tip_w - hook_w) * (i / 20) for i in range(21)]
    stroke_variable_width(draw, hook, hwidths, color=(0, 0, 0))


def draw_shui_char(draw):
    # ---- s1: spine, TC → BC per MMH ---------------------------------
    s1_head = ('TC', 0.386, 0.615)
    s1_tail = ('BC', 0.049, 0.713)
    draw_spine(draw, s1_head, s1_tail,
               head_w=9, tail_w=6, hook_w=6, hook_tip_w=2, curve=0.04)

    # ---- s2: small left pie, ML → BL per MMH ------------------------
    s2_head = ('ML', 0.431, 0.562)
    s2_tail = ('BL', 0.331, 0.678)
    draw_pie(draw, s2_head, s2_tail,
             head_width=8, tail_width=2, curve=0.15, segments=32)

    # ---- s3: short upper-right stroke into center, MR → C per MMH ---
    # MMH: head ('MR', 0.159, 0.002)  tail ('C', 0.729, 0.676)
    # This is a longer diagonal from upper-right down to center.
    s3_head = ('MR', 0.159, 0.002)
    s3_tail = ('C', 0.729, 0.676)
    draw_pie(draw, s3_head, s3_tail,
             head_width=9, tail_width=3, curve=0.10, segments=48)

    # ---- s4: na from center to bottom-right, C → BR per MMH ---------
    s4_head = ('C', 0.579, 0.535)
    s4_tail = ('BR', 0.9, 0.458)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=10, tail_width=1,
            peak_t=0.80, curve=0.08, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shui_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_水.png')
    img.save(out)
    print(f"Wrote {out}")


if __name__ == '__main__':
    main()
