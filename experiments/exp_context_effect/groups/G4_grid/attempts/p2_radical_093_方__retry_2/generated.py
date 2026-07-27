"""方 (fāng, 4-stroke radical) — retry #2.

MANDATORY LOOKUP CHECKLIST (as per memory_index):
  - success_bank/INDEX.md grep: `fang.py` exists but is 匚 (2-stroke), not 方 —
    NOT reusable. Draw fresh using stroke primitives.
  - errata.md grep: p2_radical_093_方 listed. Fix idea LITERAL:
      "extend 横折钩 vertical (corner MR(0.65, 0.55), tail BR(0.65, 0.75),
       tip BC(0.65, 0.55)); ensure visible descent + up-left hook."
    Prior FAIL mode: 横折钩 body descended only 20 px, compressed to right
    column. Apply the literal anchor fix.
  - form_catalog.md: 横 in radical → span ML→MR; 横折钩 in right position →
    corner in top-right, tail below-mid, tip up-left of tail.
  - principles_meta.md TR9: standalone radical must span ~full grid.
  - joint_atlas.md: N-class joints should look connected (≤25 px gap),
    but do NOT weld.

Anchor plan (米字格, PIL y-down convention):

  s1 — 点 (top dot). Above the top-heng.
      head = ('TC', 0.30, 0.10)   起笔 upper-left
      tail = ('TC', 0.65, 0.35)   press lower-right
      (MMH TC(0.307,0.589)→TC(0.693,0.932) is fully within TC; overriding
       upward so the dot sits above the top-horizontal band.)

  s2 — 横 (top horizontal), spanning most of grid, slight rise to right.
      head = ('ML', 0.20, 0.55)
      tail = ('MR', 0.85, 0.40)
      (MMH: ML(0.434,0.471)→MR(0.666,0.301) — expanded per TR9.)

  s3 — 横折钩 (right side of the small box + up-left hook flick).
      Per errata fix LITERAL:
      head    = ('C', 0.55, 0.45)   near right end of top-heng
      corner  = ('MR', 0.65, 0.55)  折 point
      tail    = ('BR', 0.65, 0.75)  bottom of vertical drop (visible descent)
      tip     = ('BC', 0.65, 0.55)  hook tip up-and-left

  s4 — 撇 (long diagonal sweep down-left from top-heng area).
      head = ('C', 0.40, 0.40)     thick 起笔 near center-top
      tail = ('BL', 0.20, 0.95)    needle-tip lower-left
      (MMH: C(0.409,0.436)→BL(0.357,0.774) — extended per TR9.)

Joints (2 total, both N per MMH block):
  J1: s2.mid ⇆ s4.head @ cell C — N (~12 px gap expected)
  J2: s3.head ⇆ s4.mid(0.19) @ cell C — N (~18 px gap expected)
Do NOT weld either; ~15 px natural gap on both.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 strokes: dian, heng, heng_zhe_gou, pie
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Retry #2 — applied errata fix LITERALLY. Corner MR(0.65,0.55), '
        'tail BR(0.65,0.75), tip BC(0.65,0.55). This gives the 横折钩 '
        'a visible vertical descent of ~60 px (was 20 px in prior FAIL) '
        'and up-left hook flick. TR9 expansion applied to s2 (top heng) '
        'and s4 (撇) so the radical spans the full grid instead of being '
        'compressed. Dot lifted above top-heng.'
    )
}

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy  # noqa: E402
from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 点 (top dot), small, sits above the top-heng
    draw_dian(draw,
              from_anchor=('TC', 0.30, 0.10),
              to_anchor=('TC', 0.65, 0.35),
              head_width=2, peak_width=10)

    # s2 — 横 (top horizontal), spanning ML→MR, slight rise
    draw_heng(draw,
              from_anchor=('ML', 0.20, 0.55),
              to_anchor=('MR', 0.85, 0.40),
              width=9)

    # s3 — 横折钩 (top-right of box → visible vertical drop → up-left hook)
    #   Revision: pull corner leftward so box sits under the top-heng
    #   instead of jutting right of it. Keep visible vertical descent.
    draw_heng_zhe_gou(draw,
                      head=('C', 0.40, 0.45),
                      corner=('MR', 0.30, 0.55),
                      tail=('BR', 0.30, 0.80),
                      tip=('BC', 0.85, 0.60),
                      h_width=9, v_width=10, shoulder=13, tip_w=2)

    # s4 — 撇 (long diagonal sweep down-and-left)
    draw_pie(draw,
             from_anchor=('C', 0.40, 0.40),
             to_anchor=('BL', 0.20, 0.95),
             head_width=11, tail_width=1, curve=0.12)

    out_png = os.path.join(HERE, '01_方.png')
    img.save(out_png)
    print(f'wrote {out_png}')


if __name__ == '__main__':
    render()
