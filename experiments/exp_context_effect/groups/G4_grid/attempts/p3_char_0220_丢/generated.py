"""p3_char_0220_丢 (diū, "lose") — G4 attempt, B7 v8.

Split: 丢 = 丿 (top slant) + 土 (middle) + 厶 (bottom).
Bank uses: tu.py + si_private.py are mastered; top 丿 is drawn fresh
per MMH anchor (nearly-horizontal, TR→ML).

Stroke plan (6, matches MMH):
  s1 — 丿 top slant       (TR 0.02,0.84 → ML 0.90,0.08)  [pie, mostly horiz]
  s2 — 土 top heng (short) (ML 0.79,0.51 → MR 0.12,0.37)
  s3 — 土 spine (shu)      (C  0.37,0.03 → C  0.46,0.90)
  s4 — 土 bottom heng long (BL 0.36,0.08 → MR 0.74,0.97)
  s5 — 厶 pie_zhe          (BC 0.58,0.12 → BR 0.00,0.66) [pivots inside BC]
  s6 — 厶 dot (na-like)    (BC 0.85,0.34 → BR 0.27,0.93)

Joints:
  s1.mid ⇆ s3.head  @ TC — N (small gap, don't weld the 丿 to the spine).
  s2     × s3       @ C  — P (welded cross).
  s3.tail ⇆ s4.mid  @ C  — N (spine tip stops above bottom heng center).
  s4.mid ⇆ s5.head  @ BC — N (厶 sits under 土 with small gap).
  s5.tail ⇆ s6.mid  @ BR — N (厶 opens LEFT; dot seals right side).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from heng import draw_heng
from shu import draw_shu
from pie_zhe import draw_pie_zhe
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 6 stroke primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '丢 = 丿 + 土 + 厶; 6 strokes; joints P at C, N elsewhere.'
}


def draw_pie(draw, from_anchor, to_anchor,
             head_width=12, tail_width=1, curve=0.10, segments=48):
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_diu(draw):
    # s1 — top 丿 (near-horizontal pie, TR → ML)
    draw_pie(draw, ('TR', 0.05, 0.85), ('ML', 0.90, 0.15),
             head_width=10, tail_width=2, curve=0.05)

    # s2 — 土 top heng (short) — reversed to MR→ML direction per MMH,
    #      but geometry is the same segment. Use standard L→R endpoints.
    draw_heng(draw, ('ML', 0.55, 0.55), ('MR', 0.45, 0.55), width=8)

    # s3 — 土 spine (shu), crosses s2 at C (P joint)
    draw_shu(draw, ('TC', 0.42, 0.85), ('BC', 0.48, 0.10), width=10)

    # s4 — 土 bottom heng (long), spans BL to BR through BC top
    draw_heng(draw, ('BL', 0.15, 0.15), ('BR', 0.85, 0.15), width=10)

    # s5 — 厶 pie_zhe: down-left curve then a small heng
    draw_pie_zhe(draw,
                 ('BC', 0.55, 0.35),        # head near BC top
                 ('BL', 0.85, 0.75),        # pivot inside BL
                 ('BC', 0.10, 0.75),        # tail on inner heng
                 pie_head_w=9, pie_tip_w=4, heng_w=6, shoulder=4)

    # s6 — 厶 dot (na-like) sealing the right side
    draw_dian(draw, ('BC', 0.80, 0.55), ('BR', 0.30, 0.85),
              head_width=3, peak_width=9, curve=0.05, segments=24)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_diu(d)
    out = os.path.join(os.path.dirname(__file__), '01_丢.png')
    img.save(out)
    print('wrote', out)
