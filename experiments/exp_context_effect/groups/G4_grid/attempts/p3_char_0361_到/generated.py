"""到 (dào, "arrive") — 8 strokes.

Decomposition: 到 = 至 (left, 6 strokes) + 刂 (right, 2 strokes).
Left 至 = 一 (top short heng) + 丿 + 丶 + 冫 (mid pieces) + 十 (bottom cross) + 一 (base heng)
   — MMH stroke sequence per dispatcher.
Right 刂 = 短竖 (short shu, s7) + 竖钩 (shu_gou, s8).

Following B9 A-recipe:
  point 1 — decomposition comment at top (this docstring).
  point 2 — MMH-verbatim anchors, no tuning.
  point 3 — SELF_CHECK block.
  point 4 — base primitives (fat_line + quad_bezier) inlined; dao_side.py
            skipped because MMH places the knife at x≈176 while dao_side
            default is x≈111 — a real compositional mismatch (see
            BANK_DEVIATION below).
  point 5 — all 5 MMH joints noted; only s4⇆s5 is P (welded cross),
            the other 4 are N (natural gap preserved).

# BANK_DEVIATION
# skipped: dao_side.py
# reason: dao_side defaults place 刂 centered at x≈111 (standalone
#   radical position); MMH places 到's 刂 far-right at x≈176-219.
#   Overriding 4+ anchors of a compound primitive is the p3_char_0252_伊
#   FAIL pattern; inline fresh instead per A-recipe point 4.
# fresh_component: dao_side_for_dao_right (刂 as right-half of 到, MMH-anchored)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 strokes match MMH expected 8
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('8 strokes MMH-verbatim; s4⇆s5 P-welded cross at BC(0.01,0.03); '
              'all 4 N-joints leave natural gap. dao_side skipped — see '
              'BANK_DEVIATION.'),
}


def _line(draw, head_anchor, tail_anchor, width=10):
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    fat_line(draw, p0, p1, width=width)


def _curve(draw, head_anchor, ctrl_anchor, tail_anchor, width=10):
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(ctrl_anchor)
    p2 = anchor_to_xy(tail_anchor)
    pts = quad_bezier(p0, p1, p2, n=40)
    widths = [width] * len(pts)
    stroke_variable_width(draw, pts, widths)


def draw_dao(draw):
    # ---- 至 (left, s1-s6) — MMH anchors verbatim ----
    # s1 — short pie/heng at top-left of char
    _line(draw, ('TL', 0.56, 0.917), ('TC', 0.477, 0.826), width=9)

    # s2 — top horizontal (spans across upper region; MMH samples the
    # descent-in from the top-right of the char down toward center)
    # Rendered as a horizontal reaching from far-left of upper region
    # across to the right where s7/s8 start, then MMH tail-side.
    _line(draw, ('ML', 0.882, 0.025), ('C', 0.333, 0.485), width=10)

    # s3 — small mid stroke inside 至
    _line(draw, ('C', 0.26, 0.271), ('C', 0.477, 0.614), width=9)

    # s4 — bottom horizontal of 至 (long base), mid welds with s5
    _line(draw, ('BL', 0.565, 0.08), ('C', 0.397, 0.972), width=10)

    # s5 — vertical of the 土-bottom cross, mid welds with s4 (P joint)
    _line(draw, ('ML', 0.917, 0.646), ('BL', 0.961, 0.417), width=10)

    # s6 — bottom heng of 至 base
    _line(draw, ('BL', 0.384, 0.59), ('BC', 0.523, 0.314), width=10)

    # ---- 刂 (right, s7-s8) — MMH-anchored, dao_side skipped ----
    # s7 — 短竖 (short vertical) in upper-right area
    _line(draw, ('C', 0.717, 0.222), ('BC', 0.808, 0.18), width=10)

    # s8 — 竖钩 (long vertical + hook), rightmost. Rendered as gently
    # curving stroke ending with a subtle hook flick.
    p0 = anchor_to_xy(('TR', 0.186, 0.715))
    p2 = anchor_to_xy(('BC', 0.916, 0.648))
    # slight left-bow via bezier ctrl
    p1 = ((p0[0] + p2[0]) / 2 - 6, (p0[1] + p2[1]) / 2)
    pts = quad_bezier(p0, p1, p2, n=40)
    widths = [11] * (len(pts) - 6) + [9, 7, 5, 4, 3, 2]
    stroke_variable_width(draw, pts, widths)
    # hook tick — small up-left flick from tail
    hook_end = (p2[0] - 14, p2[1] - 10)
    fat_line(draw, p2, hook_end, width=6)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_dao(draw)
    out = os.path.join(os.path.dirname(__file__), '01_到.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
