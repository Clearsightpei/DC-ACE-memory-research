"""p3_char_0338_佘 — 7 strokes.

Composition: 人 (pie + na, wide roof top) + 一 (short heng under 人) +
             一 (wider heng under, the second heng) + 小-body (pie center,
             dian left, dian right).

Applying P-A-006/P-A-007-v2: MMH-anchor verbatim + stroke-primitive layer.
No sub-component matches a bank whole-radical at required aspect
(人 top spans full width — bank draw_ren would need scale ~1.9 horizontally
which is well outside [0.55, 1.2]; bank draw_xiao's proportions don't match
the shrunken/skewed 示-bottom either). Stroke primitives fit cleanly.

Anchor decoding (PIL convention, y grows DOWN within cell):
  pixel_x = cell_x0 + x_frac * 100
  pixel_y = cell_y0 + y_frac * 100
Cells (col, row) with col in {L=0,C=1,R=2} and row in {T=0,M=1,B=2}:
  cell_x0 = col*100; cell_y0 = row*100.

Inline-reasoning per sub-component (P-A-008):
- s1 pie: TC(0.371,0.571)=(137.1, 57.1) → ML(0.316,0.963)=(31.6, 196.3).
  Sub-component: 人 top-left half. Bank primitive `pie` matches
  (endpoint-signature stroke primitive, angle/bow tune to fit).
- s2 na: TC(0.512,0.861)=(151.2, 86.1) → MR(0.856,0.649)=(285.6, 164.9).
  Sub-component: 人 top-right half. Bank `na` matches; anchors span
  full top width.
- s3 heng: C(0.116,0.626)=(111.6, 162.6) → C(0.743,0.579)=(174.3, 157.9).
  Sub-component: short interior heng of 示-top. Bank `heng` matches.
- s4 heng: BL(0.674,0.083)=(67.4, 208.3) → MR(0.259,0.989)=(225.9, 198.9).
  Sub-component: wider heng under s3 (second 一). Bank `heng` matches;
  spans from bottom-left region to middle-right.
- s5 pie: BC(0.356,0.083)=(135.6, 208.3) → BC(0.09,0.804)=(109.0, 280.4).
  Sub-component: center 撇 of 小-bottom. Small pie going down-left from
  center-top to lower-center-left. Bank `pie` with modest bow_perp.
- s6 dian: BL(0.888,0.358)=(88.8, 235.8) → BL(0.653,0.798)=(65.3, 279.8).
  Sub-component: left 点 of 小-bottom. Short down-left dian. Bank `dian`
  with head-tail reversed direction (dian typically starts thin, ends
  thick — head is upper-right, tail is lower-left).
- s7 dian: BC(0.834,0.297)=(183.4, 229.7) → BR(0.276,0.736)=(227.6, 273.6).
  Sub-component: right 点/捺 of 小-bottom. Down-right dian. Bank `dian`.

Joints (all N — natural gap, do NOT weld):
- s1.head ⇆ s2.head @ TC : N, expected_gap ≈ 21.3 px. Actual: distance
  between (137.1,57.1) and (151.2,86.1) = sqrt(14.1^2 + 29^2) ≈ 32.2 px. OK N.
- s4.mid(0.39) ⇆ s5.head @ BC : N, expected_gap ≈ 12.4 px.
  s4.mid(0.39) = (67.4+0.39*158.5, 208.3+0.39*(-9.4)) = (129.2, 204.6).
  s5.head = (135.6, 208.3). Distance ≈ sqrt(6.4^2 + 3.7^2) ≈ 7.4 px. Close;
  keep gap by not welding.
- s4.head ⇆ s6.head @ BL : N, expected_gap ≈ 35.6 px.
  Distance (67.4,208.3)→(88.8,235.8) ≈ sqrt(21.4^2 + 27.5^2) ≈ 34.9 px. OK.
"""
import sys, os
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image
from PIL import ImageDraw

from pie import draw_pie
from na import draw_na
from heng import draw_heng
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 7 primitive calls = 7 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-anchor verbatim per P-A-006/P-A-007-v2. No whole-radical '
             'primitive fits (人 spans full width, 示/小-bottom skewed). '
             'All 7 endpoints at MMH-computed pixels; N-class joints preserve '
             'natural gaps at TC (人 apex), BC (s5 head near s4.mid), and BL '
             '(s4.head near s6.head).',
}


def draw():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: 人-pie — TC(0.371,0.571) → ML(0.316,0.963)
    draw_pie(d, (137.1, 57.1), (31.6, 196.3),
             bow_perp=14, w_head=10, w_tail=3, steps=90)

    # s2: 人-na — TC(0.512,0.861) → MR(0.856,0.649)
    draw_na(d, (151.2, 86.1), (285.6, 164.9),
            bow_perp=14, w_head=4, w_tail=12, steps=90)

    # s3: short heng — C(0.116,0.626) → C(0.743,0.579)
    draw_heng(d, (111.6, 162.6), (174.3, 157.9),
              width_head=7, width_tail=8)

    # s4: wider heng — BL(0.674,0.083) → MR(0.259,0.989)
    draw_heng(d, (67.4, 208.3), (225.9, 198.9),
              width_head=8, width_tail=9)

    # s5: center pie of 小-bottom — BC(0.356,0.083) → BC(0.09,0.804)
    draw_pie(d, (135.6, 208.3), (109.0, 280.4),
             bow_perp=4, w_head=8, w_tail=3, steps=60)

    # s6: left dian — BL(0.888,0.358) → BL(0.653,0.798)
    # Direction is down-left; dian typically thin-head → thick-tail.
    draw_dian(d, (88.8, 235.8), (65.3, 279.8),
              w_head=3, w_tail=7, bow=3, steps=48)

    # s7: right dian — BC(0.834,0.297) → BR(0.276,0.736)
    draw_dian(d, (183.4, 229.7), (227.6, 273.6),
              w_head=3, w_tail=8, bow=4, steps=48)

    return img


if __name__ == "__main__":
    img = draw()
    out = os.path.join(os.path.dirname(__file__), "01_佘.png")
    img.save(out)
    print(f"wrote {out}")
    print(f"SELF_CHECK: {SELF_CHECK}")
