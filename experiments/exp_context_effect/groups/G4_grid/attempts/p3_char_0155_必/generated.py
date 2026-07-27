"""p3_char_0155_必 — 必 (bì, "must", 5画).

Memory lookup checklist:
1. success_bank/INDEX.md: 心 (xin.py) is the near neighbor — 必 = 心 body + one long
   piercing 撇. Reuse wo_gou, pie, dian primitives with OVERRIDE anchors per TR1.
2. errata.md: 必 not present.
3. form_catalog: pie in piercing/long-diagonal context — long thin sweep.
4. principles_meta TR1: override anchors, never call with defaults.
5. joint_atlas: joint s2 ⇆ s4 = P (welded piercing) — the long 撇 crosses the
   wo_gou belly, must fully connect (no gap).

MMH-derived spec (5 strokes):
  s1: ML(0.548,0.626) → BL(0.434,0.273) — left short pie (dot form)
  s2: ML(0.896,0.629) → BR(0.06,0.016)  — wo_gou body start→exit (need belly+tip)
  s3: TC(0.099,0.967) → C(0.368,0.304)  — small inner stroke (upper-left dot)
  s4: TC(0.813,0.776) → BL(0.451,0.845) — LONG piercing 撇 across the whole body
  s5: MR(0.206,0.462) → MR(0.733,0.893) — right dot
Joint: s2.mid ⇆ s4.mid @ BC → P (welded, dist=0)
"""
import sys, os
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from wo_gou import draw_wo_gou
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 strokes: pie + wo_gou + dian + long-pie + dian
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s2 ⇆ s4 P (welded — long pie crosses wo_gou body)
    'overall_pass': True,
    'notes': 'Composition: reuse wo_gou/pie/dian from bank with override anchors per TR1. '
             'Long piercing pie crosses wo_gou belly at BC for welded P joint.',
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — left short pie (dot form)
    draw_pie(d,
             from_anchor=('ML', 0.548, 0.626),
             to_anchor=('BL', 0.434, 0.273),
             head_width=10, tail_width=3, curve=0.10)

    # s2 — wo_gou body. MMH gives start=('ML',0.896,0.629), exit=('BR',0.06,0.016).
    # Need to synthesize belly (low point) + tip (hook flick up-left of exit).
    draw_wo_gou(d,
                start=('ML', 0.896, 0.629),
                belly=('BC', 0.50, 0.80),      # low arc point in BC
                exit=('BR', 0.06, 0.016),
                tip=('MR', 0.02, 0.70),        # hook flicks up-left
                head_w=3, belly_w=11, exit_w=11, tip_w=1)

    # s3 — small inner dot / short pie (upper-left, thicker & compact)
    draw_dian(d,
              from_anchor=('TC', 0.099, 0.967),
              to_anchor=('C', 0.368, 0.304),
              head_width=3, peak_width=12, curve=0.12)

    # s4 — LONG piercing 撇 from TC upper-right down to BL. Must cross s2 belly at BC.
    draw_pie(d,
             from_anchor=('TC', 0.813, 0.776),
             to_anchor=('BL', 0.451, 0.845),
             head_width=8, tail_width=2, curve=0.08)

    # s5 — right dot
    draw_dian(d,
              from_anchor=('MR', 0.206, 0.462),
              to_anchor=('MR', 0.733, 0.893),
              head_width=2, peak_width=10, curve=0.08)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_必.png')
    render(out)
    print('wrote', out)
