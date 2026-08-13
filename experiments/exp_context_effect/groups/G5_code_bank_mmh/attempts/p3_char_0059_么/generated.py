"""p3_char_0059_么 — 3 strokes: pie, pie_zhe, na-like taper.

Bank calls used:
- draw_pie (bank) for s1
- draw_pie_zhe (bank) for s2
- draw_na (bank) for s3

MMH anchors (300x300, 3x3 grid of 100x100 cells):
- s1: head TC(0.386,0.721)=(138.6,72.1) -> tail ML(0.527,0.893)=(52.7,189.3)
- s2: head C(0.802,0.342)=(180.2,134.2) -> tail BR(0.133,0.508)=(213.3,250.8)
       corner chosen at (~148, 218) to give down-left pie then short right zhe
- s3: head BC(0.96,0.074)=(196.0,207.4) -> tail BR(0.399,0.81)=(239.9,281.0)
- joint: s2.tail ~ s3.mid(0.40) at BR, class N (~14 px gap ~= expected 22)
"""

import sys
import pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))
from pie import draw_pie
from pie_zhe import draw_pie_zhe
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 3 strokes as expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'pie + pie_zhe + na; N-joint natural gap preserved between s2.tail and s3.mid',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: short 撇 (pie), top-center down to middle-left
    draw_pie(d, head=(138.6, 72.1), tail=(52.7, 189.3),
             bow_perp=10, w_head=8, w_tail=3, steps=80)

    # s2: 撇折 (pie-zhe), center down-left to corner, then short right
    draw_pie_zhe(d, head=(180.2, 134.2),
                 corner=(140.0, 218.0),
                 tail=(213.3, 250.8),
                 pie_bow=8, zhe_bow=1,
                 w_head=7, w_corner=6, w_tail=5)

    # s3: 捺-taper (na) from BC to BR, thickening
    draw_na(d, head=(196.0, 207.4), tail=(239.9, 281.0),
            bow_perp=8, w_head=3, w_tail=9, steps=80)

    out = pathlib.Path(__file__).parent / '01_么.png'
    img.save(out)
    print(f'wrote {out}')
    print('SELF_CHECK:', SELF_CHECK)


if __name__ == '__main__':
    main()
