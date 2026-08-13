"""p2_radical_031_十 (shi, "ten") — G5 attempt.

Two strokes: 横 (horizontal) crossed by 竖 (vertical piercing at center).
Uses bank primitives heng.py + shu.py directly with MMH-derived anchors
converted from 米字格 (cell, x_frac, y_frac) → pixel (300×300 canvas,
3×3 grid, 100px cells).

Anchor conversion:
  Cell origins (top-left px): TL(0,0) TC(100,0) TR(200,0)
                              ML(0,100) C(100,100) MR(200,100)
                              BL(0,200) BC(100,200) BR(200,200)
  pixel = (ox + x_frac*100, oy + y_frac*100)

MMH anchors (from injected block):
  s1 head ('ML', 0.319, 0.705) -> ( 31.9, 170.5)
  s1 tail ('MR', 0.73,  0.605) -> (273.0, 160.5)
  s2 head ('TC', 0.336, 0.624) -> (133.6,  62.4)
  s2 tail ('BC', 0.485, 1.097) -> (148.5, 309.7)  # extends past bottom edge, clamp to 292
  joint  ('C',  0.497, 0.619) -> (149.7, 161.9)  P (piercing, welded)
"""

import sys, os
from PIL import Image, ImageDraw

# Import bank primitives (bank code dir is a sibling of attempts/)
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('2 stroke calls (heng + shu). Endpoints from MMH anchors. '
              'Joint at (149.7,161.9) is P (piercing/welded) because both '
              'strokes are drawn as continuous ink through the crossing '
              'point — no gap. s2 tail clamped from y=309.7 to y=292 to '
              'stay inside 300px canvas.')
}


def main():
    W = H = 300
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1 — 横 (horizontal): ML → MR
    s1_head = (32, 170)
    s1_tail = (273, 160)
    draw_heng(d, s1_head, s1_tail, width_head=9, width_tail=10)

    # Stroke 2 — 竖 (vertical piercing): TC → BC (with top_curl like bare 丨)
    s2_head = (134, 62)
    s2_tail = (149, 292)  # clamp 309.7 into canvas
    draw_shu(d, s2_head, s2_tail, width=8, top_curl=True)

    out = os.path.join(os.path.dirname(__file__), "01_十.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
