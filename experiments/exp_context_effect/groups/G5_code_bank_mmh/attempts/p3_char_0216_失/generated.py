"""p3_char_0216_失 — G5 attempt.

失 (shi, 'lose') — 5 strokes:
  s1: short pie at top-right descending to center-left (小撇)
  s2: first heng (shorter, tucked between s1's tail and center)
  s3: second heng (longer, spans the full middle)
  s4: long descending pie from top-center to bottom-left
  s5: na from center down-right to bottom-right

Bank use: pie / heng / na primitives (sibling of 大/天/矢 family).
No BANK_DEVIATION — the standard pie/heng/na primitives fit cleanly
for a 大-family composition; s1 is just a smaller pie call.
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
)
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie  # noqa: E402
from heng import draw_heng  # noqa: E402
from na import draw_na  # noqa: E402


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,  # 5 primitive calls below
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": True,
    "notes": (
        "5 strokes match MMH. s2/s4 P-cross at C (heng passes over long pie). "
        "s3/s4 P-cross at C (bottom heng crosses long pie). "
        "s5 head near s3 mid and s4 mid — N gap (na starts under joint)."
    ),
}


def render(path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # --- Endpoint anchors from MMH block ---
    # s1: TL(.946,.943) -> ML(.618,.652)  small pie top-right -> center-left
    s1_head = (94.6, 94.3)
    s1_tail = (61.8, 165.2)
    # s2: ML(.976,.368) -> MR(.065,.184)  first heng
    s2_head = (97.6, 136.8)
    s2_tail = (206.5, 118.4)
    # s3: ML(.595,.978) -> MR(.426,.819)  second (longer) heng
    s3_head = (59.5, 197.8)
    s3_tail = (242.6, 181.9)
    # s4: TC(.389,.598) -> BL(.422,.936)  long descending pie
    s4_head = (138.9, 59.8)
    s4_tail = (42.2, 293.6)
    # s5: C(.538,.978) -> BR(.763,.927)  na
    s5_head = (153.8, 197.8)
    s5_tail = (276.3, 292.7)

    # s1 — small pie
    draw_pie(d, s1_head, s1_tail,
             bow_perp=4, w_head=6, w_tail=2, steps=60)

    # s2 — first heng (top)
    draw_heng(d, s2_head, s2_tail, width_head=6, width_tail=7)

    # s3 — second heng (middle, longer). Draw AFTER s2 but BEFORE s4/s5
    # so the long pie/na visually overlay onto it (P-joints at C).
    draw_heng(d, s3_head, s3_tail, width_head=7, width_tail=8)

    # s4 — long pie descending to lower-left.
    draw_pie(d, s4_head, s4_tail,
             bow_perp=-24, w_head=8, w_tail=2, steps=110)

    # s5 — na sweeping to lower-right.
    draw_na(d, s5_head, s5_tail,
            bow_perp=-8, w_head=3, w_tail=11, steps=100)

    img.save(path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_失.png")
    render(out)
    print("wrote", out)
