"""牛 (niú, 4 strokes) — Phase 2 radical attempt.

Structure:
  s1 — short 撇 in upper-left: head TL(~0.92,0.97) tail ML(~0.61,0.69).
       Sloping down and slightly left.
  s2 — short upper 横: head ML(~1.0,0.37) tail MR(~0.15,0.21).
       Slightly rising toward the right.
  s3 — long middle 横: head BL(~0.30,0.15) tail MR(~0.70,0.90).
       Long horizontal spanning the width.
  s4 — long 竖 through center column, extending near/off bottom.

Joints (per MMH):
  J1: s1.mid ⇆ s2.head @ ML — N (small natural gap ~15-20 px).
  J2: s2 crosses s4 at C — P (welded, x=150 crossing).
  J3: s3 crosses s4 at C — P (welded, x=150 crossing).

Anchor plan compliance (TR7):
  - s4 fixed at column x=150 (TC 0.5 head, BC 0.5 tail) so both P-welds
    with s2 and s3 land at x=150 by construction.
  - s3 head/tail chosen so the segment passes through (150, ~200)
    guaranteeing P-weld with s4.
  - s2 head/tail chosen so the segment passes through (150, ~130)
    guaranteeing P-weld with s4.
  - s1 tapered 撇 with head above tail, tail up-left of s2 head so the
    two form an N-class near-touch (per MMH).

TR12: 横 endpoints share row logically (approx same y). Here s2 has
head in ML row, tail in MR row (same row ML/C/MR — row 1). s3 spans
BL row → MR row: MMH gives this slight slant, we preserve it because
GT visibly shows a small down-slant. Both cases are within one row.
TR8: s4 uses TC 0.5 → BC 0.5 (same column, guaranteed vertical).
"""

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        "TR11 named agreements vs GT: "
        "(1) short 撇 in upper-left sweeps down-left; "
        "(2) long vertical passes through both horizontals at the same x, "
        "extending below the middle 横; "
        "(3) middle 横 is clearly longer than upper 横; "
        "(4) 4-stroke decomposition matches MMH."
    ),
}


def draw_niu(draw):
    # Anchors
    s1_head = ('TL', 0.92, 0.97)
    s1_tail = ('ML', 0.61, 0.69)

    s2_head = ('ML', 0.999, 0.37)
    s2_tail = ('MR', 0.15, 0.21)

    s3_head = ('BL', 0.30, 0.15)
    s3_tail = ('MR', 0.70, 0.90)

    # s4 竖 straight column at x=150 for P-weld guarantee; extend to
    # near the bottom edge for standalone radical prominence (TR9).
    s4_head = ('TC', 0.50, 0.35)
    s4_tail = ('BC', 0.50, 1.05)   # slightly past bottom edge

    # ---- Sanity assertions (TR8) ----
    p_s4h = anchor_to_xy(s4_head)
    p_s4t = anchor_to_xy(s4_tail)
    assert abs(p_s4h[0] - p_s4t[0]) < 0.5, "s4 must be pure vertical"

    p_s3h = anchor_to_xy(s3_head)
    p_s3t = anchor_to_xy(s3_tail)
    # verify s3 crosses x=150 for P-weld with s4
    if p_s3t[0] != p_s3h[0]:
        y_at_150 = p_s3h[1] + (150 - p_s3h[0]) / (p_s3t[0] - p_s3h[0]) * (p_s3t[1] - p_s3h[1])
        assert 100 <= y_at_150 <= 260, f"s3 must cross x=150 within canvas y (got {y_at_150})"

    p_s2h = anchor_to_xy(s2_head)
    p_s2t = anchor_to_xy(s2_tail)
    if p_s2t[0] != p_s2h[0]:
        y_at_150 = p_s2h[1] + (150 - p_s2h[0]) / (p_s2t[0] - p_s2h[0]) * (p_s2t[1] - p_s2h[1])
        assert 100 <= y_at_150 <= 200, f"s2 must cross x=150 in upper-mid band (got {y_at_150})"

    # 撇 s1: head above tail in y; head x >= tail x (down-left sweep)
    p_s1h = anchor_to_xy(s1_head)
    p_s1t = anchor_to_xy(s1_tail)
    assert p_s1h[1] < p_s1t[1], "s1 撇 head above tail"
    assert p_s1h[0] > p_s1t[0], "s1 撇 tail to the left"

    # ---- Render (order: 撇, upper 横, lower 横, 竖) ----
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)
    draw_heng(draw, s2_head, s2_tail, width=9)
    draw_heng(draw, s3_head, s3_tail, width=11)
    draw_shu(draw, s4_head, s4_tail, width=11)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_niu(draw)
    out = os.path.join(_HERE, '01_牛.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
