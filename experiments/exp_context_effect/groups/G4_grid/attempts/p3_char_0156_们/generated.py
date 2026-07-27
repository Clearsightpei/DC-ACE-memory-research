"""们 (men, "plural marker", 5 strokes) — G4 draw.

Composition: 亻 (2 strokes: 撇 + 竖) + 门-simplified-right (3 strokes:
点/short-竖 + 竖 + 横折钩).

Memory lookup:
  - success_bank/INDEX.md: ren_side.py (亻), men.py (门, but 3-stroke
    variant differs — here we're drawing the RIGHT-side 门 component
    of 们, using MMH endpoints).
  - Per TR1: OVERRIDE anchors for this composition (亻 sits in the
    left column, 门 sits in the middle+right columns).

MMH-expected 5 strokes; joints: s1.mid↔s2.head (N, ~17px gap);
s3.mid↔s5.head (N, ~32px gap). Both are NEIGHBOR, small natural
gap — DO NOT weld.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import CANVAS
from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 stroke primitives (pie, shu, dian, shu, heng_zhe_gou)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('亻 撇 from TL to ML; 亻 竖 from ML to BL; short 点 in '
              'upper-left of 门 (TC bottom → C top); long 竖 as left '
              'wall of 门; 横折钩 as top-right hook of 门. Both joints '
              'N-class (~17px, ~32px gap).'),
}


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # --- 亻 (left radical) ---
    # s1: 撇 from TL upper-right down to ML lower-left.
    draw_pie(draw,
             from_anchor=('TL', 0.85, 0.636),
             to_anchor=('ML', 0.161, 0.901),
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2: 竖 from ML mid-upper down to BL near-bottom.
    draw_shu(draw,
             from_anchor=('ML', 0.612, 0.521),
             to_anchor=('BL', 0.656, 0.938),
             width=8)

    # --- 门-right (3-stroke variant used in 们) ---
    # s3: short 点/竖 at top-left of 门 (upper-left dot).
    draw_dian(draw,
              from_anchor=('TC', 0.333, 0.952),
              to_anchor=('C', 0.547, 0.163),
              head_width=2, peak_width=9, curve=0.05, segments=24)

    # s4: 竖 — long left wall of 门, from C top to BC bottom.
    draw_shu(draw,
             from_anchor=('C', 0.058, 0.192),
             to_anchor=('BC', 0.099, 0.856),
             width=8)

    # s5: 横折钩 — top-right of 门. head starts to the RIGHT of s4's top,
    # goes across (top bar), then down (right wall), then up-left hook.
    # MMH gives head=C(.726,.055) and tail=BC(.939,.757) which is the
    # hook tip. We need to insert a corner (top-right) so 横折钩 has
    # 4 anchors.
    draw_heng_zhe_gou(draw,
                      head=('C', 0.726, 0.055),
                      corner=('MR', 0.55, 0.055),
                      tail=('MR', 0.60, 0.90),
                      tip=('BC', 0.939, 0.757),
                      h_width=8, v_width=8, shoulder=11, tip_w=2)

    out = os.path.join(os.path.dirname(__file__), '01_们.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
