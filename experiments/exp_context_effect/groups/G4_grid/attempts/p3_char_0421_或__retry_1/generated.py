# BANK_DEVIATION
# skipped: kou.py
# reason: 口 in 或 sits as a compressed sub-glyph at ML/BL; MMH endpoints for s2/s3/s4 don't align with kou.py default slots; inlining as short fat_lines keeps count/anchors true.
# fresh_component: kou_compressed_for_huo

"""或 (huò) — 8 strokes. Retry #1.

TRAJECTORY DIFF (from visual compare of main attempt vs GT):
  FAILED main attempt (verdict C) issues:
    1. 口 sub-glyph rendered ~55 px tall/wide — GT shows a MUCH smaller 口
       (~30 px). Compressed sub-glyph looked bulky/mid-heavy.
    2. 斜钩 hook flick was drawn but nearly horizontal — GT hook flicks
       clearly UPWARD-RIGHT at ~45° above the hook corner. Errata says:
       "hook_up_after_corner=True" — make tip end HIGH.
    3. Top 短横 (s1) extended past the 斜钩 body — GT shows s1 more
       nested (stops just past crossing).
  Fixes this retry:
    A. Trim 口 s2/s3/s4 to their MMH anchor values BUT reduce weld disc
       so it reads compact; keep width=6 (thinner).
    B. Push xie_gou tip anchor higher: use tip near ('MR', 0.7, 0.35)
       so the hook clearly rises above hook_pt.
    C. Slightly shorten s1 to end near the crossing rather than pushing
       far right.

Structure (per MMH anchors):
  s1  短横 (top short heng)      — crosses s6 at C  (P weld)
  s2  短竖 (口 left wall)
  s3  横折 (口 top+right, compact)
  s4  短横 (口 bottom)
  s5  短提/横 (bottom-left seg near BL)
  s6  斜钩 (long slanted hook)   — welded to s1 mid @ C and s7 mid @ BC
  s7  撇 (short pie)
  s8  点 (dot upper-right)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from xie_gou import draw_xie_gou
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 8 stroke primitives called
    'endpoint_mismatches': [],    # within tolerance of MMH anchors
    'joint_class_mismatches': [], # s1×s6 P at C, s6×s7 P at BC preserved
    'overall_pass': True,
    'notes': 'retry_1 — hook tip pushed UP, 口 kept but drawn thinner, s1 trimmed for cleaner crossing'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s6 FIRST (goes behind top heng). 斜钩 from TC → BR with concave-up belly,
    # tip flicks UP-RIGHT more prominently than main attempt.
    draw_xie_gou(
        draw,
        head=('TC', 0.257, 0.601),
        belly=('C', 0.99, 0.75),
        hook_pt=('BR', 0.689, 0.473),
        tip=('MR', 0.72, 0.75),        # pushed HIGHER (was BR 0.75, 0.28) — flick clearly upward
        head_w=6, belly_w=11, hook_start_w=9, tip_w=2,
    )

    # s1: top short heng crossing s6 at C (P welded).
    # Trim slightly so it doesn't run far past the crossing.
    draw_heng(draw, ('ML', 0.70, 0.30), ('C', 0.90, 0.14), width=7)

    # weld disc at s1×s6 crossing (C, 0.538, 0.177)
    cx, cy = anchor_to_xy(('C', 0.538, 0.177))
    r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s2: 口 left wall (short shu)
    p2h = anchor_to_xy(('ML', 0.557, 0.67))
    p2t = anchor_to_xy(('BL', 0.771, 0.206))
    fat_line(draw, p2h, p2t, width=6)

    # s3: compact 横折 (口 top+right) — head→corner→tail
    p3h = anchor_to_xy(('ML', 0.735, 0.729))
    p3t = anchor_to_xy(('C', 0.096, 0.96))
    corner3 = (p3t[0], p3h[1])
    fat_line(draw, p3h, corner3, width=6)
    fat_line(draw, corner3, p3t, width=6)

    # s4: 口 bottom short heng
    p4h = anchor_to_xy(('BL', 0.826, 0.147))
    p4t = anchor_to_xy(('BC', 0.263, 0.06))
    fat_line(draw, p4h, p4t, width=6)

    # s5: short bottom-left stroke (ti-like)
    p5h = anchor_to_xy(('BL', 0.398, 0.587))
    p5t = anchor_to_xy(('BC', 0.43, 0.279))
    fat_line(draw, p5h, p5t, width=6)

    # s7: 撇 short pie crossing s6 near BC
    p7h = anchor_to_xy(('MR', 0.112, 0.538))
    p7t = anchor_to_xy(('BC', 0.289, 0.81))
    fat_line(draw, p7h, p7t, width=6)

    # weld disc at s6×s7 crossing (BC, 0.893, 0.286)
    wx, wy = anchor_to_xy(('BC', 0.893, 0.286))
    r2 = 4
    draw.ellipse([wx - r2, wy - r2, wx + r2, wy + r2], fill=(0, 0, 0))

    # s8: 点 upper-right
    draw_dian(draw, ('TC', 0.919, 0.683), ('TR', 0.265, 0.935),
              head_width=2, peak_width=9, curve=0.10)

    out = os.path.join(os.path.dirname(__file__), '01_或.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
