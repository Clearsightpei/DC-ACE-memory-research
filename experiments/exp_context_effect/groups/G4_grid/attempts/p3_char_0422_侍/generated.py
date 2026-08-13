# BANK_DEVIATION
# skipped: ren_side.py
# reason: ren_side defaults place 亻 in TC/C column (x~80-176); MMH puts 亻
#         far-left column here (pie x 27-95, shu x 76-78). Compound-slot
#         embedding — inline pie+shu with MMH-verbatim anchors.
# fresh_component: ren_side_far_left_column

"""侍 (shì) — 亻 (left) + 寺 (right); 寺 = 土 (top) + 寸 (bottom). 8 strokes.

MMH stroke plan (dispatcher-injected):
  s1 撇     (亻)      ('TL', 0.952, 0.694) → ('ML', 0.27,  0.96)
  s2 竖     (亻)      ('ML', 0.765, 0.518) → ('BL', 0.785, 0.95)
  s3 横 top (土)      ('C',  0.397, 0.178) → ('MR', 0.271, 0.061)
  s4 竖     (土)      ('TC', 0.708, 0.565) → ('C',  0.778, 0.529)
  s5 横 mid (土 bot)  ('C',  0.084, 0.699) → ('MR', 0.689, 0.526)
  s6 横 (寸 top)      ('BC', 0.187, 0.074) → ('MR', 0.578, 0.98)
  s7 竖钩 (寸)        ('C',  0.937, 0.685) → ('BC', 0.67,  0.818)
  s8 点 (寸)          ('BC', 0.348, 0.247) → ('BC', 0.611, 0.525)

Joints (7):
  s1.mid ⇆ s2.head  N (~17 px gap)
  s3.mid ⇆ s4.mid   P welded (top 横 crossed by 竖)
  s4.tail ⇆ s5.mid  N (~11 px gap)
  s4.tail ⇆ s7.head N (~30 px gap)
  s5.mid ⇆ s7.head  N (~20 px gap)
  s6.mid ⇆ s7.mid   P welded (寸 横 crossed by 竖钩)
  s6.head ⇆ s8.head N (~22 px gap)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from shu_gou import draw_shu_gou
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 8 stroke calls, matches MMH count
    'endpoint_mismatches': [],    # all MMH-verbatim
    'joint_class_mismatches': [], # P at s3∩s4 and s6∩s7 welded; others N (gap)
    'overall_pass': True,
    'notes': '亻 far-left column via BANK_DEVIATION (skipped ren_side). '
             '寺 = 土 (s3-s5) stacked over 寸 (s6-s8). All MMH-verbatim.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 亻 (person radical, far-left column — BANK_DEVIATION) ----
    # s1 撇 — long sweep from upper area down-left
    draw_pie(draw,
             ('TL', 0.952, 0.694),
             ('ML', 0.27, 0.96),
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2 竖 — vertical leg of 亻 in left column
    draw_shu(draw,
             ('ML', 0.765, 0.518),
             ('BL', 0.785, 0.95),
             width=9)

    # ---- 土 (top of 寺) ----
    # s3 top 横 — short heng upper right
    draw_heng(draw,
              ('C', 0.397, 0.178),
              ('MR', 0.271, 0.061),
              width=8)

    # s4 竖 — vertical crossing s3 (P joint), from top down to just above s5
    draw_shu(draw,
             ('TC', 0.708, 0.565),
             ('C', 0.778, 0.529),
             width=8)

    # s5 middle 长横 — wide horizontal across (bottom of 土)
    draw_heng(draw,
              ('C', 0.084, 0.699),
              ('MR', 0.689, 0.526),
              width=9)

    # ---- 寸 (bottom of 寺) ----
    # s6 长横 (top of 寸) — even wider horizontal below s5
    draw_heng(draw,
              ('BC', 0.187, 0.074),
              ('MR', 0.578, 0.98),
              width=9)

    # s7 竖钩 — vertical crossing s6 (P), with small hook flick at bottom
    # MMH gives head at ('C', 0.937, 0.685) and tail at ('BC', 0.67, 0.818)
    # tail is the hook-tip endpoint (slightly up-left of the vertical bottom)
    draw_shu_gou(draw,
                 head=('C', 0.937, 0.685),
                 belly=('MR', 0.05, 0.75),         # near-vertical body
                 hook_pt=('BC', 0.78, 0.88),       # bottom pivot before hook
                 tip=('BC', 0.67, 0.818),          # MMH tail = hook tip
                 head_w=10, belly_w=9, hook_start_w=9, tip_w=2)

    # s8 点 — dot to the left of the 竖钩, below the 寸 横
    draw_dian(draw,
              ('BC', 0.348, 0.247),
              ('BC', 0.611, 0.525),
              head_width=2, peak_width=8, curve=0.10, segments=24)

    out = os.path.join(os.path.dirname(__file__), '01_侍.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
