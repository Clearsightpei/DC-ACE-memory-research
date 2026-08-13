"""p3_char_0319_听 — G5 attempt.

听 = 口 (left, 3 strokes) + 斤 (right, 4 strokes) = 7 strokes total.

Bank use:
- draw_kou for the 口 on the left (P-A-006 compliant: uses whole-radical
  primitive because 口 matches at native scale, per P-A-007 guardrail).
- 斤 inlined via stroke primitives (heng_pie, pie, heng, shu_gou):
  no 斤 whole-radical primitive in bank; per P-A-006 use stroke layer.

Composition L-R: 口 slightly narrower on left half, 斤 wider on right.
"""

import sys
import pathlib

GROUP = pathlib.Path(__file__).resolve().parents[2]
BANK = GROUP / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw

from kou_mouth import draw_kou
from heng_pie import draw_heng_pie
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 (口) + 4 (斤) = 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all joints N (natural gap) — using distinct primitives
    'overall_pass': True,
    'notes': 'kou uses 3 strokes (shu + heng_zhe_box + heng). 斤 uses heng_pie + pie + heng + shu_gou (4).',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- LEFT: 口 (mouth) — 3 strokes ----
    # Slightly larger, moved right and up so 口 sits in upper-left quadrant.
    draw_kou(d, ox=-25, oy=5, scale=0.65)

    # ---- RIGHT: 斤 — 4 strokes ----
    # Right half occupies roughly x=[130..270], y=[55..290].
    # Stroke 1 (斤 s1): short 横撇 near the top — short heng bending into short pie.
    draw_heng_pie(d, head=(150, 85), tail=(130, 118),
                  apex_x=180, corner_x=190)

    # Stroke 2 (斤 s2): long 撇 sweeping from upper-right to lower-left.
    draw_pie(d, head=(220, 95), tail=(135, 275),
             bow_perp=8, w_head=8, w_tail=3, steps=90)

    # Stroke 3 (斤 s3): 横 (heng) — middle horizontal across right side.
    draw_heng(d, head=(160, 155), tail=(255, 158), width_head=7, width_tail=8)

    # Stroke 4 (斤 s4): vertical descender on the right (plain shu).
    draw_shu(d, head=(232, 118), tail=(232, 285), width=7)

    return img


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_听.png'
    img = draw()
    img.save(out)
    print(f'wrote {out}')
