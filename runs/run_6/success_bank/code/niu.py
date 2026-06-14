"""牛 (niú, "ox/cow") — composed character. 4 strokes.

Mastered: run_6 c59, panel 3/3 YES (calligraphy-aware with per-joint
class summary).

Joints (from MMH classify_joints):
- s1.mid ⇆ s2.head @ ML: N (neighbor, ~17 px gap)
- s2.mid ⇆ s4.mid @ C:   P (piercing)
- s3.mid ⇆ s4.mid @ BC:  P (piercing)

Reuse:
    from niu import draw_niu
    draw_niu(t)
"""
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu


def draw_niu(t):
    draw_pie(t, ('TL', 0.708, 0.772), ('ML', 0.28, 0.756))
    draw_heng(t, ('ML', 0.816, 0.328), ('MR', 0.392, 0.1))
    draw_heng(t, ('BL', -0.084, 0.288), ('BR', 1.14, 0.048))
    draw_shu(t, ('TC', 0.36, 0.236), ('BC', 0.544, 1.3))
