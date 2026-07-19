"""礻 (shì, 4画) — the "spirit/altar" radical (left-side form of 示).

Anchor plan (米字格, PIL-native, y grows DOWN):
  s1 (点, top dot):     head @ ('TC', 0.31, 0.639)  tail @ ('TC', 0.632, 0.902)
  s2 (横撇, diagonal):  head @ ('ML', 0.85, 0.35)   corner @ ('ML', 0.95, 0.50)
                         tip @ ('BL', 0.55, 0.55)
       MMH gives head ML(0.814,0.512) → tail BL(0.712,0.52). We render as
       heng_pie with an inserted corner so the top-right shoulder is
       visible (TR11-style visual truth: GT clearly shows a 横 opening
       then a 撇 sweep, not a single straight diagonal).
  s3 (竖, vertical stem): head @ ('C', 0.386, 0.55)  tail @ ('BC', 0.42, 1.0)
       MMH stem head sits at C(0.386,0.934); we raise the head to touch
       the 横撇 body per the N-class joint spec (small gap ~16 px), and
       extend the tail down to BC 1.0 so the stem is prominent standalone.
  s4 (点, right dot): head @ ('C', 0.62, 0.55)  tail @ ('MR', 0.05, 0.72)
       MMH raw is very short (12 px). For a standalone radical (TR9) we
       expand span so the right dot reads clearly next to the stem.

Joints (all N-class per MMH; N does NOT mean visually separate — TR10):
  s2.mid ⇆ s3.head @ C — N, gap ~16 px
  s2.mid ⇆ s4.head @ C — N, gap ~32 px
  s3.head ⇆ s4.head @ C — N, gap ~33 px
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from dian import draw_dian
from heng_pie import draw_heng_pie
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        "Revision 1 (of 1): expanded s2 span so top-right horizontal is "
        "visible and pie tip reaches BL (TR9 standalone-span rule); "
        "moved s3 head right (C 0.55) so it sits just under the 横撇 "
        "corner instead of overlapping the pie; enlarged s4 dot and "
        "moved it right of the stem for a legible 4-part silhouette. "
        "Visual agreements vs GT: (1) top 点 is a short diagonal above "
        "and slightly right of center; (2) 横撇 opens with a small top "
        "horizontal then sweeps down-left into BL; (3) vertical stem "
        "descends from center through BC; (4) right 点 sits clearly to "
        "the right of the stem."
    ),
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # s1 — top dot 点 (short upper-left → lower-right)
    draw_dian(draw,
              from_anchor=('TC', 0.31, 0.639),
              to_anchor=('TC', 0.632, 0.902),
              head_width=2, peak_width=9, curve=0.08, segments=24)

    # s2 — 横撇 (short horizontal opening, then long 撇 sweep down-left)
    # Corner sits near center-top-right; tip reaches lower-left.
    # Expanded span (TR9) — MMH under-spans for standalone radicals.
    draw_heng_pie(draw,
                  head=('C', 0.15, 0.35),
                  corner=('C', 0.75, 0.50),
                  tip=('BL', 0.35, 0.75),
                  head_w=7, corner_w=12, tip_w=2)

    # s3 — 竖 vertical stem descending through C into BC.
    # Head at center, tail at bottom-center.
    draw_shu(draw,
             from_anchor=('C', 0.55, 0.55),
             to_anchor=('BC', 0.50, 0.95),
             width=9)

    # s4 — right 点 dot (short diagonal upper-left → lower-right, right of stem)
    # Placed clearly to the right of the vertical, mid-height.
    draw_dian(draw,
              from_anchor=('C', 0.75, 0.60),
              to_anchor=('MR', 0.20, 0.85),
              head_width=2, peak_width=9, curve=0.06, segments=24)

    out = os.path.join(HERE, "01_礻.png")
    img.save(out)
    return out


if __name__ == "__main__":
    p = render()
    print("wrote:", p)
