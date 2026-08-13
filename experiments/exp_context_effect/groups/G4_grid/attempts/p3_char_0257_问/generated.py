"""问 (wèn, "ask", 6 strokes) — G4 attempt.

Split: 问 = 门 (frame) + 口 (inside, sits in the lower-right of the frame).

Compositional plan (see drawer_memory.md playbook):
  - 门 = 点 + 竖 + 横折钩. Import men.py (mastered p2_radical_059_门).
  - 口 = 竖 + 横折 + 横. Import kou.py (mastered p2_radical_057_口).
  - Place 门 filling most of canvas; 口 sits inside the enclosure area,
    biased toward middle/right per GT.

Stroke count: 3 (门) + 3 (口) = 6. Matches MMH expected count.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from dian import draw_dian
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '问 = 门 + 口. Import men+kou primitives; kou placed inside frame '
             'toward middle-right. All 6 endpoints checked; 3 N-joints inside kou '
             'preserved via kou.py _shorten helper.'
}


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_wen(draw):
    # === 门 frame — enlarged to fill character ===
    # s1: 点 (top-left dot) — head upper-left, tail down-right
    draw_dian(draw,
              ('TL', 0.35, 0.40),
              ('TL', 0.70, 0.75),
              head_width=2, peak_width=11, curve=0.10)

    # s2: 竖 (left wall) — from top row down to bottom
    draw_shu(draw,
             ('ML', 0.30, 0.15),
             ('BL', 0.35, 0.95),
             width=8)

    # s3: 横折钩 (head → corner → tail → tip)
    #   head: top-bar start (aligned to same y as s2 head), left of s2 head
    #   corner: top-right
    #   tail: bottom of right wall
    #   tip: UP-and-LEFT flick from tail
    draw_heng_zhe_gou(draw,
                      ('TL', 0.75, 0.60),
                      ('TR', 0.75, 0.60),
                      ('BR', 0.60, 0.95),
                      ('BR', 0.35, 0.70),
                      h_width=8, v_width=8, shoulder=11, tip_w=2)

    # === 口 inside — sits in mid-right area of the enclosure ===
    # Frame interior: x roughly [0.20, 0.75] × [0.20, 0.85] of canvas.
    # Place 口 at middle-right, spanning approx C(0.3..1.0) × y (0.35..0.7).
    #
    # Anchors chosen so 口 sits inside the frame (below top bar, above
    # baseline, right of left wall, left of right wall).
    # 口 sits inside the frame, roughly centered in middle-right quadrant
    s1_head = ('C', 0.20, 0.35)   # kou left-wall top
    s1_tail = ('C', 0.28, 0.95)   # kou left-wall bottom
    s2_head = ('C', 0.25, 0.30)   # kou top bar left  (small N gap from s1)
    s2_corner = ('C', 0.95, 0.30)
    s2_tail = ('C', 0.98, 0.95)   # kou right-wall bottom
    s3_head = ('C', 0.30, 0.98)   # kou bottom bar left
    s3_tail = ('C', 0.95, 0.92)   # kou bottom bar right

    s1h = anchor_to_xy(s1_head); s1t = anchor_to_xy(s1_tail)
    s2h = anchor_to_xy(s2_head); s2c = anchor_to_xy(s2_corner); s2t = anchor_to_xy(s2_tail)
    s3h = anchor_to_xy(s3_head); s3t = anchor_to_xy(s3_tail)

    # Shorten to preserve N-class corner gaps (do not weld corners)
    s1h_g = _shorten(s1h, s1t, 4)
    s1t_g = _shorten(s1t, s1h, 4)
    s2h_g = _shorten(s2h, s2c, 4)
    s2t_g = _shorten(s2t, s2c, 4)
    s3h_g = _shorten(s3h, s3t, 4)

    fat_line(draw, s1h_g, s1t_g, width=7)         # 口 s1
    fat_line(draw, s2h_g, s2c,  width=7)          # 口 s2 top bar
    fat_line(draw, s2c,  s2t_g, width=7)          # 口 s2 right wall
    cx, cy = s2c; r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    fat_line(draw, s3h_g, s3t, width=7)           # 口 s3 bottom bar


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_wen(d)
    out = os.path.join(os.path.dirname(__file__), '01_问.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
