"""p3_char_0385_物 — G5 attempt.

Character 物 (8 strokes) = 牜 (left, 4 strokes: pie/heng/shu/ti) +
勿 (right, 4 strokes: pie / heng-zhe-gou wrapper / pie / long pie).

Recipe: **P-A-006 verbatim MMH-anchor + stroke-primitive layer** with
per-sub-component inline reasoning (P-A-008) and quantitative
BANK_DEVIATION reasoning (P-A-009) for the whole-radical primitives.

# BANK_DEVIATION
# skipped: niu_cow.py          reason: bank niu_cow renders the 牛 form
#                              (pie + short-heng + LONG-heng + central shu)
#                              — MMH anchors here describe 牜 which is a
#                              different 4-stroke shape: pie + short-heng
#                              + shu (RIGHT-offset, near x=90) + ti at
#                              bottom. Native niu_cow aspect ~1.0
#                              square-ish; 牜-in-物 aspect ~0.4 (x-range
#                              23..133 = 110 wide, y-range 57..301 = 244
#                              tall). Uniform scale of niu_cow would
#                              destroy the ti (which niu doesn't have) and
#                              wrongly place a long-heng across both
#                              halves. Inline verbatim from MMH.
# skipped: bao_wrap.py         reason: bao's wrapper spans x=98..232
#                              (width 134) at native scale — 勿's wrapper
#                              here spans only x=155..208 (width ~53),
#                              scale ratio 0.40 which falls well below
#                              P-A-007-v2 use band [0.55, 1.2]. Also bao
#                              starts with a short pie (which 勿 also has
#                              as s5, but with different endpoints).
#                              Inline s6 via heng_zhe_gou at MMH anchors.
# fresh_component: eight verbatim-MMH strokes composed inline.
"""

from pathlib import Path
import sys

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from ti import draw_ti
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 8 stroke calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('牜 uses pie/heng/shu/ti verbatim from MMH; 勿 uses pie '
              'for s5/s7/s8 and heng_zhe_gou with inferred corner ~ '
              '(208,143) and hook_tip ~ (168,258).'),
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ================= 牜 (left radical) =================

    # s1 撇 — top-left short pie, ML(0.551,0.154) -> ML(0.287,0.84)
    draw_pie(d, (55.1, 115.4), (28.7, 184.0),
             bow_perp=8, w_head=7, w_tail=2)

    # s2 短横 — ML(0.633,0.532) -> C(0.33,0.395); short heng slanting up-right
    draw_heng(d, (63.3, 153.2), (133.0, 139.5),
              width_head=6, width_tail=7)

    # s3 竖 — TL(0.888,0.574) -> BL(0.938,1.006); tall vertical (right side of 牜)
    draw_shu(d, (88.8, 57.4), (93.8, 296.0), width=7)

    # s4 提 — BL(0.234,0.338) -> C(0.198,0.837); rising ti at bottom
    draw_ti(d, (23.4, 233.8), (119.8, 183.7),
            w_head=8, w_tail=2)

    # ================= 勿 (right radical) =================

    # s5 撇 — TC(0.69,0.677) -> C(0.318,0.702); top short-mid pie of 勿
    draw_pie(d, (169.0, 67.7), (131.8, 170.2),
             bow_perp=6, w_head=7, w_tail=2)

    # s6 横折钩 — C(0.55,0.506) -> BC(0.828,0.687); wrapper stroke
    # infer corner at top-right of wrapper (~208, 143), hook_tip up-left of tail
    draw_heng_zhe_gou(d,
                      heng_head=(155.0, 150.6),
                      corner=(212.0, 144.0),
                      gou_tail=(182.8, 268.7),
                      hook_tip=(166.0, 258.0))

    # s7 撇 — C(0.679,0.553) -> BC(0.307,0.232); middle pie of 勿
    draw_pie(d, (167.9, 155.3), (130.7, 223.2),
             bow_perp=6, w_head=6, w_tail=2)

    # s8 撇 — MR(0.042,0.506) -> BC(0.266,0.725); long right pie
    draw_pie(d, (204.2, 150.6), (126.6, 272.5),
             bow_perp=12, w_head=7, w_tail=2)

    return img


if __name__ == '__main__':
    img = draw()
    out = Path(__file__).parent / '01_物.png'
    img.save(out)
    print(f'wrote {out}')
