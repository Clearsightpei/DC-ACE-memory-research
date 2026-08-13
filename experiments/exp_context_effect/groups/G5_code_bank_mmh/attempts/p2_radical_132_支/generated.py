"""G5 attempt: p2_radical_132_支 (支, 4-stroke radical).

Composition: 十 (top: heng + shu) + 又 (bottom: heng_pie + na).
All 4 strokes come from stroke-bank primitives (draw_heng, draw_shu,
draw_heng_pie, draw_na). No BANK_DEVIATION — bank stroke primitives
fit cleanly with MMH endpoint anchors.

Note: not calling draw_you() whole-radical because MMH gives us
different anchor spread and joint geometry for 又-inside-支
(top-heng is longer, pie tail moved right). Composing from stroke
bank preserves anchor fidelity — same lesson validated in B2 for
日/囗.
"""

import pathlib
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from heng import draw_heng
from shu import draw_shu
from heng_pie import draw_heng_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives called, matches MMH count
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke1 heng head=ML(88,127) tail=MR(207,112); '
             'stroke2 shu head=TC(134,55) tail=C(138,174); '
             'stroke3 heng_pie head=ML(88,187) tail=BL(47,293), '
             'apex_x=hx+95 keeps 又-heng modest so P-joint with na lands ~BC(146,245); '
             'stroke4 na head=BL(93,206) tail=BR(280,297). '
             'Joints: (s1.mid,s2.mid)=P at C(~145,120), '
             '(s2.tail,s3.start)=N gap ~13.5px (bottom of 十 does not touch top of 又), '
             '(s3.pie,s4.na)=P weld in cell BC.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # --- Stroke 1: heng (top of 十) ---
    s1_head = (87.6, 126.9)
    s1_tail = (207.4, 111.9)
    draw_heng(d, s1_head, s1_tail, width_head=9, width_tail=10)

    # --- Stroke 2: shu (vertical of 十) ---
    s2_head = (133.9, 55.1)
    s2_tail = (138.3, 173.7)
    draw_shu(d, s2_head, s2_tail, width=7)

    # --- Stroke 3: heng_pie (top of 又) ---
    # apex_x controls how far right the 横 portion extends before cornering
    # into the pie. Default is hx+130 which overshoots for 支; use hx+95
    # so the 又-heng lands about half-canvas wide and the pie corners
    # cleanly for the P-joint with the na.
    s3_head = (87.6, 186.9)
    s3_tail = (46.6, 292.7)
    draw_heng_pie(d, s3_head, s3_tail, apex_x=s3_head[0] + 95,
                  corner_x=s3_head[0] + 92)

    # --- Stroke 4: na (bottom-right sweep of 又) ---
    s4_head = (92.6, 206.2)
    s4_tail = (279.5, 297.4)
    draw_na(d, s4_head, s4_tail, bow_perp=12, w_head=4, w_tail=12, steps=90)

    out = pathlib.Path(__file__).parent / '01_支.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
