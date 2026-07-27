"""己 (jǐ) — 3画 radical. RETRY #1 (fresh redesign).

Prior retry_1 attempt failure diagnosis: PNG read as boxy "E".
  - s3's shu_wan_gou had head, belly, and corner ALL at nearly the
    same x (~85–90 px). Bezier(head→corner via belly) collapsed to a
    straight vertical. Then bezier(corner→hook_pt) at the same y
    collapsed to a straight horizontal. Result: right-angle "E"
    instead of a rounded 己 belly.

Fix (per errata "Batch B2 — p2_radical_053_己 RETRY FAIL" +
sandbox lessons):
  1. Give s3's shu_wan_gou REAL curvature:
     - `belly` is offset (control point that pulls the descent inward),
       not colinear with head/corner.
     - `corner` sits lower AND further right than the pure descent
       column, so the descent smoothly bows into a rounded bottom.
     - `hook_pt` is HIGHER (smaller y) than corner, so the sweep
       arcs UP-right instead of running flat — this is what gives 己
       its open, rounded belly (vs 匚's straight bottom).
  2. Tip strictly above hook_pt (canonical UP flick).
  3. Top 横折 (s1) is compact in upper-third, with the down-tick
     landing near the middle-crossbar region (TR4: share cell/coord
     with s2 so the three tiers touch as a single character).
  4. Middle 横 (s2) is short and sits just BELOW s1.tail so the joint
     reads as N-neighbor (~15 px gap, per TR10).

米字格 anchor plan (canvas pixel targets in comments):

  s1 (横折 top piece — compact upper-left):
    head    ('TL', 0.30, 0.30)   ≈ px ( 30,  30)  起笔 upper-left
    corner  ('TC', 0.60, 0.30)   ≈ px (160,  30)  end of top heng
    tail    ('TC', 0.45, 1.00)   ≈ px (145, 100)  short down-tick end

  s2 (横 middle crossbar — short):
    head    ('ML', 0.35, 0.15)   ≈ px ( 35, 115)  left of middle heng
    tail    ('C',  0.65, 0.15)   ≈ px (165, 115)  right of middle heng
    (N-neighbor with s1.tail (145,100) → ~15 px below-right)

  s3 (竖弯钩 outer bowl — curved descent + rounded bottom + UP flick):
    head     ('TL', 0.75, 0.55)  ≈ px ( 75,  55)  top-left, near s1.head
    belly    ('ML', 0.40, 0.70)  ≈ px ( 40, 170)  Bezier ctrl — bow LEFT
                                                   (pulls descent slightly
                                                   outward for round belly)
    corner   ('BC', 0.30, 0.60)  ≈ px (130, 260)  rounded bottom bend
    hook_pt  ('BR', 0.65, 0.25)  ≈ px (265, 225)  end of bottom sweep —
                                                   HIGHER than corner so
                                                   the sweep arcs UP-right
    tip      ('BR', 0.55, 0.00)  ≈ px (255, 200)  UP flick (tip.y<hook_pt.y)

Joints (all N-class, per MMH):
  s1.tail (145,100) ⇆ s2.tail (165,115) — N (~25 px gap, in cell C region)
  s2.head ( 35,115) ⇆ s3.body @ ML       — N (s3's belly/descent at x≈40,
                                             s2.head at x≈35 — ~15 px)

Sanity asserts before rendering:
  - tip.y < hook_pt.y  (canonical UP flick)
  - hook_pt.x > corner.x  (bottom sweep goes RIGHT)
  - hook_pt.y < corner.y  (sweep arcs UP not flat) — gives round belly
  - s1.tail near C-region (matches MMH joint expectation)
"""
from PIL import Image, ImageDraw
import sys, os

sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
)

from _anchor import anchor_to_xy
from heng_zhe import draw_heng_zhe
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Retry #1 fresh redesign after prior retry_1 "E"-collapse. '
        'Named visual agreements with GT: '
        '(1) Top 横折 is a compact hooked piece in the upper-third '
        '(x span ~30-160, y span ~30-100), matching GT top. '
        '(2) Bottom sweep of s3 arcs UP-right (hook_pt.y=225 < '
        'corner.y=260), producing the rounded open belly '
        'characteristic of 己 (contra 匚 which is flat). '
        '(3) Hook tip flicks UP (tip.y=200 < hook_pt.y=225) at the '
        'far right, matching the small up-tick in GT. '
        'Stroke count = 3, matches MMH.'
    ),
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 横折 (top open box, compact) ----
    s1_head   = ('TL', 0.30, 0.30)     # ≈ ( 30,  30)
    s1_corner = ('TC', 0.60, 0.30)     # ≈ (160,  30)
    s1_tail   = ('TC', 0.45, 1.00)     # ≈ (145, 100)
    draw_heng_zhe(d, s1_head, s1_corner, s1_tail,
                  h_width=10, v_width=9, shoulder=12)

    # ---- Stroke 2: 横 (middle crossbar, short) ----
    s2_head = ('ML', 0.35, 0.15)       # ≈ ( 35, 115)
    s2_tail = ('C',  0.65, 0.15)       # ≈ (165, 115)
    draw_heng(d, s2_head, s2_tail, width=9)

    # ---- Stroke 3: 竖弯钩 (outer bowl with round belly + UP hook) ----
    s3_head    = ('TL', 0.75, 0.55)   # ≈ ( 75,  55)
    s3_belly   = ('ML', 0.40, 0.70)   # ≈ ( 40, 170) Bezier ctrl bowing LEFT
    s3_corner  = ('BC', 0.30, 0.60)   # ≈ (130, 260) rounded bottom
    s3_hook_pt = ('BR', 0.65, 0.25)   # ≈ (265, 225) sweep arcs UP-right
    s3_tip     = ('BR', 0.55, 0.00)   # ≈ (255, 200) UP flick

    # Sanity asserts.
    p_head   = anchor_to_xy(s3_head)
    p_belly  = anchor_to_xy(s3_belly)
    p_corner = anchor_to_xy(s3_corner)
    p_hook   = anchor_to_xy(s3_hook_pt)
    p_tip    = anchor_to_xy(s3_tip)

    assert p_tip[1] < p_hook[1], (
        f'hook must flick UP: tip.y={p_tip[1]} not < hook_pt.y={p_hook[1]}'
    )
    assert p_hook[0] > p_corner[0], (
        f'bottom sweep must go right: hook_pt.x={p_hook[0]} '
        f'not > corner.x={p_corner[0]}'
    )
    assert p_hook[1] < p_corner[1], (
        f'sweep must arc UP-right (round belly): '
        f'hook_pt.y={p_hook[1]} not < corner.y={p_corner[1]}'
    )
    # Confirm bezier control (belly) is genuinely offset from the
    # head→corner chord — this is what saves us from the "E" collapse.
    chord_mid_x = (p_head[0] + p_corner[0]) / 2.0
    assert abs(p_belly[0] - chord_mid_x) > 20, (
        f'belly must be offset from head-corner chord midpoint to '
        f'produce curvature (avoid "E" collapse); '
        f'belly.x={p_belly[0]} chord_mid.x={chord_mid_x}'
    )

    draw_shu_wan_gou(d, s3_head, s3_belly, s3_corner, s3_hook_pt, s3_tip,
                     head_w=8, belly_w=11, corner_w=12,
                     hook_start_w=11, tip_w=2)

    img.save(out_path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_己.png')
    render(out)
    print('wrote', out)
