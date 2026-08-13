"""p3_char_0320_伾 — G4 attempt.

Decomposition: 伾 = 亻 (2 strokes) + 丕 (5 strokes) = 7 strokes.
丕 = 不 (heng + pie + shu + dian) + bottom heng.

Memory index consulted:
- drawer_memory.md — 亻+X pattern; ren_side default anchors sit in
  TC/C, but MMH anchors for 伾 place 亻 far-left (TL/ML/BL column).
  Per B8 note (p3_char_0252_伊 FAIL), do NOT partially-override
  ren_side defaults — inline the 2 strokes with MMH anchors.
- MMH structural block — 7 strokes verbatim.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes: 亻 (pie+shu, MMH anchors inline) + 丕 (top heng, pie, shu welded across pie at C, right dian, bottom heng).'
}


def draw_pi(draw):
    # s1 — 亻 pie: TL(0.87, 0.656) -> BL(0.196, 0.03)
    draw_pie(draw, ('TL', 0.87, 0.656), ('BL', 0.196, 0.03),
             head_width=11, tail_width=1, curve=0.08, segments=48)
    # s2 — 亻 shu: ML(0.697, 0.518) -> BL(0.732, 0.965)
    draw_shu(draw, ('ML', 0.697, 0.518), ('BL', 0.732, 0.965), width=8)

    # s3 — 丕 top heng: C(0.198, 0.195) -> MR(0.508, 0.022)
    draw_heng(draw, ('C', 0.198, 0.195), ('MR', 0.508, 0.022), width=7)

    # s4 — 丕 pie: C(0.843, 0.157) -> BC(0.084, 0.306)
    draw_pie(draw, ('C', 0.843, 0.157), ('BC', 0.084, 0.306),
             head_width=10, tail_width=1, curve=0.06, segments=48)

    # s5 — 丕 vertical shu, welded P to s4 mid at cell C.
    #   head @ C(0.62, 0.479), tail @ BC(0.72, 0.563)
    draw_shu(draw, ('C', 0.62, 0.479), ('BC', 0.72, 0.563), width=8)

    # s6 — 丕 right dian: MR(0.062, 0.822) -> BR(0.64, 0.259)
    draw_dian(draw, ('MR', 0.062, 0.822), ('BR', 0.64, 0.259),
              head_width=3, peak_width=10, curve=0.05, segments=24)

    # s7 — 丕 bottom heng: BC(0.122, 0.807) -> BR(0.675, 0.792)
    draw_heng(draw, ('BC', 0.122, 0.807), ('BR', 0.675, 0.792), width=8)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_pi(d)
    out = os.path.join(_HERE, '01_伾.png')
    img.save(out)
    print('wrote', out)
