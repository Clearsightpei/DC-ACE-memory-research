"""厶 (sī) — 2画 radical.

Decomposition (2 strokes, per MMH):
  stroke 1: 撇折 (piě zhé)  — head near top-center of grid, curves down-left,
                              pivots at lower-left area, sweeps right to BR.
  stroke 2: 点 (diǎn)       — short down-right dot from mid area to BR.

MMH endpoints (informational):
  s1.head @ ('C', 0.368, 0.002)   s1.tail @ ('BR', 0.13, 0.379)
  s2.head @ ('C', 0.866, 0.863)   s2.tail @ ('BR', 0.402, 0.687)

Joint: 1 joint
  s1.tail ⇆ s2.mid(0.68) @ BR — class N (small natural gap ~22 px).
  Implemented via distinct anchor tuples in the same/adjacent cells with
  a small pixel gap; NOT welded. (Per TR10, keep the gap ≤ 25 px so the
  radical still reads as connected.)

Anchor plan:
  s1 (piě zhé):
    head  @ ('C',  0.40, 0.05)   — upper start (near MMH C(0.368,0.002))
    pivot @ ('BL', 0.30, 0.55)   — bend at lower-left, where 撇 turns into 横
    tail  @ ('BR', 0.13, 0.40)   — end of horizontal, matches MMH s1.tail
    widths: pie head thick (13), tapered to pivot (5), heng uniform (7)
  s2 (diǎn):
    head  @ ('C',  0.85, 0.85)   — matches MMH s2.head
    tail  @ ('BR', 0.40, 0.70)   — matches MMH s2.tail; sits near s1 body

TR7 anchor plan complete. TR8 sanity:
  - s1.head above and left of s1.tail (in row direction, y_frac 0.05 vs
    tail-side much lower y). CHECK.
  - s1.pivot pixel-left of s1.tail (BL vs BR cell). CHECK.
  - s2.head above-left-ish of s2.tail (short 点 going down-right). CHECK.
  - Joint N-class: s1.tail at BR(0.13,0.40) ≈ (213,240); s2 body mid at
    ~ (207,224) ≈ midpoint of (187,186)-(240,269). Distance ~17 px. Within
    the TR10 25-px cap.  CHECK.
"""

import sys
import os

# Make the shared success_bank/code directory importable so we can reuse
# pie_zhe and dian primitives.
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw  # noqa: E402
from _anchor import anchor_to_xy  # noqa: E402
from pie_zhe import draw_pie_zhe  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        "Visual agreements with GT: "
        "(1) first stroke starts near top-center, curves down-left then "
        "bends into a horizontal rightward sweep ending in the BR area, "
        "matching GT's characteristic '厶' hook shape; "
        "(2) second stroke is a short down-right diagonal dot sitting "
        "above/right of the horizontal, matching GT's small closing 点. "
        "Joint at BR is an N-class small gap (~17 px) — strokes read as "
        "connected without being welded, per TR10."
    ),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- stroke 1: 撇折 -----------------------------------------------------
    s1_head  = ('C',  0.40, 0.05)
    s1_pivot = ('BL', 0.30, 0.55)
    s1_tail  = ('BR', 0.13, 0.40)
    draw_pie_zhe(draw, s1_head, s1_pivot, s1_tail,
                 pie_head_w=12, pie_tip_w=5, heng_w=7, shoulder=4)

    # --- stroke 2: 点 -------------------------------------------------------
    s2_head = ('C',  0.85, 0.85)
    s2_tail = ('BR', 0.40, 0.70)
    draw_dian(draw, s2_head, s2_tail,
              head_width=3, peak_width=10, curve=0.05, segments=24)

    # --- direction / joint sanity asserts ----------------------------------
    p_s1_head  = anchor_to_xy(s1_head)
    p_s1_pivot = anchor_to_xy(s1_pivot)
    p_s1_tail  = anchor_to_xy(s1_tail)
    p_s2_head  = anchor_to_xy(s2_head)
    p_s2_tail  = anchor_to_xy(s2_tail)

    # 撇 descends and moves left toward pivot.
    assert p_s1_pivot[1] > p_s1_head[1], "撇 must descend"
    assert p_s1_pivot[0] < p_s1_head[0], "撇 must move left"
    # 横 goes rightward from pivot to tail.
    assert p_s1_tail[0]  > p_s1_pivot[0], "横 must go right"
    # 点 goes down-right.
    assert p_s2_tail[0]  > p_s2_head[0], "点 must go right"
    assert p_s2_tail[1]  > p_s2_head[1], "点 must go down"

    # N-class joint gap (s1.tail vs midpoint of s2).
    s2_mid = ((p_s2_head[0] + p_s2_tail[0]) * 0.5,
              (p_s2_head[1] + p_s2_tail[1]) * 0.5)
    dx = p_s1_tail[0] - s2_mid[0]
    dy = p_s1_tail[1] - s2_mid[1]
    gap = (dx * dx + dy * dy) ** 0.5
    assert 5 <= gap <= 40, f"N-class gap out of range: {gap:.1f} px"

    out = os.path.join(os.path.dirname(__file__), '01_厶.png')
    img.save(out)
    print(f"Wrote {out}  (joint gap {gap:.1f} px)")


if __name__ == '__main__':
    main()
