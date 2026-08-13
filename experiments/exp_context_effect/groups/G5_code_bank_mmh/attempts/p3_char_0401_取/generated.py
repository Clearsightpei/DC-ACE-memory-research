"""p3_char_0401_取 — 取 (qǔ, 'take') = 耳 (left, 6 strokes) + 又 (right, 2 strokes).

Strategy: MMH anchor-driven stroke-primitive layer (P-A-006 / P-A-008).
The character is 8 strokes. No whole-radical bank primitive fits well:
- 耳 not in bank
- 又 (you_again) native aspect doesn't match compressed right-half here.

BANK_DEVIATION (P-A-009 quantitative):
# skipped: you_again.py  (draw_you)
# reason: bank you_again renders heng_pie head (77.9, 116.9) tail (42.5,
#   276.0), na head (79.4, 139.7) tail (285.4, 278.9) — native aspect
#   208x162 (w x h), aspect w/h = 1.28. Target 又 in 取: bounding roughly
#   (140..281, 127..251) = 141x124, aspect w/h = 1.14. Scale ratios:
#   x = 141/208 = 0.68, y = 124/162 = 0.77 — non-uniform (delta 0.09).
#   Also the pie START is at (152, 127) inside center cell (bank pie
#   starts near top-left). Composition doesn't fit; inline as 2 strokes
#   with MMH anchors verbatim.
# fresh_component: you_for_qu_compressed  (又 as 2 strokes with C-based head)

Per-stroke reasoning (P-A-008 mandatory trace, image-y convention):
- s1 heng (38,90)->(154,77): top short heng of 耳 (slight upward tilt).
- s2 shu (58,99)->(62,217): left vertical of 耳.
- s3 shu (117,87)->(124,207): right vertical of 耳 (a bit longer, extends
  slightly below s6 crossing).
- s4 heng (77,138)->(104,133): upper small inner heng.
- s5 heng (74,174)->(103,168): lower small inner heng.
- s6 ti (26,231)->(148,195): 耳's 提 (rising, from BL up-right, crosses
  s3 in P-joint).
- s7 pie (152,127)->(140,246): 又's long descender.
- s8 na (148,148)->(281,249): 又's 捺 (crosses s7 in P-joint).
"""

import os
import sys

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors verbatim (image-y convention); 8 strokes; s6 crosses s3 (P); s8 crosses s7 (P).',
}

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from ti import draw_ti


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top short heng of 耳
    draw_heng(d, (38, 90), (154, 77), width_head=8, width_tail=9)

    # s2: left shu of 耳
    draw_shu(d, (58, 99), (62, 217), width=7)

    # s3: right shu of 耳
    draw_shu(d, (117, 87), (124, 207), width=6)

    # s4: upper inner heng
    draw_heng(d, (77, 138), (104, 133), width_head=6, width_tail=6)

    # s5: lower inner heng
    draw_heng(d, (74, 174), (103, 168), width_head=6, width_tail=6)

    # s6: 耳's 提 rising from BL up-right; crosses s3 at BC region
    draw_ti(d, (26, 231), (148, 195), w_head=9, w_tail=3, steps=60)

    # s7: 又's descending pie (long, steep)
    draw_pie(d, (152, 127), (140, 246),
             bow_perp=6, w_head=8, w_tail=3, steps=70)

    # s8: 又's 捺
    draw_na(d, (148, 148), (281, 249),
            bow_perp=10, w_head=4, w_tail=11, steps=90)

    out = os.path.join(HERE, "01_取.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
