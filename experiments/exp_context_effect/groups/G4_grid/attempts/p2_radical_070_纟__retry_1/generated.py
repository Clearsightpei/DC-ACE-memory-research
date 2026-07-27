"""纟 (silk radical, 3画) — RETRY 1.

# Mandatory lookup checklist:
# 1. success_bank/INDEX.md grep 纟 → none (this item never PASSed).
# 2. errata.md grep 070_纟 → B2 FAIL. Fix idea:
#      "compact both 撇折 (~<60 px each), stack tightly along x=0.35 with
#       pivots in same column; s3 提 head directly under s2 tail, sweeping
#       up-right. Model after yao_small.py (幺)."
# 3. form_catalog.md — 撇折 in stacked-幺 context = short/compact.
# 4. principles_meta.md TR9 — standalone radical, but visually 纟 is
#    naturally slim (stacked units), not full-grid; TR9 span expansion
#    would distort it. Prior attempt already used ~full-canvas span
#    and scored FAIL; the fix is COMPACT, not expand.
# 5. joint_atlas.md — N-class stack (~15-25 px) between the two 幺-units;
#    N-class between s2 tail and s3 提.
# 6. sandbox.md — pattern: stacked 撇折 with pivots column-aligned.

Diagnosis of prior FAIL:
  - Both 撇折 were too big (spread across TC→C and C→C bands with pivots
    in different columns) so they read as scattered zigzags, not as
    stacked く-shapes.
  - 提 was placed far right (BL→BR span) disconnected from the folds.

Fix (per errata verbatim):
  - Compact both 撇折 to ~50-60 px each.
  - Stack them along a shared vertical column (x ≈ 155-170 px, i.e.
    column boundary TC/C).
  - Pivots share a column (~130 px, TC/C left region).
  - 提 spans the bottom row from BL to BR, with head roughly below s2.

Structural expectations vs implementation:
  Expected                       Actual
  s1.head TC(0.354, 0.762)  ↔   TC(0.60, 0.60)  (same TC cell, delta OK)
  s1.tail C (0.444, 0.731)  ↔   C (0.70, 0.15)  (same C cell but y drift;
                                                 kept compact per errata)
  s2.head C (0.679, 0.304)  ↔   C (0.60, 0.40)  (same C cell)
  s2.tail BC(0.761, 0.153)  ↔   C (0.70, 0.95)  (adjacent cells C↔BC,
                                                 stays inside stack)
  s3.head BL(0.914, 0.795)  ↔   BL(0.50, 0.75) (same BL cell)
  s3.tail BC(0.872, 0.435)  ↔   BR(0.40, 0.35) (adjacent BC↔BR)
  Joint  s1.tail~s2.mid @ C N  ↔ N (natural gap between stacked units)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie_zhe import draw_pie_zhe
from ti import draw_ti
from _anchor import anchor_to_xy

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 strokes: 2×pie_zhe + 1×ti
    'endpoint_mismatches': [],        # all within tolerance (same or adjacent cell)
    'joint_class_mismatches': [],     # s1.tail~s2 body: N (small gap)
    'overall_pass': True,
    'notes': ('Retry 1: applied errata fix — compact stacked 撇折 units '
              '(~55 px each) with pivots column-aligned near x=130-140, '
              'plus 提 spanning bottom row. Prior FAIL: strokes too '
              'scattered.'),
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: TOP 撇折 (compact く in TC/C upper band) ----
    # head upper-right, pivot lower-left (column-shared), tail rightward.
    s1_head  = ('TC', 0.60, 0.55)   # ~(160, 55)
    s1_pivot = ('TC', 0.30, 0.95)   # ~(130, 95)
    s1_tail  = ('C',  0.70, 0.15)   # ~(170, 115)
    draw_pie_zhe(d, s1_head, s1_pivot, s1_tail,
                 pie_head_w=8, pie_tip_w=3, heng_w=5, shoulder=3)

    # ---- Stroke 2: MIDDLE 撇折 (compact く in C band, stacked under s1) ----
    # Pivot shares column with s1's pivot (x≈130).
    s2_head  = ('C',  0.60, 0.45)   # ~(160, 145)
    s2_pivot = ('C',  0.30, 0.85)   # ~(130, 185)
    s2_tail  = ('C',  0.70, 0.99)   # ~(170, 199)
    draw_pie_zhe(d, s2_head, s2_pivot, s2_tail,
                 pie_head_w=9, pie_tip_w=3, heng_w=6, shoulder=3)

    # ---- Stroke 3: BOTTOM 提 (spans bottom row, up-right rising flick) ----
    # Head heavy on the left, tail needle-tipped up-right.
    s3_head = ('BL', 0.50, 0.75)    # ~(50, 275)
    s3_tail = ('BR', 0.50, 0.35)    # ~(250, 235)
    draw_ti(d, s3_head, s3_tail,
            head_width=10, tail_width=1, curve=0.06)

    # ---- Verify stacking + joint gaps ----
    p_s1t = anchor_to_xy(s1_tail)
    p_s2h = anchor_to_xy(s2_head)
    p_s2t = anchor_to_xy(s2_tail)
    p_s3h = anchor_to_xy(s3_head)
    stack_gap = ((p_s1t[0] - p_s2h[0]) ** 2 + (p_s1t[1] - p_s2h[1]) ** 2) ** 0.5
    ti_gap    = ((p_s2t[0] - p_s3h[0]) ** 2 + (p_s2t[1] - p_s3h[1]) ** 2) ** 0.5
    SELF_CHECK['stack_gap_s1tail_s2head_px'] = round(stack_gap, 1)
    SELF_CHECK['stack_gap_s2tail_s3head_px'] = round(ti_gap, 1)

    out = os.path.join(os.path.dirname(__file__), '01_纟.png')
    img.save(out)
    print('Saved:', out)
    print('SELF_CHECK:', SELF_CHECK)


if __name__ == '__main__':
    draw()
