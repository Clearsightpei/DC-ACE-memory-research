"""p3_char_0170_发 — retry #1. 5 strokes.

TRAJECTORY DIFF (from inspecting FAIL main-attempt PNG vs GT)
============================================================

FAIL main-attempt (attempts/p3_char_0170_发/01_发.png):
1. Character was too TOP-HEAVY / compressed in the upper-left quadrant.
   s1 (top diagonal) crossed s2 (long pie) around (110, 108) instead of
   near cell C=(132, 146). The joint anchor of cell C wasn't honored —
   verbatim MMH endpoint→endpoint straight geometries with mild bow just
   don't cross where MMH's median-parameter joint spec says they should.
2. Bottom joint (s3 short pie ⇆ s4 na @ cell BC=(162, 245)) also DID
   NOT weld — s3 and s4 heads sit only ~6px apart and their paths diverge
   from t=0, so the two strokes never crossed on the failed render.
3. Stroke widths too heavy (heng width 8-9 caused a chunky/cluttered
   silhouette). GT calligraphy is thinner-mid, tapered at ends.
4. s4 na was thick+short-feeling relative to GT's long sweep to BR corner.

FIXES this retry (per P-A-005 retry-A recipe — force welded crossings
at MMH-anchored joint points via bow direction & aggressive tail shifts
still within ±0.20 x_frac/y_frac tolerance):

A) s1: shift tail down (MR(0.4, 0.55) vs MMH MR(0.355, 0.356)) so the
   diagonal slopes more steeply, meeting s2 lower.
B) s2: give NEGATIVE bow_perp (curves right/down in y-down screen coords)
   AND shift head down toward TC bottom (TC(0.4, 0.75)) so the upper
   third of the pie sweeps through cell C region. Bow_perp=-32 pulls
   the belly right toward the crossing.
C) s3: BANK_DEVIATION — inline as a curved pie that starts a bit right
   of MMH C(0.201, 0.91)=(120, 191) — shift to (140, 195) — and curves
   right-down through cell BC before terminating at BL. This makes the
   short-pie visually cross the na at BC.
D) s4: standard na but head shifted slightly right (BC(0.25, 0.15) vs
   MMH BC(0.14, 0.071)) so the crossing with s3 happens closer to BC.
   Reduced widths for less-heavy visual footprint.
E) s5: dot at upper-right, MMH-verbatim.

BANK_DEVIATION
# skipped: none for s1/s2/s4/s5 (bank primitives with tuned bow used)
# replaced: pie.py for s3 with inline curved pie (control point at cell BC
#           anchor) — the bank pie's midpoint+perp geometry can't force
#           passage through BC (162, 245) given s3's short head→tail chord
#           from (140, 195) to (55, 285) whose midpoint is (97.5, 240).
# reason: welding the s3⇆s4 P-joint at BC requires s3's curve to bulge
#         RIGHT beyond what bow_perp=-15 on the standard pie achieves.
# fresh_component: pie_curl_right_for_发_s3 (unlikely reusable — very
#         specific to 发's bottom-又 geometry).

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'retry_1: forced P-joint welds via aggressive bow + s3 inline.'
}
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from dian import draw_dian
from heng import draw_heng
from na import draw_na
from pie import draw_pie


# 3x3 米字格 cell origins on a 300x300 canvas
CELL = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELL[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


def _bezier_taper(draw, p0, p1, p2, w_head, w_tail, steps=80):
    """Inline tapered bezier for BANK_DEVIATION s3."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_fa(d):
    # ---- s1: top horizontal-diagonal tick (heng), tail shifted DOWN vs MMH
    # for a steeper slope that meets s2 lower/further right.
    s1_head = anchor('ML', 0.70, 0.10)   # (70, 110); MMH was (79, 101)
    s1_tail = anchor('MR', 0.40, 0.55)   # (240, 155); MMH was (236, 136)
    draw_heng(d, s1_head, s1_tail, width_head=5, width_tail=6)

    # ---- s2: long left-sweeping pie with NEGATIVE bow_perp to bulge RIGHT,
    # forcing the s1⇆s2 P-joint to occur in cell C rather than TC.
    s2_head = anchor('TC', 0.40, 0.75)   # (140, 75); MMH was (135, 56)
    s2_tail = anchor('BL', 0.20, 0.90)   # (20, 290); MMH was (28, 274.5)
    draw_pie(d, s2_head, s2_tail, bow_perp=-32, w_head=7, w_tail=3)

    # ---- s4: main na sweeping down-right, natural bow.
    # Head shifted slightly right so its upper section crosses s3 at BC region.
    s4_head = anchor('BC', 0.20, 0.10)   # (120, 210); MMH was (114, 207)
    s4_tail = anchor('BR', 0.85, 0.92)   # (285, 292); MMH was (276, 292)
    draw_na(d, s4_head, s4_tail, bow_perp=14, w_head=3, w_tail=10)

    # ---- s3: INLINE tapered bezier (BANK_DEVIATION) — short pie that
    # bulges through cell BC(0.617, 0.451)=(162, 245) to weld with s4.
    s3_head = anchor('C', 0.40, 0.90)    # (140, 190); MMH was (120, 191)
    s3_ctrl = anchor('BC', 0.60, 0.45)   # (160, 245) — the joint anchor
    s3_tail = anchor('BL', 0.60, 0.90)   # (60, 290); MMH was (71, 286)
    _bezier_taper(d, s3_head, s3_ctrl, s3_tail, w_head=6, w_tail=2, steps=70)

    # ---- s5: small dian at upper-right (MMH-verbatim).
    s5_head = anchor('TC', 0.913, 0.747)  # (191.3, 74.7)
    s5_tail = anchor('MR', 0.247, 0.028)  # (224.7, 102.8)
    draw_dian(d, s5_head, s5_tail, w_head=3, w_tail=7, bow=3)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_fa(d)
    out = pathlib.Path(__file__).parent / '01_发.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
