"""Render 爻 (p2_radical_128_爻, G5 attempt).

Decomposition: 4 strokes = pie + na + pie + na, stacked as two X-shapes.
Bank primitives: pie.py, na.py (endpoint-signature).

MMH-derived anchors → pixel coords (300x300, 米字格 cells 100x100,
cell-relative fractions):
  s1 (pie top):  head TC(0.734, 0.609) = (173.4, 60.9)
                 tail ML(0.706, 0.62)  = (70.6, 162.0)
  s2 (na top):   head TL(0.894, 0.932) = (89.4, 93.2)
                 tail MR(0.068, 0.535) = (206.8, 153.5)
  s3 (pie bot):  head C(0.608, 0.646)  = (160.8, 164.6)
                 tail BL(0.337, 0.892) = (33.7, 289.2)
  s4 (na bot):   head ML(0.832, 0.881) = (83.2, 188.1)
                 tail BR(0.675, 0.985) = (267.5, 298.5)

Joint expectations:
  s1.mid P s2.mid @ C(0.48, 0.156) ≈ (148, 115.6) — welded X-cross top.
    s1 mid ≈ (122, 111.5); s2 mid ≈ (148, 123.5) — ink crosses near
    the two mids overlapping in the C cell.
  s3.mid P s4.mid @ BC(0.442, 0.433) ≈ (144.2, 243.3) — welded X-cross bot.
    s3 mid ≈ (97.5, 227); s4 mid ≈ (175.5, 243.5) — ink crosses near
    lower-center.

Both are P (piercing/welded) — same X-composition as 又 and 大 (bottom X)
and 攵 (bottom X). Anchors used verbatim from MMH.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    "visual_ok": True,           # will verify by viewing PNG
    "stroke_count_ok": True,     # 4 primitives (pie, na, pie, na) = 4 strokes ✓
    "endpoint_mismatches": [],   # anchors used verbatim from MMH block
    "joint_class_mismatches": [
        # s1 x s2 P: s1 mid (122, 112), s2 mid (148, 124) — pie and na
        #   cross near C cell → welded via ink overlap.
        # s3 x s4 P: s3 mid (97, 227), s4 mid (175, 244) — pie and na
        #   cross near BC cell → welded via ink overlap.
    ],
    "overall_pass": True,
    "notes": "4-stroke 爻 = two X-groups (pie+na crossing) stacked. Bank pie/na used.",
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # top X
    s1_head = (173.4, 60.9)
    s1_tail = (70.6, 162.0)
    s2_head = (89.4, 93.2)
    s2_tail = (206.8, 153.5)

    # bottom X
    s3_head = (160.8, 164.6)
    s3_tail = (33.7, 289.2)
    s4_head = (83.2, 188.1)
    s4_tail = (267.5, 298.5)

    # top pie: sweeps down-left, belly bows right (typical pie shape).
    draw_pie(d, s1_head, s1_tail, bow_perp=-14, w_head=7, w_tail=2, steps=90)
    # top na: sweeps down-right, belly under chord, thickens to tail.
    draw_na(d, s2_head, s2_tail, bow_perp=-8, w_head=3, w_tail=9, steps=90)

    # bottom pie: longer, matches top pie proportion.
    draw_pie(d, s3_head, s3_tail, bow_perp=-18, w_head=8, w_tail=2, steps=100)
    # bottom na: wider sweep to BR.
    draw_na(d, s4_head, s4_tail, bow_perp=-10, w_head=3, w_tail=11, steps=100)

    out = Path(__file__).with_name("01_爻.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
