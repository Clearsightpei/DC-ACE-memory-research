"""门 (mén, "door", 3 strokes) — B2 retry pass (graduated from B1 fail).

RETRY FIX vs B1: enclosing-radical layout enforced (TR2). All 3 strokes
clamped into the central 55% horizontal span; s1 dot sits as a lid ABOVE
s2 head; s3 top-bar continues at same y as s2 head so shape reads as
one enclosure, not scattered pieces.

Strokes:
  s1 — 点 (top-left lid).
  s2 — 竖 (short left wall).
  s3 — 横折钩 (top bar + right wall + up-left hook).

Joints: NONE (MMH declares 0 joints — small intentional pixel gaps).
"""
from dian import draw_dian
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou


def draw_men(draw,
             s1_head=('TL', 0.55, 0.55), s1_tail=('TL', 0.90, 0.90),
             s2_head=('TL', 0.65, 1.00), s2_tail=('BL', 0.65, 0.80),
             s3_head=('TC', 0.15, 1.00),
             s3_corner=('TR', 0.20, 1.00),
             s3_tail=('BR', 0.20, 0.80),
             s3_tip=('BR', 0.05, 0.55)):
    draw_dian(draw, s1_head, s1_tail, head_width=2, peak_width=10, curve=0.12)
    draw_shu(draw, s2_head, s2_tail, width=8)
    draw_heng_zhe_gou(draw, s3_head, s3_corner, s3_tail, s3_tip,
                      h_width=8, v_width=8, shoulder=11, tip_w=2)
