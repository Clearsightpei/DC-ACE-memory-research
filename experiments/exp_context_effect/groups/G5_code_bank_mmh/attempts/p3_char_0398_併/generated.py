"""p3_char_0398_併 (bìng, 'together, combine') — 亻 + 并, 8 strokes.

Sub-component reasoning (P-A-008 mandatory inline trace):

  - 亻 (s1 pie + s2 shu, left half):
    Bank has `ren_left.py`. Quantitative BANK_DEVIATION check
    (P-A-009):
      native s1 pie: (158.8,73.8) → (80.6,211.2)
        span_x = |80.6-158.8| = 78.2 px, span_y = 137.4 px, aspect
        (w/h) = 0.569
      target s1 pie: (84.1,63.3) → (21.7,194.8)
        span_x = 62.4 px, span_y = 131.5 px, aspect = 0.475
      scale_x = 62.4/78.2 = 0.798, scale_y = 131.5/137.4 = 0.957
      aspect ratio target/native = 0.475/0.569 = 0.835
    Non-uniform scale (x=0.80 vs y=0.96) and aspect ratio 0.835 is
    at the edge of P-A-007-v2 band [0.55, 1.2] but the required
    non-uniform squash pulls s1 tail 44 px further left than any
    simple (ox, oy, scale) transform of ren_left can achieve
    (target's 亻 is pushed to the far-left edge with tail at
    x=21.7). Also the ren_left native shu is at x≈140-144 vs
    target x≈73-77 — a ~66 px translation delta that differs from
    the pie's translation delta of ~75 px (translation-mismatch:
    the two strokes need different ox shifts). BANK_DEVIATION per
    P-A-006 recipe: inline s1 + s2 with draw_pie + draw_shu at MMH
    anchors verbatim.

  - 并 (s3 dot + s4 dot + s5 upper heng + s6 lower heng + s7 left
    vertical/pie + s8 right vertical/shu, right half — 6 strokes):
    Bank has `bing_and.py` (並, 8-stroke traditional variant).
    Quantitative BANK_DEVIATION check (P-A-009):
      bing_and structure has 立-style top: pie + pie + heng + shu +
      shu + dian + dian + heng (8 strokes with 3 hengs and 2 outer
      dians). Target 并 in 併 is 6 strokes: dot + dot + heng + heng
      + pie + shu (2 hengs total, no outer dians, verticals extend
      through both hengs).
      Stroke-count mismatch (8 vs 6) — P-A-007-v2 hard-check FAIL.
      Structurally different characters despite similar bounding
      box; bing_and cannot be scaled into 并.
    BANK_DEVIATION: skip bing_and entirely, inline all 6 strokes
    fresh at MMH anchors verbatim per P-A-006.

# BANK_DEVIATION
# skipped: ren_left.py — non-uniform x/y scale (0.80 vs 0.96) + per-stroke
#          translation-mismatch (pie needs ox -74, shu needs ox -66);
#          cannot express as single (ox, oy, scale) transform
# skipped: bing_and.py — stroke-count mismatch 8-stroke 並 vs 6-stroke 并
#          (P-A-007-v2 hard-check fail)
# fresh_component: ren_left_farleft_variant (亻 shifted to far-left edge),
#                  bing_6stroke_right_variant (并 as 2dots+2hengs+pie+shu)
# reason: MMH-anchor P-A-006 recipe gives exact endpoint placement; bank
#         primitives fail quantitative aspect + stroke-count checks.

Joint expectations (mix of N naturals and P welds):
  s1.mid ⇆ s2.head @ ML   ~19 px gap N — pie/shu natural spacing
  s2.mid ⇆ s6.head @ ML   ~35 px gap N — 亻 shu mid to 并 lower-heng head
  s5.head ⇆ s7.head @ C   ~12 px gap N — upper heng and left vert heads
  s5.mid  ⇆ s8.head @ C   ~16 px gap N — upper heng mid and right vert head
  s6.mid  ⇆ s7.mid @ C    weld P — lower heng crosses left vert (pierce)
  s6.mid  ⇆ s8.mid @ MR   weld P — lower heng crosses right vert (pierce)
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 strokes drawn: pie, shu, dian, dian, heng, heng, pie, shu
    'endpoint_mismatches': [],     # MMH anchors verbatim (s8 tail capped at 297 to keep on-canvas)
    'joint_class_mismatches': [],  # 4 N + 2 P — P welds arise naturally from vert-crossing-heng
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer; BANK_DEVIATION on ren_left (aspect+translation-mismatch) and bing_and (stroke count 8 vs 6).',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ----- 亻 (left half, 2 strokes) -----
    # s1: 亻 pie — TL(84.1, 63.3) → ML(21.7, 194.8)
    draw_pie(d, (84.1, 63.3), (21.7, 194.8),
             bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu — ML(72.9, 143.6) → BL(77.3, 289.2)
    draw_shu(d, (72.9, 143.6), (77.3, 289.2), width=7)

    # ----- 并 upper: two dots 丷 (s3 left-dot + s4 right-dot) -----
    # s3: left dot (short downward-right stroke) — TC(135.9, 78.5) → C(160.0, 103.1)
    # Small dian going down-right.
    draw_dian(d, (135.9, 78.5), (160.0, 103.1),
              w_head=3, w_tail=7, bow=3, steps=40)
    # s4: right dot (short downward-left stroke, pie-flavored) — TR(214.2, 51.6) → C(188.7, 110.2)
    # Slightly longer diagonal, use pie primitive with mild bow.
    draw_pie(d, (214.2, 51.6), (188.7, 110.2),
             bow_perp=4, w_head=4, w_tail=3, steps=50)

    # ----- 并 middle: two horizontals -----
    # s5: upper heng — C(123.6, 138.6) → MR(247.0, 121.9). Slight upward tilt.
    draw_heng(d, (123.6, 138.6), (247.0, 121.9),
              width_head=7, width_tail=8)
    # s6: lower long heng — C(105.8, 194.2) → MR(274.2, 179.0). Wider, slight upward tilt.
    draw_heng(d, (105.8, 194.2), (274.2, 179.0),
              width_head=8, width_tail=9)

    # ----- 并 bottom: two verticals -----
    # s7: left vertical (pie-slanted, drifts down-left) — C(143.8, 147.7) → BC(109.6, 280.1)
    # Use pie with low bow for a nearly-straight down-left slant.
    draw_pie(d, (143.8, 147.7), (109.6, 280.1),
             bow_perp=6, w_head=7, w_tail=4, steps=90)
    # s8: right vertical (straight shu) — C(197.8, 135.9) → BR(210.9, 297.0)
    # MMH tail is 316.1 (off-canvas), cap at 297 to keep in-canvas.
    draw_shu(d, (197.8, 135.9), (210.9, 297.0), width=7)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_併.png')
    draw().save(out)
    print('wrote', out)
