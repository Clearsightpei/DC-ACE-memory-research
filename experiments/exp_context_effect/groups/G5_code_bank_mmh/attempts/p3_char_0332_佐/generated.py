"""p3_char_0332_佐 — G5 attempt.

Recipe: P-A-006 — MMH anchors verbatim, stroke-primitive layer.
Bypasses whole-radical primitives (ren_left + gong_work) to keep MMH
anchors intact for a cleaner joint match. 7 strokes:
  s1: 亻 pie   (long TL→BL descender)
  s2: 亻 shu   (vertical descender)
  s3: 𠂇 heng  (short mid-right horizontal)
  s4: 𠂇 pie   (long TC→BL descender, welded-crossing s3 at C)
  s5: 工 heng  (top horizontal, right)
  s6: 工 shu   (short vertical, right)
  s7: 工 heng  (bottom horizontal, spans wide)

P-COMP-011 fit: 佐's right half (𠂇+工) is all straight-stroke
(heng/pie/shu), so P-A-006 stroke layer is appropriate.

Joint intents:
  s3 × s4 : P (welded cross at cell C)
  all others: N (natural gap; stroke primitives leave a small gap by
                 anchor spacing, no explicit weld)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 stroke-layer; 7 primitives call: pie, shu, heng, pie, heng, shu, heng.'
}

import sys
import pathlib

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


def draw(d: ImageDraw.ImageDraw):
    # s1: 亻 pie — TL(0.908,0.683) → BL(0.161,0.065)
    draw_pie(d, (91, 68), (16, 207),
             bow_perp=15, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu — ML(0.727,0.509) → BL(0.744,0.971)
    draw_shu(d, (73, 151), (74, 297), width=7)
    # s3: 𠂇 heng — C(0.204,0.477) → MR(0.481,0.354)
    draw_heng(d, (120, 148), (248, 135), width_head=8, width_tail=9)
    # s4: 𠂇 pie — TC(0.746,0.706) → BL(0.882,0.646)
    #   welded crossing with s3 at cell C (P joint).
    draw_pie(d, (175, 71), (88, 265),
             bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s5: 工 heng (top) — BC(0.526,0.106) → MR(0.367,0.995)
    draw_heng(d, (153, 211), (237, 200), width_head=8, width_tail=9)
    # s6: 工 shu — BC(0.84,0.153) → BC(0.813,0.646)
    draw_shu(d, (184, 215), (181, 265), width=6)
    # s7: 工 heng (bottom) — BC(0.154,0.777) → BR(0.728,0.733)
    draw_heng(d, (115, 278), (273, 273), width_head=9, width_tail=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw(d)
    out = HERE.parent / f'01_佐.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
