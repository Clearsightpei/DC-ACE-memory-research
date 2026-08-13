"""山 (shān, "mountain", 3 strokes: 竖 + 竖折 + 竖) — B1 pass.

Strokes:
  s1 — middle vertical 竖 (tallest).
  s2 — 竖折 (left wall + bottom horizontal).
  s3 — right vertical 竖 (shorter than middle).

Joints: both N-class (~15-25 px small pixel gaps).
"""
from shu import draw_shu
from shu_zhe import draw_shu_zhe


def draw_shan(draw,
              S1_HEAD=('TC', 0.383, 0.809), S1_TAIL=('BC', 0.444, 0.391),
              S2_HEAD=('ML', 0.574, 0.834),
              S2_CORNER=('BL', 0.55, 0.70),
              S2_TAIL=('BR', 0.309, 0.306),
              S3_HEAD=('MR', 0.373, 0.564), S3_TAIL=('BR', 0.338, 0.833)):
    draw_shu(draw, S1_HEAD, S1_TAIL, width=10)
    draw_shu_zhe(draw, S2_HEAD, S2_CORNER, S2_TAIL,
                 v_width=10, h_width=10, shoulder=13)
    draw_shu(draw, S3_HEAD, S3_TAIL, width=10)
