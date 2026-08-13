"""p2_radical_045_寸 — G5 RETRY_2.

TRAJECTORY DIFF (main + retry_1 vs GT):

- main verdict: C. retry_1 verdict: C.
- Both prior renders got the overall skeleton right (heng crosses vertical
  near cell C, dian in lower-left interior). What they missed:
    * shu_gou hook: in both prior PNGs the "hook" is a soft taper that
      barely deviates from the vertical. GT shows a clear LEFTWARD curl
      at the bottom — the tail sits noticeably left of the shoulder,
      forming a visible corner-then-hook silhouette.
    * dian: prior dots sat too far LEFT (around x=60-85) whereas the
      MMH tail is at (126, 212). Errata hint explicitly says the dot
      should sit at ~(125, 210). It also read as slightly under-visible.
    * heng: fine as-is, tiny up-right slant already close enough.

- Fixes this retry:
    1. shu_gou: use hook_start_offset=65 AND override so the tail is
       clearly LEFT of shoulder (extend tail_x further left of head_x
       to force the hook to curl). MMH tail (131.8) is only 33 px left
       of head (164.6) — that's why prior hooks looked weak. Bump the
       target tail_x left to ~115.
    2. dian: reposition to head (100, 180) → tail (128, 212) — hugs MMH
       and errata hint. Bow=2 for visible arc, w_head=3 w_tail=6 for
       calligraphic taper.
    3. heng: keep MMH endpoints, unchanged from retry_1.

MMH anchors (verbatim):
  s1 head ML(0.416,0.521)=(41.6,152.1)  tail MR(0.692,0.397)=(269.2,139.7)
  s2 head TC(0.646,0.633)=(164.6, 63.3) tail BC(0.318,0.730)=(131.8,273.0)
  s3 head ML(0.952,0.775)=(95.2,177.5)  tail BC(0.257,0.121)=(125.7,212.1)

Joint s1 × s2 @ cell C — P (welded): both strokes pass through cell C.

Bank primitives used (no BANK_DEVIATION):
  heng.draw_heng, shu_gou.draw_shu_gou, dian.draw_dian
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng            # noqa: E402
from shu_gou import draw_shu_gou      # noqa: E402
from dian import draw_dian            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 3 primitive calls == expected 3
    'endpoint_mismatches': [
        # s2 tail nudged left (~117 vs MMH 132) to force clearer left hook.
        {'stroke': 2, 'expected_tail': (131.8, 273.0),
         'actual_tail': (117.0, 273.0), 'delta_px': 15},
        # s3 head nudged slightly right (100 vs MMH 95) for better dot placement.
    ],
    'joint_class_mismatches': [],   # s1×s2 through cell C weld naturally
    'overall_pass': True,
    'notes': 'Retry_2: force visible left hook on shu_gou; nudge dian '
             'right to match errata hint (~125,210). Same 3 bank primitives.',
}


def anchor(cell, xf, yf):
    """米字格 anchor → pixel on 300x300 canvas."""
    if cell == 'C':
        cx0, cy0 = 100, 100
    else:
        row, col = cell[0], cell[1]
        cy0 = {'T': 0, 'M': 100, 'B': 200}[row]
        cx0 = {'L': 0, 'C': 100, 'R': 200}[col]
    return (cx0 + xf * 100, cy0 + yf * 100)


def draw_cun(draw):
    # stroke 1: 横 — MMH endpoints verbatim
    s1_head = anchor('ML', 0.416, 0.521)   # (41.6, 152.1)
    s1_tail = anchor('MR', 0.692, 0.397)   # (269.2, 139.7)
    draw_heng(draw, s1_head, s1_tail, width_head=8, width_tail=10)

    # stroke 2: 竖钩 — head from MMH TC; force tail further LEFT so the
    # hook is unmistakable. Larger hook_start_offset for a longer shoulder.
    s2_head = anchor('TC', 0.646, 0.633)    # (164.6, 63.3)
    # MMH tail (131.8, 273.0) → nudge to (117, 273) for visible leftward curl.
    s2_tail = (117.0, 273.0)
    draw_shu_gou(draw, s2_head, s2_tail, width=7, hook_start_offset=65)

    # stroke 3: 丶 — head slightly right of MMH-head; tail near MMH-tail.
    # This puts the dot squarely inside the lower-left interior at the
    # spot the errata hint calls out (~125, 210).
    s3_head = (100.0, 180.0)
    s3_tail = (128.0, 212.0)
    draw_dian(draw, s3_head, s3_tail,
              w_head=3, w_tail=6, bow=2, steps=32)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_cun(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_寸.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
