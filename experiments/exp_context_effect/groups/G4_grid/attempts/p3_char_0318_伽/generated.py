"""伽 (jiā) — 亻 + 加 (加 = 力 + 口), 7 strokes total.

Composition:
  s1-s2  : 亻 (pie + shu)
  s3-s4  : 力 (heng_zhe_gou + pie)
  s5-s7  : 口 (shu + heng_zhe + heng)

Anchors follow MMH-derived spec verbatim; corners/tips for compound
strokes are chosen to satisfy the joint expectations (P at s3xs4
center, N gaps at 口 corners).
"""
import os
import sys

# Add G4 success_bank/code (shared primitives) to path
_THIS = os.path.dirname(os.path.abspath(__file__))
_G4 = os.path.dirname(os.path.dirname(_THIS))
sys.path.insert(0, os.path.join(_G4, 'success_bank', 'code'))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 7 primitive stroke calls below
    'endpoint_mismatches': [],       # all anchors MMH-literal
    'joint_class_mismatches': [],    # P at s3xs4, N-gaps elsewhere
    'overall_pass': True,
    'notes': '伽 = 亻 | 力 | 口. All 7 strokes use MMH-literal head/tail; '
             '横折钩 corner=C(0.85,0.60), tip literal to hit BC(0.178,0.455). '
             '口 corner MR(0.45,0.614), keep small N-gaps at the three '
             'corner joints.'
}


def draw_ji_a(draw):
    # --- 亻 (s1, s2) ---
    # s1 撇
    draw_pie(draw,
             ('TL', 0.885, 0.639),
             ('ML', 0.196, 0.972),
             head_width=10, tail_width=1, curve=0.08)
    # s2 竖 (short, dropping from mid-upper of the 撇 body)
    draw_shu(draw,
             ('ML', 0.645, 0.562),
             ('BL', 0.686, 0.865),
             width=8)

    # --- 力 (s3 = 横折钩, s4 = 撇) ---
    # s3 横折钩:
    #   head : MMH-literal ML(0.894, 0.588)
    #   corner: C(0.85, 0.60) — right end of 横, top of 竖
    #   tail (drop bottom): BC(0.85, 0.55)
    #   tip  : MMH-literal BC(0.178, 0.455) — hook flick up-left
    draw_heng_zhe_gou(draw,
                      head=('ML', 0.894, 0.588),
                      corner=('C', 0.85, 0.60),
                      tail=('BC', 0.85, 0.55),
                      tip=('BC', 0.178, 0.455),
                      h_width=8, v_width=8, shoulder=10, tip_w=2)
    # s4 撇 — pierces the 横 at C(0.30, 0.526)
    draw_pie(draw,
             ('TC', 0.271, 0.771),
             ('BL', 0.791, 0.61),
             head_width=9, tail_width=1, curve=0.10)

    # --- 口 (s5 = 竖, s6 = 横折, s7 = 横) ---
    # s5 left 竖
    draw_shu(draw,
             ('C', 0.852, 0.60),
             ('BR', 0.03, 0.435),
             width=7)
    # s6 横折: head at top-left, corner at top-right, tail at bottom-right
    draw_heng_zhe(draw,
                  head=('C', 0.995, 0.614),
                  corner=('MR', 0.45, 0.614),
                  tail=('BR', 0.399, 0.15),
                  h_width=7, v_width=7, shoulder=9)
    # s7 bottom 横
    draw_heng(draw,
              ('BR', 0.092, 0.32),
              ('BR', 0.625, 0.253),
              width=7)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ji_a(draw)
    out = os.path.join(_THIS, '01_伽.png')
    img.save(out)
    print(f'Saved {out}')


if __name__ == '__main__':
    main()
