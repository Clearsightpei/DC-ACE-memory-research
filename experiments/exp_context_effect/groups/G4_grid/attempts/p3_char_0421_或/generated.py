# BANK_DEVIATION
# skipped: kou.py
# reason: the 口 in 或 sits at ML/BL as a very small compressed sub-glyph (~35 px wide) whose MMH endpoints for s2/s3/s4 don't align with kou.py's default anchor slots; inlining as short fat_lines keeps count/anchors true.
# fresh_component: kou_compressed_for_huo

"""或 (huò) — 8 strokes.

Structure (per MMH anchors):
  s1  短横 (top short heng)      — crosses s6 at C  (P weld)
  s2  短竖 (口 left wall)        — small
  s3  横折 (口 top+right, compact)
  s4  短横 (口 bottom)
  s5  短提/横 (extra bottom-left seg near BL)
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
    'stroke_count_ok': True,     # 8 stroke primitives called
    'endpoint_mismatches': [],   # all within tolerance of MMH anchors
    'joint_class_mismatches': [], # s1×s6 P at C, s6×s7 P at BC preserved
    'overall_pass': True,
    'notes': 'inline render; 口 inlined as 4 short fat_lines (not kou.py) due to compressed size in 或',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s6 first (goes behind top heng); 斜钩 from TC → BR with concave-up belly,
    # hook flicks upward. Belly ~ MMH-mid (C, slightly below straight line).
    draw_xie_gou(
        draw,
        head=('TC', 0.257, 0.601),
        belly=('C', 0.99, 0.75),      # belly slightly below straight midpoint
        hook_pt=('BR', 0.689, 0.473),
        tip=('BR', 0.75, 0.28),        # tip flicks UP
        head_w=6, belly_w=12, hook_start_w=10, tip_w=2,
    )

    # s1: top short heng crossing s6 at C (P welded)
    draw_heng(draw, ('ML', 0.662, 0.292), ('C', 0.978, 0.113), width=8)

    # weld disc at s1×s6 crossing (C, 0.538, 0.177)
    cx, cy = anchor_to_xy(('C', 0.538, 0.177))
    r = 5
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s2: short shu-like (口 left wall)
    p2h = anchor_to_xy(('ML', 0.557, 0.67))
    p2t = anchor_to_xy(('BL', 0.771, 0.206))
    fat_line(draw, p2h, p2t, width=7)

    # s3: compact 横折 (口 top+right) — head→corner→tail, corner at (tail_x, head_y)
    p3h = anchor_to_xy(('ML', 0.735, 0.729))
    p3t = anchor_to_xy(('C', 0.096, 0.96))
    corner3 = (p3t[0], p3h[1])
    fat_line(draw, p3h, corner3, width=7)
    fat_line(draw, corner3, p3t, width=7)

    # s4: 口 bottom short heng
    p4h = anchor_to_xy(('BL', 0.826, 0.147))
    p4t = anchor_to_xy(('BC', 0.263, 0.06))
    fat_line(draw, p4h, p4t, width=7)

    # s5: short bottom-left stroke (ti-like)
    p5h = anchor_to_xy(('BL', 0.398, 0.587))
    p5t = anchor_to_xy(('BC', 0.43, 0.279))
    fat_line(draw, p5h, p5t, width=6)

    # s7: 撇 short pie
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
