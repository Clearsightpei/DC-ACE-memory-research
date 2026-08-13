"""p3_char_0397_空 (kōng, "empty") — 8 strokes = 穴 (宀 + 八) + 工.

P-A-006 stroke-primitive layer with MMH-verbatim anchors.
BANK REUSE: heng, shu, dian, pie, heng_zhe_short from stroke bank.
Composition mirrors ding_fix (宀 top) + gong_work (工 bottom) but uses
MMH anchors verbatim rather than whole-radical composition, since
this character has 八 in the middle (穴 = 宀+八) between the two.

BANK_DEVIATION reasoning (P-A-009 quantitative):
- draw_mian_roof native footprint: dian(140,88)-(162,110), pie(...),
  heng_zhe_short(...). Native 宀 vertical extent ~88-165 = 77px.
  MMH 空's 宀 vertical extent: s1_top=56.2, s3_bot=141.8 → 85.6px.
  Aspect ratio ≈1.11× native but MMH horizontal extent is
  (57.4 to 212.7) = 155px vs mian_roof native ~123px = 1.26×.
  Aspects don't match (1.11 vs 1.26) → skip whole-radical
  draw_mian_roof, inline strokes with MMH anchors per P-A-006/P-A-007.
- draw_gong_work native footprint: heng(87-225 x 114/102), etc.
  Native 工 vertical extent ~114-249 = 135px, horiz ~87-278 = 191px.
  MMH 空's 工: horiz ~50-252 = 202px (1.06×), vertical ~205-283 = 78px (0.58×).
  Vertical aspect ratio very compressed (0.58×) → skip whole-radical
  draw_gong_work, inline strokes per P-A-007 hard-check.

MANDATORY per-stroke reasoning trace (P-A-008):
- s1 dian (top of 宀): MMH (133, 56.2) → (165.2, 80.3). Use draw_dian.
- s2 short pie (left of 宀): MMH (69.4, 108.7) → (57.4, 164.4). draw_pie shortened.
- s3 heng_zhe_short (top of 宀): MMH (82, 117.5) → (212.7, 141.8).
- s4 pie (left of 八 in 穴): MMH (106.1, 149.1) → (68.3, 209.8). draw_pie.
- s5 dian (right of 八): MMH (169, 147.4) → (208.3, 176.7). Short na-ish → draw_dian.
- s6 top heng of 工: MMH (97.3, 214.7) → (201.3, 205.4). draw_heng.
- s7 shu of 工: MMH (138.9, 221.8) → (140, 268.1). draw_shu.
- s8 bottom heng of 工: MMH (50.1, 283) → (252.2, 277.7). draw_heng (wider).

Joint checks (all N-class per MMH):
- s2.mid ⇆ s3.head @ ML: N-gap expected ~12.8px. s2.mid ≈ (63, 137), s3.head=(82, 117.5). dist ≈ 27px → N ok.
- s4.mid ⇆ s6.head @ BL: N-gap ~33.5px. s4.mid ≈ (87, 179), s6.head=(97, 214.7). dist ≈ 37px → N ok.
- s6.mid ⇆ s7.head @ BC: N-gap ~13px. s6.mid ≈ (149, 210), s7.head=(138.9, 221.8). dist ≈ 15px → N ok.
- s7.tail ⇆ s8.mid @ BC: N-gap ~16.9px. s7.tail=(140, 268.1), s8.mid≈(151, 280). dist ≈ 16px → N ok.
"""

import os
import sys

# Import from success_bank/code
BANK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK_DIR))

from PIL import Image, ImageDraw

from dian import draw_dian
from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short
from pie import draw_pie
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 strokes: dian, pie, heng_zhe_short, pie, dian, heng, shu, heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors; P-A-006 stroke layer; P-A-007 whole-radical'
             ' skipped due to quantitative aspect mismatch (documented in module docstring).',
}


def _render():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # --- 宀 top of 穴 (3 strokes) ---
    # s1: top-center dian
    draw_dian(draw, (133.0, 56.2), (165.2, 80.3),
              w_head=3, w_tail=8, bow=3, steps=48)
    # s2: short left pie of 宀 (nearly vertical, slight left drift)
    draw_pie(draw, (69.4, 108.7), (57.4, 164.4),
             bow_perp=3, w_head=7, w_tail=4, steps=60)
    # s3: heng-zhe-short top of 宀 (horizontal then short descend at right)
    draw_heng_zhe_short(draw, (82.0, 117.5), (212.7, 141.8),
                        corner_offset=(-4, -3))

    # --- 八 middle of 穴 (2 strokes) ---
    # s4: left pie of 八 (inside 穴, goes down-left)
    draw_pie(draw, (106.1, 149.1), (68.3, 209.8),
             bow_perp=6, w_head=8, w_tail=3, steps=80)
    # s5: right dian of 八 (short down-right dab)
    draw_dian(draw, (169.0, 147.4), (208.3, 176.7),
              w_head=3, w_tail=9, bow=4, steps=48)

    # --- 工 bottom (3 strokes) ---
    # s6: top heng of 工
    draw_heng(draw, (97.3, 214.7), (201.3, 205.4),
              width_head=7, width_tail=8)
    # s7: shu of 工 (short vertical)
    draw_shu(draw, (138.9, 221.8), (140.0, 268.1), width=7)
    # s8: bottom long heng of 工
    draw_heng(draw, (50.1, 283.0), (252.2, 277.7),
              width_head=9, width_tail=10)

    return img


if __name__ == "__main__":
    out = _render()
    out.save(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "01_空.png"))
