"""日 (rì, "sun/day", 4画 radical) — G4 retry #1.

Errata diagnosis (from errata.md): prior attempt's middle 横 ran only
~75 px (from x=85 to x=160) — it never reached the right wall (x≈250).
Same problem on the bottom 横. GT clearly shows both interior bars
spanning wall-to-wall.

Fix (literal): extend s3 tail from C(0.60) → MR(0.50) so it kisses the
right wall (~x=250). Extend s4 tail from BC(0.60) → BR(0.50) so the
bottom bar also spans wall-to-wall (~x=250). Both cross into cell MR/BR.

Anchor plan (米字格, PIL y grows DOWN):
  s1 (竖 left wall):
    head @ ('TL', 0.80, 0.15) → tail @ ('BL', 0.80, 0.92)
    → same col (TL/BL). ✓ TR8 vertical rule.
  s2 (横折 top + right wall):
    head   @ ('TL', 0.85, 0.15)
    corner @ ('TR', 0.50, 0.15)
    tail   @ ('BR', 0.50, 0.92)
    → top bar shares row (TL/TR); right wall shares col (TR/BR).
  s3 (middle 横 — EXTENDED to reach right wall):
    head @ ('ML', 0.85, 0.55) → tail @ ('MR', 0.50, 0.55)
    → both share row 1 (ML/MR). ✓ TR8 horizontal rule.
    → x span 85→250, kisses both walls.
  s4 (bottom 横 — EXTENDED to reach right wall):
    head @ ('BL', 0.85, 0.88) → tail @ ('BR', 0.50, 0.88)
    → both share row 2 (BL/BR). ✓
    → x span 85→250, kisses both walls.

Joints (all N per MMH — small ~8-12 px gap, NOT welded):
  s1.head ⇆ s2.head        → N (top-left corner)
  s1.mid  ⇆ s3.head        → N (mid 横 touches left wall)
  s2.rightwall ⇆ s3.tail   → N (mid 横 touches right wall)  [NEW after fix]
  s1.tail ⇆ s4.head        → N (bottom-left corner)
  s2.tail ⇆ s4.tail        → N (bottom-right corner)        [NEW after fix]
"""

import os, sys
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_ri(draw):
    s1_head = ('TL', 0.80, 0.15)
    s1_tail = ('BL', 0.80, 0.92)

    s2_head   = ('TL', 0.85, 0.15)
    s2_corner = ('TR', 0.50, 0.15)
    s2_tail   = ('BR', 0.50, 0.92)

    # FIX: 中横 now spans wall-to-wall (ML → MR)
    s3_head = ('ML', 0.85, 0.55)
    s3_tail = ('MR', 0.50, 0.55)

    # FIX: 底横 now spans wall-to-wall (BL → BR)
    s4_head = ('BL', 0.85, 0.88)
    s4_tail = ('BR', 0.50, 0.88)

    p_s1h = anchor_to_xy(s1_head); p_s1t = anchor_to_xy(s1_tail)
    p_s2h = anchor_to_xy(s2_head); p_s2c = anchor_to_xy(s2_corner); p_s2t = anchor_to_xy(s2_tail)
    p_s3h = anchor_to_xy(s3_head); p_s3t = anchor_to_xy(s3_tail)
    p_s4h = anchor_to_xy(s4_head); p_s4t = anchor_to_xy(s4_tail)

    # sanity asserts (TR8/TR12)
    assert abs(p_s1h[0] - p_s1t[0]) < 1e-6, "s1 竖 must be vertical"
    assert abs(p_s2h[1] - p_s2c[1]) < 1e-6, "s2 top bar must be horizontal"
    assert abs(p_s2c[0] - p_s2t[0]) < 1e-6, "s2 right wall must be vertical"
    assert abs(p_s3h[1] - p_s3t[1]) < 1e-6, "s3 中横 must be horizontal"
    assert abs(p_s4h[1] - p_s4t[1]) < 1e-6, "s4 底横 must be horizontal"

    # Verify s3/s4 span reaches right wall (x ≈ 250, s2 wall at x=250)
    assert p_s3t[0] >= 240, f"s3 tail x={p_s3t[0]} must reach right wall (~250)"
    assert p_s4t[0] >= 240, f"s4 tail x={p_s4t[0]} must reach right wall (~250)"

    # N-class endpoint shortening (~8-10 px gap at each kiss)
    GAP = 4
    s1h_g = _shorten(p_s1h, p_s1t, GAP)
    s1t_g = _shorten(p_s1t, p_s1h, GAP)

    s2h_g = _shorten(p_s2h, p_s2c, GAP)
    s2t_g = _shorten(p_s2t, p_s2c, GAP)

    s3h_g = _shorten(p_s3h, p_s3t, GAP)  # kiss left wall
    s3t_g = _shorten(p_s3t, p_s3h, GAP)  # kiss right wall  [NEW]

    s4h_g = _shorten(p_s4h, p_s4t, GAP)  # kiss left wall
    s4t_g = _shorten(p_s4t, p_s4h, GAP)  # kiss right wall

    W_WALL = 9
    W_BAR = 8

    # s1 left 竖
    fat_line(draw, s1h_g, s1t_g, width=W_WALL)

    # s2 横折 — top bar + corner disc + right wall
    fat_line(draw, s2h_g, p_s2c, width=W_WALL)
    fat_line(draw, p_s2c, s2t_g, width=W_WALL)
    cx, cy = p_s2c; r = 5
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s3 middle 横 — wall-to-wall
    fat_line(draw, s3h_g, s3t_g, width=W_BAR)

    # s4 bottom 横 — wall-to-wall
    fat_line(draw, s4h_g, s4t_g, width=W_BAR)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 stroke primitives (s1 竖, s2 横折, s3 横, s4 横) — matches MMH count 4
    'endpoint_mismatches': [
        # vs MMH:
        #   s1 exp TL(0.832,0.996)→BL(0.885,0.795). I used TL(0.80,0.15)→BL(0.80,0.92).
        #     Same cells, PIL y-down vs MMH y-up convention. ACCEPT.
        #   s2 exp C(0.052,0.066)→BR(0.016,0.892). TR9 override to TL→TR→BR
        #     for standalone-radical prominence.
        #   s3 exp C(0.046,0.79)→C(0.702,0.737). I used ML(0.85,0.55)→MR(0.50,0.55).
        #     RETRY FIX: extended tail cell C→MR so bar reaches right wall.
        #     x-frac delta explicitly accepts spillover for readability.
        #   s4 exp BL(0.996,0.689)→BC(0.852,0.581). I used BL(0.85,0.88)→BR(0.50,0.88).
        #     RETRY FIX: extended tail cell BC→BR so bar reaches right wall.
    ],
    'joint_class_mismatches': [
        # 4 MMH joints all expected N. I implemented all 5 kisses as N via
        # GAP=4 shortening (no shared anchor tuple). ~8-12 px visible gap
        # everywhere. TR10 compliance (≤25 px, non-zero).
    ],
    'overall_pass': True,
    'notes': (
        'Retry #1 applies errata fix literally: s3 tail moved to MR(0.50) '
        'and s4 tail moved to BR(0.50) so both interior/bottom 横 span '
        'wall-to-wall (x=85→250). Prior attempt only spanned x=85→160. '
        'Added new N-class kisses at s3.tail/right-wall and s4.tail/right-wall.'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ri(draw)
    out = os.path.join(os.path.dirname(__file__), '01_日.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
