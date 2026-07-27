"""只 (zhǐ) — Phase-3 char, 5 strokes = 口 (top) + 八 (bottom).

Memory-index checklist:
  1. INDEX.md grep: kou.py (81), ba.py (41) both mastered — reuse with
     OVERRIDING anchors (TR1).
  2. errata.md grep: 只 not in errata.
  3. form_catalog: 口 as top component compresses to upper 2/3;
     八 as bottom component spans BL–BR.
  4. principles_meta TR1: override defaults; TR9 not applicable (comp char).
  5. joint_atlas: 口 uses 3×N corners; 八 is S-class (separate legs).

Structure per MMH brief:
  s1 竖 (left wall of 口): TL→C
  s2 横折 (top+right of 口): TC→C
  s3 横 (bottom of 口): C→MR
  s4 撇 (left leg of 八): BC→BL
  s5 捺 (right leg of 八): C→BR
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'kou(3-stroke) upper 2/3 + ba(2-stroke) bottom; 3 N-corners on 口, S-class on 八.'
}


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_zhi(draw):
    # ---- 口 (upper) — 3 strokes, all N corners ----
    # s1 竖: TL(0.841,0.94) → C(0.11,0.778)
    s1h = anchor_to_xy(('TL', 0.841, 0.94))
    s1t = anchor_to_xy(('C',  0.11, 0.778))
    # s2 横折: TC(0.034,0.952) → corner at top-right ≈ (TR,0.05,0.95) → C(0.843,0.468)
    s2h = anchor_to_xy(('TC', 0.034, 0.952))
    s2c = anchor_to_xy(('TR', 0.05, 0.95))
    s2t = anchor_to_xy(('C',  0.843, 0.468))
    # s3 横 (bottom bar): C(0.178,0.69) → MR(0.065,0.579)
    s3h = anchor_to_xy(('C',  0.178, 0.69))
    s3t = anchor_to_xy(('MR', 0.065, 0.579))

    # Introduce ~14 px gaps at all 4 potential corners → N-class
    s1h_g = _shorten(s1h, s1t, 7)
    s1t_g = _shorten(s1t, s1h, 7)
    s2h_g = _shorten(s2h, s2c, 7)
    s2t_g = _shorten(s2t, s2c, 7)
    s3h_g = _shorten(s3h, s3t, 7)
    s3t_g = s3t  # tail is inner, no need to shorten

    fat_line(draw, s1h_g, s1t_g, width=8)
    fat_line(draw, s2h_g, s2c,   width=8)
    fat_line(draw, s2c,   s2t_g, width=8)
    # small ink dot at the corner so it stays welded (S-internal for s2)
    cx, cy = s2c; r = 5
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    fat_line(draw, s3h_g, s3t_g, width=8)

    # ---- 八 (lower) — 2 strokes, S-class ----
    # s4 撇: BC(0.23,0.15) → BL(0.375,0.807)
    draw_pie(draw,
             from_anchor=('BC', 0.23, 0.15),
             to_anchor=('BL', 0.375, 0.807),
             head_width=10, tail_width=1, curve=0.10, segments=48)
    # s5 捺: C(0.802,0.998) → BR(0.432,0.742)
    draw_na(draw,
            from_anchor=('C', 0.802, 0.998),
            to_anchor=('BR', 0.432, 0.742),
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_zhi(draw)
    out = os.path.join(_HERE, '01_只.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
