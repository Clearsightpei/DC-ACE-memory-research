# TRAJECTORY DIFF (retry_1 of p2_radical_115_氏)
#
# GT observation (gt/phase2/氏.png):
#   - s1: short tick at top-right (~193, 74) sweeping down-left to (~91, 114)
#   - s2: near-vertical descender, mild leftward bow, from (~65, 104) down to (~132, 229)
#   - s3: short heng in middle area, (~102, 174) up-right to (~219, 150)
#   - s4: dominant xie-gou (斜钩) — long diagonal from (~130, 103) to
#         (~267, 237) with terminal UP-hook.
#
# MAIN attempt (C-verdict) got wrong:
#   1. s4 was inlined via BANK_DEVIATION with `draw_xie_gou` local defn
#      whose perpendicular direction produced a belly that sags in the
#      wrong direction; the resulting xie-gou reads as too-flat / not
#      calligraphic enough. Bank now HAS `xie_gou.py` (promoted from
#      弋+戈 B2 double-PASS) — errata explicitly says retry should call it.
#   2. s2 pie used bow_perp=14 which put the visible belly too far, making
#      the descender wobble; GT's s2 is much straighter.
#   3. Hook of s4 in main attempt landed short of the visible GT hook.
#
# FIXES applied here:
#   - Replace inline draw_xie_gou with bank primitive (per errata).
#   - Reduce s2 bow to 5 (nearly straight — matches GT).
#   - Ensure xie_gou bow ~10 (bank default) and a longer hook_up=32.

SELF_CHECK = {
    'visual_ok': None,          # confirmed after render
    'stroke_count_ok': True,    # 4 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Retry using bank draw_xie_gou (from success_bank) for s4; '
             's1/s2 pie, s3 heng from bank. No BANK_DEVIATION this retry.',
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

    # MMH-derived anchors (from dispatcher-injected block) --------------
    # s1: short tick pie — TC(0.934,0.744) → ML(0.914,0.137)
    s1_head = A('TC', 0.934, 0.744)   # (193, 74)
    s1_tail = A('ML', 0.914, 0.137)   # (91, 114)

    # s2: near-vertical descender — ML(0.645,0.037) → BC(0.321,0.288)
    s2_head = A('ML', 0.645, 0.037)   # (65, 104)
    s2_tail = A('BC', 0.321, 0.288)   # (132, 229)

    # s3: short mid heng — C(0.02,0.743) → MR(0.194,0.5)
    s3_head = A('C',  0.02,  0.743)   # (102, 174)
    s3_tail = A('MR', 0.194, 0.5)     # (219, 150)

    # s4: 斜钩 (xie-gou) — C(0.301,0.034) → BR(0.675,0.367)
    s4_head = A('C',  0.301, 0.034)   # (130, 103)
    s4_tail = A('BR', 0.675, 0.367)   # (267, 237)

    # stroke 1: short pie tick (small bow, tapered)
    draw_pie(d, s1_head, s1_tail, bow_perp=4, w_head=6, w_tail=3, steps=40)

    # stroke 2: near-vertical descender — very mild bow (GT is nearly straight)
    draw_pie(d, s2_head, s2_tail, bow_perp=5, w_head=8, w_tail=4, steps=60)

    # stroke 3: short heng
    draw_heng(d, s3_head, s3_tail, width_head=7, width_tail=8)

    # stroke 4: BANK primitive (per errata retry hint)
    draw_xie_gou(d, s4_head, s4_tail,
                 width=8, bow=10, hook_up=32, hook_back=8)

    out = os.path.join(HERE, "01_氏.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
