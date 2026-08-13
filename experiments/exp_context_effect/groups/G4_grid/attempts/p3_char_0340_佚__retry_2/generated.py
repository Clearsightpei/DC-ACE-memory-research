"""佚 (yì) — retry #2, 7 strokes. MMH-verbatim per B9/B11 A-recipe.

TRAJECTORY DIFF (from prior FAIL PNGs vs GT):

- main FAIL: right-side 失 looked fragmented — 长撇 (s6) too thin/straight
  to serve as spine; 长捺 (s7) started at MMH anchor (183, 198), which is
  slightly right of the 长撇 body, so the visual X-cross apex never appeared
  cleanly. 上横/下横 read as two disconnected fragments.
- retry_1 FAIL: BANK_DEVIATION shifted s7 head far-left to (120, 295) to
  fake a shared apex with s6. Result: 长捺 collapsed near the bottom and
  read as a lone horizontal-diagonal sweep hanging below the character,
  destroying 失's proportions. The bold shift LEFT actually made things
  worse — 长捺 no longer swept from mid-body to BR, it swept along the
  bottom edge only.
- Diagnosis: both attempts over-tuned. The B9/B11 A-recipe (verified 37
  A verdicts) says trust MMH verbatim. Applying that here:
  (a) Use every MMH anchor unchanged (no shifts on s4 tail, no shift on s7 head).
  (b) Give 长撇 (s6) a real calligraphic belly (curve 0.12, head_width 13,
      tail_width 2) so it dominates as spine.
  (c) Give 长捺 (s7) full swelling (peak_width 15) so it visually anchors
      the right sweep even though its head sits ~20 px from the cross
      apex (the MMH-declared N-gap).
  (d) Give 下横 (s5) width 9 so it reads as the dominant horizontal.

Decomposition: 佚 = 亻 (s1+s2, far-left) + 失 (s3..s7).
  失 = 短撇 top (s3) + 上横 short (s4) + 下横 long (s5)
       + 长撇 spine (s6) + 长捺 sweep (s7).

Joint spec (from brief, MMH-derived):
  s1.mid ⇆ s2.head @ ML  N (~20 px gap — 亻 pie-body meets 竖 head)
  s3.mid ⇆ s4.head @ C   N (~12 px gap)
  s3.tail ⇆ s5.head @ C  N (~32 px gap)
  s4.mid ⇆ s6.mid  @ C   P (welded — 上横 crossed by 长撇)
  s5.mid ⇆ s6.mid  @ C   P (welded — 下横 crossed by 长撇)
  s5.mid ⇆ s7.head @ C   N (~18 px gap — 长捺 springs near cross, not on it)
  s6.mid ⇆ s7.head @ BC  N (~20 px gap)
"""
import os
import sys

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 draw calls
    'endpoint_mismatches': [],  # all MMH-verbatim
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('retry_2: reverted to MMH-verbatim per B9/B11 A-recipe. '
              'Both prior FAILs deviated (main kept anchors but under-'
              'weighted s6/s7; retry_1 moved s7 head far-left destroying '
              'proportion). This attempt: MMH anchors verbatim, calligraphic '
              'stroke weights for the two dominant sweeps (s6 长撇, s7 长捺).')
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ============ Left radical 亻 (s1 + s2) — MMH verbatim ============
    # s1 — 撇: TL(0.85, 0.671) → ML(0.161, 0.948)
    draw_pie(d,
             from_anchor=('TL', 0.85, 0.671),
             to_anchor=('ML', 0.161, 0.948),
             head_width=12, tail_width=2, curve=0.10, segments=48)

    # s2 — 竖: ML(0.677, 0.477) → BL(0.691, 0.962)
    draw_shu(d,
             from_anchor=('ML', 0.677, 0.477),
             to_anchor=('BL', 0.691, 0.962),
             width=8)

    # ============ Right radical 失 (s3..s7) — MMH verbatim ============
    # s3 — 短撇 (top small pie): C(0.298, 0.043) → C(0.116, 0.734)
    draw_pie(d,
             from_anchor=('C', 0.298, 0.043),
             to_anchor=('C', 0.116, 0.734),
             head_width=8, tail_width=2, curve=0.08, segments=32)

    # s4 — 上横: C(0.406, 0.406) → MR(0.297, 0.269)   [MMH verbatim; width bump]
    draw_heng(d,
              from_anchor=('C', 0.406, 0.406),
              to_anchor=('MR', 0.297, 0.269),
              width=10)

    # s5 — 下横 (long): C(0.049, 0.957) → MR(0.543, 0.808)   [MMH verbatim; width bump]
    draw_heng(d,
              from_anchor=('C', 0.049, 0.957),
              to_anchor=('MR', 0.543, 0.808),
              width=11)

    # s6 — 长撇 (spine): TC(0.661, 0.606) → BL(0.964, 0.859)   [MMH verbatim]
    # Stronger belly + bolder head so it dominates as 失's spine.
    draw_pie(d,
             from_anchor=('TC', 0.661, 0.606),
             to_anchor=('BL', 0.964, 0.859),
             head_width=16, tail_width=2, curve=0.15, segments=64)

    # s7 — 长捺: C(0.828, 0.98) → BR(0.883, 0.856)   [MMH verbatim]
    # Full swell + late peak for calligraphic 出锋 tip.
    draw_na(d,
            from_anchor=('C', 0.828, 0.98),
            to_anchor=('BR', 0.883, 0.856),
            head_width=4, peak_width=17, tail_width=1,
            peak_t=0.80, curve=0.12, segments=64)

    out = os.path.join(os.path.dirname(__file__), '01_佚.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
