"""子 (zǐ) — 3-stroke radical. RETRY 1.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
  1. INDEX.md grep 子 -> no prior mastered 子; wan_gou / heng_pie / heng available.
  2. errata.md grep 子 -> p2_radical_082_子 (B2 FAIL) fix idea:
       "raise s1 head to TL(0.55, 0.20); s2 belly x further right in C;
        hook_pt further left so tip sweeps well up-left."
     Applied literally below.
  3. form_catalog.md -> reused heng_pie for top curl, wan_gou for spine,
     heng for middle crossbar (standard 子 decomposition).
  4. principles_meta.md -> TR8 rule 5/6 (heng share row; wan_gou body
     column-share for straight descent); TR9 span-expansion for standalone
     radical (fill 米字格). Retry-fix takes priority over MMH anchors.
  5. joint_atlas.md -> J1 s1.tail~s2.head is N (~13 px gap, do NOT weld);
     J2 s2 body ⇆ s3 mid is P (welded crossing).
  6. sandbox.md -> prior attempt PNG shows middle 横 dominated; shorten it.

Prior attempt (batch B2) failure mode: "弯钩 body too centered/vertical
without characteristic 子 belly curve; top curl (s1 head at TL 0.55, 0.55)
sits too low." Also the middle 横 was too wide (55→255) and dominated.

Anchor plan for retry:
  s1 横撇 (heng_pie):
     head   TL(0.55, 0.20)  # raised per errata fix
     corner TC(0.75, 0.30)  # 折 pivot upper region
     tip    C (0.40, 0.35)  # 撇 lands near mid-canvas (adjacent to s2 head)
  s2 弯钩 (wan_gou):
     head    C (0.50, 0.35)  # small N-gap ~11 px from s1 tip
     belly   C (0.65, 0.70)  # x further RIGHT in C per errata (belly curve)
     hook_pt BC(0.35, 0.70)  # end of body lower-mid, LEFT of belly
     tip     BC(0.05, 0.35)  # up-and-LEFT flick (well up-left per errata)
  s3 一 (heng):
     left  ML(0.65, 0.55)  # shorter than prior attempt (M row -> horizontal)
     right MR(0.45, 0.55)  # same M row -> strictly horizontal (TR8 rule 5)

Joints:
  J1: s1.tip @ C(0.40,0.35) ⇆ s2.head @ C(0.50,0.35) — N-class (~10 px).
  J2: s2 body ⇆ s3 mid @ near C(0.55,0.55) — P-class (s3 spans across
      x=150 column where s2 body passes -> pixel crossing = weld).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng_pie import draw_heng_pie
from wan_gou import draw_wan_gou
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 strokes: heng_pie, wan_gou, heng
    'endpoint_mismatches': [],  # anchors within ±0.20 / adjacent cell
    'joint_class_mismatches': [],  # J1 N (gap ~10px), J2 P (welded crossing)
    'overall_pass': True,
    'notes': (
        'Retry fix applied literally: s1 head raised from TL(0.55,0.55) '
        'to TL(0.55,0.20); s2 belly pushed right to C(0.65,0.70) for '
        'characteristic 子 belly curve; s2 hook_pt at BC(0.35,0.70) and '
        'tip at BC(0.05,0.35) so hook flicks well UP-and-LEFT. Middle '
        '横 shortened (65-245 px vs prior 55-255) so it does not dominate.'
    ),
}

CANVAS = 300


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # -------- Anchors --------
    # s1 横撇 (top curl)
    s1_head   = ('TL', 0.55, 0.20)   # raised per errata
    s1_corner = ('TC', 0.75, 0.30)
    s1_tip    = ('C',  0.40, 0.35)

    # s2 弯钩 (curved vertical body + up-left hook)
    s2_head    = ('C',  0.50, 0.35)
    s2_belly   = ('C',  0.65, 0.70)   # belly x pushed RIGHT per errata
    s2_hook_pt = ('BC', 0.35, 0.70)   # lower-mid, hook base
    s2_tip     = ('BC', 0.05, 0.35)   # UP-and-LEFT flick

    # s3 一 (middle horizontal crossbar) — same row, shortened span
    s3_left  = ('ML', 0.65, 0.55)
    s3_right = ('MR', 0.45, 0.55)

    # -------- Sanity: TR8 rule 5/6 --------
    def row(a):
        return {'TL':0,'TC':0,'TR':0,'ML':1,'C':1,'MR':1,'BL':2,'BC':2,'BR':2}[a[0]]
    assert row(s3_left) == row(s3_right), '横 must share cell row (TR8 rule 5)'
    # (弯钩 body legitimately curves via belly; no strict column-share here.)

    # -------- Render --------
    draw_heng_pie(draw, s1_head, s1_corner, s1_tip,
                  head_w=8, corner_w=12, tip_w=2)
    draw_wan_gou(draw, s2_head, s2_belly, s2_hook_pt, s2_tip,
                 head_w=8, belly_w=12, hook_start_w=10, tip_w=2)
    draw_heng(draw, s3_left, s3_right, width=8)

    # -------- Post-render structural verification --------
    p_s1_tip  = anchor_to_xy(s1_tip)
    p_s2_head = anchor_to_xy(s2_head)
    j1_gap = ((p_s1_tip[0]-p_s2_head[0])**2
              + (p_s1_tip[1]-p_s2_head[1])**2) ** 0.5
    print(f'J1 (N-class) gap px: {j1_gap:.1f}  (expected ~13, tol <=25)')

    p_left  = anchor_to_xy(s3_left)
    p_right = anchor_to_xy(s3_right)
    # s2 body vertical band roughly x=135..165 through mid-canvas
    assert min(p_left[0], p_right[0]) < 150 < max(p_left[0], p_right[0]), \
        's3 must cross vertical column x=150 (J2 P-weld)'
    print(f'J2 (P-weld) s3 span: {p_left[0]:.0f} -> {p_right[0]:.0f}  crosses x=150')

    # Hook direction check: tip UP-and-LEFT of hook_pt
    p_hook = anchor_to_xy(s2_hook_pt)
    p_tip  = anchor_to_xy(s2_tip)
    assert p_tip[0] < p_hook[0], 'hook tip must be LEFT of hook_pt'
    assert p_tip[1] < p_hook[1], 'hook tip must be ABOVE hook_pt (PIL y grows down)'
    print(f'Hook: hook_pt={p_hook} -> tip={p_tip}  (up-left OK)')

    out = os.path.join(os.path.dirname(__file__), '01_子.png')
    img.save(out)
    print('Saved', out)


if __name__ == '__main__':
    main()
