"""G5 attempt: p3_char_0244_仳 (pi, "be equal / mate").

Structure: 亻 (left, 2 strokes: 撇+竖) + 比 (right, 4 strokes: 提+竖弯钩+撇+竖弯钩).
Total = 6 strokes, matches MMH block.

Recipe = P-A-006 (MMH-anchor verbatim + stroke-primitive layer). We
explicitly refuse `draw_ren_left` / `draw_hua` whole-radical composition
because Phase-3 5-6-stroke L-R chars double-transform (per P-COMP-009);
inline stroke primitives at MMH-derived anchors are the A-recipe.

Per-stroke MMH anchors (from injected block, converted to canvas px on
300x300 米字格; cells: TL[0-100,0-100], TC[100-200,0-100], TR[200-300,0-100],
ML[0-100,100-200], C[100-200,100-200], MR[200-300,100-200], BL, BC, BR):
  s1 撇   : TL(85.5, 63.9)   -> BL(14.1, 202.7)     [亻 pie]
  s2 竖   : ML(66.5, 152.1)  -> BL(68.0, 295.0)     [亻 shu, joins s1.mid]
  s3 提   : C(124.5, 173.7)  -> C(166.7, 159.4)     [比 left 提]
  s4 竖弯钩: C(103.4, 125.1) -> BC(157.9, 219.7)    [比 left main curl]
  s5 撇   : MR(240.8, 123.9) -> C(192.8, 169.6)     [比 right pie]
  s6 竖弯钩: TC(172.0, 82.0) -> BR(272.8, 212.4)    [比 right main curl]

Joints (all class N — natural gap, no welding):
  J1: s1.mid(0.52) ⇆ s2.head @ ML — 亻 shu head touches pie mid
  J2: s3.head    ⇆ s4.mid(0.36) @ C — 比 left 提 head touches its shu
  J3: s3.tail    ⇆ s6.mid(0.28) @ C — inter-half contact
  J4: s5.tail    ⇆ s6.mid(0.32) @ C — 比 right pie tail touches its shu

Reference: p3_char_0136_比__retry_1 (PASS) — retry pattern reused with
right-shifted anchors because 亻 occupies the left ~1/3.
"""

import sys
import pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from ti import draw_ti
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitive calls: pie + shu + ti + swg + pie + swg
    'endpoint_mismatches': [], # anchors used verbatim from MMH block (int-rounded)
    'joint_class_mismatches': [], # all N; no weld, natural gap preserved
    'overall_pass': True,
    'notes': ('P-A-006 route: MMH-anchor verbatim + stroke-primitive layer. '
              '比 sub-structure reuses proven B7 retry-PASS pattern (retry_1 '
              'PASS): 提 with w_head=10, left 竖弯钩 bottom_extra=36, right 撇 '
              'with negative bow (-8) for calligraphic weight, right 竖弯钩 '
              'bottom_extra=42 to match left mass. 亻 rendered from raw pie+shu '
              'at MMH anchors — refuses draw_ren_left / draw_hua whole-radical '
              'per P-COMP-009 (double-transform hazard on 5-6-stroke L-R).'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left, 2 strokes) ----

    # s1: 撇 — TL(86,64) -> BL(14,203). Long slanting pie.
    draw_pie(d, head=(86, 64), tail=(14, 203),
             bow_perp=15, w_head=9, w_tail=3, steps=80)

    # s2: 竖 — ML(67,152) -> BL(68,295). Straight down. Joins s1.mid at ML.
    draw_shu(d, head=(67, 152), tail=(68, 295), width=7, top_curl=True)

    # ---- 比 (right, 4 strokes) — retry-PASS pattern, right-shifted ----

    # s3: 提 (left 匕's rising) — C(125,174) -> C(167,159).
    draw_ti(d, head=(125, 174), tail=(167, 159),
            w_head=10, w_tail=2, steps=50)

    # s4: 竖弯钩 (left main curl) — C(103,125) -> BC(158,220).
    # bottom_extra=36 (retry-PASS value) balances mass with s6.
    draw_shu_wan_gou(d, head=(103, 125), tail=(158, 220),
                     width=7, bottom_extra=36, knee_ratio=0.72)

    # s5: 撇 (right short pie) — MR(241,124) -> C(193,170).
    # NEGATIVE bow_perp per P-A-005 for calligraphic weight (retry-PASS).
    draw_pie(d, head=(241, 124), tail=(193, 170),
             bow_perp=-8, w_head=10, w_tail=3, steps=80)

    # s6: 竖弯钩 (right main curl) — TC(172,82) -> BR(273,212).
    # bottom_extra=42 (retry-PASS) — slightly under s4 but taller start.
    draw_shu_wan_gou(d, head=(172, 82), tail=(273, 212),
                     width=8, bottom_extra=42, knee_ratio=0.70)

    out = pathlib.Path(__file__).with_name('01_仳.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
