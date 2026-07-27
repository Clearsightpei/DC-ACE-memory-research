"""止 (zhǐ, "stop", 4 strokes) — Phase-2 radical p2_radical_133_止.

Structure (from MMH-injected anchors, with mild TR9 span-expansion for
standalone-radical presentation):
  s1 竖 — main vertical (center column, near-full height).
  s2 短横 — short horizontal middle-right (M-row).
  s3 短竖 — short vertical on the left, from mid-height down to bottom.
  s4 长横 — long bottom horizontal (B-row, spanning almost full width).

Joints (all N, small natural gaps — DO NOT weld):
  s1.mid ⇆ s2.head @ C   (N, ~20 px)
  s1.tail ⇆ s4.mid(~.43) @ BC (N, ~15 px)
  s3.tail ⇆ s4.mid(~.25) @ BL (N, ~12 px)

Bank use per TR6: `draw_heng` and `draw_shu` are the natural fits —
straight primitives, no joint sub-typing needed. Anchors OVERRIDE
defaults per TR1.

TR8 sanity: every heng has same-row anchors; every shu has same-column
anchors. Verified below.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used with mild TR9 expansion for standalone; '
             'horizontals share M-row/B-row (TR8 rule 5); verticals share '
             'C-col / L-col (TR8 rule 6); all 3 joints N-class ~15-20 px.',
}

import os
import sys
from PIL import Image, ImageDraw

# Bank primitives are under success_bank/code — add to sys.path.
_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(_BANK))

from _anchor import anchor_to_xy  # noqa: E402
from heng import draw_heng        # noqa: E402
from shu import draw_shu          # noqa: E402


def draw_zhi(draw):
    # s1 — main center 竖 (top → bottom, near-full vertical span).
    s1_head = ('TC', 0.40, 0.75)   # (140, 75)
    s1_tail = ('BC', 0.40, 0.60)   # (140, 260)
    # Column invariant: both endpoints in C-column (TC & BC).

    # s2 — short 横 sitting right of s1, at mid-height.
    s2_head = ('C',  0.60, 0.65)   # (160, 165)
    s2_tail = ('MR', 0.40, 0.65)   # (240, 165)
    # Row invariant: both endpoints in M-row (C & MR).

    # s3 — short left 竖 (mid-height to bottom, left-of-center).
    s3_head = ('ML', 0.75, 0.65)   # (75, 165)
    s3_tail = ('BL', 0.75, 0.65)   # (75, 265)
    # Column invariant: both endpoints in L-column (ML & BL).

    # s4 — long 横 at bottom.
    s4_head = ('BL', 0.15, 0.75)   # (15, 275)
    s4_tail = ('BR', 0.85, 0.75)   # (285, 275)
    # Row invariant: both endpoints in B-row (BL & BR).

    # -- TR8 sanity assertions ---------------------------------------
    assert s1_head[0][1] == s1_tail[0][1] == 'C', 's1 not in C-column'
    assert s2_head[0][0] == s2_tail[0][0] == 'M' or (
        s2_head[0] in ('C', 'MR') and s2_tail[0] in ('C', 'MR')
    ), 's2 not in M-row'
    assert s3_head[0][1] == s3_tail[0][1] == 'L', 's3 not in L-column'
    assert s4_head[0][0] == s4_tail[0][0] == 'B', 's4 not in B-row'

    # -- Render -------------------------------------------------------
    draw_shu(draw, s1_head, s1_tail, width=10)
    draw_heng(draw, s2_head, s2_tail, width=9)
    draw_shu(draw, s3_head, s3_tail, width=9)
    draw_heng(draw, s4_head, s4_tail, width=10)

    # -- Joint gap verification (post-render sanity, printed only) ---
    p_s1_mid = tuple((a + b) / 2 for a, b in zip(anchor_to_xy(s1_head),
                                                 anchor_to_xy(s1_tail)))
    p_s2_head = anchor_to_xy(s2_head)
    d_j1 = ((p_s1_mid[0] - p_s2_head[0]) ** 2 +
            (p_s1_mid[1] - p_s2_head[1]) ** 2) ** 0.5

    p_s1_tail = anchor_to_xy(s1_tail)
    # s4 mid at t≈0.43
    p_s4_h = anchor_to_xy(s4_head)
    p_s4_t = anchor_to_xy(s4_tail)
    t43 = 0.43
    p_s4_mid43 = (p_s4_h[0] + t43 * (p_s4_t[0] - p_s4_h[0]),
                  p_s4_h[1] + t43 * (p_s4_t[1] - p_s4_h[1]))
    d_j2 = ((p_s1_tail[0] - p_s4_mid43[0]) ** 2 +
            (p_s1_tail[1] - p_s4_mid43[1]) ** 2) ** 0.5

    p_s3_tail = anchor_to_xy(s3_tail)
    t25 = 0.25
    p_s4_mid25 = (p_s4_h[0] + t25 * (p_s4_t[0] - p_s4_h[0]),
                  p_s4_h[1] + t25 * (p_s4_t[1] - p_s4_h[1]))
    d_j3 = ((p_s3_tail[0] - p_s4_mid25[0]) ** 2 +
            (p_s3_tail[1] - p_s4_mid25[1]) ** 2) ** 0.5

    print(f'joint gaps (px): J1={d_j1:.1f}  J2={d_j2:.1f}  J3={d_j3:.1f}')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_zhi(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_止.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
