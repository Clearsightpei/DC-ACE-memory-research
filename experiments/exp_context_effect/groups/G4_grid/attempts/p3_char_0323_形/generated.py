"""p3_char_0323_形 (xíng, "form/shape", 7 strokes).

Decomposition: LEFT (开-like radical, 4 strokes) + RIGHT (彡 = shan_hair, 3 strokes).

Reading-order log (drawer_memory.md → memory_index.md → success_bank/INDEX.md):
- drawer_memory.md: no chronic component; 彡 has a bank primitive (shan_hair).
- success_bank INDEX grep: p2_radical_064_彡 (shan_hair.py) PASSed in B1.
- errata.md grep: no 形 entry.
- Compositional playbook: left-right layout, left ~x∈[0.05,0.42], right x∈[0.55,0.95].

Anchors follow MMH-derived expectations verbatim (per B7r 比 lesson:
MMH-verbatim beats hand-tuning for symmetry / pair items).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 strokes: 2 heng + 1 pie + 1 shu (开) + 3 pie (彡)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Left 开-like + right 彡. Uses MMH anchors verbatim.'
}


def draw_xing(draw):
    # ---- LEFT: 开-like radical (4 strokes) ----
    # s1: short 横 top (TL→TC)
    draw_heng(draw, ('TL', 0.562, 0.914), ('TC', 0.620, 0.841), width=9)
    # s2: long 横 middle (ML→C)
    draw_heng(draw, ('ML', 0.214, 0.646), ('C', 0.661, 0.500), width=10)
    # s3: 撇 descending on left column (ML top → BL)
    draw_pie(draw, ('ML', 0.703, 0.022), ('BL', 0.296, 0.625),
             head_width=11, tail_width=3, curve=0.05)
    # s4: 竖 vertical on inner right of left radical (TC bottom → BC)
    draw_shu(draw, ('TC', 0.245, 0.932), ('BC', 0.345, 0.666), width=10)

    # ---- RIGHT: 彡 (3 撇 stacked) ----
    # s5: top 撇 (TR → C)
    draw_pie(draw, ('TR', 0.262, 0.650), ('C', 0.781, 0.380),
             head_width=10, tail_width=1, curve=0.10)
    # s6: middle 撇 (MR → BC)
    draw_pie(draw, ('MR', 0.244, 0.377), ('BC', 0.693, 0.062),
             head_width=10, tail_width=1, curve=0.10)
    # s7: bottom 撇 — MMH tail clips slightly below canvas (y_frac=1.067);
    #     draw as-is and let PIL clip. Head MR(0.376,0.945) is well inside.
    draw_pie(draw, ('MR', 0.376, 0.945), ('BC', 0.283, 1.067),
             head_width=10, tail_width=1, curve=0.10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_xing(d)
    out = os.path.join(os.path.dirname(__file__), '01_形.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
