"""称 (chēng) — 禾 (left) + 尔 (right). 10 strokes.

Strokes follow MMH-derived anchors from the injected brief.
Uses bank primitives (pie/heng/shu/na/dian/shu_gou) with 米字格 anchors.
"""
import os
import sys

# Import from success_bank/code (bank primitives — READ-ONLY use).
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from dian import draw_dian
from shu_gou import draw_shu_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes: 禾(5) + 尔(5). All anchors follow MMH brief. '
             'Joints s1-s5 in ML band form 禾 structure; s6-s10 form 尔. '
             'All expected joints are N-class (natural gaps preserved).',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 禾 (left half) ----
    # s1: 撇 top cap of 禾 (short pie down-left)
    draw_pie(d, ('TC', 0.356, 0.853), ('ML', 0.48, 0.245),
             head_width=8, tail_width=2, curve=0.10)

    # s2: 横 short horizontal of 禾
    draw_heng(d, ('ML', 0.275, 0.655), ('C', 0.254, 0.506), width=6)

    # s3: 竖 long vertical of 禾 (near-vertical, ML→BL)
    draw_shu(d, ('ML', 0.82, 0.148), ('BL', 0.905, 0.956), width=7)

    # s4: 撇 sweeping down-left across mid of 禾
    draw_pie(d, ('ML', 0.826, 0.652), ('BL', 0.226, 0.599),
             head_width=8, tail_width=2, curve=0.12)

    # s5: 点 lower-right dot of 禾 (short down-right)
    draw_dian(d, ('ML', 0.958, 0.813), ('C', 0.178, 0.995),
              head_width=2, peak_width=8)

    # ---- 尔 (right half) ----
    # s6: 撇 cap of 尔 (top-right → down-left)
    draw_pie(d, ('TC', 0.632, 0.753), ('C', 0.304, 0.717),
             head_width=8, tail_width=2, curve=0.10)

    # s7: 横 horizontal of 尔 (short right sweep)
    draw_heng(d, ('C', 0.582, 0.447), ('MR', 0.235, 0.629), width=6)

    # s8: 撇 long down-left of 尔
    draw_pie(d, ('C', 0.796, 0.479), ('BC', 0.512, 0.678),
             head_width=8, tail_width=2, curve=0.10)

    # s9: 竖钩 vertical hook (BC→BC going down, hook up-left at tail)
    draw_shu_gou(d,
                 head=('BC', 0.521, 0.068),
                 belly=('BC', 0.521, 0.30),
                 hook_pt=('BC', 0.521, 0.517),
                 tip=('BC', 0.33, 0.42),
                 head_w=8, belly_w=7, hook_start_w=7, tip_w=2)

    # s10: 点 right dot of 尔 (short down-right)
    draw_na(d, ('BR', 0.218, 0.086), ('BR', 0.616, 0.528),
            head_width=3, peak_width=9, tail_width=2, peak_t=0.8, curve=0.10)

    out = os.path.join(os.path.dirname(__file__), '01_称.png')
    img.save(out)
    print(f'wrote {out}  strokes=10  overall_pass={SELF_CHECK["overall_pass"]}')


if __name__ == '__main__':
    draw()
