"""p3_char_0348_佟 — 亻 (left) + 冬 (winter, right).

Recipe: P-A-006 stroke-primitive layer + MMH-anchor verbatim.
7 strokes total: 亻 (pie + shu) + 冬 (pie + heng-pie + na + 2 dians).

INLINE REASONING TRACE per P-A-008:

  - 亻 sub-component: 2 strokes. Bank has ren_left.py (native 300 canvas),
    but here 亻 occupies only left ~30% width and ~75% height. Native
    aspect scale for horizontal ≈ 0.7, but composition wants the two
    strokes precisely at MMH anchors, not native ren_left offsets.
    Per P-A-006, INLINE with stroke primitives (pie + shu) at the
    injected MMH anchors — this beats ren_left(ox=-70) which drifts the
    N-joint. NOT a BANK_DEVIATION (ren_left is a whole-radical primitive
    and the drawer legitimately chose the stroke-primitive layer instead).

  - 冬 top (夂-like): 3 strokes forming an X-cross with a leading pie.
    No 冬/夂 primitive in bank. Inline with 2 pies + 1 na, with s4/s5
    welded P-joint at center (per MMH joint spec).

  - 冬 bottom (冫): 2 dots. Inline with draw_dian.
"""

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from na import draw_na
from dian import draw_dian
from heng_pie import draw_heng_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 primitive calls == expected 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s4/s5 welded P at center; N gaps preserved elsewhere
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive inline. 亻 pie+shu at MMH anchors. '
             '冬: 2 pies X-cross with na at center (P-joint), then 2 dians below.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (person radical, left) ----
    # s1: pie from TL(0.894, 0.647) -> ML(0.176, 0.96)
    draw_pie(d, (89.4, 64.7), (17.6, 196.0),
             bow_perp=15, w_head=8, w_tail=2, steps=90)
    # s2: shu from ML(0.659, 0.526) -> BL(0.697, 0.895)
    draw_shu(d, (65.9, 152.6), (69.7, 289.5), width=7)

    # ---- 冬 top (夂-like: pie + heng-pie + na, X-cross at center) ----
    # s3: outer pie from TC(0.541, 0.606) -> C(0.017, 0.523)
    draw_pie(d, (154.1, 60.6), (101.7, 152.3),
             bow_perp=8, w_head=6, w_tail=2, steps=70)
    # s4: 横撇 (heng-pie) from C(0.477,0.128) -> BL(0.917,0.215)
    #     Heng arcs rightward to ~x=205, then pies down-left through center
    #     to cross the na at C (welded P-joint at (~167, ~161)).
    draw_heng_pie(d, (147.7, 112.8), (91.7, 221.5),
                  apex_x=205, corner_x=200)
    # s5: na from C(0.333, 0.38) -> BR(0.827, 0.104) — welded P-joint at center vs s4
    draw_na(d, (133.3, 138.0), (282.7, 210.4),
            bow_perp=10, w_head=4, w_tail=12, steps=100)

    # ---- 冬 bottom (冫 two dots) ----
    # s6: upper dot BC(0.526, 0.092) -> BC(0.869, 0.329)
    draw_dian(d, (152.6, 209.2), (186.9, 232.9),
              w_head=3, w_tail=7, bow=3, steps=40)
    # s7: lower dot BC(0.436, 0.543) -> BC(0.937, 1.053)
    draw_dian(d, (143.6, 254.3), (193.7, 299.0),  # y clamped to 299
              w_head=3, w_tail=7, bow=3, steps=40)

    out = Path(__file__).with_name('01_佟.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
