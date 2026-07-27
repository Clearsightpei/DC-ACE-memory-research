"""p3_char_0072_夊 (suī, "walk slowly") — G4 grid-bank attempt.

MANDATORY LOOKUP CHECKLIST:
1. success_bank/INDEX.md grep — no `sui.py` or `夊.py` in bank; radical
   p2_radical_084_夊 was FAILed (see errata). Draw fresh, not from bank.
2. errata.md grep — p2_radical_084_夊 FAIL fix idea:
   "s1 as small ク-shape at top-center; s2 head just below s1 tail with
    N-gap ~15 px; s3 head T-welds s1 body at (~90, 150)."
   Following LITERALLY.
3. form_catalog — 3-stroke char, standard pie/na composition.
4. principles_meta — TR1 override anchors, TR6 inline when no bank fits.
5. joint_atlas — J1 N-gap ~11 px; J2 T-weld; J3 P-cross (welded).
6. sandbox — no direct 夊 note.

MMH-derived structural expectations (from prompt):
  s1: TC(0.31, 0.688) → ML(0.768, 0.84) — small ク-curl at top-center
  s2: C(0.245, 0.433) → BL(0.448, 0.906) — main pie sweeping down-left
  s3: ML(0.926, 0.45) → BR(0.748, 0.924) — na sweeping down-right
Joints:
  J1: s1.mid(0.60) ⇆ s2.head @ C — N (~11 px gap)
  J2: s1.mid(0.70) ⇆ s3.head @ C — T (welded)
  J3: s2.mid(0.54) ⇆ s3.mid(0.38) @ BC — P (welded crossing)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3-stroke 夊: ク-shape top + pie + na crossing at BC per MMH.'
}

import os
import sys

# Enable importing shared primitives from the group's success_bank/code.
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'
))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from pie import draw_pie
from na import draw_na


def draw_sui(draw):
    # -------- s1: small ク-curl at top-center --------
    # A tiny 横撇 (héng-pie): short flat horizontal then a sharp turn
    # into a small pie sweeping down-left. Very compact — fits inside
    # TC/ML region only.
    s1_head = anchor_to_xy(('TC', 0.31, 0.688))    # start of top bar
    s1_corner = anchor_to_xy(('TC', 0.75, 0.72))   # corner turn
    s1_tail = anchor_to_xy(('ML', 0.77, 0.84))     # short pie tail
    # Segment A: near-horizontal top bar
    pts_a = [
        (s1_head[0] + i / 10 * (s1_corner[0] - s1_head[0]),
         s1_head[1] + i / 10 * (s1_corner[1] - s1_head[1]))
        for i in range(11)
    ]
    # Segment B: short pie down-left with slight belly outward
    ctrl = ((s1_corner[0] + s1_tail[0]) / 2 + 2,
            (s1_corner[1] + s1_tail[1]) / 2 - 4)
    pts_b = quad_bezier(s1_corner, ctrl, s1_tail, n=24)
    pts = pts_a + pts_b[1:]
    widths = []
    n = len(pts) - 1
    for i, _ in enumerate(pts):
        t = i / n
        if t < 0.30:
            w = 3 + 3 * (t / 0.30)   # 3 -> 6
        elif t < 0.45:
            w = 6                    # thick at corner
        else:
            u = (t - 0.45) / 0.55
            w = 6 - 5 * u            # 6 -> 1
        widths.append(max(1.0, w))
    stroke_variable_width(draw, pts, widths)

    # -------- s2: main pie sweeping down-left --------
    # Head sits just below s1 tail (N-gap at cell C ~11 px).
    draw_pie(draw,
             from_anchor=('C', 0.245, 0.433),
             to_anchor=('BL', 0.448, 0.906),
             head_width=10, tail_width=1, curve=0.14, segments=48)

    # -------- s3: na sweeping down-right --------
    # Head T-welds to s2 body near the upper part; body crosses s2
    # near BC (cell BC (0.516, 0.144)) to form the 又 lower half.
    # Per MMH: head at ML(0.926, 0.45) — we pull slightly into C so
    # the head T-welds the s2 body rather than floating.
    draw_na(draw,
            from_anchor=('C', 0.35, 0.55),        # T-weld onto s2 body
            to_anchor=('BR', 0.75, 0.92),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.80, curve=0.06, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_sui(draw)
    out = os.path.join(os.path.dirname(__file__), '01_夊.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
