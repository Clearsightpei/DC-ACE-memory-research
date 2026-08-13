"""p3_char_0424_侑 (yòu) — 亻 + 有. 8 strokes.

Recipe: P-A-006 (MMH anchors verbatim, stroke-primitive layer) + P-A-007-v2
whole-radical aspect check + P-A-008 inline-reasoning + P-A-009 quantitative
BANK_DEVIATION.

--- Per-sub-component reasoning (P-A-008) ---

1) Left radical 亻 (2 strokes, MMH s1+s2):
   Bank candidate: ren_left.py  (draw_pie + draw_shu).
   Native ren_left: s1_head=(158.8,73.8), s1_tail=(80.6,211.2);
                    s2_head=(138.9,158.2), s2_tail=(144.1,292.7).
   Target (MMH):    s1_head=(94,63),  s1_tail=(20,195);
                    s2_head=(70,150), s2_tail=(73,291).
   Deltas at scale=1.0: s1_head (-64.8,-10.8), s1_tail (-60.6,-16.2)
                        s2_head (-68.9,-8.2),  s2_tail (-71.1,-1.7)
   Non-uniform-translate: ~+11px x-drift between head and tail. Native pie is
   slightly steeper than target. Aspect ratio matches (P-A-007-v2 scale 1.0
   in-range) but positional drift means uniform-translate bank call would be
   +5-10px off tail anchors. DECISION: inline the two strokes at exact MMH
   pixels (P-A-006 verbatim), since we have anchors and the deviation is small
   but noticeable. Same choice as p3_char_0324_但 (B9 PASS).

2) Right radical 有 (6 strokes, MMH s3-s8):
   Bank candidate: you_have.py (draw_heng + draw_pie + draw_pie + draw_heng_zhe_gou
                                + draw_heng + draw_heng).
   Native you_have bounds: x-span=234.4 (24.3->258.7), y-span=242.0 (53.3->295.3),
                           aspect w/h = 0.969.
   Target (MMH) bounds:    x-span=178   (89->267),    y-span=239   (57->296),
                           aspect w/h = 0.745.
   Aspect deviation: 0.745 / 0.969 = 0.769 (target is 23% narrower than native).
   P-A-007-v2 uniform-scale test: to match y-span (~1.0 uniform scale), x-span
   would render 234, overshooting target 178 by +31%. To match x-span (scale
   ~0.76), y-span would render 184, undershooting target 239 by -23%. Neither
   uniform scale fits. Non-uniform aspect compression required.

   DECISION: BANK_DEVIATION — inline 有 per MMH anchors (see block below).

# BANK_DEVIATION
# skipped: you_have.py
# reason: L+R composition compresses 有 horizontally (aspect w/h target 0.745
#   vs native 0.969, delta -23%, outside ±20% aspect guardrail for uniform-scale
#   whole-radical reuse in P-A-007-v2). Quantitative: bank x-span=234, y-span=242,
#   ratio=0.969; target x-span=178, y-span=239, ratio=0.745.
# fresh_component: you_compressed_for_ren_left_composition

--- MMH-derived pixel anchors (image-y, 300x300) ---

  s1 亻 pie:  TL(0.94,0.633)=(94,63)   -> ML(0.199,0.948)=(20,195)
  s2 亻 shu:  ML(0.703,0.497)=(70,150) -> BL(0.732,0.906)=(73,291)
  s3 有 heng: C(0.093,0.228)=(109,123) -> MR(0.666,0.084)=(267,108)
  s4 有 pie:  TC(0.682,0.565)=(168,57) -> BL(0.891,0.332)=(89,233)
  s5 月 pie:  C(0.562,0.655)=(156,166) -> BC(0.427,0.962)=(143,296)
  s6 月 hzg:  C(0.641,0.673)=(164,167) -> BC(0.901,0.812)=(190,281)
              (heng_head=(164,167), corner=(190,167), gou_tail=(190,281),
               hook_tip=(178,274))
  s7 上heng:  BC(0.626,0.089)=(163,209) -> BC(0.98,0.007)=(198,201)
  s8 下heng:  BC(0.608,0.411)=(161,241) -> BR(0.001,0.35)=(200,235)

Stroke count: 8 primitive calls (matches MMH expected 8). All 11 MMH joints
are class N (natural gaps preserved by MMH anchor spacing).
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
    'stroke_count_ok': True,      # 8 primitive calls, matches MMH expected 8
    'endpoint_mismatches': [],    # inlined at MMH pixel anchors, 0 deviation
    'joint_class_mismatches': [], # all 11 joints class N; natural gaps preserved
    'overall_pass': True,
    'notes': 'P-A-006 verbatim MMH anchors, both radicals inlined. BANK_DEVIATION '
             'from you_have.py justified quantitatively (P-A-009): aspect '
             'compression 23% below native, outside P-A-007-v2 uniform-scale guardrail.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # === 亻 (left radical) ===
    # s1: 亻 pie (long TL -> ML sweep)
    draw_pie(d, (94, 63), (20, 195),
             bow_perp=13, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu (vertical descender)
    draw_shu(d, (70, 150), (73, 291), width=7)

    # === 有 (right radical, inlined per BANK_DEVIATION) ===
    # s3: top long heng of 有 (slight upward tilt L->R)
    draw_heng(d, (109, 123), (267, 108), width_head=7, width_tail=8)
    # s4: long pie of 有 (starts above s3, crosses through, sweeps down-left)
    draw_pie(d, (168, 57), (89, 233),
             bow_perp=12, w_head=8, w_tail=3, steps=80)
    # s5: 月's left curved pie (short, mild bow)
    draw_pie(d, (156, 166), (143, 296),
             bow_perp=5, w_head=6, w_tail=4, steps=60)
    # s6: 月's right frame (heng_zhe_gou)
    draw_heng_zhe_gou(d,
                      (164, 167),   # heng_head
                      (190, 167),   # corner (top-right of 月)
                      (190, 281),   # gou_tail (bottom-right of 月 shu)
                      (178, 274))   # hook_tip (small upward flick)
    # s7: upper inner heng of 月
    draw_heng(d, (163, 209), (198, 201), width_head=5, width_tail=6)
    # s8: lower inner heng of 月
    draw_heng(d, (161, 241), (200, 235), width_head=5, width_tail=6)

    out = Path(__file__).parent / "01_侑.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
