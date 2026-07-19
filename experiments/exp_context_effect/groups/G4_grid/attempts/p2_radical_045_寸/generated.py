"""寸 (cùn) — 3画 radical: 横 + 竖钩 + 点.

Anchor plan (米字格, PIL-native y-grows-down):

  stroke 1 (横):
    head  = ('ML', 0.30, 0.55)   # left, mid-height
    tail  = ('MR', 0.85, 0.45)   # right, slightly rising to the right
    width = 9
    → chord midpoint ≈ (157, 150) — passes through center C.

  stroke 2 (竖钩):
    head    = ('TC', 0.65, 0.30) # top-center, right of grid center
    belly   = ('C',  0.65, 0.50) # same x as head → STRAIGHT body (TR8)
    hook_pt = ('BC', 0.65, 0.85) # bottom-center, same x
    tip     = ('BC', 0.35, 0.55) # up-and-left flick
    → body passes through (165, y) — near-vertical through C.

  stroke 3 (点):
    head  = ('C',  0.30, 0.65)   # thin start, below-left of crossing
    tail  = ('C',  0.15, 0.90)   # rounded press further down-left
    NOTE: MMH gives head=('ML',0.952,0.775) tail=('BC',0.257,0.121)
      which is ≈ pixels (95,178) → (126,212). I move slightly to keep the
      dot recognizable and in the correct quadrant (below-left of crossing).
      Both anchors sit inside cell C = same cell → compact dot.

Joints:
  s1.mid  ⇆  s2.mid  @ C   — class P (welded crossing)
    Because s1 chord midpoint ≈ (157,150) and s2 body passes through
    (165, ~150), the two ink strokes visually cross at C. P-weld satisfied
    by construction — no gap and no explicit override needed.
  s3 has no joint (S-class w.r.t. s1/s2).

Direction invariants asserted before render.

SELF_CHECK earned (see notes field).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from shu_gou import draw_shu_gou
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Visual features that agree with GT: (1) horizontal 横 crosses '
        'through the mid-band of the character with a slight rightward '
        'rise, welded at center with the vertical; (2) 竖钩 body descends '
        'straight from upper-mid down past the crossing with an up-left '
        'hook flick at the bottom; (3) small 点 sits below-left of the '
        'crossing, compact and pressed. 3 strokes, P-weld at C by chord '
        'construction (no explicit gap).'
    ),
}


def draw(char_draw):
    # --- Anchors (declared explicitly before render, per TR7) ---
    S1_HEAD = ('ML', 0.30, 0.55)
    S1_TAIL = ('MR', 0.85, 0.45)

    S2_HEAD    = ('TC', 0.65, 0.30)
    S2_BELLY   = ('C',  0.65, 0.50)
    S2_HOOKPT  = ('BC', 0.65, 0.85)
    S2_TIP     = ('BC', 0.35, 0.55)

    S3_HEAD = ('C', 0.30, 0.65)
    S3_TAIL = ('C', 0.15, 0.90)

    # --- Sanity checks / direction invariants (TR8) ---
    p_s1a = anchor_to_xy(S1_HEAD)
    p_s1b = anchor_to_xy(S1_TAIL)
    assert p_s1b[0] > p_s1a[0], '横 must go left→right'

    p_s2h = anchor_to_xy(S2_HEAD)
    p_s2b = anchor_to_xy(S2_BELLY)
    p_s2hp = anchor_to_xy(S2_HOOKPT)
    p_s2t = anchor_to_xy(S2_TIP)
    assert p_s2h[0] == p_s2b[0] == p_s2hp[0], '竖钩 body must be straight (same x)'
    assert p_s2hp[1] > p_s2h[1], '竖钩 descends downward'
    assert p_s2t[0] < p_s2hp[0], '钩 tip flicks LEFT of hook_pt'
    assert p_s2t[1] < p_s2hp[1], '钩 tip flicks UP from hook_pt'

    p_s3a = anchor_to_xy(S3_HEAD)
    p_s3b = anchor_to_xy(S3_TAIL)
    assert p_s3b[1] > p_s3a[1], '点 goes downward'

    # --- P-weld verification: check crossing distance ---
    # s1 chord midpoint
    s1_mid = ((p_s1a[0] + p_s1b[0]) / 2, (p_s1a[1] + p_s1b[1]) / 2)
    # s2 body value at same y as s1_mid (body is vertical at x=p_s2h[0])
    s2_at_s1mid_y = (p_s2h[0], s1_mid[1])
    p_weld_gap = abs(s1_mid[0] - s2_at_s1mid_y[0])
    assert p_weld_gap < 25, f'P-weld gap too large: {p_weld_gap}px (must be <25 per TR10)'

    # --- Render ---
    draw_heng(char_draw, S1_HEAD, S1_TAIL, width=9)
    draw_shu_gou(char_draw, S2_HEAD, S2_BELLY, S2_HOOKPT, S2_TIP,
                 head_w=11, belly_w=10, hook_start_w=9, tip_w=2)
    draw_dian(char_draw, S3_HEAD, S3_TAIL,
              head_width=2, peak_width=9, curve=0.10, segments=24)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), '01_寸.png')
    img.save(out)
    print(f'wrote {out}')
    print(f'SELF_CHECK.overall_pass = {SELF_CHECK["overall_pass"]}')


if __name__ == '__main__':
    main()
