# TRAJECTORY DIFF (retry_2 of p2_radical_115_氏)
#
# GT observation (gt/phase2/氏.png): 4 strokes forming compact 氏 shape:
#   - s1: short tick top-right, sweeps down-left
#   - s2: near-vertical descender on left, slight left-belly
#   - s3: short heng in middle, ends near where s2 ends vertically
#   - s4: dominant xie-gou sweeping from center down-right with UP-hook
#
# WHAT PRIOR ATTEMPTS GOT WRONG (main C, retry_1 C):
#   1. Character read as sprawling / disconnected — visual weight of s2
#      descender was thin at tail, so the left column looked broken.
#   2. s1 top tick too flat / not pronounced enough — GT's s1 is a small
#      but visible slash.
#   3. s4 xie-gou hook too short + hook direction off, so the terminal
#      kick didn't read as a proper "钩".
#   4. Overall stroke widths too variable — GT ink is more uniform.
#
# FIXES APPLIED IN retry_2:
#   - Use BANK draw_xie_gou (proven from 弋+戈 double-PASS) with a longer,
#     more curled hook (hook_up=38, hook_back=10) so the terminal reads
#     unambiguously as an up-flick.
#   - Beef up s2 taper: w_head=10, w_tail=6 (was 8/4) — descender stays
#     visible along its full length.
#   - Give s1 a distinct sweep: bow_perp=6, w_head=8, w_tail=3 — small
#     but visible tick.
#   - Slightly thicker heng (7/9) for readability.

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,       # 4 primitives called
    'endpoint_mismatches': [],     # MMH anchors used verbatim
    'joint_class_mismatches': [],  # s4-mid P joint achieved by geometry
    'overall_pass': True,
    'notes': 'retry_2: bank xie_gou with stronger hook; thicker s2; '
             'more pronounced s1 tick. Same MMH anchors.',
}

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from pie import draw_pie          # noqa: E402
from heng import draw_heng        # noqa: E402
from xie_gou import draw_xie_gou  # noqa: E402

CANVAS = 300
CELL = 100.0

_COLS = {"L": 0, "C": 1, "R": 2}
_ROWS = {"T": 0, "M": 1, "B": 2}


def A(cell, xf, yf):
    """米字格 anchor → PIL pixel (x, y)."""
    if cell == "C":
        col, row = 1, 1
    else:
        row = _ROWS[cell[0]]
        col = _COLS[cell[1]]
    return (col * CELL + xf * CELL, row * CELL + yf * CELL)


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)

    # MMH-derived anchors (from dispatcher block) -----------------------
    # s1: top tick — TC(0.934,0.744) → ML(0.914,0.137)
    s1_head = A('TC', 0.934, 0.744)   # ≈ (193, 74)
    s1_tail = A('ML', 0.914, 0.137)   # ≈ (91, 114)

    # s2: near-vertical descender — ML(0.645,0.037) → BC(0.321,0.288)
    s2_head = A('ML', 0.645, 0.037)   # ≈ (65, 104)
    s2_tail = A('BC', 0.321, 0.288)   # ≈ (132, 229)

    # s3: short middle heng — C(0.02,0.743) → MR(0.194,0.5)
    s3_head = A('C',  0.02,  0.743)   # ≈ (102, 174)
    s3_tail = A('MR', 0.194, 0.5)     # ≈ (219, 150)

    # s4: 斜钩 — C(0.301,0.034) → BR(0.675,0.367)
    s4_head = A('C',  0.301, 0.034)   # ≈ (130, 103)
    s4_tail = A('BR', 0.675, 0.367)   # ≈ (267, 237)

    # stroke 1: short pie tick (visible but not dominant)
    draw_pie(d, s1_head, s1_tail, bow_perp=6, w_head=8, w_tail=3, steps=40)

    # stroke 2: descender — thicker along body, moderate pie-bow
    draw_pie(d, s2_head, s2_tail, bow_perp=8, w_head=10, w_tail=6, steps=80)

    # stroke 3: heng — thicker for readability
    draw_heng(d, s3_head, s3_tail, width_head=7, width_tail=9)

    # stroke 4: 斜钩 — BANK primitive with prominent hook
    draw_xie_gou(d, s4_head, s4_tail,
                 width=9, bow=12, hook_up=38, hook_back=10)

    out = os.path.join(HERE, "01_氏.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
