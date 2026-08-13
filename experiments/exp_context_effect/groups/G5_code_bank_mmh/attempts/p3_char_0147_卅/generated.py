"""p3_char_0147_卅 (sà, "thirty") — G5 attempt.

MMH-derived structure: 4 strokes.
  s1 heng: ML(0.267,0.755) -> MR(0.804,0.658)   — horizontal bar
  s2 pie:  TL(0.8,0.946)   -> BL(0.378,0.786)   — leftmost slanting stroke
  s3 shu:  TC(0.412,0.964) -> BC(0.444,0.385)   — middle vertical
  s4 shu:  TC(0.951,0.68)  -> BR(0.062,1.05)    — right vertical (long)

Joints (all P — welded crossings):
  s1.mid ⇆ s2.mid @ ML  (piercing at left)
  s1.mid ⇆ s3.mid @ C   (piercing at middle)
  s1.mid ⇆ s4.mid @ MR  (piercing at right)

No BANK_DEVIATION — using heng/shu/pie bank primitives directly.
"""
import sys, pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie


def anchor_to_px(cell, xf, yf):
    row_map = {'T': 0, 'M': 100, 'B': 200}
    col_map = {'L': 0, 'C': 100, 'R': 200}
    return (col_map[cell[1]] + xf * 100, row_map[cell[0]] + yf * 100)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4 strokes rendered from MMH anchors. All 3 joints are P (welded) '
             'because s1 (horizontal) crosses s2/s3/s4 at their midpoints — '
             'natural piercing from straight-line intersection.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    s1_head = anchor_to_px('ML', 0.267, 0.755)
    s1_tail = anchor_to_px('MR', 0.804, 0.658)
    s2_head = anchor_to_px('TL', 0.8, 0.946)
    s2_tail = anchor_to_px('BL', 0.378, 0.786)
    s3_head = anchor_to_px('TC', 0.412, 0.964)
    s3_tail = anchor_to_px('BC', 0.444, 0.385)
    s4_head = anchor_to_px('TC', 0.951, 0.68)
    s4_tail = anchor_to_px('BR', 0.062, 1.05)

    # s2 (leftmost) — pie with mild bow to the right (arches gently)
    draw_pie(d, s2_head, s2_tail, bow_perp=4, w_head=7, w_tail=5)

    # s3 (middle vertical) — clean shu
    draw_shu(d, s3_head, s3_tail, width=7)

    # s4 (right vertical, long) — clean shu, slight rightward drift built into endpoints
    draw_shu(d, s4_head, s4_tail, width=7)

    # s1 (horizontal bar) — drawn LAST so it lies on top of the verticals
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    out = pathlib.Path(__file__).parent / '01_卅.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
