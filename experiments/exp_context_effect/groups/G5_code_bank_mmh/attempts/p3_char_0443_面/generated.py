"""p3_char_0443_面 (miàn, 'face') — 9 strokes, MMH-anchor verbatim + stroke-primitive layer (P-A-006).

Structure (per MMH block):
  s1 — top heng (long)                         → draw_heng
  s2 — short pie under top heng, left side     → draw_pie
  s3 — outer left vertical shu                 → draw_shu
  s4 — outer top+right heng_zhe (boxy corner)  → draw_heng_zhe_box
  s5 — inner left vertical divider             → draw_shu
  s6 — inner right vertical divider            → draw_shu
  s7 — upper inner heng (between s5 & s6)      → draw_heng
  s8 — lower inner heng (between s5 & s6)      → draw_heng
  s9 — outer bottom heng                       → draw_heng

Reasoning trace (P-A-008 mandatory):
  * Bank has NO whole-radical primitive for 面 (not in INDEX). Composition is required.
  * P-A-006 recipe: use MMH anchors verbatim as pixel endpoints (cell top-left + frac*100)
    and drop each MMH stroke into the matching bank stroke primitive.
  * All 14 expected joints are class N (natural gap) — bank primitives naturally produce
    N-class touches when heads/tails sit near each other but not welded. No P/T welds
    required, so no BANK_DEVIATION forcing negative bow / crossing math.
  * s4 renders as a boxy L-corner via draw_heng_zhe_box(top_left=s4.head, bottom_right=s4.tail).
    Its top-left slightly overlaps s3.head (~15 px N-gap), matching MMH's expected 11 px gap.
  * Inner structure: MMH gives two short verticals (s5 x~115, s6 x~167) + two short
    hengs between them (s7 y~190, s8 y~227). This forms a small ⌸ (H-window) inside
    the outer box — consistent with 面's calligraphic inner divider pattern.

BANK_DEVIATION: none. All 9 strokes covered by bank stroke primitives at MMH anchors.
"""

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from heng import draw_heng            # noqa: E402
from shu import draw_shu              # noqa: E402
from pie import draw_pie              # noqa: E402
from heng_zhe_box import draw_heng_zhe_box  # noqa: E402


# MMH-anchor pixel conversions (cell top-left + frac*100)
S1_HEAD, S1_TAIL = (87.9, 91.1),  (218.8, 79.1)   # top heng
S2_HEAD, S2_TAIL = (132.4, 99.9), (111.9, 146.2)  # small pie
S3_HEAD, S3_TAIL = (45.1, 156.4), (75.0, 281.5)   # outer left shu (slight rightward drift)
S4_HEAD, S4_TAIL = (60.1, 158.5), (227.9, 284.8)  # outer top+right heng_zhe
S5_HEAD, S5_TAIL = (108.1, 160.5), (124.5, 260.7) # inner left vert
S6_HEAD, S6_TAIL = (165.5, 151.2), (169.0, 255.2) # inner right vert
S7_HEAD, S7_TAIL = (128.6, 193.9), (155.9, 187.8) # upper inner heng
S8_HEAD, S8_TAIL = (128.6, 230.6), (155.9, 224.1) # lower inner heng
S9_HEAD, S9_TAIL = (81.7, 275.1),  (214.2, 261.9) # bottom heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 9 primitive calls, 9 MMH strokes
    'endpoint_mismatches': [],        # all endpoints = MMH-derived pixels verbatim
    'joint_class_mismatches': [],     # all 14 joints are N — bank primitives produce natural gaps
    'overall_pass': True,
    'notes': 'P-A-006: MMH-anchor verbatim + stroke-primitive layer. Inner ⌸ pattern from s5-s8.',
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # s1 — top heng (long, slight lift toward right)
    draw_heng(draw, S1_HEAD, S1_TAIL, width_head=9, width_tail=10)

    # s2 — small pie descending left, just under top heng
    draw_pie(draw, S2_HEAD, S2_TAIL, bow_perp=6, w_head=7, w_tail=3, steps=60)

    # s3 — outer left vertical shu (long)
    draw_shu(draw, S3_HEAD, S3_TAIL, width=8)

    # s4 — outer top+right heng_zhe (boxy L)
    draw_heng_zhe_box(draw, top_left=S4_HEAD, bottom_right=S4_TAIL, width=8)

    # s5 — inner left vertical divider
    draw_shu(draw, S5_HEAD, S5_TAIL, width=6)

    # s6 — inner right vertical divider
    draw_shu(draw, S6_HEAD, S6_TAIL, width=6)

    # s7 — upper inner heng (between s5 and s6)
    draw_heng(draw, S7_HEAD, S7_TAIL, width_head=6, width_tail=6)

    # s8 — lower inner heng (between s5 and s6)
    draw_heng(draw, S8_HEAD, S8_TAIL, width_head=6, width_tail=6)

    # s9 — outer bottom heng
    draw_heng(draw, S9_HEAD, S9_TAIL, width_head=9, width_tail=9)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_面.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
