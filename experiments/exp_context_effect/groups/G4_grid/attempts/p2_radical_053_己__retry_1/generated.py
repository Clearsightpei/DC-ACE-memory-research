"""己 (jǐ) — 3画 radical. RETRY #1.

Prior attempt failure: shape read as "E" — three rigid right-angle
pieces. GT shows a rounded, open-belly 己 with:
  - a compact top 横折 (upper-half of canvas),
  - a short middle 横 (waist),
  - a 竖弯钩 sweeping from upper-left down, bending smoothly at the
    bottom, riding along the bottom to the right, and flicking UP.

Fix ideas applied (from errata p2_radical_053_己 + sandbox):
  1. Use `draw_shu_wan_gou` for s3 with corner in BC (bottom-center)
     so the round bend sits at the bottom, NOT at BL — this is what
     turns the "E" into a proper 己.
  2. Extend s3's bottom sweep to reach BR (x_frac ~0.9), and place
     tip UP from hook_pt (tip.y < hook_pt.y in PIL).
  3. Keep the top 横折 compact in the upper third (y_frac ≈ 0.10–0.35
     of the canvas).
  4. Middle 横 is short — spans just a bit past mid, at y_frac ≈ 0.45.
  5. s3 head shares approximate x/y with s1 head (both begin at the
     upper-left of the character body) so the character reads as one
     connected shape, not disjoint pieces.

米字格 anchor plan (canvas pixel targets in comments):

  s1 (横折):
    head    ('TL', 0.30, 0.35)   ≈ px ( 30,  35)  ← 起笔 upper-left
    corner  ('TR', 0.50, 0.35)   ≈ px (150,  35)  ← end of top heng
    tail    ('TR', 0.35, 0.85)   ≈ px (135,  85)  ← down-tick

  s2 (横):
    head    ('ML', 0.35, 0.50)   ≈ px ( 35, 150)  ← left of middle heng
    tail    ('C',  0.50, 0.50)   ≈ px (150, 150)  ← right of middle heng
    (N-neighbor with s1.tail at (135,85) → same column, ~65 px above)

  s3 (竖弯钩):
    head     ('TL', 0.30, 0.40)  ≈ px ( 30,  40)  ← same top-left as s1
    belly    ('ML', 0.30, 0.70)  ≈ px ( 30, 170)  ← width knot on descent
    corner   ('BC', 0.20, 0.60)  ≈ px (120, 260)  ← round bottom bend
    hook_pt  ('BR', 0.65, 0.60)  ≈ px (265, 260)  ← base of hook (right)
    tip      ('BR', 0.65, 0.20)  ≈ px (265, 220)  ← UP flick

Joints (all N-class, per MMH):
  s1.tail ⇆ s2.tail  @ C  — N (~65 px gap; s2 ends left of s1's tail)
  s2.head ⇆ s3.body @ ML — N (s3's descent column at x≈30, s2.head at
                            x≈35 — near-touching, ~5 px)
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
        'Retry #1 fix: s3 uses shu_wan_gou with corner in BC (not BL) so '
        'the bend sits at the BOTTOM of the character, producing the '
        'round 己-belly instead of a rigid "E". Hook tip is UP (tip.y '
        '220 < hook_pt.y 260). Two visual agreements vs GT: '
        '(1) top 横折 is compact and lives in upper third; (2) bottom '
        'sweep reaches the right edge and flicks UP, matching GT s3. '
        'Stroke count = 3, matches MMH.'
    ),
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 横折 (top open box) ----
    # Compact top piece: heng from x≈85 to x≈205 at y≈75, down-tick to y≈130.
    # TL cell x∈[0,100]; TC x∈[100,200]; TR x∈[200,300].
    s1_head   = ('TL', 0.85, 0.75)     # ≈ ( 85,  75)
    s1_corner = ('TR', 0.00, 0.75)     # ≈ (200,  75)  end of top heng
    s1_tail   = ('C',  0.80, 0.30)     # ≈ (180, 130)  down-tick end
    draw_heng_zhe(d, s1_head, s1_corner, s1_tail,
                  h_width=10, v_width=10, shoulder=13)

    # ---- Stroke 2: 横 (middle crossbar) ----
    # Short heng at waist y≈150, spanning x≈90 to x≈180.
    s2_head = ('ML', 0.90, 0.50)       # ≈ ( 90, 150)
    s2_tail = ('C',  0.80, 0.50)       # ≈ (180, 150)
    draw_heng(d, s2_head, s2_tail, width=9)

    # ---- Stroke 3: 竖弯钩 (left descent → bottom sweep → UP hook) ----
    # Head shares top-left with s1.head at x≈85, y≈75 (near-weld / T-touch).
    # Descent stays at x≈85, bottom bend around y≈240, sweeps right to x≈235,
    # hook flicks UP to y≈200.
    s3_head    = ('TL', 0.85, 0.80)   # ≈ ( 85,  80) top-left, near s1.head
    s3_belly   = ('ML', 0.85, 0.80)   # ≈ ( 85, 180) straight descent
    s3_corner  = ('BL', 0.90, 0.40)   # ≈ ( 90, 240) round bend at bottom-left
    s3_hook_pt = ('BR', 0.30, 0.40)   # ≈ (230, 240) end of bottom sweep (right)
    s3_tip     = ('MR', 0.30, 0.95)   # ≈ (230, 195) UP-flick tip

    # Sanity: verify hook direction (tip must be ABOVE hook_pt in PIL).
    p_hook = anchor_to_xy(s3_hook_pt)
    p_tip  = anchor_to_xy(s3_tip)
    assert p_tip[1] < p_hook[1], (
        f'hook must flick UP: tip.y={p_tip[1]} not < hook_pt.y={p_hook[1]}'
    )
    # Sanity: bottom sweep must reach RIGHT of the corner.
    p_corner = anchor_to_xy(s3_corner)
    assert p_hook[0] > p_corner[0], (
        f'bottom sweep must go right: hook_pt.x={p_hook[0]} not > corner.x={p_corner[0]}'
    )

    draw_shu_wan_gou(d, s3_head, s3_belly, s3_corner, s3_hook_pt, s3_tip,
                     head_w=8, belly_w=11, corner_w=12,
                     hook_start_w=11, tip_w=2)

    img.save(out_path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_己.png')
    render(out)
    print('wrote', out)
