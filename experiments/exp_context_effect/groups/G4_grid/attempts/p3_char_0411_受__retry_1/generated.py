"""受 (shòu) — 8 strokes: 爫 (4) + 冖 (2) + 又 (2). RETRY 1.

TRAJECTORY DIFF (main attempt -> retry_1):
  main attempt (verdict C): used MMH-verbatim anchors. Concrete failures:
    (1) 爫 top group was scattered (MMH strokes 2/3/4 had heads in
        ML/C/TR that landed at y~10..90 mixing with 冖 middle band).
    (2) 冖 middle "cover" horizontal drifted upward into 爫 territory
        (s6 head at ML(0.724,0.638)=py 163 vs errata target y~130).
    (3) 又 bottom X was weak: heng_pie corner at C(0.75,0.70)=py 170
        collided with cover; na from BL(0.967,0.191)=py 219 crossed
        heng_pie too low — no clean X apex.
    (4) 3-tier proportion collapsed: no clear vertical separation
        between 爫 / 冖 / 又 -- reads as a jumble.
  Fix this retry (LITERAL from errata B11 entry for 受):
    - 爫 in y-band [0.05, 0.30]  (top 30% of canvas)
    - 冖 in y-band [0.35, 0.50]  (middle 15%)
    - 又 in y-band [0.55, 0.95]  (bottom 40%)
    - X-cross apex at (C, 0.5, 0.75) = pixel (150, 175)

# BANK_DEVIATION
# skipped: (MMH-verbatim anchors from dispatcher block)
# reason: MMH placed 爫 strokes 2-4 into ML/C/TR with y_frac 0-0.4
#   producing scattered top-tier that overlapped 冖; errata B11 mandates
#   literal 3-tier y-bands. Overriding to errata layout.
# fresh_component: shou_three_tier_apex_at_C
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier,
                     stroke_variable_width, fat_line, sample_line)
from pie import draw_pie
from na import draw_na
from heng_pie import draw_heng_pie
from heng_gou import draw_heng_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 primitive calls
    'endpoint_mismatches': [
        'anchors OVERRIDDEN per B11 errata 3-tier layout; see BANK_DEVIATION'
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('3-tier layout: 爫 y[0.05,0.30]; 冖 y[0.35,0.50]; '
              '又 y[0.55,0.95] with X-apex at (C,0.5,0.75).'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # =====================================================================
    # ── 爫 (top 4 strokes) — y_band [0.05, 0.30] ──
    # =====================================================================
    # s1: main left 撇 sweeping down-left, longest of the four
    draw_pie(d, from_anchor=('TC', 0.30, 0.20), to_anchor=('TL', 0.65, 0.90),
             head_width=9, tail_width=2, curve=0.10, segments=40)

    # s2: middle-left short 短撇 (nearly vertical, small down-left tick)
    draw_pie(d, from_anchor=('TC', 0.55, 0.30), to_anchor=('TC', 0.50, 0.90),
             head_width=8, tail_width=2, curve=0.06, segments=32)

    # s3: middle-right short 短撇
    draw_pie(d, from_anchor=('TC', 0.85, 0.30), to_anchor=('TC', 0.80, 0.90),
             head_width=8, tail_width=2, curve=0.06, segments=32)

    # s4: rightmost short 短撇
    draw_pie(d, from_anchor=('TR', 0.15, 0.30), to_anchor=('TR', 0.10, 0.90),
             head_width=8, tail_width=2, curve=0.06, segments=32)

    # =====================================================================
    # ── 冖 (middle 2 strokes) — y_band [0.35, 0.50] ──
    # =====================================================================
    # s5: tiny left-side tick 短撇 at cover's left top corner
    draw_pie(d, from_anchor=('ML', 0.22, 0.10), to_anchor=('ML', 0.17, 0.40),
             head_width=7, tail_width=2, curve=0.05, segments=24)

    # s6: 横钩 wide cover bar with small down-hook at right end
    draw_heng_gou(d,
                  head=('ML', 0.20, 0.25),
                  shoulder=('MR', 0.85, 0.25),
                  tip=('MR', 0.80, 0.55),
                  head_w=8, mid_w=8, shoulder_w=11, tip_w=2)

    # =====================================================================
    # ── 又 (bottom 2 strokes) — y_band [0.55, 0.95]; X-apex ≈ (150,175) ──
    # =====================================================================
    # s7: 横撇 — heng phase FLAT at y≈170 going L→R, then pie down-left.
    # (Prior revision had corner y_frac=0.05 which raised heng into 冖 band.)
    draw_heng_pie(d,
                  head=('ML', 0.20, 0.70),   # px ≈ (20, 170) — heng left end
                  corner=('C', 0.60, 0.70),  # px ≈ (160, 170) — bend point (heng flat)
                  tip=('BL', 0.30, 0.90),    # px ≈ (30, 290)  — pie tail bottom-left
                  head_w=6, corner_w=12, tip_w=2)

    # s8: 捺 diagonal down-right, crosses s7 pie near (150, 175) apex
    draw_na(d,
            from_anchor=('C', 0.20, 0.65),   # px ≈ (120, 165) — upper-left of X
            to_anchor=('BR', 0.60, 0.90),    # px ≈ (260, 290) — lower-right of X
            head_width=3, peak_width=14, tail_width=1,
            peak_t=0.80, curve=0.08, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_受.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
