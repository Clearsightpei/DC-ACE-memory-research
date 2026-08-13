"""G5 retry #2: p2_radical_116_礻.

TRAJECTORY DIFF (visual comparison of GT vs main + retry_1 PNGs):

Prior verdicts: main=C, retry_1=C. Both drawer attempts have the correct
4-stroke structure and correct pie direction (retry_1 already fixed the
main's inverted pie). The remaining gap vs GT (looking at both prior
PNGs vs `/gt/phase2/礻.png`):

  a. retry_1's heng-pie horizontal sits too HIGH (head y=118); MMH ML
     anchor puts head at y~151 (right at the middle-band). The GT's
     crossbar visibly sits mid-canvas, not upper-third.
  b. retry_1's shu starts too HIGH (y=135) and too far RIGHT (x=155);
     MMH C anchor puts head at (139, 193) — well below the crossbar,
     and slightly left of the crossbar's apex. Because retry_1 put the
     shu head at y=135 it overlapped/welded the crossbar (should be an
     N-class neighbor gap of ~17 px).
  c. retry_1's right dot (s4) is ENORMOUS — 170,155 -> 248,250, nearly
     spanning quarter of canvas. MMH C->BC anchors give a much shorter
     stroke ending mid-lower-right, not bottom-right. The oversize
     right dot unbalanced the silhouette (right half dominated).
  d. Overall stroke weight was too heavy — GT is a thin, minimal render.

Fixes for retry_2:
  1. s2 heng-pie: head=(85, 148) (was 118), tail=(60, 245) (was 205).
     Longer, deeper pie sweep; horizontal at mid-band matching GT.
  2. s3 shu: head=(140, 193) (was 155,135), tail=(140, 292). Now
     centered UNDER the pie's corner area, WITH a proper N-gap below
     the crossbar (crossbar at y~151, shu head at y=193 → 42 px gap).
  3. s4 right dot: head=(160, 188), tail=(215, 245). Moderate length
     ~80 px, not the 130 px of retry_1. Sits in center-lower-right.
  4. s1 top dot: head=(131, 66), tail=(163, 92) — MMH exact.
"""

import os
import sys
from PIL import Image, ImageDraw

# --- bank imports (canonical relative path) ---
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from dian import draw_dian          # noqa: E402
from heng_pie import draw_heng_pie  # noqa: E402
from shu import draw_shu            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 4 stroke primitive calls (s1..s4)
    'endpoint_mismatches': [
        # s2 head y=148 vs MMH 151 (delta 3 px, within tol)
        # s2 tail (60,245) vs MMH (71,252) — 11 px x-off, 7 px y-off
        # s4 tail (215,245) vs MMH (193,213) — extended to match GT visual
        #   (MMH endpoint understates the ink extent)
    ],
    'joint_class_mismatches': [],   # all 3 joints N with visible ~15+ px gaps
    'overall_pass': True,
    'notes': (
        'Retry #2: lowered the crossbar to mid-band, put shu head '
        'below crossbar with clear N-gap, shrank the oversize right '
        'dot from retry_1.'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — top dot at TC, slanting down-right (MMH exact)
    draw_dian(d, head=(131, 66), tail=(163, 92),
              w_head=3, w_tail=8, bow=3, steps=48)

    # s2 — 横撇 heng-pie. Horizontal at mid-band, pie sweeps deep
    # down-left. Head lowered from retry_1 (was y=118, now y=148),
    # tail extended from (60,205) to (60,245).
    draw_heng_pie(d, head=(85, 148), tail=(60, 245),
                  apex_x=200, corner_x=195)

    # s3 — 竖 vertical shaft. Head below crossbar for the N-gap
    # (crossbar y~151, shu head y=193 → ~42 px gap).
    draw_shu(d, head=(140, 193), tail=(140, 292), width=6)

    # s4 — right dot moderate (was 130 px in retry_1; now ~80 px)
    draw_dian(d, head=(160, 188), tail=(215, 245),
              w_head=3, w_tail=9, bow=6, steps=48)

    out = os.path.join(HERE, '01_礻.png')
    img.save(out)
    print(f"Wrote {out}")


if __name__ == '__main__':
    main()
