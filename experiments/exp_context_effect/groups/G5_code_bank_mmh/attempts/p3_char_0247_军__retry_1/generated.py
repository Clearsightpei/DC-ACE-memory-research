"""p3_char_0247_军 — G5 retry #1.

TRAJECTORY DIFF (from Read-tool inspection of GT + main FAIL PNG):
  - Main FAIL used correct MMH anchors but inlined all 6 strokes with
    dian/heng_zhe_short/heng/pie_zhe/heng/shu. Visually the 车 body
    looked disjointed: the pie_zhe stroke 4 rendered as an S-curve
    instead of a proper 撇折-style compound. Errata prescribes P-A-007
    fix: CALL bank primitives mi_cover.py (2 strokes) and che_car.py
    (4 strokes) instead of hand-inlining. Whole-radical primitives
    carry MMH-tested joint geometry that inlined strokes don't.
  - Fixes applied this retry: draw_mi_cover for 冖 top (ox=8, oy=-18,
    scale=1.0 to match MMH TL/ML anchors); draw_che for 车 body
    (ox=28, oy=49, scale=0.85 — compresses 车 to fit under the 冖
    while keeping shu bottom at y=300).
"""

import sys
import pathlib
from PIL import Image, ImageDraw

# expose success_bank/code for imports
BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from mi_cover import draw_mi_cover
from che_car import draw_che


# Per MANDATORY pre-submit self-check.
# 6 strokes total: mi_cover contributes 2 (dian + heng_zhe_short);
# che_car contributes 4 (heng + shu_zhe + heng + shu). = 6 ✓
#
# Endpoint check (bank primitives after transform vs MMH anchors):
#   mi_cover s1 dian:        (76,74)→(62,130)   vs MMH (75.6,73.2)→(60.9,130.7)  ✓
#   mi_cover s2 heng_zhe:    (86,90)→(221,122)  vs MMH (86.4,89.4)→(204.5,106.9) close
#   che_car s1 top heng:     (97,145)→(212,137) vs MMH (85.3,144.4)→(209.5,130.7) close
#   che_car s2 shu_zhe:      head(146,97)→corner(110,195)→tail(213,199)
#                            vs MMH head(133.6,97)→tail(203.6,191.9)             close
#   che_car s3 bottom heng:  (56,252)→(255,249) vs MMH (56.2,242)→(252.5,235.5)  close
#   che_car s4 shu:          (149,175)→(158,300) vs MMH (145.3,163.2)→(154.1,300) ✓
# All within ±0.20 cell tolerance.
#
# Joint checks:
#   s3.mid ⇆ s4.mid P @ C: shu_zhe head-to-corner segment crosses top heng — welded ✓
#   s4.mid ⇆ s6.mid P @ C: shu_zhe tail segment crosses central shu     — welded ✓
#   s5.mid ⇆ s6.mid P @ BC: bottom heng crosses shu                     — welded ✓
#   s2.mid ⇆ s3.mid N @ TL: mi heng-hook drops beside 车 top heng       — small gap ✓
#   s2.tail ⇆ s3.tail N @ MR: mi hook tail (221,122) vs 车 heng tail (212,137) — gap ~18px ✓

SELF_CHECK = {
    "visual_ok": None,          # set after render+compare
    "stroke_count_ok": True,    # 2 (mi_cover) + 4 (che_car) = 6
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": None,
    "notes": "P-A-007 fix: use mi_cover + che_car bank primitives instead of inlining.",
}


def draw_jun(img_path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # Top: 冖 via bank primitive (2 strokes)
    draw_mi_cover(d, ox=8, oy=-18, scale=1.0)

    # Body: 车 via bank primitive (4 strokes), vertically compressed
    draw_che(d, ox=28, oy=49, scale=0.85)

    img.save(img_path)


if __name__ == "__main__":
    out = pathlib.Path(__file__).parent / "01_军.png"
    draw_jun(out)
    print("saved:", out)
