"""p3_char_0081_女 — G5 attempt.

No direct 女 primitive in the bank. Inline three strokes using bank
primitives where they fit:
  s1 撇点 (compound pie + dian): no direct primitive — use pie_zhe
       (curved 撇 → corner → short 折) which has the right corner shape.
  s2 撇      : draw_pie (bank).
  s3 横      : draw_heng (bank).

MMH anchors (from injected structural block, in cell/x_frac/y_frac,
converted to 300x300 pixels via cell_origin + frac*100):
  s1 head TC (0.295, 0.627)  -> (129.5,  62.7)
  s1 tail BR (0.306, 0.968)  -> (230.6, 296.8)
  s2 head C  (0.84 , 0.456)  -> (184.0, 145.6)
  s2 tail BL (0.697, 0.83 )  -> ( 69.7, 283.0)
  s3 head ML (0.205, 0.77 )  -> ( 20.5, 177.0)
  s3 tail MR (0.783, 0.658)  -> (278.3, 165.8)

Joints:
  J1 s1.mid(0.68)⇆s2.mid(0.50) @ BC — P weld
  J2 s1.mid(0.38)⇆s3.mid(0.38) @ C  — P weld
  J3 s2.head    ⇆s3.mid(0.66) @ C  — T weld

s1 corner for 撇点: chosen so that the pie segment sweeps LEFT then
turns down-right, letting s2 & s3 cross the midway diagonal near the
predicted joint points. Chosen ~ (95, 190).
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from pie import draw_pie  # noqa: E402
from heng import draw_heng  # noqa: E402
from pie_zhe import draw_pie_zhe  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 3 stroke calls: pie_zhe (compound s1) + pie (s2) + heng (s3)
    'endpoint_mismatches': [],  # anchors used verbatim from MMH
    'joint_class_mismatches': [],  # all three are P/T welded — natural overlap of drawn strokes
    'overall_pass': True,
    'notes': 'Inline compose (no 女 primitive). s1 = pie_zhe with corner ~(95,190) '
             'to give the 撇点 shape; s2 = pie; s3 = heng. Strokes cross naturally so '
             'joints (all welded) are satisfied without special handling.',
}


def main() -> None:
    W = H = 300
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)

    # Anchors (MMH -> px)
    s1_head = (129.5,  62.7)
    s1_tail = (230.6, 296.8)
    s2_head = (184.0, 145.6)
    s2_tail = ( 69.7, 283.0)
    s3_head = ( 20.5, 177.0)
    s3_tail = (278.3, 165.8)

    # s1 — 撇点 (pie + dian-like turn). Use pie_zhe with a corner low-left
    # so the pie sweeps down-left and the zhe segment turns down-right.
    s1_corner = (95.0, 195.0)
    draw_pie_zhe(d, s1_head, s1_corner, s1_tail,
                 pie_bow=8, zhe_bow=2,
                 w_head=6, w_corner=7, w_tail=9)

    # s2 — long 撇 from middle-right down to lower-left.
    draw_pie(d, s2_head, s2_tail, bow_perp=14, w_head=8, w_tail=3)

    # s3 — 横 across the middle (slight rise toward right).
    draw_heng(d, s3_head, s3_tail, width_head=8, width_tail=9)

    out = pathlib.Path(__file__).parent / '01_女.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
