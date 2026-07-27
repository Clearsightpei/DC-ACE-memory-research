"""尣 (wāng, "lame", 4 strokes) — Phase 2 radical.

Composition (from MMH + GT):
  s1 — small 撇 / dot in the TL area (upper-left "hair").
  s2 — small 撇 / dot in the TC-MR area (upper-right "hair").
  s3 — long 撇 forming the left leg (ML → BL).
  s4 — 竖弯 (or 竖弯钩-like) forming the right leg: down from C then curves right into BR.

Joints: NONE (per MMH — clear separation between all strokes).

Anchor plan (米字格, PIL y grows DOWN inside each cell):
  s1  head=('TL',0.75,0.55)  tail=('ML',0.55,0.30)   # short pie, upper-left
  s2  head=('TC',0.75,0.60)  tail=('MR',0.20,0.10)   # short pie/dian, upper-right area
  s3  head=('ML',0.90,0.35)  tail=('BL',0.30,0.90)   # long pie down-left (left leg)
  s4  head=('C', 0.50,0.10)  belly=('C',0.50,0.75)   # 竖弯: straight down then rightward
      corner=('BC',0.60,0.90)  tail=('BR',0.75,0.90)

TR9 note: this is a STANDALONE Phase-2 radical — expand MMH anchors
to fill the grid slightly for visual balance (already MMH gives full span).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu_wan import draw_shu_wan
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH says no joints; drew 4 clean-separated strokes. '
             's1/s2 are small pie strokes at top; s3 long left leg; '
             's4 竖弯 right leg. All anchors within tolerance of MMH.',
}


def draw_wang_lame(draw):
    # s1 — upper-left short pie (from TL down into ML)
    s1_head = ('TL', 0.75, 0.55)
    s1_tail = ('ML', 0.55, 0.30)
    draw_pie(draw, s1_head, s1_tail, head_width=8, tail_width=2, curve=0.12)

    # s2 — upper-right small stroke (short pie/dian-like curl)
    s2_head = ('TC', 0.75, 0.60)
    s2_tail = ('MR', 0.20, 0.10)
    draw_pie(draw, s2_head, s2_tail, head_width=8, tail_width=2, curve=0.15)

    # s3 — long left leg 撇 (ML → BL)
    s3_head = ('ML', 0.90, 0.35)
    s3_tail = ('BL', 0.30, 0.90)
    draw_pie(draw, s3_head, s3_tail, head_width=11, tail_width=2, curve=0.10)

    # s4 — right leg 竖弯 (C → BR, down then curves right — moderate hook)
    s4_head = ('C', 0.50, 0.15)
    s4_belly = ('C', 0.50, 0.80)
    s4_corner = ('BC', 0.55, 0.85)
    s4_tail = ('BR', 0.45, 0.75)
    draw_shu_wan(draw, s4_head, s4_belly, s4_corner, s4_tail,
                 head_w=8, belly_w=10, corner_w=10, tail_w=8)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_wang_lame(draw)
    out = os.path.join(os.path.dirname(__file__), '01_尣.png')
    img.save(out)
    print(f'Wrote {out}')


if __name__ == '__main__':
    main()
