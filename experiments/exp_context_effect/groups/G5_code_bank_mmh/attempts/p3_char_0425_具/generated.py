"""p3_char_0425_具 (jù, "tool") — 8 strokes.

Structure: 目 on top (5 strokes: left shu + heng_zhe_box + 3 interior/closing
hengs) + wide horizontal heng (s6) + 八-bottom (pie s7 + na/dot s8).

Approach: P-A-006 (MMH-verbatim + stroke-primitive layer). Bank does have
ri_sun (日, 4 strokes) but 具's top is 目 = 5 strokes (one extra interior
heng), so ri_sun would undershoot stroke count. Also 具's 八-bottom is
short/compressed at the base (not the tall ba.py native rendering).

BANK_DEVIATION reasoning:
  P-A-009 quantitative: 具-top box aspect vs ri_sun bank:
    - ri_sun box footprint ≈ x∈[83..201]=118w × y∈[100..289]=189h → 0.62 aspect
    - 具 top-box target ≈ x∈[96..182]=86w × y∈[78..220]=142h → 0.60 aspect
    Close, but stroke count differs (4 vs 5). Inline for exact count match.
  P-A-009 quantitative: 具-八 vs ba.py bank:
    - ba.py native span: pie(97,162)→(26,264), na(132,96)→(287,257) — 168h span
    - 具-八 target: pie(130,254)→(65,302), na(176,248)→(231,300) — 54h span
    - Scale ratio ≈ 54/168 = 0.32 — extreme compression, ba.py is a tall
      radical form; here the 八 sits as small feet under the base heng.
    Inline both bottom strokes with fresh dian/pie/na primitives.
"""
# BANK_DEVIATION
# skipped: ri_sun.py (would give 4 strokes, need 5 for 目-top)
# skipped: ba.py (native tall 八, target compressed 八-feet at 0.32 scale)
# reason: exact stroke-count match required; 八 compression too extreme
# fresh_component: inline_mu_top_5stroke, inline_ba_feet_short

from PIL import Image, ImageDraw
import pathlib, sys

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 turtle-primitive calls, matches MMH count
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 7 joints are class N (neighbor). MMH anchors used verbatim; no welding, natural pixel gaps preserved by stroke widths.',
}


def draw_ju(d):
    # --- 目 top (5 strokes) ---
    # s1: left shu of 目 box
    draw_shu(d, (95.8, 77.9), (103.1, 220.6), width=7)
    # s2: heng_zhe_box (top + right vertical of 目)
    draw_heng_zhe_box(d, (113.4, 81.2), (181.9, 211.2), width=7)
    # s3: top interior heng
    draw_heng(d, (118.1, 124.2), (162.9, 115.7), width_head=5, width_tail=6)
    # s4: middle interior heng
    draw_heng(d, (118.9, 157.6), (163.8, 150.9), width_head=5, width_tail=6)
    # s5: bottom heng closing 目 (still inside box footprint)
    draw_heng(d, (118.1, 192.8), (165.8, 185.7), width_head=5, width_tail=6)

    # --- wide base heng (s6) ---
    draw_heng(d, (34.0, 232.3), (276.6, 223.8), width_head=8, width_tail=10)

    # --- 八-feet (s7 pie + s8 na) — compressed at bottom ---
    # s7: left pie (short, moderate bow)
    draw_pie(d, (130.1, 253.7), (64.7, 301.8),
             bow_perp=6, w_head=7, w_tail=3)
    # s8: right na (short, tapered)
    draw_na(d, (175.8, 248.4), (230.9, 300.3),
            bow_perp=6, w_head=3, w_tail=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_ju(d)
    out = pathlib.Path(__file__).parent / '01_具.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
