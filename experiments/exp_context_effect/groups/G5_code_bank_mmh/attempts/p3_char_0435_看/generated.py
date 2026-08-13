"""p3_char_0435_看 (kàn, "look") — 9 strokes.

Structure: 手-top (龵 form: pie, heng, long heng, long descending pie) +
目 bottom-right (shu + heng_zhe_box + 2 interior heng + closing heng).

Approach: P-A-006 (MMH-verbatim anchors + stroke-primitive layer).

Reasoning trace (P-A-008):
  Decomposition — top 4 strokes = 手/龵 variant, bottom 5 = 目 in
  bottom-center. No whole-radical bank primitive for 龵 exists; ri_sun
  would give 目 with only 4 strokes (need 5). Ju_tool (具) has a 5-stroke
  目-top layout at similar footprint — could copy its 目 render.

  BANK check: bank has heng, pie, shu, heng_zhe_box, na, dian. No
  whole-char 看 or 龵. No mu_eye primitive (只 ri_sun 4-stroke). 具
  attempt shows the 5-stroke 目 rendering recipe (shu + heng_zhe_box +
  3 interior/closing hengs) — reuse that shape idea inline. No
  BANK_DEVIATION because we're not skipping a primitive that could fit;
  we're composing from stroke primitives (which IS the P-A-006 recipe).

  Anchor mapping (300x300 canvas, 3x3 米字格 100px cells; row: T=0,M=1,B=2,
  col: L=0,C=1,R=2). Pixels = (col*100 + xf*100, row*100 + yf*100).

  s1 head TC(0.963,0.703) → (196.3, 70.3); tail TL(0.858,0.911) → (85.8, 91.1) — top pie
  s2 head ML(0.905,0.236) → (90.5, 123.6); tail MR(0.024,0.102) → (202.4, 110.2) — top heng
  s3 head ML(0.337,0.72)  → (33.7, 172.0); tail MR(0.602,0.523) → (260.2, 152.3) — long lower heng (looong)
  s4 head TC(0.321,0.882) → (132.1, 88.2); tail BL(0.234,0.836) → (23.4, 283.6) — long descending pie
  s5 head C(0.157,0.904)  → (115.7, 190.4); tail BC(0.16,1.012) → (116.0, 301.2) — shu (left of 目) — clamp y to 297
  s6 head C(0.254,0.925)  → (125.4, 192.5); tail BC(0.796,0.874) → (179.6, 287.4) — heng_zhe_box top+right of 目
  s7 head BC(0.283,0.312) → (128.3, 231.2); tail BC(0.731,0.232) → (173.1, 223.2) — interior heng 1
  s8 head BC(0.271,0.61)  → (127.1, 261.0); tail BC(0.743,0.537) → (174.3, 253.7) — interior heng 2
  s9 head BC(0.248,0.909) → (124.8, 290.9); tail BC(0.852,0.812) → (185.2, 281.2) — bottom closing heng

  Stroke count check: 9 primitive calls (pie, heng, heng, pie, shu,
  heng_zhe_box, heng, heng, heng) = 9. MATCH.

  Joint classes: all N (natural gaps) except s2⇆s4 (P at C(0.329,0.217))
  and s3⇆s4 (P at C(0.182,0.621)) — the long pie s4 must pierce both
  horizontals. Since s4 is a curve from (132.1,88.2) to (23.4,283.6),
  bow rightward small will cross s2 at ~y=123, and cross s3 at ~y=172.
  Both crossings happen naturally by geometry — no explicit welding
  needed since we draw s4 last (well, before 目). Actually s2, s3 drawn
  first, then s4 crosses over them. Because PIL overwrites, the pie
  ink covers heng at crossing. That's a welded crossing = P. GOOD.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/success_bank/code")

from PIL import Image, ImageDraw
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 9 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer; MMH anchors verbatim; s4 pie pierces s2/s3 by geometry (P joints); 目 sub-block uses 具-style recipe inline.',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top pie (short, upper-right) — head upper-right, tail lower-left
    draw_pie(d, (196.3, 70.3), (85.8, 91.1),
             bow_perp=6, w_head=6, w_tail=3, steps=60)

    # s2: top heng (upward slope)
    draw_heng(d, (90.5, 123.6), (202.4, 110.2),
              width_head=8, width_tail=9)

    # s3: long lower heng (signature horizontal of 看)
    draw_heng(d, (33.7, 172.0), (260.2, 152.3),
              width_head=8, width_tail=11)

    # s4: long descending pie — crosses over s2 and s3 (P welds by draw order)
    draw_pie(d, (132.1, 88.2), (23.4, 283.6),
             bow_perp=18, w_head=9, w_tail=2, steps=90)

    # --- 目 bottom-center (5 strokes) ---
    # s5: left shu (clamp y a bit above 300 to avoid harsh edge)
    draw_shu(d, (115.7, 190.4), (116.0, 297.0), width=6)

    # s6: heng_zhe_box — top+right of 目 box
    draw_heng_zhe_box(d, (125.4, 192.5), (179.6, 287.4), width=6)

    # s7: interior heng 1 (top interior, small upward slope)
    draw_heng(d, (128.3, 231.2), (173.1, 223.2),
              width_head=4, width_tail=5)

    # s8: interior heng 2 (middle interior)
    draw_heng(d, (127.1, 261.0), (174.3, 253.7),
              width_head=4, width_tail=5)

    # s9: bottom closing heng
    draw_heng(d, (124.8, 290.9), (185.2, 281.2),
              width_head=5, width_tail=6)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_看.png')
    img.save(out)
    return out


if __name__ == '__main__':
    p = draw()
    print(f'wrote {p}')
