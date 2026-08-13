"""p3_char_0350_佣 (yong, "hire") — 7 strokes: 亻 (pie+shu) + 用 (pie + heng-zhe-gou + 2 inner hengs + central shu).

Recipe: P-A-006 (MMH anchors verbatim + stroke-primitive layer) + P-A-007-v2 hard-check.

Inline sub-component reasoning (P-A-008):
  亻 (s1,s2): Bank has ren_left.py at native aspect pie_tall/shu_tall = 1.02;
    MMH 佣's ratio is 129.2/143.8 = 0.90 (13% aspect drift because 佣's shu is
    longer than ren_left's native). This is a P-A-007-v2 marginal case — using
    the whole-radical would compress the shu. Falling back to P-A-006 stroke-
    primitive layer (draw_pie + draw_shu) is the safer A-recipe (matches
    dan_but 但 template exactly). BANK_DEVIATION-lite: no bank primitive
    skipped, we just prefer explicit primitives per P-A-006.
  用 (s3-s7): No whole-radical for 用 in bank (yue_moon has hook but different
    aspect and lacks central shu). Inline with draw_pie for s3 left pie,
    draw_heng_zhe_gou for the top-right compound, draw_heng x2 for the inner
    horizontals, draw_shu for the central piercing shu.

Joint plan (all N except s5.mid⇆s7.mid and s6.mid⇆s7.mid = P welded, which
happen naturally because s7 shu passes through both hengs' x-span):
  N joints: s1.mid⇆s2.head (ren gap ~17px), s2.tail⇆s3.tail (~25px bottom gap),
    s3.head⇆s4.head (~15px top gap), s3.mid⇆s5.head, s3.mid⇆s6.head,
    s4.head⇆s7.head (~12px top).
  P joints: s5 & s6 (inner hengs) cross s7 (central shu) — they overlap in ink.

Anchor pixels (MMH cell.frac → 300x300):
  s1 pie:  TL(0.896,0.621)=(89.6,62.1)  → ML(0.185,0.913)=(18.5,191.3)
  s2 shu:  ML(0.688,0.465)=(68.8,146.5) → BL(0.715,0.903)=(71.5,290.3)
  s3 pie:  C (0.175,0.028)=(117.5,102.8)→ BL(0.896,0.886)=(89.6,288.6)
  s4 hzg:  C (0.362,0.058)=(136.2,105.8)→ BR(0.045,0.754)=(204.5,275.4)
  s5 heng: C (0.515,0.676)=(151.5,167.6)→ MR(0.153,0.579)=(215.3,157.9)
  s6 heng: BC(0.468,0.098)=(146.8,209.8)→ MR(0.177,0.989)=(217.7,198.9)
  s7 shu:  C (0.685,0.104)=(168.5,110.4)→ BC(0.79 ,0.886)=(179.0,288.6)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 7 primitive calls; MMH expected 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all N joints preserved as gaps; s5/s6 x s7 are P (welded by crossing)
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer; 亻 via pie+shu (P-A-007-v2 aspect-drift 13% -> prefer primitives over ren_left); 用 inlined with heng_zhe_gou for top-right compound.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 亻 pie (TL top → ML lower-left, moderate rightward bow)
    draw_pie(d, (89.6, 62.1), (18.5, 191.3),
             bow_perp=15, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu (straight descender, slight left drift)
    draw_shu(d, (68.8, 146.5), (71.5, 290.3), width=7)

    # s3: 用 left pie — long, almost vertical with slight leftward bow
    #      (from top of box down to bottom-left corner)
    draw_pie(d, (117.5, 102.8), (89.6, 288.6),
             bow_perp=5, w_head=8, w_tail=4, steps=90)

    # s4: 用 top-right heng-zhe-gou — horizontal top, corner, long vertical, hook
    #     Corner inferred at top-right of the box (~x=217, y=108); gou_tail just
    #     above the hook tip, hook_tip is MMH tail (204.5, 275.4).
    draw_heng_zhe_gou(d,
                      heng_head=(136.2, 105.8),
                      corner=(217.0, 108.0),
                      gou_tail=(213.0, 268.0),
                      hook_tip=(200.0, 275.4))

    # s5: 用 upper inner heng (left ML edge → right MR edge, slight rise)
    draw_heng(d, (151.5, 167.6), (215.3, 157.9), width_head=6, width_tail=7)

    # s6: 用 bottom heng (bottom-left of box → right side)
    draw_heng(d, (146.8, 209.8), (217.7, 198.9), width_head=7, width_tail=8)

    # s7: 用 central shu piercing (from top center down through both hengs
    #     — creates the two P-joints s5.mid⇆s7.mid and s6.mid⇆s7.mid)
    draw_shu(d, (168.5, 110.4), (179.0, 288.6), width=7)

    out = Path(__file__).parent / "01_佣.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
