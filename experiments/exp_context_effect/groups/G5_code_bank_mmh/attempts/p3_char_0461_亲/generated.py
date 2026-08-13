"""p3_char_0461_亲 (qīn, "relative/parent") — 9 strokes.

Structure: 立 top (5 strokes, compressed) + 木-like bottom
(heng + shu descending from 立 baseline + pie + na) = 9 strokes.

Recipe: P-A-006 (stroke-primitive layer with verbatim MMH anchors).
Bank primitives li_stand.py and mu_wood.py both exist but neither
fits directly:
  - li_stand geometry expects full-canvas 立 (y 74-273); here 立 top
    is compressed to y 58-181 with tighter widths.
  - mu_wood expects a standalone 木 with heng at y=140 and central
    shu piercing it; here the "shu" (s7) starts at y=179 (before the
    bottom heng at y=216) and descends through the bottom heng, so
    the composition is not a plain 木 — it's a shu descending from
    the 立 baseline that pierces the 木-heng below.

BANK_DEVIATION rationale is quantitative (P-A-009):
  li_stand native y-range = 273-74 = 199 px.  Target 立 y-range =
    181-58 = 123 px.  Vertical compression = 123/199 = 0.62.
  li_stand native s5 width = 271-33 = 238 px. Target s5 width =
    252-42 = 210 px.  Horizontal compression = 210/238 = 0.88.
  Non-uniform scale (0.62 vertical vs 0.88 horizontal) — a single
  scale param cannot achieve this. Similarly mu_wood assumes shu
  passes through the heng midway, not descending from above.
  → inline both halves per MMH anchors.
"""

# BANK_DEVIATION
# skipped: li_stand.py, mu_wood.py
# reason: non-uniform vertical/horizontal compression (0.62 vs 0.88)
#   for 立 top; bottom is not a standalone 木 (shu s7 originates from
#   立 baseline, not from above the bottom heng).
# fresh_component: qin_top (compressed 立), qin_bot (linked shu + 木-heng + pie + na)

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 9 primitive calls verified below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Anchors read verbatim from MMH block. s7 (shu) drawn as '
             'a leaning shu (drift ~30px left from head->tail) to match '
             'MMH endpoints (135.1, 179.3) -> (103.7, 279.5).',
}


def draw_qin(draw):
    # ==================== 立 TOP (s1-s5) ====================
    # s1: top dian — TC(0.236, 0.583) -> TC(0.588, 0.812)
    #     pixel: (123.6, 58.3) -> (158.8, 81.2)
    draw_dian(draw, (123.6, 58.3), (158.8, 81.2),
              w_head=2, w_tail=7, bow=3, steps=48)

    # s2: upper heng — ML(0.879, 0.046) -> TR(0.095, 0.932)
    #     pixel: (87.9, 104.6) -> (209.5, 93.2)
    draw_heng(draw, (87.9, 104.6), (209.5, 93.2),
              width_head=7, width_tail=8)

    # s3: left short dian/slant — ML(0.996, 0.298) -> C(0.178, 0.538)
    #     pixel: (99.6, 129.8) -> (117.8, 153.8)
    draw_dian(draw, (99.6, 129.8), (117.8, 153.8),
              w_head=2, w_tail=6, bow=2, steps=32)

    # s4: right short pie — C(0.805, 0.093) -> C(0.567, 0.641)
    #     pixel: (180.5, 109.3) -> (156.7, 164.1)
    draw_pie(draw, (180.5, 109.3), (156.7, 164.1),
             bow_perp=3, w_head=5, w_tail=2, steps=48)

    # s5: long 立-base heng — ML(0.416, 0.813) -> MR(0.517, 0.696)
    #     pixel: (41.6, 181.3) -> (251.7, 169.6)
    draw_heng(draw, (41.6, 181.3), (251.7, 169.6),
              width_head=8, width_tail=9)

    # ==================== 木-like BOTTOM (s6-s9) ====================
    # s6: bottom heng (of 木) — BL(0.703, 0.215) -> BR(0.188, 0.115)
    #     pixel: (70.3, 221.5) -> (218.8, 211.5)
    draw_heng(draw, (70.3, 221.5), (218.8, 211.5),
              width_head=7, width_tail=8)

    # s7: descending shu (P-joint welded to s6 at BC(0.487, 0.132)) —
    #     C(0.351, 0.793) -> BC(0.037, 0.795)
    #     pixel: (135.1, 179.3) -> (103.7, 279.5)
    #     Slight leftward drift built into endpoints; use draw_shu.
    draw_shu(draw, (135.1, 179.3), (103.7, 279.5), width=6)

    # s8: pie — BL(0.987, 0.423) -> BL(0.674, 0.839)
    #     pixel: (98.7, 242.3) -> (67.4, 283.9)
    draw_pie(draw, (98.7, 242.3), (67.4, 283.9),
             bow_perp=4, w_head=5, w_tail=2, steps=48)

    # s9: na — BC(0.808, 0.42) -> BR(0.279, 0.854)
    #     pixel: (180.8, 242.0) -> (227.9, 285.4)
    draw_na(draw, (180.8, 242.0), (227.9, 285.4),
            bow_perp=6, w_head=3, w_tail=9, steps=60)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_qin(d)
    out = os.path.join(_HERE, "01_亲.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
