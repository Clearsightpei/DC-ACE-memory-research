"""马 (mǎ, "horse") — 3-stroke, canonical hand-written primitive.

Chronic-cluster item, promoted at position 300 after 3 failed retries.

Baked anchors (do NOT tune):

  s1 = 横折 top-box top-bar:
     head    @ ('TL', 0.35, 0.30)  ( 35,  30)
     corner  @ ('TR', 0.05, 0.30)  (205,  30)  (row-lock with head — TR8 rule 5)
     tail    @ ('MR', 0.05, 0.20)  (205, 120)  (short right drop, col-lock)

  s2 = 竖折折钩 spine (top-box left wall → middle bar → right wall → hook):
     head    @ ('TL', 0.35, 0.30)  ( 35,  30)   (T-weld shared with s1.head)
     corner1 @ ('ML', 0.35, 0.40)  ( 35, 140)   (STRICT vertical — TR8 rule 6)
     corner2 @ ('MR', 0.05, 0.40)  (205, 140)   (middle bar — row-lock, sweeps right)
     hook_pt @ ('BR', 0.05, 0.20)  (205, 220)   (right wall bottom — col-lock)
     tip     @ ('BC', 0.65, 0.05)  (165, 205)   (hook flick UP-LEFT)

  s3 = 长横 bottom bar:
     head @ ('BL', 0.10, 0.55)  ( 10, 255)
     tail @ ('BR', 0.95, 0.55)  (295, 255)   (row-lock — TR8 rule 5)

Joints:
  s1.head ⇆ s2.head : T-weld at TL(0.35, 0.30)   [shared anchor tuple]
  s1.tail ⇆ s2.corner2 : near-weld at (205, ~140)  [closes top-right of box]
  s3 is a bottom bar ~35 px below s2.hook_pt — N-class visual span,
  reads as a distinct crossbar (not fused).

Root cause fix: B2-B5 马 failed with (a) top-box too small OR (b) S2
slanting instead of strict vertical OR (c) bottom heng overlapping
S2 hook_pt. This plan hits all three invariants — 170×110 top box,
strict-vertical S2 first and third legs, bottom heng ~35 px clear.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..')))

from _anchor import anchor_to_xy
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from shu_zhe_zhe_gou import draw_shu_zhe_zhe_gou


def draw_ma_horse(draw, color=(0, 0, 0)):
    SHARED_HEAD = ('TL', 0.35, 0.30)

    # s1 — 横折 top-box top-bar + short right drop
    draw_heng_zhe(draw,
                  SHARED_HEAD,
                  ('TR', 0.05, 0.30),
                  ('MR', 0.05, 0.20),
                  h_width=8, v_width=8, shoulder=11, color=color)

    # s2 — 竖折折钩 spine (uses stock primitive which requires heng-right;
    # here the middle bar DOES go right, so the primitive fits)
    draw_shu_zhe_zhe_gou(draw,
                         SHARED_HEAD,
                         ('ML', 0.35, 0.40),
                         ('MR', 0.05, 0.40),
                         ('BR', 0.05, 0.20),
                         ('BC', 0.65, 0.05),
                         v_width=8, h_width=8, shoulder=11,
                         hook_start_w=9, tip_w=1, color=color)

    # s3 — 长横 bottom bar (row-lock)
    draw_heng(draw, ('BL', 0.10, 0.55), ('BR', 0.95, 0.55),
              width=8, color=color)
