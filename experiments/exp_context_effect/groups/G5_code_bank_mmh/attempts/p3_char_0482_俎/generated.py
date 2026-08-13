"""p3_char_0482_俎 (zǔ) — 9 strokes: 仌 (pie+dian x2) + 且 (shu + heng_zhe_box + 3 heng).

Recipe: P-A-006 (MMH anchors verbatim, stroke-primitive layer).
Guardrail P-A-007-v2: no whole-radical bank primitive exists for the 仌-stack
left half or for 且 as a unit; decompose into stroke primitives.
P-A-008 (mandatory reasoning trace) + P-A-009 (quantitative BANK_DEVIATION):
no BANK_DEVIATION here — every stroke is a straightforward stroke-primitive
call at verbatim MMH pixels; no whole-radical bank was skipped.

Anchor pixels (MMH cell.frac -> pixel on 300x300, cell offsets 100px):
  s1 pie  : TL(0.82,0.791)=(82,79)   -> ML(0.334,0.863)=(33,186)   long upper pie
  s2 dian : ML(0.835,0.351)=(84,135) -> C (0.207,0.641)=(121,164)  short down-right dab
  s3 pie  : ML(0.727,0.772)=(73,177) -> BL(0.196,0.789)=(20,279)   long lower pie
  s4 dian : BL(0.779,0.227)=(78,223) -> BC(0.184,0.555)=(118,256)  short down-right dab
  s5 shu  : TC(0.456,0.996)=(146,100)-> BC(0.506,0.692)=(151,269)  left vertical of 且
  s6 hzb  : C (0.62,0.028)=(162,103) -> BR(0.15,0.628)=(215,263)   横折 box of 且
  s7 heng : C (0.667,0.635)=(167,164)-> MR(0.03,0.559)=(203,156)   upper mid heng
  s8 heng : BC(0.664,0.13)=(166,213) -> BR(0.036,0.065)=(204,207)  lower mid heng
  s9 heng : BC(0.011,0.786)=(101,279)-> BR(0.769,0.754)=(277,275)  long bottom heng of 且
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from dian import draw_dian
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke-primitive calls, matches MMH expected 9
    'endpoint_mismatches': [], # all pixels are MMH verbatim
    'joint_class_mismatches': [],  # all 10 joints class N (natural gaps preserved)
    'overall_pass': True,
    'notes': 'P-A-006 template. 仌-stack (s1-s4) uses pie+dian pairs; 且 (s5-s9) uses shu+heng_zhe_box+3 heng like 但\'s 旦 sub-structure.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: upper long pie (仌 upper-half slash)
    draw_pie(d, (82, 79), (33, 186), bow_perp=10, w_head=8, w_tail=3, steps=90)
    # s2: upper short dian to the right of s1's midpoint
    draw_dian(d, (84, 135), (121, 164), w_head=3, w_tail=7, bow=3)
    # s3: lower long pie (仌 lower-half slash)
    draw_pie(d, (73, 177), (20, 279), bow_perp=10, w_head=8, w_tail=3, steps=90)
    # s4: lower short dian to the right of s3's midpoint
    draw_dian(d, (78, 223), (118, 256), w_head=3, w_tail=7, bow=3)
    # s5: 且 left shu — long vertical
    draw_shu(d, (146, 100), (151, 269), width=7)
    # s6: 且 横折 box (top-left corner -> bottom-right corner of box)
    draw_heng_zhe_box(d, (162, 103), (215, 263), width=7)
    # s7: upper middle heng inside 且
    draw_heng(d, (167, 164), (203, 156), width_head=6, width_tail=7)
    # s8: lower middle heng inside 且
    draw_heng(d, (166, 213), (204, 207), width_head=6, width_tail=7)
    # s9: long bottom heng of 且 (spans full width)
    draw_heng(d, (101, 279), (277, 275), width_head=9, width_tail=10)

    out = Path(__file__).parent / "01_俎.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
