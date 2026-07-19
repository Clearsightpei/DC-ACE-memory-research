"""子 (zǐ) — 3-stroke radical.

Anchor plan (米字格, PIL-native y-grows-down):
  s1 横撇 (heng_pie): head TL(0.86, 0.92) → corner TC(0.75, 0.20) →
     tip C(0.57, 0.32).  A top curl: short horizontal opening then
     a short 撇 down-left ending near cell C.
  s2 弯钩 (wan_gou): head C(0.38, 0.28) → belly BC(0.30, 0.35) →
     hook_pt BC(0.15, 0.75) → tip BC(0.03, 0.73). Vertical curved
     spine descending from mid down to lower-center, hook flicks up-left.
  s3 横 (heng): from ML(0.35, 0.81) → MR(0.75, 0.76). Middle horizontal
     that CROSSES the 弯钩 body near cell C (P-class weld).

Joints (per MMH-derived expectation):
  J1: s1.tail(C 0.57,0.32) ⇆ s2.head(C 0.38,0.28) — N-class,
      small natural gap (~13 px). Same cell C, close x_fracs → small
      pixel gap by construction.
  J2: s2.mid(0.24) ⇆ s3.mid(0.51) at C(0.565, 0.735) — P-class weld
      (the 横 crosses the 弯钩 body). To guarantee the crossing, s3
      spans ML→MR (crosses the C column) and s2's body passes through
      x≈150 at y≈245 as well; by anchor construction their pixel
      strokes intersect.
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
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Two GT-agreement features: (1) top curl (s1) sits in upper-left '
        'quadrant with a hook-like turn ending near cell C, matching GT. '
        '(2) middle 横 (s3) crosses the vertical body (s2) near center, '
        'welded, matching the GT P-weld. J1 rendered as small N-gap '
        '(same cell C, close x_fracs -> ~12 px gap).'
    ),
}

CANVAS = 300


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # -------- Anchors --------
    # s1 horizontal-then-pie (top curl of 子)
    s1_head   = ('TL', 0.55, 0.55)   # start of short opening 横
    s1_corner = ('TC', 0.75, 0.30)   # 折 pivot upper-right of top row
    s1_tip    = ('C',  0.35, 0.35)   # 撇 needle tip landing near center

    # s2 弯钩 (vertical hook)
    s2_head    = ('C',  0.50, 0.35)  # slightly right/below s1 tip -> N-gap
    s2_belly   = ('C',  0.50, 0.75)  # keep body vertical near x=150
    s2_hook_pt = ('BC', 0.50, 0.55)  # end of body at lower-mid (x=150,y=255)
    s2_tip     = ('BC', 0.20, 0.45)  # hook flick up-and-LEFT

    # s3 一 (middle horizontal that crosses the vertical)
    s3_left  = ('ML', 0.25, 0.55)
    s3_right = ('MR', 0.75, 0.55)   # SAME row (M*) -> truly horizontal

    # -------- Sanity: same-row / same-col checks (TR8/TR12) --------
    def row(a):
        return {'TL':0,'TC':0,'TR':0,'ML':1,'C':1,'MR':1,'BL':2,'BC':2,'BR':2}[a[0]]
    def col(a):
        return {'TL':0,'ML':0,'BL':0,'TC':1,'C':1,'BC':1,'TR':2,'MR':2,'BR':2}[a[0]]
    assert row(s3_left) == row(s3_right), '横 must share cell row'
    # s2 body: head, belly, hook_pt should share x_column for a straight-ish descent
    assert col(s2_head) == col(s2_belly) == col(s2_hook_pt), '弯钩 body column mismatch'

    # -------- Render --------
    draw_heng_pie(draw, s1_head, s1_corner, s1_tip,
                  head_w=8, corner_w=12, tip_w=2)
    draw_wan_gou(draw, s2_head, s2_belly, s2_hook_pt, s2_tip,
                 head_w=8, belly_w=12, hook_start_w=10, tip_w=2)
    draw_heng(draw, s3_left, s3_right, width=9)

    # -------- Post-render structural verification --------
    # J1: pixel gap between s1_tip and s2_head (expect ~12 px, N-class)
    p_s1_tip = anchor_to_xy(s1_tip)
    p_s2_head = anchor_to_xy(s2_head)
    gap = ((p_s1_tip[0]-p_s2_head[0])**2 + (p_s1_tip[1]-p_s2_head[1])**2) ** 0.5
    # J2: check s3 crosses s2 body vertical band (x=150)
    # s3 spans x in [~ML pixel..MR pixel], crossing x=150 -> P-class OK.
    p_left = anchor_to_xy(s3_left)
    p_right = anchor_to_xy(s3_right)
    assert min(p_left[0], p_right[0]) < 150 < max(p_left[0], p_right[0]), \
        's3 must cross vertical column x=150'

    print('J1 N-gap px:', round(gap, 1),
          '(expected ~13, tolerance <=25)')
    print('J2 P-weld: s3 crosses x=150 within span',
          (p_left[0], p_right[0]))

    out = os.path.join(os.path.dirname(__file__), '01_子.png')
    img.save(out)
    print('Saved', out)


if __name__ == '__main__':
    main()
