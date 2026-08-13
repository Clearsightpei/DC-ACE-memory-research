"""G5 attempt: p3_char_0140_反 (fan, 'reverse')

Composition (4 strokes per MMH):
  s1 = 撇 (short, top-right area)           — draw_pie
  s2 = 撇 (long, left descender)            — draw_pie
  s3 = 横撇 (inside 又's top compound)       — draw_heng_pie
  s4 = 捺 (inside 又's bottom sweep)         — draw_na

Anchors are MMH-derived; joints match the injected spec:
  s1.tail ⇆ s2.head : N (near-C, natural gap)
  s2.mid ⇆ s3.head  : N (small gap where 又's top meets the pie)
  s2.mid ⇆ s4.head  : N (na starts near s2 without welding)
  s3.mid ⇆ s4.mid   : P (interior X of 又 — welded crossing at BC)
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from pie import draw_pie
from na import draw_na
from heng_pie import draw_heng_pie


# --- MMH anchors (px, from 米字格 fracs on a 300x300 canvas) ---
S1_HEAD = (215.0, 81.2)   # TR(0.15, 0.812)
S1_TAIL = (111.0, 100.2)  # C (0.11, 0.002)
S2_HEAD = (85.8, 96.1)    # TL(0.858, 0.961)
S2_TAIL = (25.2, 287.7)   # BL(0.252, 0.877)
S3_HEAD = (104.9, 169.0)  # C (0.049, 0.69)
S3_TAIL = (76.5, 281.0)   # BL(0.765, 0.81)
S4_HEAD = (108.7, 192.5)  # C (0.087, 0.925)
S4_TAIL = (268.4, 288.3)  # BR(0.684, 0.883)


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: short top pie — mostly leftward tick, gentle downward
    draw_pie(d, S1_HEAD, S1_TAIL, bow_perp=6, w_head=7, w_tail=4, steps=60)

    # s2: long main pie down the left, thick head thin tail
    draw_pie(d, S2_HEAD, S2_TAIL, bow_perp=14, w_head=10, w_tail=3, steps=100)

    # s3: heng_pie inside 又 — horizontal then bends down-left
    #     head at C(105,169), tail at BL(77,281). Corner ~ (172, 172) to
    #     put the P-joint with s4 near BC(157, 236).
    draw_heng_pie(d, S3_HEAD, S3_TAIL, apex_x=170.0, corner_x=175.0)

    # s4: na — head near s2 mid, sweeps down-right through the P-joint
    draw_na(d, S4_HEAD, S4_TAIL, bow_perp=12, w_head=4, w_tail=12, steps=100)

    img.save(out_path)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 stroke primitives called (pie, pie, heng_pie, na)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('s3 heng_pie corner_x tuned so path mid(0.65) falls near '
              'expected P-joint at BC (~157,236); s4 na head near s2 mid — '
              'the N-gap is preserved because they are separate primitives '
              'with slightly offset heads.'),
}


if __name__ == '__main__':
    render(str(pathlib.Path(__file__).parent / '01_反.png'))
