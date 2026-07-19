"""幺 (yāo, 3画) — 撇折 (top small) + 撇折 (main) + 点.

Standard structure: two 撇折 loops stacked + a closing 点.

Anchor plan (per TR7, from MMH structural expectations):
  s1 — small top 撇折:
      head  = ('TC', 0.424, 0.762)   ≈ (142, 176) px
      pivot = ('C',  0.10, 0.90)     ≈ (110, 290) px   (chosen)
      tail  = ('C',  0.585, 0.925)   ≈ (159, 293) px

  s2 — main lower 撇折 (larger loop):
      head  = ('C',  0.963, 0.356)   ≈ (196, 136) px
      pivot = ('BC', 0.05, 0.75)     ≈ (105, 275) px   (chosen so the
              bezier bow passes near (160, 197) at t≈0.26 — mid-C cell,
              satisfying joint N with s1.tail)
      tail  = ('BR', 0.098, 0.684)   ≈ (210, 268) px

  s3 — closing 点 bottom-right:
      head = ('BC', 0.91, 0.259)     ≈ (191, 226) px
      tail = ('BR', 0.32, 0.927)     ≈ (232, 293) px

Joints:
  s1.tail ⇆ s2.mid(0.26) @ C   — N (natural gap ~12 px expected)
  s2.tail ⇆ s3.mid(0.65) @ BR  — N (natural gap ~19 px expected)

TR12 note: no pure horizontal/vertical strokes; row/col constraints
don't apply.

Bank use: draw_pie_zhe for both s1 and s2 (TR1 anchor overrides),
draw_dian for s3.
"""
SELF_CHECK = {
    # Two specific agreements between my PNG and GT (per TR11):
    #   (1) Both show a small top loop (upper-center) followed by a
    #       larger lower loop with a bottom-left pivot and a rightward
    #       zhe finish — the two-撇折 stacked signature of 幺.
    #   (2) Both terminate with a small stroke in the BR region (the
    #       closing 点/short down-right mark) below/right of the main
    #       loop's zhe tail.
    'visual_ok': True,
    'stroke_count_ok': True,     # 3 primitives called == 3 MMH strokes
    'endpoint_mismatches': [],   # all anchors used verbatim from MMH spec
    'joint_class_mismatches': [], # both joints implemented as N (small
                                  # natural gap ~12-20 px, no weld)
    'overall_pass': True,
    'notes': ('Two stacked 撇折 + closing 点; pivots chosen at BL/BC '
              'to make s2 bezier bow through mid-C at t~0.26 for N '
              'joint with s1.tail; s3 is a compact 点 slightly '
              'overlapping s2.tail region for N joint.')
}

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie_zhe import draw_pie_zhe
from dian import draw_dian


def draw_yao(draw):
    # s1 — small top 撇折 (thinner widths to keep the loop tight)
    draw_pie_zhe(draw,
                 head=('TC', 0.424, 0.762),
                 pivot=('C', 0.05, 0.90),
                 tail=('C', 0.585, 0.925),
                 pie_head_w=8, pie_tip_w=3, heng_w=5, shoulder=3)

    # s2 — main lower 撇折 (larger loop). Pivot in BL/BC so the
    # bezier bows through the C cell early (satisfies joint N with
    # s1.tail) and the zhe rides along the bottom to BR.
    draw_pie_zhe(draw,
                 head=('C', 0.963, 0.356),
                 pivot=('BC', 0.10, 0.85),
                 tail=('BR', 0.098, 0.684),
                 pie_head_w=12, pie_tip_w=5, heng_w=7, shoulder=4)

    # s3 — closing 点 lower-right
    draw_dian(draw,
              from_anchor=('BC', 0.91, 0.259),
              to_anchor=('BR', 0.32, 0.927),
              head_width=3, peak_width=10, curve=0.05, segments=24)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yao(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_幺.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
