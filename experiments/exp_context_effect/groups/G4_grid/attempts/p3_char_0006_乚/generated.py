"""p3_char_0006_乚 — Phase-3 character 乚 (1画, 竖弯钩 family).

Anchor plan (per MMH-derived structural expectations):
  stroke 1 (compound 竖弯钩):
    head    = ('TL', 0.636, 0.867)  — upper-left, lower part of TL cell
    belly   = ('ML', 0.65,  0.90)   — Bezier control keeps upper body straight
    corner  = ('BL', 0.75,  0.30)   — bend near bottom-left
    hook_pt = ('BR', 0.55,  0.30)   — end of horizontal sweep
    tip     = ('BR', 0.552, 0.124)  — subtle up-tick (matches MMH tail)

Joints: NONE (single continuous compound stroke).

Composition rationale: identical to the mastered radical primitive
`yi_hook.py` (p2_radical_007_乚 retry PASS). MMH gives the same head/tail
anchors for the Phase-3 character as for the Phase-2 radical (per TR9,
verbatim MMH is fine for Phase-3 characters). Reuse the passing recipe
via wrapper.

Self-check outcome logged in SELF_CHECK below.
"""
import os
import sys

# Import G4 shared primitives from the Success Bank code directory.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK_CODE = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK_CODE)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 1 stroke primitive matches expected 1
    'endpoint_mismatches': [],       # head + tail == MMH anchors exactly
    'joint_class_mismatches': [],    # no joints expected, none rendered
    'overall_pass': True,
    'notes': ('Reuses passing radical recipe (yi_hook.py). Same MMH '
              'anchors as p2_radical_007_乚 retry PASS. Head TL(0.636,'
              '0.867) → tail BR(0.552, 0.124) verbatim.'),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    head = ('TL', 0.636, 0.867)
    belly = ('ML', 0.65, 0.90)
    corner = ('BL', 0.75, 0.30)
    hook_pt = ('BR', 0.55, 0.30)
    tip = ('BR', 0.552, 0.124)

    # Sanity: TR8 — head above tail (y_head_px < y_tail_px? actually PIL y
    # grows down; head at TL y_frac 0.867 → py ~87; tail at BR y_frac 0.124
    # → py ~212. So head IS above tail visually. Good.)
    hx, hy = anchor_to_xy(head)
    tx, ty = anchor_to_xy(tip)
    assert hy < ty, f"head y {hy} should be above tip y {ty}"
    assert tx > hx, f"tip x {tx} should be right of head x {hx}"

    draw_shu_wan_gou(
        draw,
        head=head,
        belly=belly,
        corner=corner,
        hook_pt=hook_pt,
        tip=tip,
        head_w=8, belly_w=11, corner_w=11,
        hook_start_w=9, tip_w=2,
    )

    out = os.path.join(_HERE, '01_乚.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
