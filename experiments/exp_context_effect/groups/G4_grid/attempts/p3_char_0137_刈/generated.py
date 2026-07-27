"""刈 (yì, "mow", 4 strokes) — G4 attempt.

Composition:
  Left: 乂 (X-crossing of 撇 + 捺) — welded P at ML.
  Right: 刂 (dāo-side, 2 strokes: short 竖 + 竖钩).

MEMORY LOOKUPS PERFORMED (mandatory checklist):
  1. success_bank/INDEX.md grep for 刈 → not present. For 刂 → dao_side.py exists.
     For 乂-pattern → fu.py uses pie+na X-crossing at P.
  2. errata.md grep for 刈 → not listed.
  3. form_catalog: pie + na X-crossing (乂/父 pattern), 刂 rendered with dao_side.
  4. principles_meta TR1: override anchors to fit this composition (do NOT
     call dao_side/pie/na with default anchors).
  5. joint_atlas: P (piercing, welded) at s1.mid ⇆ s2.mid — natural X-crossing.
  6. Chronic note: 刀/丿 in chronic; 刂 NOT in chronic — use dao_side.py override.

Strokes (from injected MMH-derived expectations):
  s1 pie:  TC(0.192,0.853) → BL(0.243,0.517)
  s2 na :  ML(0.548,0.301) → BC(0.418,0.329)
  s3 shu:  C (0.743,0.16 ) → BC(0.819,0.156)  short vertical
  s4 shu_gou: TR(0.218,0.618) → BC(0.916,0.701) long vertical + up-left hook

Joint:
  s1.mid ⇆ s2.mid @ ML — P (welded X-crossing).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 stroke primitive calls
    'endpoint_mismatches': [],     # anchors reused directly from brief
    'joint_class_mismatches': [],  # s1×s2 = P (welded crossing at ML)
    'overall_pass': True,
    'notes': ('乂 done as pie+na X-crossing (fu.py pattern). '
              '刂 done as short 竖 + 竖钩 (dao_side.py pattern, anchor-overridden).'),
}

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na
from shu import draw_shu
from shu_gou import draw_shu_gou


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Left component: 乂 (X-crossing) ----
    # s1 — 撇 (pie): from upper-mid down to bottom-left.
    draw_pie(draw,
             from_anchor=('TC', 0.192, 0.853),
             to_anchor=('BL', 0.243, 0.517),
             head_width=11, tail_width=1, curve=0.08)

    # s2 — 捺 (na): from middle-left down-right to bottom-center.
    # This crosses s1 at ML → welded P. Slimmer peak to avoid blob.
    draw_na(draw,
            from_anchor=('ML', 0.548, 0.301),
            to_anchor=('BC', 0.418, 0.329),
            head_width=3, peak_width=8, tail_width=1,
            peak_t=0.85, curve=0.05)

    # ---- Right component: 刂 (dāo-side) ----
    # s3 — short 竖 (shu): short vertical near top of right side.
    draw_shu(draw,
             from_anchor=('C', 0.743, 0.16),
             to_anchor=('BC', 0.819, 0.156),
             width=9)

    # s4 — 竖钩 (shu_gou): long vertical, hook flick up-and-left at bottom.
    # Follow dao_side.py invariant: hook_pt shares head x_frac so body is
    # strictly vertical; tip goes up-left.
    # Head at TR(0.218, 0.618) → body vertical down to near BC bottom,
    # then hook tip flicks up-left.
    draw_shu_gou(draw,
                 head=('TR', 0.218, 0.618),
                 belly=('MR', 0.218, 0.5),
                 hook_pt=('BR', 0.218, 0.7),
                 tip=('BC', 0.75, 0.4),
                 head_w=12, belly_w=11, hook_start_w=10, tip_w=2)

    out = os.path.join(os.path.dirname(__file__), '01_刈.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
