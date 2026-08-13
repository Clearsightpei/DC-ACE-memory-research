"""弋 (yì, "arrow", 3 strokes) — B2 pass.

Strokes:
  s1 — 横 (short 提-like top bar).
  s2 — 斜钩 (long slanted body with up-hook).
  s3 — 点 (small dot upper-right of the hook).

Joints:
  s1.mid ⇆ s2.mid @ C(0.418, 0.531) — P (welded). Belly placed AT the
  P-cross point + a 顿笔 disc (r=6) at the crossing.

Draw order matters: render s2 first, then s1 on top so the heng sits
over the crossing.
"""
from _anchor import anchor_to_xy
from xie_gou import draw_xie_gou
from heng import draw_heng
from dian import draw_dian


def draw_yi_arrow(draw,
                  s1_head=('ML', 0.48, 0.764), s1_tail=('MR', 0.095, 0.38),
                  s2_head=('TC', 0.02, 0.806),
                  s2_belly=('C', 0.42, 0.531),
                  s2_hook_pt=('BR', 0.581, 0.347),
                  s2_tip=('BR', 0.62, 0.15),
                  s3_head=('TC', 0.822, 0.694), s3_tail=('TR', 0.183, 0.97)):
    # Draw s2 spine first so heng sits on top.
    draw_xie_gou(draw, s2_head, s2_belly, s2_hook_pt, s2_tip,
                 head_w=6, belly_w=13, hook_start_w=11, tip_w=2)
    draw_heng(draw, s1_head, s1_tail, width=9)
    # P-weld disc at the crossing.
    p_cross = anchor_to_xy(s2_belly)
    r = 6
    draw.ellipse([p_cross[0]-r, p_cross[1]-r, p_cross[0]+r, p_cross[1]+r],
                 fill=(0, 0, 0))
    draw_dian(draw, s3_head, s3_tail, head_width=2, peak_width=8, curve=0.10)
