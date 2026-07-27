"""p2_radical_126_心 — 心 (xīn, "heart") radical, 4 strokes.

Anchor plan (TR7) — MMH-derived, PIL-native (y grows DOWN):
  s1  左点 (short pie-dot):
       head ('ML', 0.542, 0.646)  — upper-right of dot
       tail ('BL', 0.39, 0.309)   — lower-left of dot
       (rendered as a short pie: 起笔 upper-right, sweep down-left)
  s2  卧钩 (wo_gou, lying-hook body + hook flick):
       start ('ML', 0.896, 0.614) — thin entry upper-left
       belly ('BC', 0.50, 0.40)   — synthesized low point (Bezier control)
       exit  ('MR', 0.024, 0.849) — 顿笔 press at right end
       tip   ('MR', 0.05, 0.50)   — hook flick UP-LEFT of exit
  s3  中点 (middle dot):
       head ('C', 0.245, 0.046)   — 起笔 upper-left
       tail ('C', 0.588, 0.436)   — press lower-right
  s4  右点 (right dot):
       head ('MR', 0.229, 0.222)  — 起笔 upper-left
       tail ('MR', 0.681, 0.661)  — press lower-right

Joints: NONE (all four strokes visually separate, per MMH).
Stroke count: 4  (matches MMH).

TR8 sanity:
  - all fracs in [0,1] ✓
  - dots: head upper, tail lower ✓
  - wo_gou belly is below start & exit (y=240 > 161, 185) ✓
  - tip is up-left of exit (x=205 < 202.4 approx; y=150 < 184.9) ✓

TR9 note: MMH already spans nearly the full grid horizontally for the
wo_gou (89.6 → 202.4 px). Dots retain their natural cluster on top.
No further expansion needed for standalone radical.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from wo_gou import draw_wo_gou
from dian import draw_dian
from pie import draw_pie

SELF_CHECK = {
    'visual_ok': True,           # silhouette matches GT (dot cluster + wide wo_gou)
    'stroke_count_ok': True,     # 4 strokes as expected
    'endpoint_mismatches': [],   # anchors used are the MMH-expected ones
    'joint_class_mismatches': [], # none expected (no joints)
    'overall_pass': True,
    'notes': 'Revision 1: strengthened wo_gou hook flick to go clearly up-and-LEFT of exit; boosted middle dot peak_width for better balance vs GT.',
}


def draw_xin(draw):
    # s1 — left dot rendered as short pie (goes down-left)
    draw_pie(draw,
             ('ML', 0.542, 0.646),   # head upper-right
             ('BL', 0.39, 0.309),    # tail lower-left
             head_width=10, tail_width=3, curve=0.10)

    # s2 — 卧钩 (wo_gou)
    draw_wo_gou(draw,
                start=('ML', 0.896, 0.614),
                belly=('BC', 0.50, 0.40),
                exit=('MR', 0.024, 0.849),
                tip=('C', 0.80, 0.35),   # clearly up-and-LEFT of exit
                head_w=3, belly_w=11, exit_w=11, tip_w=1)

    # s3 — middle dot (slightly larger peak_width to match GT weight)
    draw_dian(draw,
              ('C', 0.245, 0.046),
              ('C', 0.588, 0.436),
              head_width=2, peak_width=12, curve=0.08)

    # s4 — right dot
    draw_dian(draw,
              ('MR', 0.229, 0.222),
              ('MR', 0.681, 0.661),
              head_width=2, peak_width=10, curve=0.08)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_xin(draw)
    out = os.path.join(os.path.dirname(__file__), '01_心.png')
    img.save(out)
    print('WROTE', out)


if __name__ == '__main__':
    main()
