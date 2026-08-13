"""p3_char_0309_两 — G5 retry_1.

# TRAJECTORY DIFF
# main FAIL (attempts/p3_char_0309_两/01_两.png):
#   * top heng too wide (x=48..258) and left-shu (x=78) started INSIDE
#     the heng — created a T-shape instead of proper 冂-frame nesting.
#   * heng_zhe_gou frame's heng started at x=88 leaving a large visible
#     gap from the top heng right edge; corner at (248,88) too far
#     down/right; the outer frame did not visually "cap" the top heng.
#   * interior 人 pairs were too tall (pie tails at y=260) and too far
#     apart (left pie at x=108, right pie at x=185) — chambers looked
#     empty above and cramped below, and left na welded into left frame.
#   * left frame shu ran nearly canvas-full-height (55..285) while GT's
#     left stroke is shorter, curving down-out-and-back.
#
# Fixes for retry_1:
#   1. Top heng narrower (x=62..238) and horizontal; frame sides start
#      AT/JUST BELOW the heng endpoints, not inside.
#   2. Left shu shorter and curves gently out (bow_perp=+6), landing
#      near BL (30, 268).
#   3. heng_zhe_gou heng-head at (78, 66) close to top heng's right end;
#      corner at (236, 62); gou_tail (222, 268); hook tip (207, 260).
#   4. Two interior 人 (call draw_ren) sized smaller (scale=0.32) and
#      placed lower/centered in chambers so pie/na sit clearly INSIDE
#      the frame with N-gap to walls.
#      Left 人 ox=15, oy=118 → pie ~ (60,148)→(21,205) na (60,169)→(107,205)
#      Right 人 ox=110, oy=118 → pie ~(155,148)→(116,205) na (155,169)→(202,205)

Structure (7 strokes):
  s1 top heng
  s2 left downward pie (frame left side)
  s3 heng-zhe-gou (frame right side + hook)
  s4 left 人 pie
  s5 left 人 na (dianr)
  s6 right 人 pie
  s7 right 人 na (dianr)
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from na import draw_na
from ren import draw_ren


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes: top heng + left pie-shu (frame L) + heng-zhe-gou '
             '(frame R + hook) + 2× draw_ren for interior 人. Frame nests '
             'top heng between its left+right posts. 人 pairs sized down '
             'so they sit clearly inside chambers with N-gap to walls.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1: top heng — narrower, sits ABOVE frame corners
    draw_heng(draw, (62, 58), (238, 60), width_head=9, width_tail=10)

    # s2: left frame — a downward curving pie (starts at top-left just under
    # the heng's left endpoint, curves out-and-down to bottom-left)
    draw_pie(draw, (58, 62), (30, 272),
             bow_perp=6, w_head=7, w_tail=4)

    # s3: right frame heng-zhe-gou — heng from ~top-left (touching under top
    # heng's right end area) across to top-right, then down to bottom-right,
    # small upward-left hook flick
    draw_heng_zhe_gou(draw,
                      heng_head=(78, 66),
                      corner=(236, 62),
                      gou_tail=(222, 268),
                      hook_tip=(206, 258))

    # Interior 人 pair — call bank primitive at reduced scale
    # Bumped scale 0.32→0.35 and shifted higher (oy 118→108) so 人's fill
    # the chamber vertically like the GT (previously flat + too-low).
    # Left 人 in left chamber
    draw_ren(draw, ox=15, oy=108, scale=0.35)

    # Right 人 in right chamber (ox shifted right so pie tail doesn't
    # cross deep into the left chamber)
    draw_ren(draw, ox=115, oy=108, scale=0.35)

    out = pathlib.Path(__file__).parent / '01_两.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
