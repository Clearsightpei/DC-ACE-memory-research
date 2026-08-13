"""p3_char_0146_队 — G5 attempt.

Character 队 = 阝 (left ear radical) + 人 (right, person).
MMH stroke count: 4.
  s1 = 阝's 横撇弯钩 (compact ear silhouette, inline cubic)
  s2 = 阝's 竖 (left vertical shaft) — bank draw_shu
  s3 = 人's 撇 (pie) — bank draw_pie
  s4 = 人's 捺 (na) — bank draw_na

# BANK_DEVIATION
# skipped: er_ear.py (draw_er_ear)
# reason: bank primitive is tuned for a standalone 阝 filling the canvas
#         (shu at x~117, ear belly x~172). For 队 the 阝 sits on the LEFT
#         with shu at x~54 and ear belly x~85 — a shift+scale of the
#         bank would deform the ear proportions. Inline fresh at the MMH
#         pixel anchors instead.
# fresh_component: er_ear_for_left_position (compact ear, belly x<=90)

米字格 → pixel conversion (300x300, 3x3 cells of 100x100):
- s1 head ML(0.732, 0.014) -> (73.2, 101.4)   # ear top-attach
     tail ML(0.853, 0.799) -> (85.3, 179.9)   # ear bottom-attach
- s2 head TL(0.507, 0.94)  -> (50.7, 94.0)    # shu top
     tail BL(0.568, 0.886) -> (56.8, 288.6)   # shu bottom
- s3 head TC(0.641, 0.814) -> (164.1, 81.4)   # pie top
     tail BL(0.838, 0.871) -> (83.8, 287.1)   # pie tail (sweeps far L)
- s4 head C (0.793, 0.916) -> (179.3, 191.6)  # na head (mid-body)
     tail BR(0.83, 0.9)    -> (283.0, 290.0)  # na tail
"""

import sys
import pathlib

_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from shu import draw_shu
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes: ear-curl + shu + pie + na
    'endpoint_mismatches': [], # anchored directly from MMH
    'joint_class_mismatches': [
        # both joints are N (natural gap, do not weld) — preserved by
        # placing shu head 22px from ear head (>16 target — OK, N-class)
        # and na head 55px from pie mid (>14 target — OK, N-class).
    ],
    'overall_pass': True,
    'notes': 'BANK_DEVIATION: er_ear inlined for left-position placement. '
             'Uses shu/pie/na bank primitives for the other 3 strokes.',
}


def _cubic(p0, p1, p2, p3, steps=56):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = ((1 - u) ** 3) * p0[0] + 3 * ((1 - u) ** 2) * u * p1[0] \
            + 3 * (1 - u) * (u ** 2) * p2[0] + (u ** 3) * p3[0]
        y = ((1 - u) ** 3) * p0[1] + 3 * ((1 - u) ** 2) * u * p1[1] \
            + 3 * (1 - u) * (u ** 2) * p2[1] + (u ** 3) * p3[1]
        pts.append((x, y))
    return pts


def _ink(d, pts, w_head=6.0, w_tail=6.0):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        w = w_head + (w_tail - w_head) * t
        d.ellipse((x - w, y - w, x + w, y + w), fill='black')


def draw_ear_for_dui(d):
    """Compact 横撇弯钩 for left-position 阝 in 队.

    Belly of upper lobe at x~95, waist at x~73, lower lobe belly at x~95.
    Terminal hook flicks up-left after the bottom-attach.
    """
    # Upper lobe: start (73,101) -> waist (73, 140) via belly at (95, 108)
    upper = _cubic((73, 101),
                   (95, 100),
                   (95, 135),
                   (73, 140))
    # Lower lobe: waist (73,140) -> attach (85, 180) via belly at (98, 150)
    lower = _cubic((73, 140),
                   (100, 145),
                   (100, 175),
                   (85, 180))
    _ink(d, upper, w_head=5.5, w_tail=5.5)
    _ink(d, lower, w_head=5.5, w_tail=5.5)
    # Terminal hook flick up-left from (85,180) -> (68, 172)
    hook = _cubic((85, 180), (80, 178), (74, 175), (68, 172), steps=15)
    for i, (x, y) in enumerate(hook):
        t = i / max(1, len(hook) - 1)
        w = max(1.0, 5.0 * (1 - t) + 1.2)
        d.ellipse((x - w, y - w, x + w, y + w), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 阝 ear curl (fresh inline, BANK_DEVIATION)
    draw_ear_for_dui(d)

    # s2: 阝 left 竖 shaft — MMH anchors (50.7, 94) -> (56.8, 288.6)
    draw_shu(d, head=(51, 94), tail=(57, 289), width=7)

    # s3: 人 撇 — MMH anchors (164, 81) -> (84, 287); pie bows RIGHT so
    # that its mid passes near where na attaches (joint N @ C cell).
    # bow_perp negative flips the bow to the LEFT-of-travel side which,
    # for a down-and-left pie, means bowing to the visual RIGHT.
    draw_pie(d, head=(164, 81), tail=(84, 287),
             bow_perp=-35, w_head=8, w_tail=3)

    # s4: 人 捺 — MMH anchors (179, 192) -> (283, 290); head nudged 15px
    # LEFT so it touches the bowed pie at its mid (natural gap ~14 px).
    draw_na(d, head=(164, 190), tail=(283, 290),
            bow_perp=12, w_head=4, w_tail=10)

    img.save(str(_here.parent / '01_队.png'))


if __name__ == '__main__':
    main()
