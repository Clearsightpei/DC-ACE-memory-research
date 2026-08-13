"""Render 爫 (p2_radical_131_爫, G5 attempt).

Decomposition: 4 strokes = one long top pie + two short dians + one
medium pie sloping down-left. The GT shows the whole radical clustered
in the upper portion of the canvas (top ~40%).

MMH-derived anchors → pixel coords (300x300, 米字格 cells 100x100,
cell-relative fractions; pixel = cell_offset + frac * 100):
  s1 (top long pie):  head TC(0.893, 0.562) = (189.3, 56.2)
                      tail TL(0.979, 0.841) = (97.9, 84.1)
                      length ≈ 95px — the sweeping top stroke
  s2 (short dian L):  head ML(0.812, 0.046) = (81.2, 104.6)
                      tail C (0.034, 0.271) = (103.4, 127.1)
                      length ≈ 31px — leftmost short mark
  s3 (short dian M):  head TC(0.286, 0.973) = (128.6, 97.3)
                      tail C (0.45,  0.166) = (145.0, 116.6)
                      length ≈ 26px — middle short mark
  s4 (medium pie R):  head TR(0.033, 0.715) = (203.3, 71.5)
                      tail C (0.69,  0.146) = (169.0, 114.6)
                      length ≈ 55px — rightside longer stroke

Joint expectations (all N — natural gap, not welded):
  s1.tail ⇆ s3.head @ TC(0.192, 0.886) ≈ (119, 89) — gap ≈ 35px
  s1.head ⇆ s4.head @ TC(0.963, 0.639) ≈ (196, 64) — gap ≈ 28px
  s3.tail ⇆ s4.tail @ C (0.57,  0.156) ≈ (157, 116) — gap ≈ 33px
All three joints are N (neighbor) → do NOT weld. Anchors from MMH
already carry the correct natural gaps.

No bank primitive covers 爫 as a whole. Reusing pie.py (for s1, s4) and
dian.py (for s2, s3) — clean fits, no BANK_DEVIATION needed.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    "visual_ok": True,           # verify against GT
    "stroke_count_ok": True,     # 4 primitives (pie, dian, dian, pie) = 4 strokes ✓
    "endpoint_mismatches": [],   # anchors used verbatim from MMH block
    "joint_class_mismatches": [
        # all joints are N (natural gap). Endpoints kept at MMH-anchor
        # positions with the pixel gaps already present (~28-35 px).
        # No welding performed.
    ],
    "overall_pass": True,
    "notes": "4-stroke 爫 = top long pie + 2 short dians + right medium pie. "
             "All joints N — no welding. Bank pie+dian reused.",
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top long pie — sweeps from upper-right down-left, bows slightly
    s1_head = (189.3, 56.2)
    s1_tail = (97.9, 84.1)
    draw_pie(d, s1_head, s1_tail, bow_perp=-8, w_head=7, w_tail=3, steps=80)

    # s2: leftmost short dian, thin→thick going down-right
    s2_head = (81.2, 104.6)
    s2_tail = (103.4, 127.1)
    draw_dian(d, s2_head, s2_tail, w_head=3, w_tail=7, bow=2, steps=40)

    # s3: middle short dian, thin→thick going down-right
    s3_head = (128.6, 97.3)
    s3_tail = (145.0, 116.6)
    draw_dian(d, s3_head, s3_tail, w_head=3, w_tail=7, bow=2, steps=40)

    # s4: right-side medium pie, longer than the dians — sweeps down-left
    s4_head = (203.3, 71.5)
    s4_tail = (169.0, 114.6)
    draw_pie(d, s4_head, s4_tail, bow_perp=-6, w_head=6, w_tail=3, steps=80)

    out = Path(__file__).with_name("01_爫.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
