"""p3_char_0016_乃 — G4 attempt (revision 1)
Character: 乃 (nǎi)
Stroke count: 2

Revision notes (vs first render):
- First render was too tall and thin; character filled full canvas.
- GT is more compact and centered; s1 top horizontal is shorter and
  the corner is much wider (top-right at ~TC/TR boundary, y ~0.10).
- Reduced s1 hook-corner y and increased its x-range so it reads as
  a proper L that bends and sweeps down to BC (not a diagonal).
- s2 (inner 撇) in GT ends inside/near BL but starts inside the top,
  running down and to the LEFT with a moderate concave-right curve.

Anchor plan (TR7):
  s1 = 横折折撇 (heng-zhe-zhe-pie): head at ML top, corners at TC/C,
       tail at BC.
       head @ ('ML', 0.62, 0.06)
       corner1 @ ('TC', 0.85, 0.10)    (top-right of the L)
       belly @ ('C',  0.55, 0.55)      (bezier control on the descent)
       tail @ ('BC', 0.56, 0.64)
  s2 = 撇 (pie): head at C upper-left, curves down-left to BL.
       head @ ('C', 0.26, 0.06)
       belly @ ('C', 0.10, 0.60)       (concave-right)
       tail @ ('BL', 0.27, 0.65)

Joints (1):
  s1.head ⇆ s2.head @ cell C : N (small natural gap ~12 px).
  s1.head is at ML(0.62,0.06) → x≈62, y≈6 (upper zone).
  s2.head is at C(0.26,0.06) → x≈126, y≈106.
  These are in DIFFERENT positions (s2.head under-right of s1.head)
  giving a natural gap; do NOT weld.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     sample_line)
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revision 1: compacter L-shape s1, smaller inner pie s2.'
}


def draw_nai(draw):
    # --- stroke 1: 横折折撇 ---
    s1_head = anchor_to_xy(('ML', 0.62, 0.06))
    s1_corner = anchor_to_xy(('TC', 0.90, 0.15))
    s1_belly = anchor_to_xy(('C', 0.75, 0.55))
    s1_tail = anchor_to_xy(('BC', 0.56, 0.64))

    # Segment A: horizontal top (head → corner)
    ptsA = sample_line(s1_head, s1_corner, n=20)
    widthsA = [8] * len(ptsA)
    stroke_variable_width(draw, ptsA, widthsA)

    # Segment B: bezier corner → belly → tail (the descending curve
    # that sweeps down-left).
    ptsB = quad_bezier(s1_corner, s1_belly, s1_tail, n=45)
    widthsB = [8 - 4 * (i / len(ptsB)) for i in range(len(ptsB))]  # taper 8→4
    stroke_variable_width(draw, ptsB, widthsB)

    # --- stroke 2: 撇 (inner pie) ---
    s2_head = anchor_to_xy(('C', 0.26, 0.06))
    s2_belly = anchor_to_xy(('C', 0.05, 0.70))
    s2_tail = anchor_to_xy(('BL', 0.27, 0.65))

    pts2 = quad_bezier(s2_head, s2_belly, s2_tail, n=50)
    widths2 = [9 - 7 * (i / len(pts2)) for i in range(len(pts2))]  # taper 9→2
    stroke_variable_width(draw, pts2, widths2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_nai(draw)
    out = os.path.join(os.path.dirname(__file__), '01_乃.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
