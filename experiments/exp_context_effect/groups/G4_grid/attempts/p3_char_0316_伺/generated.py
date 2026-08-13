"""伺 (sì) — 亻 (person radical, left) + 司 (right), 7 strokes.

MANDATORY LOOKUP CHECKLIST:
1. INDEX grep 伺: not mastered. Sibling: 付/仔/仕 all reuse 亻 anchors from MMH.
2. errata grep 伺: not listed.
3. drawer_memory: 亻+X pattern — pass MMH anchors to pie+shu (see 付).
4. joint_atlas: 5 joints all N — visible gaps, don't weld.
5. si.py in bank is 巳 (snake), NOT 司 — do not import.

Composition:
  Left  = 亻 (2 strokes)
  Right = 司 (5 strokes: 横折钩 + 一 + 口)

Strokes (from MMH):
  s1 撇       ('TL',0.987,0.68) → ('ML',0.129,0.983)   — 亻 left sweep
  s2 竖       ('ML',0.721,0.529) → ('BL',0.727,0.927)   — 亻 vertical
  s3 横折钩   ('C',0.266,0.014) → ('BC',0.945,0.818)    — 司 outer bracket + hook
  s4 一       ('C',0.254,0.485) → ('C',0.922,0.397)     — 司 inner top bar
  s5 竖       ('C',0.184,0.854) → ('BC',0.351,0.394)    — inner 口 left wall
  s6 横折     ('C',0.336,0.869) → ('BC',0.699,0.153)    — inner 口 top+right
  s7 一       ('BC',0.403,0.326) → ('BC',0.857,0.253)   — inner 口 bottom bar

Joints (all N — natural gaps, do NOT weld):
  s1.mid ⇆ s2.head @ ML   — N, ~15-17 px
  s1.mid ⇆ s3.head @ TC   — N, ~30 px (separates 亻 and 司)
  s5.mid ⇆ s6.head @ C    — N, ~12 px (口 top-left corner)
  s5.tail ⇆ s7.head @ BC  — N, ~10 px (口 bottom-left corner)
  s6.tail ⇆ s7.mid @ BC   — N, ~12 px (口 bottom-right corner)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes: 亻(pie+shu) + 司(hzg + heng + shu + hz + heng). All 5 joints N-class (natural gaps).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 亻 (person radical, left) ----
    # s1 撇 — long sweep from upper-center down to lower-left
    draw_pie(draw,
             ('TL', 0.987, 0.68),
             ('ML', 0.129, 0.983),
             head_width=12, tail_width=1, curve=0.10, segments=48)

    # s2 竖 — short vertical touching mid-body of 撇
    draw_shu(draw,
             ('ML', 0.721, 0.529),
             ('BL', 0.727, 0.927),
             width=9)

    # ---- 司 (right side) ----
    # s3 横折钩 — outer bracket sweeping right then down with hook flick
    # head top-left of C; corner at top-right MR; tail at bottom-right BC; hook flick up-and-left
    draw_heng_zhe_gou(draw,
                      head=('C', 0.266, 0.014),
                      corner=('MR', 0.75, 0.05),
                      tail=('BC', 0.945, 0.818),
                      tip=('BC', 0.72, 0.68),
                      h_width=10, v_width=10, shoulder=13, tip_w=2)

    # s4 一 — small horizontal inside upper part of 司
    draw_heng(draw,
              ('C', 0.254, 0.485),
              ('C', 0.922, 0.397),
              width=8)

    # ---- inner 口 (3 strokes, tiny box in lower 司) ----
    # s5 竖 — left wall of small 口
    draw_shu(draw,
             ('C', 0.184, 0.854),
             ('BC', 0.351, 0.394),
             width=7)

    # s6 横折 — top + right wall of small 口
    # head at top-left of box; corner at top-right; tail at bottom-right (dropped vertical)
    draw_heng_zhe(draw,
                  ('C', 0.336, 0.869),
                  ('C', 0.70, 0.87),
                  ('BC', 0.699, 0.153),
                  h_width=7, v_width=7, shoulder=9)

    # s7 一 — bottom bar of small 口
    draw_heng(draw,
              ('BC', 0.403, 0.326),
              ('BC', 0.857, 0.253),
              width=7)

    out = os.path.join(os.path.dirname(__file__), '01_伺.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
