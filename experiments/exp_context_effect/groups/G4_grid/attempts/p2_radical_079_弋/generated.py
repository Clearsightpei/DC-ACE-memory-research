"""p2_radical_079_弋 (yì, 3画) — G4 grid-bank attempt.

Composition: 提 (s1) + 斜钩 (s2) + 点 (s3).

Anchor plan (米字格, PIL-native — y grows DOWN):
  s1 (提/short 横): head=('ML', 0.48, 0.764), tail=('MR', 0.095, 0.38)
      — both endpoints in cell ROW 1 (ML, MR) → TR12 row-match OK.
      Left-lower to right-upper diagonal (slight rise) — MMH shape.
  s2 (斜钩): head=('TC', 0.02, 0.806) [px ~102,80],
             belly=('C', 0.42, 0.531) [P-cross weld target, px ~142,159],
             hook_pt=('BR', 0.581, 0.347) [px ~258,234],
             tip=('BR', 0.62, 0.15) [short UP-flick, tip.y < hook_pt.y].
      Uses draw_xie_gou primitive. Body bows down-left through belly,
      hook flicks UP at bottom-right.
  s3 (点): head=('TC', 0.822, 0.694), tail=('TR', 0.183, 0.97)
      — both endpoints in cell ROW 0 (TC, TR). Small diagonal dot
      in upper-right region.

Joints (1):
  s1.mid ⇆ s2.mid @ C(0.418, 0.531) — P (welded crossing).
  s2 belly deliberately placed AT the P-cross pixel so the curve
  passes through it. s1 midpoint sits ~13 px left of P-cross; we
  add a small 顿笔 disc at P-cross to visually cement the weld
  (per principle_bank compound-joint convention).

Sanity: TR12 row-match for s1 (both ML/MR = row 1) and s3 (both TC/TR
= row 0). Direction assert: p_tip.y < p_hook.y for xie_gou UP flick.
"""
import os
import sys
from PIL import Image, ImageDraw

SB = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(SB))

from _anchor import anchor_to_xy  # noqa: E402
from heng import draw_heng        # noqa: E402  (used for s1 提/short-横)
from xie_gou import draw_xie_gou  # noqa: E402
from dian import draw_dian        # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('First pass. TR11 named agreements vs GT: '
              '(1) both have a long diagonal 斜钩 sweep from upper-'
              'mid down to lower-right with a small up-flick; '
              '(2) both have a short horizontal-ish stroke crossing '
              'that 斜钩 through the middle band; '
              '(3) both have a small 点 tucked into the upper-right '
              'region above the crossing. Stroke count = 3 = MMH. '
              'P-weld handled via belly-through-P_cross + disc.')
}


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ---- Anchors (MMH-derived, verbatim endpoints) ----
    s1_head = ('ML', 0.48, 0.764)
    s1_tail = ('MR', 0.095, 0.38)

    s2_head = ('TC', 0.02, 0.806)
    s2_belly = ('C', 0.42, 0.531)          # = P-cross point
    s2_hook_pt = ('BR', 0.581, 0.347)
    s2_tip = ('BR', 0.62, 0.15)            # short UP flick

    s3_head = ('TC', 0.822, 0.694)
    s3_tail = ('TR', 0.183, 0.97)

    # ---- Direction / sanity asserts ----
    p_hook = anchor_to_xy(s2_hook_pt)
    p_tip = anchor_to_xy(s2_tip)
    assert p_tip[1] < p_hook[1], "xie_gou hook must flick UP"
    assert p_tip[0] > p_hook[0] - 5, "hook_pt→tip should not swing far left"

    # TR12 row assertions (rows: T*=0, M*=1, B*=2)
    def row(cell):
        return {'TL': 0, 'TC': 0, 'TR': 0,
                'ML': 1, 'C': 1, 'MR': 1,
                'BL': 2, 'BC': 2, 'BR': 2}[cell]
    assert row(s1_head[0]) == row(s1_tail[0]), \
        "s1 (提/横) endpoints must share cell row"
    assert row(s3_head[0]) == row(s3_tail[0]), \
        "s3 (点) endpoints must share cell row"

    # ---- Render ----
    # s2 first so s1 (crossing 提) sits on top at the weld — cleaner cross.
    draw_xie_gou(draw, s2_head, s2_belly, s2_hook_pt, s2_tip,
                 head_w=6, belly_w=13, hook_start_w=11, tip_w=2)

    # s1 提/short 横 — draw as a slightly-tapered heng using fat_line width 9
    draw_heng(draw, s1_head, s1_tail, width=9)

    # P-weld 顿笔 disc at the intended crossing
    p_cross = anchor_to_xy(('C', 0.418, 0.531))
    r = 6
    draw.ellipse([p_cross[0] - r, p_cross[1] - r,
                  p_cross[0] + r, p_cross[1] + r], fill=(0, 0, 0))

    # s3 small 点 (upper-right)
    draw_dian(draw, s3_head, s3_tail,
              head_width=2, peak_width=8, curve=0.10, segments=24)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_弋.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
