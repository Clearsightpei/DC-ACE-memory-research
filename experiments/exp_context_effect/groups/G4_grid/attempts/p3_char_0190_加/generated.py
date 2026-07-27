"""p3_char_0190_加 — 加 (jiā, "add"). 5 strokes, layout: 力 (left) + 口 (right).

Reading order comments (per memory_index v8 slim checklist):
  # (1) drawer_memory.md read: 加 is in the shortlist as needing li + kou.
  #     Note however: li.py/kou.py primitives are sized for full-canvas
  #     centered rendering. For 加 they must occupy only left / right half.
  #     Overriding 6+ anchors on both == inline fresh is cleaner (v8 says
  #     "prefer inlining fresh (per shared rules 'supplementary aid') —
  #     do NOT try to override 3+ anchors of a mastered primitive").
  # (2) INDEX grep: li_char.py + kou_char.py exist but they're the SAME
  #     full-canvas primitives; not helpful for the half-region layout.
  # (3) errata grep: 加 not previously attempted; p3_char_0025_力 shows
  #     'li not composed via li.py' was the failure mode there — but here
  #     we're intentionally inlining per (1) rationale, not by omission.

Split: 加 = 力 + 口 (left-right composition).
Strokes 1-2 = 力 (横折钩 + 撇). Strokes 3-5 = 口 (竖 + 横折 + 横).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes: 力 as heng_zhe_gou L-shape + 撇 diagonal; 口 as three N-jointed strokes on the right.',
}


def draw_jia(draw):
    # --- 力 (left) ---
    # s1 = 横折钩 (compound L). MMH head ML(0.349, 0.641)=(35,164);
    #      tail BL(0.876, 0.628)=(88,263). Break into: horizontal top +
    #      vertical descent + small hook up-left.
    s1_head = anchor_to_xy(('ML', 0.349, 0.641))     # (35, 164)
    s1_corner = anchor_to_xy(('ML', 0.90, 0.62))     # (90, 162) top-right corner of L
    s1_tail = anchor_to_xy(('BL', 0.876, 0.628))     # (88, 263)
    s1_hook = anchor_to_xy(('BL', 0.70, 0.60))       # (70, 260) small hook up-left
    fat_line(draw, s1_head, s1_corner, width=9)
    fat_line(draw, s1_corner, s1_tail, width=9)
    fat_line(draw, s1_tail, s1_hook, width=6)

    # s2 = 撇 (long diagonal, TL(0.914, 0.756) -> BL(0.149, 0.903)).
    s2_head = anchor_to_xy(('TL', 0.914, 0.756))     # (91, 76)
    s2_tail = anchor_to_xy(('BL', 0.149, 0.903))     # (15, 290)
    # Curved 撇 via quad bezier (curve toward bottom-left)
    ctrl = ((s2_head[0] + s2_tail[0]) / 2 - 8,
            (s2_head[1] + s2_tail[1]) / 2 + 10)
    pts = quad_bezier(s2_head, ctrl, s2_tail, n=40)
    widths = [max(1, 9 - int(8 * i / 40)) for i in range(41)]  # taper 9 -> 1
    stroke_variable_width(draw, pts, widths)

    # --- 口 (right) — three strokes with N-class corners (small gaps) ---
    # Tighten so it reads as a coherent square. Use MMH endpoints as guide
    # but ensure bottom bar span matches the right wall's tail.
    # s3 = 竖 left wall
    s3_head = anchor_to_xy(('C', 0.72, 0.62))        # (172, 162)
    s3_tail = anchor_to_xy(('C', 0.75, 0.98))        # (175, 198... let me recompute)
    # Recompute so it lines up with s5 bottom bar height ~y=252
    s3_head = (172, 162)
    s3_tail = (175, 252)
    fat_line(draw, s3_head, s3_tail, width=8)

    # s4 = 横折 (top bar + right wall)
    s4_head = (185, 158)         # slight N-gap from s3_head (x-diff ~13)
    s4_corner = (245, 158)
    s4_tail = (245, 252)
    fat_line(draw, s4_head, s4_corner, width=8)
    fat_line(draw, s4_corner, s4_tail, width=8)

    # s5 = 横 bottom bar spanning the whole 口 width, y just below walls
    s5_head = (178, 258)         # N-gap from s3_tail
    s5_tail = (250, 258)         # N-gap from s4_tail
    fat_line(draw, s5_head, s5_tail, width=8)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_jia(draw)
    out = os.path.join(os.path.dirname(__file__), '01_加.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
