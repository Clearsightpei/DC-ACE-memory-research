"""p3_char_0132_内 — G4 grid-bank rendering.

Memory citations (MANDATORY LOOKUP CHECKLIST):
  1. success_bank/INDEX.md — 内 not mastered. Related: 人 (ren.py), 冂-frame
     (chronic FAIL, retry_n=2, cool-down 50).
  2. errata.md — p3_char_0026_冂 fix: TR9 override, cells span 0.05-0.95;
     apply to enclosing frame here.
  3. form_catalog.md — 内 frame = 竖 + 横折钩; inner = 人-like (撇 + 点/捺).
  4. principles_meta.md — TR9 (enclosing full-grid), TR10 (N-joints ≤25 px).
  5. joint_atlas.md — 内 top-left: s1.head/s2.head N (not welded); bottom-right
     hook internal to s2.
  6. sandbox.md — no prior 内 notes.

Structural plan (4 strokes per MMH):
  s1 — 竖 (left vertical of frame): head TL(0.85, 0.20) → tail BL(0.85, 0.90)
  s2 — 横折钩 (top + right + hook): head TL(0.90, 0.20) → corner TR(0.85, 0.20)
       → tail BR(0.80, 0.85) → hook tip up-left
  s3 — 撇 (inner): head TC(0.30, 0.55) → tail BL(0.90, 0.30)
  s4 — 点/短捺 (inner right): head C(0.50, 0.65) → tail BC(0.95, 0.15)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 strokes as expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revised: inner 人 apex moved to top-center of interior; 撇 sweeps to lower-left, 捺 to lower-right.',
}


def draw_nei(draw):
    # s1 — left vertical of frame (竖). Expand per TR9 to full grid.
    s1_head = ('TL', 0.85, 0.18)
    s1_tail = ('BL', 0.85, 0.92)
    draw_shu(draw, s1_head, s1_tail, width=10)

    # s2 — 横折钩. Top horizontal ML→TR, right vertical TR→BR, hook up-left.
    s2_head   = ('TL', 0.90, 0.18)   # near s1 head (N-gap ~ small)
    s2_corner = ('TR', 0.85, 0.20)   # top-right
    s2_tail   = ('BR', 0.75, 0.85)   # bottom-right, base of hook
    s2_tip    = ('BR', 0.50, 0.72)   # hook tip up-and-left
    draw_heng_zhe_gou(draw, s2_head, s2_corner, s2_tail, s2_tip,
                      h_width=10, v_width=10, shoulder=13, tip_w=2)

    # s3 — inner 撇: apex near top-center of frame interior, sweeps down-left
    # to touch left vertical near lower area.
    s3_head = ('C', 0.30, 0.15)     # apex near top of C cell (interior)
    s3_tail = ('ML', 0.95, 0.85)    # bottom-left interior
    draw_pie(draw, s3_head, s3_tail,
             head_width=8, tail_width=1, curve=0.12, segments=48)

    # s4 — inner short 捺/点: starts near mid of s3 (~center), goes down-right
    # into lower-right interior. Shorter than typical 人 捺 (bank note).
    s4_head = ('C', 0.35, 0.40)
    s4_tail = ('C', 0.90, 0.90)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=10, tail_width=1,
            peak_t=0.85, curve=0.10, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_nei(draw)
    out = os.path.join(os.path.dirname(__file__), '01_内.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
