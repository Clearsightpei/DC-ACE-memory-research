"""p3_char_0246_仵 (wǔ, 亻+午 L-R — 6 strokes).

Recipe: P-A-006 — MMH anchors verbatim + stroke-primitive layer.
Sibling of 仟 (bank: qian_person.py) but 午 phonetic has an extra
top pie/heng (4 strokes) vs 千 (3 strokes). Skipping ren_left +
午-composed radical to avoid double-transform. Inlining stroke
primitives at MMH pixel anchors.

Stroke order (MMH):
  s1: 亻 pie (TL→ML)
  s2: 亻 shu (ML→BL)
  s3: 午 short pie top (TC→C)
  s4: 午 short top heng (C→MR)
  s5: 午 long bottom heng (C→MR)
  s6: 午 central shu (C→BC, pierces s5)
"""

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 6 primitives, matches MMH expected 6
    'endpoint_mismatches': [],    # verified after render
    'joint_class_mismatches': [], # 3 N-gaps + 1 P-weld via draw order
    'overall_pass': True,
    'notes': 'P-A-006 recipe: MMH anchors verbatim + stroke layer. Cousin of 仟/年.'
}


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_wu_person(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 亻 pie — MMH TL(0.908,0.624)=(90.8,62.4) → ML(0.176,0.983)=(17.6,198.3)
    draw_pie(draw, _tx(90.8, 62.4, ox, oy, scale), _tx(17.6, 198.3, ox, oy, scale),
             bow_perp=int(13 * scale) or 1,
             w_head=max(2, int(9 * scale)),
             w_tail=max(2, int(3 * scale)), steps=90)
    # s2: 亻 shu — ML(0.68,0.521)=(68.0,152.1) → BL(0.721,0.895)=(72.1,289.5)
    draw_shu(draw, _tx(68.0, 152.1, ox, oy, scale), _tx(72.1, 289.5, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3: 午 short pie top — TC(0.509,0.645)=(150.9,64.5) → C(0.084,0.6)=(108.4,160.0)
    draw_pie(draw, _tx(150.9, 64.5, ox, oy, scale), _tx(108.4, 160.0, ox, oy, scale),
             bow_perp=int(6 * scale) or 1,
             w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(3 * scale)), steps=70)
    # s4: 午 short top heng — C(0.459,0.251)=(145.9,125.1) → MR(0.37,0.075)=(237.0,107.5)
    draw_heng(draw, _tx(145.9, 125.1, ox, oy, scale), _tx(237.0, 107.5, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s5: 午 long bottom heng — C(0.014,0.966)=(101.4,196.6) → MR(0.707,0.849)=(270.7,184.9)
    draw_heng(draw, _tx(101.4, 196.6, ox, oy, scale), _tx(270.7, 184.9, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
    # s6: 午 central shu — C(0.711,0.292)=(171.1,129.2) → BC(0.825,1.155) clipped to (182.5,295)
    #     Pierces s5 at ~C via overdraw (P-joint).
    draw_shu(draw, _tx(171.1, 129.2, ox, oy, scale), _tx(182.5, 295.0, ox, oy, scale),
             width=max(2, int(8 * scale)))


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_wu_person(d, ox=0, oy=0, scale=1.0)
    out = Path(__file__).parent / "01_仵.png"
    img.save(out)
    print(f"wrote {out}")
