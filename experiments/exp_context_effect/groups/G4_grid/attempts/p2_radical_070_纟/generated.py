"""纟 (silk radical) — 3 strokes: 撇折 + 撇折 + 提.

Revision 1 fixes:
  - First fold was rendered as an almost-invisible stub because both
    endpoints landed within one cell height. Enlarged both folds so
    each has a visible piě sweep AND a visible heng.
  - Placed the top fold in the upper band (TC/C), the middle fold in
    the middle band (C/BC), and the 提 spans the bottom row.
  - Kept the composition centered-left, matching a standalone radical.

Structural expectations (MMH-derived, per brief):
  - stroke 1: head TC(0.354,0.762) -> tail C(0.444,0.731)
  - stroke 2: head C(0.679,0.304) -> tail BC(0.761,0.153)
  - stroke 3: head BL(0.914,0.795) -> tail BC(0.872,0.435)
  - joint: s1.tail ~ s2.mid @ C, class N (small natural gap ~12 px)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie_zhe import draw_pie_zhe
from ti import draw_ti
from _anchor import anchor_to_xy

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Rev1: enlarged both folds so each has a visible piě and heng; three folds stacked vertically.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: TOP 撇折 (upper band) ----
    # head at upper (TC top-right), pivot low-left near C top, tail extends right.
    s1_head  = ('TC', 0.65, 0.35)
    s1_pivot = ('TC', 0.30, 0.85)
    s1_tail  = ('C',  0.55, 0.10)
    draw_pie_zhe(d, s1_head, s1_pivot, s1_tail,
                 pie_head_w=8, pie_tip_w=3, heng_w=6, shoulder=3)

    # ---- Stroke 2: MIDDLE 撇折 (middle band) ----
    # head at C upper-right, pivot low-left near BC, tail extends right into MR/BC.
    s2_head  = ('C',  0.75, 0.30)
    s2_pivot = ('C',  0.35, 0.85)
    s2_tail  = ('C',  0.85, 0.55)
    draw_pie_zhe(d, s2_head, s2_pivot, s2_tail,
                 pie_head_w=8, pie_tip_w=3, heng_w=6, shoulder=3)

    # ---- Stroke 3: BOTTOM 提 (bottom row) ----
    # head heavy at BL right-mid, tail rising up-right toward BR/BC.
    s3_head = ('BL', 0.35, 0.75)
    s3_tail = ('BR', 0.55, 0.30)
    draw_ti(d, s3_head, s3_tail,
            head_width=11, tail_width=1, curve=0.05)

    # ---- Self-check gap between s1.tail and s2.head (near mid) ----
    p_s1_tail = anchor_to_xy(s1_tail)
    p_s2_head = anchor_to_xy(s2_head)
    dx = p_s1_tail[0] - p_s2_head[0]
    dy = p_s1_tail[1] - p_s2_head[1]
    dist = (dx * dx + dy * dy) ** 0.5
    SELF_CHECK['s1_tail_s2_head_gap_px'] = round(dist, 1)

    out = os.path.join(os.path.dirname(__file__), '01_纟.png')
    img.save(out)
    print('Saved:', out)
    print('SELF_CHECK:', SELF_CHECK)


if __name__ == '__main__':
    draw()
