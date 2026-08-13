"""p2_radical_109_攴 — G5 retry #1.

TRAJECTORY DIFF (from inspecting GT + FAIL PNG):

FAIL (main attempt):
  - Structure was correct (shu + short heng on top; pie + na on bottom)
    and followed MMH endpoints exactly.
  - But visually WEAK: (1) top strokes too thin (width 6-7) while na tail
    was thick (12), giving a top-light / bottom-heavy imbalance; (2) the
    pie and na barely crossed — s4 head @ MMH (97, 189) sits essentially
    ON s3 (which passes through (~93, 189) near t=0.15), so instead of a
    proper X the na hangs off the top of the pie; (3) the whole glyph
    read as three floating fragments (shu / heng / bottom-V) with poor
    connection to the shu.

GT shows:
  - A clear 卜 top: shu with short accent heng touching / very close to it.
  - A clear X bottom: pie and na cross NEAR THE MIDDLE of both strokes
    (not near either endpoint), forming a proper "又"-like intersection.
  - Consistent stroke weight — no dramatic thin-top / thick-bottom.

Fixes applied here:
  1. Thicken top strokes (shu w=10, heng w=9) so they read at same weight
     as the bottom.
  2. Reduce na tail weight (w_tail 13→11) to reduce bottom heaviness.
  3. Shift s3 (pie) head UP toward s1 tail area so the pie starts higher,
     letting the crossing land in the middle of both strokes rather than
     at s4's head. Uses ('C', 0.05, 0.55) ≈ (105, 155) instead of MMH's
     (0.017, 0.717) — within ±0.20 tolerance in y_frac (0.717 - 0.55 =
     0.167) and cell C matches.
  4. Shift s4 (na) head slightly right + down so it starts clearly RIGHT
     of the pie's upper section and the two form a clean X. Uses ('C',
     0.15, 0.90) ≈ (115, 190) instead of ML(0.973, 0.893) — cell adjacent
     (ML→C, immediately adjacent), delta well under tolerance.
  5. Increase pie bow_perp to 18 so its belly reaches further right,
     making the crossing zone geometrically well-defined at BC.
"""

# BANK_DEVIATION
# skipped: bu_divine.py — bu's s2 is a diagonal dian going down-right
#   with a hardcoded belly; 攴's MMH s2 is a near-horizontal short heng
#   going up-right. Use draw_heng directly (as FAIL did).
# skipped: you_again.py — you's s1 is heng_pie (starts with a horizontal
#   segment then breaks into pie); 攴's s3 is a plain pie without the
#   horizontal shoulder. Use draw_pie directly.
# reason: sub-stroke shape mismatch despite structural similarity.
# fresh_component: none — all four strokes are base bank primitives
#   (shu, heng, pie, na) called with endpoint tuning.

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from shu import draw_shu
from heng import draw_heng
from pie import draw_pie
from na import draw_na


# ---- 米字格 anchor helper (3x3 cells, 100x100 each on 300x300 canvas) ----
_CELL_ORIGINS = {
    'TL': (0,   0), 'TC': (100,  0), 'TR': (200,  0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def anchor(cell, xf, yf):
    ox, oy = _CELL_ORIGINS[cell]
    return (ox + xf * 100, oy + yf * 100)


W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


# ---- Stroke 1: 竖 short vertical (top of 卜-part) ----
# MMH: TC(0.339, 0.636) -> C(0.406, 0.611) ~= (134, 64) -> (141, 161)
s1_head = anchor('TC', 0.339, 0.636)
s1_tail = anchor('C',  0.406, 0.611)
draw_shu(d, s1_head, s1_tail, width=10, top_curl=False)


# ---- Stroke 2: short 横 to the right of s1 (near-horizontal, slight up) ----
# MMH: C(0.567, 0.16) -> MR(0.165, 0.055) ~= (157, 116) -> (217, 106)
s2_head = anchor('C',  0.567, 0.16)
s2_tail = anchor('MR', 0.165, 0.055)
draw_heng(d, s2_head, s2_tail, width_head=8, width_tail=9)


# ---- Stroke 3: 撇 (pie — long sweep down-left) ----
# MMH says head @ C(0.017, 0.717) ~ (102, 172). Shift head UP to be
# closer to s1's tail area so the pie crosses s4 near BOTH strokes'
# midpoints, not at s4's head.
# Adjusted head: C(0.05, 0.55) ~= (105, 155)  [within tolerance, cell C]
# Tail: BL(0.437, 0.868) ~= (44, 287)  [MMH verbatim]
s3_head = anchor('C',  0.05, 0.55)
s3_tail = anchor('BL', 0.437, 0.868)
draw_pie(d, s3_head, s3_tail, bow_perp=18, w_head=9, w_tail=3, steps=90)


# ---- Stroke 4: 捺 (na — long sweep down-right, crosses pie at BC) ----
# MMH says head @ ML(0.973, 0.893) ~ (97, 189), tail @ BR(0.792, 0.927)
# ~ (279, 293). Head placement forced s4 to START at the pie's early
# path, so no proper X formed. Shift head slightly right + down so the
# two strokes form a clean crossing near the middle.
# Adjusted head: C(0.15, 0.90) ~= (115, 190)  [cell C, immediately adjacent to ML]
# Tail: BR(0.792, 0.927) ~= (279, 293)  [MMH verbatim]
s4_head = anchor('C',  0.15, 0.90)
s4_tail = anchor('BR', 0.792, 0.927)
draw_na(d, s4_head, s4_tail, bow_perp=12, w_head=5, w_tail=11, steps=90)


SELF_CHECK = {
    'visual_ok': None,   # to verify after render
    'stroke_count_ok': True,   # 4 primitive calls: shu, heng, pie, na
    'endpoint_mismatches': [
        {'stroke': 3, 'expected': "C(0.017, 0.717)", 'actual': "C(0.05, 0.55)",
         'delta_yfrac': 0.167, 'reason': 'raise pie start to form central X'},
        {'stroke': 4, 'expected': "ML(0.973, 0.893)", 'actual': "C(0.15, 0.90)",
         'delta': 'adjacent cell, x shifted right ~18px', 'reason': 'push na head off pie top-line'},
    ],
    'joint_class_mismatches': [],   # geometry still P for s3xs4, N for s1-s2 and s1-s3
    'overall_pass': None,
    'notes': ('Retry #1: fixes stroke-weight balance (thicken top), '
              'reduces na tail weight, and adjusts s3/s4 heads so pie & '
              'na cross near their midpoints instead of at s4.head. '
              'BANK_DEVIATION preserved: bu_divine and you_again skipped.'),
}


out = pathlib.Path(__file__).parent / '01_攴.png'
img.save(out)
print(f'wrote {out}')
