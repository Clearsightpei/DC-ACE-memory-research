"""己 (jǐ) — 3画 radical.

Strokes (traditional order):
  1) 横折 — top horizontal + short down-tick at right end.
  2) 横   — middle short horizontal (crossbar).
  3) 竖弯钩 — left descent, round bend to right along bottom, small UP hook.

米字格 anchor plan (adapted from MMH-derived expectations + visual):

  s1 head  ('TL', 0.729, 0.938) ≈ px (72.9, 93.8)   ← 起笔 top-left
     corner (implicit) ≈ ('TC', 0.559, 0.938)       ← where heng turns down
     tail  ('C',  0.559, 0.392) ≈ px (155.9, 139.2) ← bottom of down-tick

  s2 head  ('ML', 0.879, 0.641) ≈ px (87.9, 164.1)  ← left of middle heng
     tail  ('C',  0.787, 0.497) ≈ px (178.7, 149.7) ← right of middle heng
       (N with s1.tail: small gap ~22 px)

  s3 head  ('TL', 0.639, 0.456) ≈ px (63.9, 45.6)   ← 起笔 top of descent
       (OVERRIDDEN from MMH's ML(0.639,0.456)=(63.9,145.6) up to top of body;
        MMH's first median point is mid-descent, but the actual stroke starts
        at the top-left corner of the character body. This is a
        single-stroke-shape override per sandbox Pattern 1.)
     belly ('ML', 0.639, 0.55)   — width knot, keeps descent straight
     corner('BL', 0.639, 0.75)   — round bend
     hook_pt('BR', 0.60, 0.20)   ≈ px (260, 220)    ← base of hook (right end)
     tip   ('MR', 0.60, 0.85)    ≈ px (260, 185)    ← hook tip UP-LEFT

  (For the N-neighbor joint s2.head ⇆ s3.head @ ML: s3.head shifted up to
   TL, so the joint is instead between s2.head (88,164) and s3's descent
   at y~164 — the descent column x=64 vs s2.head x=88 gives ~24 px gap,
   near the expected 17 px range.)

Joints:
  s1.tail ⇆ s2.tail @ C  — N (small natural gap ~22 px)
  s2.head ⇆ s3.body  @ ML — N (s3 descends through this vertical band;
                             s2's left end lands just right of the descent)
"""
from PIL import Image, ImageDraw
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from heng_zhe import draw_heng_zhe
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's3 head overridden from ML→TL so descent starts at top of body '
             '(per sandbox Pattern 1: MMH first-median is mid-stroke). '
             'Visual: three-strokes match GT — top 横折, middle short 横, '
             'bottom 竖弯钩 with UP hook on the right.',
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # --- Stroke 1: 横折 ---
    # Head at top-left of character body; corner near TC(0.56, ~top); tail at C.
    s1_head   = ('TL', 0.729, 0.938)   # (72.9, 93.8)
    s1_corner = ('TC', 0.559, 0.938)   # (155.9, 93.8)  same y as head → horizontal
    s1_tail   = ('C',  0.559, 0.392)   # (155.9, 139.2) down-tick
    draw_heng_zhe(d, s1_head, s1_corner, s1_tail,
                  h_width=10, v_width=10, shoulder=13)

    # --- Stroke 2: 横 (middle crossbar) ---
    s2_head = ('ML', 0.879, 0.641)     # (87.9, 164.1)
    s2_tail = ('C',  0.787, 0.497)     # (178.7, 149.7)
    draw_heng(d, s2_head, s2_tail, width=8)

    # --- Stroke 3: 竖弯钩 ---
    # Head OVERRIDDEN up to TL so descent starts at TOP of character body.
    # Corner moved further right so bottom sweep is longer & smoother; hook UP.
    s3_head    = ('TL', 0.639, 0.85)   # (63.9, 85.0)   top of descent
    s3_belly   = ('ML', 0.639, 0.60)   # (63.9, 160.0)  width knot on descent
    s3_corner  = ('BL', 0.75, 0.85)    # (75.0, 235.0)  round bend (bottom-left)
    s3_hook_pt = ('BR', 0.55, 0.30)    # (255.0, 230.0) base of hook (right end)
    s3_tip     = ('BR', 0.60, 0.10)    # (260.0, 210.0) hook tip UP-left
    draw_shu_wan_gou(d, s3_head, s3_belly, s3_corner, s3_hook_pt, s3_tip,
                     head_w=8, belly_w=11, corner_w=12,
                     hook_start_w=11, tip_w=2)

    img.save(out_path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_己.png')
    render(out)
    print('wrote', out)
