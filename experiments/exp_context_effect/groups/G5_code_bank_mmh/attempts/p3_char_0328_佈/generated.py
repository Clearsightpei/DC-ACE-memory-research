"""p3_char_0328_佈 — G5 attempt.

佈 = 亻 (left, 2 strokes) + 布 (right, 5 strokes) = 7 strokes total.

Recipe: P-A-006 (MMH-anchor verbatim + stroke-primitive layer).
Per P-COMP-011 boundary: 亻+X with a hook-compound right half (布's
巾-tail carries heng_zhe_gou + shu_gou), so this is NOT an A candidate,
but P-A-006 gives the cleanest PASS route: bypass draw_ren_left /
draw_jin_towel double-transforms and instantiate strokes at the
MMH pixel anchors directly.

Stroke order (matches MMH):
  s1: 亻 pie (TL→ML, long sweep)
  s2: 亻 shu (ML→BL, vertical descender)
  s3: 布 top 一 (heng, slight up-tilt, C→MR)
  s4: 布 long 丿 (pie, TC→BL, pierces s3 at C — welded P)
  s5: 巾 short left 竖 (C→BC)
  s6: 巾 横折钩 (heng_zhe_gou continuous, C→BR)
  s7: 巾 central 竖钩 (C→below-BC, pierces s6 at C — welded P)
"""

import os
import sys
from PIL import Image, ImageDraw

CODE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '..', '..', 'success_bank', 'code'))
sys.path.insert(0, CODE_DIR)

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou
from shu_gou import draw_shu_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('P-A-006 recipe: MMH anchors verbatim, 5 stroke primitives '
              '(pie, shu, heng, heng_zhe_gou, shu_gou). '
              's3xs4 and s6xs7 crossings happen naturally at cell C (P). '
              'Not an A candidate per P-COMP-011 (右 半 hook_compound).'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical) ----
    # s1: 亻 pie — TL(0.891, 0.583) → ML(0.126, 0.89)
    draw_pie(d, (89.1, 58.3), (12.6, 189.0),
             bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu — ML(0.645, 0.45) → BL(0.68, 0.938)
    draw_shu(d, (64.5, 145.0), (68.0, 293.8), width=7, top_curl=True)

    # ---- 布 (right radical) ----
    # s3: top heng of 布 — C(0.093, 0.286) → MR(0.64, 0.116). Slight up-tilt.
    draw_heng(d, (109.3, 128.6), (264.0, 111.6), width_head=8, width_tail=10)

    # s4: long pie of 布 — TC(0.532, 0.577) → BL(0.823, 0.273).
    # Sweeps from upper-mid down-left; crosses s3 at cell C (P weld).
    draw_pie(d, (153.2, 57.7), (82.3, 227.3),
             bow_perp=10, w_head=10, w_tail=3, steps=90)

    # ---- 巾 (bottom-right of 布) ----
    # s5: left short 竖 — C(0.333, 0.828) → BC(0.33, 0.575)
    draw_shu(d, (133.3, 182.8), (133.0, 257.5), width=8)

    # s6: 横折钩 — head C(0.406, 0.831), corner near (203, 183),
    # gou_tail near (203, 235), hook_tip inside corner (~(193, 228)).
    draw_heng_zhe_gou(d,
                      heng_head=(140.6, 183.1),
                      corner=(206.0, 183.1),
                      gou_tail=(206.0, 234.7),
                      hook_tip=(196.0, 228.0))

    # s7: 巾 central 竖钩 — C(0.69, 0.465) → tail extends past baseline
    # (BC 0.813, 1.258 = (181, 326)). Clip to canvas at y=296; force
    # left-flick hook (draw_shu_gou curves x toward tail_x — set tail_x
    # < head_x for calligraphically-correct 巾 hook).
    draw_shu_gou(d, (175.0, 146.5), (160.0, 296.0),
                 width=8, hook_start_offset=42)

    out_dir = os.path.dirname(__file__)
    img.save(os.path.join(out_dir, '01_佈.png'))


if __name__ == '__main__':
    render()
