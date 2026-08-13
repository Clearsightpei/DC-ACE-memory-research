"""p3_char_0469_便 (retry_1) — 便 (biàn) — 9 strokes, 亻 + 更.

TRAJECTORY DIFF (from visual inspection of main attempt + GT):

Main FAIL (`../p3_char_0469_便/01_便.png`) visual gaps vs GT:
  (a) 日 box top-left corner OPEN — s4 head (109.6,132.1) and s5 head
      (122.2,131.5) were 13px apart, leaving a visible gap on top of
      the box. In GT the 日 has a fully-closed rectangle. Fix: align
      s4.head.x with s5.head.x so the 丨 meets the 横折's start.
  (b) 亻 pie was drawn with bow_perp=14 → too curved, looks like a
      hook not a smooth pie. GT's 亻 pie is a gentler sweep. Fix:
      reduce bow_perp to ~8 and lengthen the head→tail travel.
  (c) 亻 shu used top_curl=True producing a bulb blob at the head that
      isn't in GT. GT's shu joins the pie mid-flow with a light
      point. Fix: top_curl=False, head sits inside the pie mid.
  (d) 捺 (s9) head at raw MMH (102.5,212.4) too far left — GT shows
      the 捺 emerging from BELOW the 日 near center (~x=140), then
      sweeping down-right. The raw MMH puts it 40px too far left.
      Fix: nudge head x to ~135 while keeping tail near (285,290).
  (e) 撇 (s8) was thin and short-looking; GT descender is thick at
      head, tapered at tail, and clearly crosses the 日 box. Fix:
      widen head to 10, keep tail thin.
  (f) top 一 (s3) was slightly slanted the wrong way; GT is nearly
      level. Kept close to MMH.

Reasoning (P-A-006 + P-A-007-v2 + P-A-008 + P-A-009):
  - Bank cousin 但 (dan_but.py) is 亻+旦=7 strokes; 便 is 亻+更=9
    (更 = 一+日+撇+捺). Whole-radical 但 cannot be uniformly shifted
    into 便 (compositional mismatch — extra 撇/捺 primitives). SKIP
    dan_but per P-A-010-v2 kind-(e).
  - ren_left (亻) bank has fixed geometry tuned for standalone; in 便
    the 亻 lives in left ≤27% width and its shu is slightly SHORTER.
    Quant (P-A-009): bank 亻 shu tail y=292 vs 便 s2 tail y=291.8 —
    within 0.2px (essentially identical). Bank pie head x=158.8 vs
    便 s1 head x=83.5 — dx=-75px. So the 亻 in 便 lives at a systematic
    left-shift of ~75px — that IS uniform-adjustable per P-A-007-v2.
    However, ren_left's internal pie-shu weld is set for its native
    scale; using it here with ox=-75 would drop the shu on top of the
    pie tail geometrically. Cleaner to draw fresh at 便's MMH anchors.
  - Skip heng_zhe_box for 日 top — need to control corner-alignment
    precisely (main FAIL was corner-gap).

BANK_DEVIATION summary: use stroke-primitive layer (pie, shu, heng,
heng_zhe_box, na) at MMH anchors with the six adjustments above.
"""

# BANK_DEVIATION
# skipped: ren_left.py — bank internal spacing incompatible with 便's
#          left-column compression; inline pie+shu at MMH anchors.
# skipped: dan_but.py — 但 = 亻+旦 (7); 便 = 亻+更 (9). Compositional
#          mismatch, not uniform shift (P-A-010-v2 kind-(e)).
# reason:  main-attempt FAIL from disconnected 日 top-left corner and
#          over-bowed 亻 pie; retry re-anchors corners and softens curves.
# fresh_component: bian_convenient (亻 + 一 + 日 + 撇 + 捺 template).

SELF_CHECK = {
    'visual_ok': None,          # set after render
    'stroke_count_ok': True,    # 9 primitive calls (pie, shu, heng, shu,
                                # heng_zhe_box, heng, heng, pie, na)
    'endpoint_mismatches': [],  # adjustments (a)-(f) documented above
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'retry_1: fixed 日 corner gap, softer 亻 pie, no-bulb shu, '
             '捺 head nudged right ~30px for visual center-below-日 origin.'
}

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from na import draw_na
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ==== 亻 (2 strokes) ====
    # s1 pie: softer bow (8 not 14), MMH endpoints TL(0.835,0.671)→ML(0.141,0.948)
    draw_pie(d, (83.5, 67.1), (14.1, 194.8),
             bow_perp=8, w_head=10, w_tail=3, steps=90)
    # s2 shu: no top_curl, head sits inside pie mid-body (fix (c))
    draw_shu(d, (65.0, 145.0), (72.0, 291.8), width=7, top_curl=False)

    # ==== 更 (7 strokes) ====
    # s3 top 一 of 更 — TC(0.342,0.847)→TR(0.215,0.744); make level
    draw_heng(d, (110.0, 84.0), (238.0, 80.0),
              width_head=8, width_tail=9)

    # 日 box: force top-left corner alignment (fix (a))
    # We choose the top-left corner at (112, 100) and top-right/bottom-right
    # at (218, 178) so the box closes cleanly.
    BOX_TL_X, BOX_TL_Y = 112.0, 100.0
    BOX_BR_X, BOX_BR_Y = 218.0, 178.0

    # s4 丨 (left vertical of 日) — head aligned with box top-left
    draw_shu(d, (BOX_TL_X, BOX_TL_Y), (BOX_TL_X + 4, BOX_BR_Y + 4),
             width=7, top_curl=False)
    # s5 横折 (top+right of 日) — head coincides with s4 head (fix (a))
    draw_heng_zhe_box(d, (BOX_TL_X, BOX_TL_Y), (BOX_BR_X, BOX_BR_Y),
                      width=7)
    # s6 middle 横 inside 日 — spans box interior, slight up-right rise
    draw_heng(d, (BOX_TL_X + 6, 142.0), (BOX_BR_X - 4, 138.0),
              width_head=5, width_tail=6)
    # s7 bottom 横 of 日 — spans box bottom, closes the frame
    draw_heng(d, (BOX_TL_X + 4, BOX_BR_Y - 2), (BOX_BR_X - 2, BOX_BR_Y - 6),
              width_head=7, width_tail=8)

    # s8 长撇 descender — TC(0.588,0.938)→BL(0.976,0.865); MMH: (158.8,93.8)→(97.6,286.5)
    # Widen head (fix (e)), keep bow so it crosses the 日 visibly
    draw_pie(d, (162.0, 95.0), (95.0, 288.0),
             bow_perp=20, w_head=11, w_tail=3, steps=100)

    # s9 捺 — nudge head right ~30px to align visually with GT (fix (d))
    # MMH raw head (102.5, 212.4) — retry uses (135, 200) so 捺 origin
    # sits below-center of 日, sweeping to bottom-right corner (285, 290).
    draw_na(d, (135.0, 200.0), (285.0, 290.0),
            bow_perp=16, w_head=4, w_tail=13, steps=100)

    out = Path(__file__).parent / "01_便.png"
    img.save(out)
    print(f"saved: {out}")


if __name__ == "__main__":
    main()
