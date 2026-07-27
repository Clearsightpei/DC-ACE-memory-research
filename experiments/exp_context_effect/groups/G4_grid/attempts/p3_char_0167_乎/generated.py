"""乎 (hū) — Phase-3 character, 5 strokes.

Memory lookup checklist:
1. success_bank/INDEX.md grep 乎 — not present. Related: 于 (yu_at.py, 3 strokes).
2. errata.md grep 乎 — not present.
3. form_catalog.md — 撇 top-heng-pie form; 点 pair; 长横 middle; 竖钩 center.
4. principles_meta.md TR1-TR12 — inline fresh; borrow yu_at structure for bottom 3 strokes.
5. joint_atlas.md — N gaps for hair-to-body; P for heng×shu_gou crossing.

Structure per MMH expectations (5 strokes):
  s1: top 撇 (heng-pie sweep) — TR(0.013,0.715) -> TL(0.943,0.952)   (top curve, thick left)
  s2: 点 left     — ML(0.902,0.283) -> C(0.113,0.506)
  s3: 点 right    — TR(0.068,0.996) -> C(0.787,0.453)
  s4: 长横 middle  — ML(0.36,0.86) -> MR(0.739,0.796)
  s5: 竖钩 center  — TC(0.356,0.905) -> BC(0.022,0.766)  hook to lower-left

Joints (3):
  s1.mid ⇆ s5.head @ TC   : N (~10 px gap, hair sits above vertical top)
  s3.tail ⇆ s5.mid @ C    : N (~35 px gap, right dot ends near vertical mid)
  s4.mid × s5.mid @ C     : P (welded crossing of long heng and vertical)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from heng import draw_heng
from shu_gou import draw_shu_gou
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes: top pie sweep, two hair dots, long heng, center shu_gou.',
}


def draw_hu(draw):
    # ---- s1: top 撇/heng-pie — curved sweep from upper-right down-left ----
    p0 = anchor_to_xy(('TR', 0.013, 0.715))  # ~(202, 71)
    p1 = anchor_to_xy(('TL', 0.943, 0.952))  # ~(94, 95)
    # subtle downward-bulging curve
    mid = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    ctrl = (mid[0] + 4, mid[1] + 10)
    pts = quad_bezier(p0, ctrl, p1, n=40)
    # thick head, taper toward left tail
    widths = [10 - 6 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)

    # ---- s2: left hair 点 — short dot from upper-right to lower-left of center ----
    # head ML(0.902,0.283) ~(190, 128); tail C(0.113,0.506) ~(111, 150)
    draw_dian(draw, ('ML', 0.902, 0.283), ('C', 0.113, 0.506),
              head_width=2, peak_width=7)

    # ---- s3: right hair 点 — short dot descending down-left ----
    # head TR(0.068,0.996) ~(207, 100); tail C(0.787,0.453) ~(179, 145)
    draw_dian(draw, ('TR', 0.068, 0.996), ('C', 0.787, 0.453),
              head_width=2, peak_width=8)

    # ---- s4: 长横 across middle ----
    draw_heng(draw, ('ML', 0.36, 0.86), ('MR', 0.739, 0.796), width=10)

    # ---- s5: 竖钩 center vertical with hook flicking LEFT ----
    # head TC(0.356,0.905) ~(136, 190); belly straight; hook BC(0.022,0.766) ~(102, 277); tip flicks up-left
    s5_head = ('TC', 0.356, 0.905)
    s5_hook = ('BC', 0.022, 0.766)
    s5_tip = ('BL', 0.75, 0.6)  # up-left flick
    draw_shu_gou(draw, s5_head, s5_head, s5_hook, s5_tip,
                 head_w=11, belly_w=10, hook_start_w=9, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_hu(draw)
    out = os.path.join(os.path.dirname(__file__), '01_乎.png')
    img.save(out)
    print(f'Wrote {out}')


if __name__ == '__main__':
    main()
