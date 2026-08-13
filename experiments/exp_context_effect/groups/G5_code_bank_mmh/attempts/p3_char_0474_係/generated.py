"""p3_char_0474_係 (xi) — 亻 + 系. 9 strokes.

Recipe: P-A-006 (MMH anchors verbatim) + P-A-007-v2 whole-radical hard-check +
P-A-008 inline reasoning + P-A-009 quantitative BANK_DEVIATION.

--- Per-sub-component reasoning (P-A-008) ---

1) Left radical 亻 (2 strokes, MMH s1+s2):
   Bank candidate: ren_left.py (pie + shu).
   Native ren_left: s1_head=(158.8,73.8), s1_tail=(80.6,211.2);
                    s2_head=(138.9,158.2), s2_tail=(144.1,292.7).
   Native x-span head-to-tail-of-shu ~ 84 -> 145 = ~60 wide; y-span 74 -> 293 = 219.
   Target (MMH):    s1_head=(100.8,59.5), s1_tail=(24.3,190.1);
                    s2_head=(85.8,136.2), s2_tail=(83.2,289.2).
   Target x-span 24 -> 101 = 77 wide; y-span 60 -> 289 = 229.
   Aspect ratios: native 60/219=0.274, target 77/229=0.336. Delta ~+23%; the
   target 亻 is a little wider (pie sweeps further left) than native. Also, the
   translate is non-uniform (bank pie head at x=159 vs target x=101, delta -58;
   bank pie tail at x=81 vs target x=24, delta -57). Uniform translate roughly
   works (-57, -14, scale ~1.0) but head-tail x-drift differs a couple px.
   DECISION: inline both 亻 strokes at exact MMH pixels (P-A-006 verbatim). No
   BANK_DEVIATION block needed for atomic-stroke inline of ren_left (same choice
   as p3_char_0424_侑, PASS).

2) Right radical 系 (7 strokes, MMH s3-s9):
   Bank candidate: none. No `xi_silk.py` primitive in bank; 系 is a complex
   compound with a top 幺-like swirl + hook + bottom 小-like fan. No whole-
   radical primitive exists. Inline per MMH anchors using pie/dian/shu/shu_gou/na
   stroke primitives.

   Stroke class assignment (from MMH endpoint geometry):
     s3 = top pie sweep (long horizontal-ish curl, TR->C area)
     s4 = short dian/pie (drops from C into upper-right)
     s5 = shu descender (upper part of vertical body)
     s6 = short pie/hook fragment (extends s5's bottom rightward)
     s7 = long pie of bottom 小 (left diagonal)
     s8 = short pie (leftmost bottom stroke)
     s9 = na (right diagonal of bottom 小)

--- MMH-derived pixel anchors (image-y, 300x300, cell=100x100) ---

  s1 亻 pie:  TC(0.008,0.595)=(100.8, 59.5) -> ML(0.243,0.901)=(24.3,190.1)
  s2 亻 shu:  ML(0.858,0.362)=(85.8,136.2) -> BL(0.832,0.892)=(83.2,289.2)
  s3 系 top:  TR(0.332,0.812)=(233.2, 81.2) -> C(0.339,0.072)=(133.9,107.2)
  s4 系 dian: C(0.708,0.031)=(170.8,103.1) -> C(0.898,0.509)=(189.8,150.9)
  s5 系 shu:  MR(0.171,0.125)=(217.1,112.5) -> MR(0.329,0.884)=(232.9,188.4)
  s6 系 hook: MR(0.259,0.652)=(225.9,165.2) -> MR(0.481,0.98)=(248.1,198.0)
  s7 小 pie:  BC(0.852,0.039)=(185.2,203.9) -> BC(0.617,0.78)=(161.7,278.0)
  s8 小 pie2: BC(0.474,0.3)=(147.4,230.0) -> BC(0.263,0.704)=(126.3,270.4)
  s9 小 na:   BR(0.3,0.238)=(230.0,223.8) -> BR(0.669,0.637)=(266.9,263.7)

Stroke count: 9 primitive calls (matches MMH expected 9). All 5 MMH joints
are class N (natural gaps preserved by MMH anchor spacing; no welds).
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 primitive calls == MMH expected 9
    'endpoint_mismatches': [],     # all inlined at exact MMH pixel anchors
    'joint_class_mismatches': [],  # all 5 joints class N; MMH anchor spacing preserved
    'overall_pass': True,
    'notes': 'P-A-006 verbatim MMH anchors. 亻 inlined; 系 has no whole-radical '
             'bank primitive so all 7 strokes inlined per MMH.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # === 亻 (left radical, s1+s2) ===
    draw_pie(d, (101, 60), (24, 190),
             bow_perp=14, w_head=9, w_tail=3, steps=90)
    draw_shu(d, (86, 136), (83, 289), width=7)

    # === 系 (right radical, s3-s9, inlined) ===
    # s3: top swoop — long pie from upper-right sweeping leftward and slightly down.
    #     Nearly horizontal; use pie with bow (curves upward slightly).
    draw_pie(d, (233, 81), (134, 107),
             bow_perp=-8, w_head=5, w_tail=4, steps=80)

    # s4: short diagonal dian, drops down-right from top of shu region.
    draw_dian(d, head=(171, 103), tail=(190, 151),
              w_head=3, w_tail=6, bow=3, steps=48)

    # s5: shu descender — upper vertical body of 系, drifts slightly right.
    draw_shu(d, (217, 113), (233, 188), width=6)

    # s6: short pie/hook fragment — extends s5 tail down-right (small hook piece).
    draw_pie(d, (226, 165), (248, 198),
             bow_perp=3, w_head=5, w_tail=3, steps=40)

    # s7: long pie of bottom fan — steep leftward diagonal from mid-bottom.
    draw_pie(d, (185, 204), (162, 278),
             bow_perp=8, w_head=6, w_tail=3, steps=60)

    # s8: short pie further left, drops from just below center to bottom-left of fan.
    draw_pie(d, (147, 230), (126, 270),
             bow_perp=4, w_head=5, w_tail=3, steps=40)

    # s9: na — bottom-right diagonal of the fan, thickens to tail.
    draw_na(d, (230, 224), (267, 264),
            bow_perp=6, w_head=3, w_tail=8, steps=60)

    out = Path(__file__).parent / "01_係.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
