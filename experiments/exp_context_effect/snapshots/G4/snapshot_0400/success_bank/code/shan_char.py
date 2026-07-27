"""山 (shān, "mountain" as Phase-3 CHAR, 3画) — B4 main promotion.

Thin wrapper: char-context reuse of shan.py (Phase-2 radical 山).
Character 山 == radical 山 shape. TR1: pass MMH-injected anchors
explicitly rather than calling with defaults.

Strokes: 竖 + 竖折 + 竖.
Joints: s1.tail ⇆ s2.mid @ BC : N (~17 px);
        s2.tail ⇆ s3.mid @ BR : N (~19 px).
"""
from shan import draw_shan


def draw_shan_char(draw,
                   S1_HEAD=('TC', 0.383, 0.809), S1_TAIL=('BC', 0.444, 0.391),
                   S2_HEAD=('ML', 0.574, 0.834),
                   S2_CORNER=('BL', 0.55, 0.70),
                   S2_TAIL=('BR', 0.309, 0.306),
                   S3_HEAD=('MR', 0.373, 0.564), S3_TAIL=('BR', 0.338, 0.833)):
    draw_shan(draw,
              S1_HEAD=S1_HEAD, S1_TAIL=S1_TAIL,
              S2_HEAD=S2_HEAD, S2_CORNER=S2_CORNER, S2_TAIL=S2_TAIL,
              S3_HEAD=S3_HEAD, S3_TAIL=S3_TAIL)
