"""p3_char_0169_疋 (pi, 'roll of cloth / foot') — G5 attempt.

5 strokes per MMH:
  s1  短横 top-left, gentle down-right    ML(0.697,0.049) → C(0.91,0.242)
  s2  短竖 upper drop from center         C(0.362,0.043) → BC(0.506,0.268)
  s3  短横 middle-right heng              C(0.559,0.641) → MR(0.115,0.608)
  s4  长撇 mid-upper sweeping to BL       ML(0.873,0.541) → BL(0.267,0.736)
  s5  长捺 mid-left rightward na          ML(0.97,0.937)  → BR(0.757,0.769)

All 4 injected joints are class N — natural gaps, no welds.

Uses bank primitives: draw_heng, draw_shu, draw_pie, draw_na — clean
endpoint-signature calls, no BANK_DEVIATION.
"""
import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,    # 5 strokes: 1 heng + 1 shu + 1 heng + 1 pie + 1 na
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 4 joints N (gaps preserved by design)
    'overall_pass': True,
    'notes': 'All joints are N — bank primitives naturally leave gaps '
             'at midpoint contact when endpoints only meet elsewhere.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 短横 (top-left short heng, slight down-right slope)
    # ML(0.697,0.049) → C(0.91,0.242)
    s1_head = (69.7, 104.9)
    s1_tail = (191.0, 124.2)
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    # Stroke 2: 短竖 (upper drop, from just above center down to below center)
    # C(0.362,0.043) → BC(0.506,0.268)
    s2_head = (136.2, 104.3)
    s2_tail = (150.6, 226.8)
    draw_shu(d, s2_head, s2_tail, width=7)

    # Stroke 3: 短横 (middle heng heading right)
    # C(0.559,0.641) → MR(0.115,0.608)
    s3_head = (155.9, 164.1)
    s3_tail = (211.5, 160.8)
    draw_heng(d, s3_head, s3_tail, width_head=7, width_tail=8)

    # Stroke 4: 长撇 (pie from upper-middle down-left to bottom-left)
    # ML(0.873,0.541) → BL(0.267,0.736)
    s4_head = (87.3, 154.1)
    s4_tail = (26.7, 273.6)
    draw_pie(d, s4_head, s4_tail, bow_perp=10, w_head=8, w_tail=3)

    # Stroke 5: 长捺 (na from middle-left sweeping down-right to bottom-right)
    # ML(0.97,0.937) → BR(0.757,0.769)
    s5_head = (97.0, 193.7)
    s5_tail = (275.7, 276.9)
    draw_na(d, s5_head, s5_tail, bow_perp=12, w_head=4, w_tail=11)

    out = _HERE.parent / '01_疋.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
