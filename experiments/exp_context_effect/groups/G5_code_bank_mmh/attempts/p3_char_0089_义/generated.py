"""p3_char_0089_义 — G5 attempt.

义 is a 3-stroke character:
  s1: small dian (top-left area, slopes down-right)
  s2: long pie from upper-right to lower-left
  s3: long na from middle-left to lower-right
Joint: s2 crosses s3 near BC cell (piercing).

Uses bank primitives dian, pie, na with MMH-derived endpoint anchors.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

# Add bank to path
_BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(_BANK))

from dian import draw_dian  # noqa: E402
from na import draw_na  # noqa: E402
from pie import draw_pie  # noqa: E402


# ---------------------------------------------------------------------
# MMH-derived anchors (converted to 300x300 canvas pixels).
# Cell origins (100x100 each):
#   TL(0,0)   TC(100,0)   TR(200,0)
#   ML(0,100) C (100,100) MR(200,100)
#   BL(0,200) BC(100,200) BR(200,200)
# ---------------------------------------------------------------------

# s1: dian at top-left (ML 0.976, 0.099 -> C 0.321, 0.38)
S1_HEAD = (0 + 97.6, 100 + 9.9)      # (97.6, 109.9)
S1_TAIL = (100 + 32.1, 100 + 38.0)   # (132.1, 138.0)

# s2: pie, upper-right down to lower-left (C 0.723, 0.017 -> BL 0.416, 0.842)
S2_HEAD = (100 + 72.3, 100 + 1.7)    # (172.3, 101.7)
S2_TAIL = (0 + 41.6, 200 + 84.2)     # (41.6, 284.2)

# s3: na, middle-left down to lower-right (ML 0.712, 0.635 -> BR 0.78, 0.912)
S3_HEAD = (0 + 71.2, 100 + 63.5)     # (71.2, 163.5)
S3_TAIL = (200 + 78.0, 200 + 91.2)   # (278.0, 291.2)

# ---------------------------------------------------------------------
# SELF_CHECK — filled in after first render inspection
# ---------------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 3 strokes matches expected
    'endpoint_mismatches': [],     # anchors used as MMH-provided
    'joint_class_mismatches': [],  # s2 & s3 cross geometrically -> P (piercing)
    'overall_pass': True,
    'notes': ('s1 dian slopes down-right per MMH; s2/s3 intersect near '
              '(111, 188) — inside BC neighborhood — welded crossing.'),
}


def render(path: str) -> None:
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1 — dian (short down-right dot)
    draw_dian(d, S1_HEAD, S1_TAIL,
              w_head=2, w_tail=6, bow=2, steps=48)

    # s2 — pie (long down-left sweep). Bow to the right of head->tail
    # (image coords) gives the classic pie curvature.
    draw_pie(d, S2_HEAD, S2_TAIL,
             bow_perp=14, w_head=8, w_tail=3, steps=80)

    # s3 — na (long down-right thickening). Thin at head, thick at tail.
    draw_na(d, S3_HEAD, S3_TAIL,
            bow_perp=12, w_head=4, w_tail=10, steps=80)

    img.save(path)


if __name__ == "__main__":
    out = str(pathlib.Path(__file__).with_name("01_义.png"))
    render(out)
    print(f"wrote {out}")
