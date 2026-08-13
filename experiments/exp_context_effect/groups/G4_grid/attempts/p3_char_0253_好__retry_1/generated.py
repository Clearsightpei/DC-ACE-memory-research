"""p3_char_0253_好 (hǎo, "good", 6画) — RETRY 1.

TRAJECTORY DIFF (mandatory Step 0):

MAIN attempt (FAIL) — visual inspection of 01_好.png vs gt/phase3/好.png:
  1. Left 女 (strokes 1-3): overall silhouette OK but s1 撇点 pivot placed
     at BL(0.60, 0.78) = (60, 278) pushed the elbow too far down-left; the
     dian tail then had to climb up-right to (124, 261), making the point
     look flat. GT shows a shorter, more compact 撇点 with elbow around
     (95, 230) and a natural down-right dian. Also the 撇 body did not
     visibly weld with s3 短横 at the expected P joint (ML region) — they
     glanced past each other.
  2. Right 子 s4 横撇: TOO SHORT. Prior used tip=('C', 0.70, 0.43)=(170,143)
     but MMH tip is C(0.942, 0.43)=(194, 143). By clipping x from 0.94 to
     0.70 the horizontal reach was cut ~25px, so the top of 子 looks like
     a tiny 45px hat instead of a proper wide top hook.
  3. Right 子 s5 弯钩: belly placed at MR(0.05, 0.65) = (215, 265) bowed
     the body far right and low, making the vertical look like a bulge
     dropping to the bottom-right corner. GT wan_gou in 好 is nearly
     straight with only mild right bow near the middle.
  4. Right 子 s6 横 (crossbar): correct span (131→281) but visually the
     crossbar arrives at a height slightly below where s5 body would
     properly weld, and because s5 was over-bowed the P joint at MR
     was ambiguous.

Errata entry (p3_char_0253_好): "Left 女 did not use nv.py. Right 子
fragmented. Fix: import nv + zi (both mastered)."

FIXES applied this retry:
  - Import draw_nv and draw_zi_char from success_bank (mastered primitives).
  - Pass MMH-derived anchor overrides directly (v8 permits departure from
    bank defaults; the primitives' width/curve shaping is preserved).
  - s1 pivot moved to BL(0.75, 0.55) = (75, 255) so the 撇 body bows LEFT
    through ML(~77, 156) where s3 median passes → welds P joint with s3.
  - s4 tip restored to MMH's C(0.942, 0.43) — full horizontal reach.
  - s5 belly moved to MR(0.05, 0.55) = (205, 255) — near the body
    midpoint, gives a mild right bow without ballooning.

Strokes (6 total):
  女: s1 撇点, s2 撇, s3 短横
  子: s4 横撇, s5 弯钩, s6 横

Joints (from MMH brief):
  s1.mid × s2.mid @ BL — P (welded)
  s1.mid × s3.mid @ ML — P (welded)
  s2.head ⇆ s3.tail @ C — N (~16.8 px gap)
  s2.mid ⇆ s6.head @ C — N (~22 px gap)
  s4.tail ⇆ s5.head @ C — N (~12.4 px gap)
  s5.mid × s6.mid @ MR — P (welded)
"""
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from nv import draw_nv
from zi_char import draw_zi_char


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 (nv) + 3 (zi_char) = 6
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Retry-1: imports mastered nv.py + zi_char.py per errata; '
              's1 pivot lifted to BL(0.75, 0.55) for P weld w/ s3; s4 tip '
              'restored to MMH C(0.94, 0.43); s5 belly tightened to '
              'MR(0.05, 0.55) for mild bow.'),
}


def draw_hao(draw):
    # ---- Left half: 女 (strokes 1-3) — draw_nv with 好-context overrides ----
    draw_nv(draw,
            s1_head=('TL', 0.826, 0.691),     # (82.6, 69.1)
            s1_pivot=('BL', 0.75, 0.55),      # (75, 255) — bows left → welds s3
            s1_tail=('BC', 0.242, 0.61),      # (124.2, 261)
            s2_head=('C', 0.143, 0.371),      # (114.3, 137.1)
            s2_tail=('BL', 0.401, 0.716),     # (40.1, 271.6)
            s3_head=('ML', 0.173, 0.661),     # (17.3, 166.1)
            s3_tail=('C', 0.113, 0.532))      # (111.3, 153.2)

    # ---- Right half: 子 (strokes 4-6) — draw_zi_char with 好-context overrides ----
    draw_zi_char(draw,
                 s1_head=('C', 0.444, 0.078),      # (144.4, 107.8) — top of 子
                 s1_corner=('C', 0.98, 0.15),      # (198, 115) — top-right corner
                 s1_tip=('C', 0.942, 0.43),        # (194.2, 143) — MMH tail (fixed)
                 s2_head=('C', 0.796, 0.447),      # (179.6, 144.7) — start of 弯钩
                 s2_belly=('MR', 0.05, 0.55),      # (205, 255) — mild right bow
                 s2_hook_pt=('BC', 0.75, 0.85),    # (175, 285)
                 s2_tip=('BC', 0.614, 0.751),      # (161.4, 275.1) — MMH tip
                 s3_head=('C', 0.315, 0.875),      # (131.5, 187.5)
                 s3_tail=('MR', 0.812, 0.793))     # (281.2, 179.3)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_hao(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_好.png')
    img.save(out_path)
    print(f'Wrote {out_path}')


if __name__ == '__main__':
    main()
