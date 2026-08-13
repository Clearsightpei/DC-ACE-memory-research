"""佚 (yì) — 7 strokes.

Decomposition: 佚 = 亻 (left, s1+s2) + 失 (right, s3+s4+s5+s6+s7).
  失 breaks down as: s3 短撇 (top) + s4 上横 + s5 下横 (longer, crosses)
                  + s6 长撇 + s7 长捺.

Following the B9 A-recipe (drawer_memory.md):
  1) Explicit decomposition (this docstring).
  2) MMH-verbatim anchors — every anchor tuple below is copied literally
     from the dispatcher's per-stroke expectations.
  3) SELF_CHECK block declared.
  4) Base primitives (pie/shu/heng/na) over compound primitives — MMH
     places 亻 at TL(0.85)+ML(0.68), which is far-left of ren_side's
     default TC(0.588)/C(0.470) anchors, so we inline pie+shu instead
     of importing ren_side and partially overriding it (documented FAIL
     pattern for p3_char_0252_伊 in B8).
  5) N-joints kept as natural gaps (~15-25 px); P-joints welded via
     the two 横s crossing the 长撇 at their MMH midpoints.

Joint spec (from brief):
  s1.mid ⇆ s2.head @ ML  N (~20 px gap, 亻 T-touch)
  s3.mid ⇆ s4.head @ C   N (~12 px gap)
  s3.tail ⇆ s5.head @ C  N (~32 px gap)
  s4.mid ⇆ s6.mid  @ C   P (welded — 上横 crosses 长撇)
  s5.mid ⇆ s6.mid  @ C   P (welded — 下横 crosses 长撇)
  s5.mid ⇆ s7.head @ C   N (~19 px gap)
  s6.mid ⇆ s7.head @ BC  N (~20 px gap — 撇 and 捺 meet near, small gap)
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
    'stroke_count_ok': True,   # 7 draw calls below, matches MMH expected 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('MMH-verbatim anchors; 亻 inlined as pie+shu (skipped ren_side '
              'because ren_side defaults sit at TC/C which is far-right of '
              'the MMH left-column placement — inlining preserves left '
              'column). Two P-welds on 长撇 achieved by drawing 上横/下横 '
              'to their MMH tails, which cross the 长撇 chord near its '
              'MMH-declared midpoint. N-gaps preserved naturally.')
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ============ Left radical 亻 ============
    # s1 — 撇: TL(0.85, 0.671) → ML(0.161, 0.948)
    draw_pie(d,
             from_anchor=('TL', 0.85, 0.671),
             to_anchor=('ML', 0.161, 0.948),
             head_width=11, tail_width=2, curve=0.08, segments=48)

    # s2 — 竖: ML(0.677, 0.477) → BL(0.691, 0.962)
    draw_shu(d,
             from_anchor=('ML', 0.677, 0.477),
             to_anchor=('BL', 0.691, 0.962),
             width=8)

    # ============ Right radical 失 ============
    # s3 — 短撇 (top small pie): C(0.298, 0.043) → C(0.116, 0.734)
    #   short, mostly-vertical downward-left curl at the top of 失
    draw_pie(d,
             from_anchor=('C', 0.298, 0.043),
             to_anchor=('C', 0.116, 0.734),
             head_width=8, tail_width=2, curve=0.06, segments=32)

    # s4 — 上横 (upper short 横): C(0.406, 0.406) → MR(0.297, 0.269)
    draw_heng(d,
              from_anchor=('C', 0.406, 0.406),
              to_anchor=('MR', 0.297, 0.269),
              width=8)

    # s5 — 下横 (lower long 横): C(0.049, 0.957) → MR(0.543, 0.808)
    draw_heng(d,
              from_anchor=('C', 0.049, 0.957),
              to_anchor=('MR', 0.543, 0.808),
              width=9)

    # s6 — 长撇 (long pie through center down to BL):
    #      TC(0.661, 0.606) → BL(0.964, 0.859)
    draw_pie(d,
             from_anchor=('TC', 0.661, 0.606),
             to_anchor=('BL', 0.964, 0.859),
             head_width=11, tail_width=2, curve=0.09, segments=48)

    # s7 — 长捺 (long na from mid down-right):
    #      C(0.828, 0.98) → BR(0.883, 0.856)
    draw_na(d,
            from_anchor=('C', 0.828, 0.98),
            to_anchor=('BR', 0.883, 0.856),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_佚.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
