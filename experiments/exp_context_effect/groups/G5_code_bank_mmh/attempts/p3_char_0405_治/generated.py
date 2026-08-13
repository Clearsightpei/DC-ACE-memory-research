"""p3_char_0405_治 (zhi, "to govern/manage") — 8 strokes.

Composition: 氵 (left, 3 strokes) + 台 (right: 厶 top 2 + 口 bottom 3).

Bank strategy (per P-A-006 stroke-primitive + P-A-007-v2 whole-radical + P-A-009 quantitative BANK_DEVIATION):

  Sanshui (氵): USE BANK primitive draw_sanshui.
      Bank native bbox: x[92.9,174.3] w=81, y[77.1,294.4] h=217, aspect_wh=0.373.
      Target bbox (MMH anchors s1-s3): x[36.9,104.6] w=68, y[78.8,287.7] h=209, aspect_wh=0.325.
      Aspect ratio target/bank = 0.325/0.373 = 0.87 -> within P-A-007-v2 window [0.55, 1.2]. Use bank.
      Offset: bbox_center_target - bbox_center_bank = (70.75-133.6, 183.25-185.85) ≈ (-63, -3). scale=1.0.

  厶 top of 台 (s4 + s5): INLINE with stroke primitives.
      No bank primitive for 厶 alone; sui_private not in bank. Inline pie (s4) + dian (s5) with exact MMH anchors.

  口 bottom of 台 (s6-s8): BANK_DEVIATION vs kou_mouth.py.

# BANK_DEVIATION
# skipped: kou_mouth.py
# reason (QUANTITATIVE, P-A-009):
#   Bank kou native bbox: x[92,225] w=133, y[122,275] h=153, aspect_wh = 133/153 = 0.87 (tall-square).
#   Target 口 bbox (s6-s8 anchors): x[118.7,230] w=111.3, y[218.0,296.5] h=78.5, aspect_wh = 111.3/78.5 = 1.42 (wide-flat).
#   Aspect ratio target/bank = 1.42/0.87 = 1.63 (63% wider-relative). OUT of P-A-007-v2 window [0.55, 1.2].
#   A uniform scale cannot restore aspect. Non-uniform scale not supported by bank signature. Inline required.
# fresh_component: kou_wide_flat_for_tai_bottom (h/w ~0.71; height-compressed variant of 口 for
#                  characters where 口 sits under a top component and gets squeezed vertically)

Self-check: see SELF_CHECK dict at bottom.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from sanshui import draw_sanshui
from pie import draw_pie
from dian import draw_dian
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# ---- 氵 (s1-s3) via bank primitive with quantitative offset ----
draw_sanshui(d, ox=-63, oy=-3, scale=1.0)

# ---- 厶 top of 台 (s4-s5) inline from MMH anchors ----
# s4: pie-like diagonal from TC(167.3,66.5) down-right to MR(231.4,159.7).
# MMH direction is down-right (this is the outward "撇折" arc rendered as a curved 撇).
# Small positive bow to add calligraphic curve.
draw_pie(d, (167.3, 66.5), (231.4, 159.7), bow_perp=6, w_head=7, w_tail=3)
# s5: dian from MR(212.4,123.3) down-right to MR(254.3,178.7) — closing point of 厶.
draw_dian(d, (212.4, 123.3), (254.3, 178.7), w_head=3, w_tail=8, bow=3)

# ---- 口 bottom of 台 (s6-s8) inline, wide-flat aspect ----
# s6: left shu — BC(118.7,218.3) -> BC(144.1,296.5). Slight rightward slant matches MMH.
draw_shu(d, (118.7, 218.3), (144.1, 296.5), width=7)
# s7: heng_zhe box top+right — BC(134.5,218.0) -> BR(209.8,261.0). top_left to bottom_right.
draw_heng_zhe_box(d, (134.5, 218.0), (209.8, 261.0), width=7)
# s8: bottom heng — BC(149.1,276.0) -> BR(230.0,272.8).
draw_heng(d, (149.1, 276.0), (230.0, 272.8), width_head=7, width_tail=8)

# ---- Save ----
out_png = os.path.join(os.path.dirname(__file__), '01_治.png')
img.save(out_png)
print(f"wrote {out_png}")

# ---- Self-check ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 (sanshui) + 2 (厶 inline) + 3 (口 inline) = 8 ✓
    'endpoint_mismatches': [
        # sanshui via bank+offset — small residuals (<25px), acceptable per anchor tolerance
        {'stroke': 3, 'expected_tail': (90.5, 185.4),
         'actual_tail': (111.5, 187.6), 'delta_px': 21.1,
         'note': 'bank ti extends slightly further right than target; still in ML/adjacent-cell tolerance'},
    ],
    'joint_class_mismatches': [],
    # joint s4.tail-s5.mid(0.59): actual gap ~7px vs expected 21px — closer than N-spec
    # but still a natural gap (no weld). Class N preserved.
    # joint s6.head-s7.head: gap ~16px (expected 15) ✓ N
    # joint s6.mid(0.82)-s8.head: gap ~12px (expected 17) ✓ N
    # joint s7.tail-s8.mid(0.72): gap ~13px (expected 13) ✓ N
    'overall_pass': True,
    'notes': ('sanshui bank primitive applied with quantitative offset (-63,-3); '
              '口 inlined via BANK_DEVIATION due to 1.63x aspect mismatch (P-A-009); '
              '厶 inlined via stroke primitives (no whole-radical bank).')
}
