"""伐 (fá, "to cut/attack") — 亻 + 戈, 6 strokes.

Memory reads (per memory_index.md v8):
  1. drawer_memory.md — noted 亻uses ren_side; 戈uses xie_gou + heng + pie + dian.
  2. success_bank/INDEX.md grep — ren_side.py, xie_gou.py, heng.py, pie.py, dian.py.
  3. errata.md grep 伐 — not present.

Split: 伐 = 亻(strokes 1-2) + 戈(strokes 3-6).
MMH stroke count = 6. We render 6 primitives.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '../../success_bank/code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from xie_gou import draw_xie_gou
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('6 strokes: s1 亻撇, s2 亻竖, s3 戈横, s4 戈斜钩(compound '
              'body+hook), s5 戈撇, s6 戈点. Joints P at s3.mid⇆s4.mid '
              '(C) and s4.mid⇆s5.mid (BC); N at s1.mid⇆s2.head (ML).')
}

def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 亻 (person radical, left) ----
    # s1: 撇 — head @ TL(0.867, 0.858) → tail @ BL(0.161, 0.183)
    draw_pie(draw, ('TL', 0.867, 0.858), ('BL', 0.161, 0.183),
             head_width=11, tail_width=1, curve=0.10, segments=48)
    # s2: 竖 — head @ ML(0.782, 0.55) → tail @ BL(0.771, 1.056)
    draw_shu(draw, ('ML', 0.782, 0.55), ('BL', 0.771, 1.056), width=9)

    # ---- 戈 (dagger-axe, right) ----
    # s3: 短横 — head @ C(0.163, 0.729) → tail @ MR(0.218, 0.38)
    draw_heng(draw, ('C', 0.163, 0.729), ('MR', 0.218, 0.38), width=8)

    # s4: 斜钩 (compound: slanted body + up-flick hook)
    #   MMH head @ TC(0.348, 0.729), MMH tail @ BR(0.736, 0.429) = hook tip.
    #   Body sweeps from upper-mid down-right to lower-right, then flicks UP.
    draw_xie_gou(draw,
                 head=('TC', 0.348, 0.729),
                 belly=('C', 0.75, 0.35),        # bow low point
                 hook_pt=('BR', 0.60, 0.80),     # where body ends
                 tip=('BR', 0.736, 0.429),       # up-flick tip
                 head_w=8, belly_w=14, hook_start_w=12, tip_w=2)

    # s5: 撇 (small, crossing 斜钩) — head @ MR(0.186, 0.702) → tail @ BC(0.201, 0.581)
    draw_pie(draw, ('MR', 0.186, 0.702), ('BC', 0.201, 0.581),
             head_width=8, tail_width=1, curve=0.08, segments=32)

    # s6: 点 (top-right of 戈) — head @ TC(0.998, 0.82) → tail @ MR(0.353, 0.069)
    draw_dian(draw, ('TC', 0.998, 0.82), ('MR', 0.353, 0.069),
              head_width=2, peak_width=11, curve=0.08, segments=24)

    out = os.path.join(os.path.dirname(__file__), '01_伐.png')
    img.save(out)
    print('wrote', out)

if __name__ == '__main__':
    render()
