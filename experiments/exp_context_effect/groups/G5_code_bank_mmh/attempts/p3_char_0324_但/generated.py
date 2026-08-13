"""p3_char_0324_但 (dan, "but") — 7 strokes: 亻 (pie+shu) + 旦 (日 + bottom-一).

Recipe: P-A-006 — MMH anchors verbatim, stroke-primitive layer.
Guardrail (P-A-007): 亻 is not a compound needing a whole radical; use the
draw_pie+draw_shu decomposition explicitly (matches template of qian_person /
仟). 日 uses the boxy heng_zhe (draw_heng_zhe_box) with an inner middle heng
and a bottom-closing heng, then a long ground-heng carries the base of 旦.

Anchor pixels (MMH cell.frac -> pixel on 300x300):
  s1 pie:    TL(0.911,0.609)=(91,61)  -> ML(0.176,0.948)=(18,195)
  s2 shu:    ML(0.759,0.412)=(76,141) -> BL(0.762,0.892)=(76,289)
  s3 shu:    C (0.295,0.102)=(130,110)-> BC(0.512,0.039)=(151,204)
  s4 h-zhe:  C (0.488,0.216)=(149,122)-> MR(0.177,0.954)=(218,195)
  s5 mid h:  C (0.518,0.567)=(152,157)-> MR(0.024,0.474)=(202,147)
  s6 bot h:  C (0.582,0.969)=(158,197)-> MR(0.077,0.922)=(208,192)
  s7 gnd h:  BC(0.043,0.502)=(104,250)-> BR(0.783,0.470)=(278,247)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 7 primitive calls, matches MMH expected 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 6 joints are class N (natural gaps preserved)
    'overall_pass': True,
    'notes': 'P-A-006 template: MMH pixels verbatim; 日 box uses heng_zhe_box + middle/bottom heng; bottom 一 spans BC->BR.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 亻 pie (long TL->ML sweep)
    draw_pie(d, (91, 61), (18, 195),
             bow_perp=13, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu (vertical descender)
    draw_shu(d, (76, 141), (76, 289), width=7)
    # s3: left shu of 日
    draw_shu(d, (130, 110), (151, 204), width=7)
    # s4: 横折 of 日 (top-left corner -> bottom-right corner)
    draw_heng_zhe_box(d, (149, 122), (218, 195), width=7)
    # s5: middle heng inside 日
    draw_heng(d, (152, 157), (202, 147), width_head=6, width_tail=7)
    # s6: bottom heng closing 日 box
    draw_heng(d, (158, 197), (208, 192), width_head=7, width_tail=8)
    # s7: long bottom heng of 旦 (spans full width)
    draw_heng(d, (104, 250), (278, 247), width_head=9, width_tail=10)

    out = Path(__file__).parent / "01_但.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
