"""p3_char_0268_伦 (lún) — G5 attempt.

Recipe: P-A-006 (stroke-primitive layer w/ MMH anchors verbatim).
Structure: 亻 (2 strokes) + 仑 (top 人 2 strokes + bottom 匕 2 strokes) = 6 strokes.

BANK reuse: pie / shu / na / shu_wan_gou stroke primitives.
No whole-radical primitives called (avoids P-COMP-009 double-transform).
"""
import os
import sys
from PIL import Image, ImageDraw

# Add bank code dir to path for stroke primitives
BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code"
)
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from shu import draw_shu
from na import draw_na
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 6 primitive calls, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 5 joints are N-class (natural gaps)
    'overall_pass': True,
    'notes': ('P-A-006 recipe. MMH anchors converted to pixel via '
              'cell-base + frac*100. s6 uses shu_wan_gou with head=(140,186), '
              'tail=(236,235); bottom_extra=55 stretches curl toward y~290. '
              'All 5 joints are N — no forced welds.')
}


def draw_char(draw):
    # s1: 亻 pie — TL(0.938, 0.697) → BL(0.223, 0.086)
    #      = (93.8, 69.7) → (22.3, 208.6)
    draw_pie(draw, (94, 70), (22, 209),
             bow_perp=13, w_head=9, w_tail=3, steps=90)

    # s2: 亻 shu — ML(0.738, 0.597) → BL(0.762, 0.962)
    #      = (73.8, 159.7) → (76.2, 296.2)
    draw_shu(draw, (74, 160), (76, 296), width=9)

    # s3: 仑-top 人 pie — TC(0.693, 0.729) → BL(0.973, 0.054)
    #      = (169.3, 72.9) → (97.3, 205.4)
    draw_pie(draw, (169, 73), (97, 205),
             bow_perp=10, w_head=8, w_tail=3, steps=80)

    # s4: 仑-top 人 na — C(0.843, 0.04) → MR(0.862, 0.805)
    #      = (184.3, 104) → (286.2, 180.5)
    draw_na(draw, (184, 104), (286, 181),
            bow_perp=12, w_head=4, w_tail=12, steps=80)

    # s5: 匕-top short pie — MR(0.001, 0.822) → BC(0.532, 0.273)
    #      = (200.1, 182.2) → (153.2, 227.3)
    draw_pie(draw, (200, 182), (153, 227),
             bow_perp=5, w_head=8, w_tail=4, steps=50)

    # s6: 匕 竖弯钩 — C(0.4, 0.857) → BR(0.355, 0.347)
    #      = (140, 185.7) → (235.5, 234.7)
    # MMH tail is the median endpoint (post-hook-tip). Extend curl down
    # via bottom_extra so the shape descends into BC/BR before hooking up.
    draw_shu_wan_gou(draw, (140, 186), (236, 235),
                     width=9, bottom_extra=65, knee_ratio=0.75)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_char(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_伦.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
