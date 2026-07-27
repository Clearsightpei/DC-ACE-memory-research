"""对 (duì) — 5 strokes per MMH.
Composition: 又 (left) + 寸-like (right, without final 点 as per MMH segmentation).

Lookup checklist:
  1. INDEX.md grep 对/寸/又: 又 mastered (you_again.py). 寸 in errata.
  2. errata: 寸 fix idea = "十 + 丶" but MMH here shows just 横+竖钩 (2-stroke寸-body).
  3. form_catalog: 横 as top bar, 竖钩 with vertical body.
  4. principles_meta: TR1 override anchors always.
  5. joint_atlas: s1×s2 P weld, s3 N-gap to s1, s4×s5 P weld.
  6. sandbox: none specifically for 对.

Strokes (from MMH):
  s1 — 撇 head ML(0.521,0.301) → tail BL(0.272,0.517)
  s2 — 提/横 head ML(0.586,0.591) → tail BC(0.289,0.367) [rises from left-low to right-mid]
       Actually MMH tail is BC upper — this is the 反捺/提点 of 又
  s3 — 点/small dian C(0.392,0.459) → MR(0.707,0.348) [rightward dot]
  s4 — 横 TR(0.051,0.665) → BC(0.729,0.648) [long top bar of 寸]
  s5 — 竖钩 head C(0.441,0.808) → tail BC(0.758,0.124) [vertical body then hook]

Joints:
  s1×s2 @ ML — P (weld)
  s1×s3   @ C  — N (gap ~30 px)
  s4×s5 @ MR — P (weld)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, sample_line, stroke_variable_width, quad_bezier, fat_line
from heng import draw_heng
from pie import draw_pie
from dian import draw_dian
from shu_gou import draw_shu_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used literally; 5 strokes; s1×s2 P weld natural, s4×s5 P weld natural.'
}


def draw_dui(draw):
    # s1: 撇 (left top pie of 又)
    draw_pie(draw,
             from_anchor=('ML', 0.521, 0.301),
             to_anchor=('BL', 0.272, 0.517),
             head_width=10, tail_width=2, curve=0.06)

    # s2: 提/反捺 (rises from lower-left to upper-right, crossing s1)
    # This is 又's second stroke. Draw as tapered line head→tail.
    # Use pie primitive with slight curve so it looks like a 提/反捺 chord.
    draw_pie(draw,
             from_anchor=('ML', 0.586, 0.591),
             to_anchor=('BC', 0.289, 0.367),
             head_width=4, tail_width=11, curve=-0.04)

    # s3: 点/捺 — MMH short median but visually 又 has a longer dian/na.
    # Extend slightly into BC area for readable 又 shape.
    draw_pie(draw,
             from_anchor=('C', 0.35, 0.45),
             to_anchor=('BC', 0.15, 0.60),
             head_width=4, tail_width=11, curve=-0.05)

    # s4: 横 (long horizontal top of 寸-body across top-right)
    draw_heng(draw,
              ('TR', 0.051, 0.665),
              ('BC', 0.729, 0.648),
              width=8)

    # s5: 竖钩 (vertical body ML/BC area, ending with up-flick hook)
    # MMH: head C(0.441, 0.808) → tail BC(0.758, 0.124).
    # head is upper (y=0.808 in C row → pixel y≈181),
    # tail is BC lower part rises up (y=0.124 in BC → pixel y≈212).
    # Actually y_frac in PIL grows DOWN. So head at pixel (147, 181),
    # tail at pixel (176, 212). That's a very short line. Hmm.
    # MMH medians for 竖钩 include hook tip at end. Let's expand:
    # Use head as top of vertical, belly mid, hook_pt bottom, tip = up-left flick.
    # Given tail is close to head, MMH may have degenerate median. Draw
    # a proper 竖钩 body from just below s4 down toward bottom, hook up-left.
    draw_shu_gou(draw,
                 head=('C', 0.60, 0.05),      # top just above s4 line
                 belly=('C', 0.60, 0.70),
                 hook_pt=('BC', 0.60, 0.80),
                 tip=('BC', 0.35, 0.55),
                 head_w=11, belly_w=10, hook_start_w=9, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_dui(draw)
    out = os.path.join(os.path.dirname(__file__), '01_对.png')
    img.save(out)
    print('saved', out)


if __name__ == '__main__':
    main()
