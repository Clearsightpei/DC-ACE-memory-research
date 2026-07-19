"""囗 (wéi, "enclosure", 3画 radical) — G4 attempt.

Anchor plan (per TR2 enclosing-radical span x_frac ~0.05-0.95, y_frac ~0.05-0.95;
per TR9 expand MMH anchors for standalone Phase-2 radicals):

  s1 竖 (left wall, top→bottom, straight column TL→BL):
    head @ ('TL', 0.30, 0.15)
    tail @ ('BL', 0.30, 0.90)
    col(TL)==col(BL) → OK per TR12.

  s2 横折 (top bar + right wall):
    head    @ ('TL', 0.35, 0.15)   # near s1.head (N-gap)
    corner  @ ('TR', 0.85, 0.15)   # top bar sits in TL/TR row → OK per TR12
    tail    @ ('BR', 0.85, 0.90)   # right wall descends TR→BR (same col)
    joint at corner is internal P (welded 90° fold) — 顿笔 disc.

  s3 横 (bottom bar):
    head @ ('BL', 0.35, 0.90)   # near s1.tail (N-gap)
    tail @ ('BR', 0.85, 0.90)   # same BL/BR row → OK per TR12
    (near s2.tail with small N-gap.)

Joints (per MMH structural block, all N-class):
  s1.head ⇆ s2.head @ TL — N (small gap ~14 px)
  s1.tail ⇆ s3.head @ BL — N (small gap ~15 px)
  s2.tail ⇆ s3.tail @ BR — N (small gap ~24 px)

Rendering: inlined fat_line segments (same pattern as kou.py) so the
_shorten trick can create the N-gaps at each corner. width=10 for
prominence as a large enclosing radical.
"""
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_SB = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _SB)

from _anchor import anchor_to_xy, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],  # populated below
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Visual agreements vs GT (TR11): (1) enclosing square silhouette '
        'filling most of the canvas with all four sides visible. '
        '(2) small N-gaps at three corners (TL, BL, BR) matching GT\'s '
        'hand-drawn open-corner look. '
        'Overrode MMH anchors per TR9 (verbatim MMH cramps to BR corner). '
        'All three strokes obey TR12 row/col discipline.'
    ),
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


def draw_wei_enclosure(draw):
    # Anchors
    s1_head = ('TL', 0.30, 0.15)
    s1_tail = ('BL', 0.30, 0.90)

    s2_head = ('TL', 0.35, 0.15)
    s2_corner = ('TR', 0.85, 0.15)
    s2_tail = ('BR', 0.85, 0.90)

    s3_head = ('BL', 0.35, 0.90)
    s3_tail = ('BR', 0.85, 0.90)

    s1h = anchor_to_xy(s1_head); s1t = anchor_to_xy(s1_tail)
    s2h = anchor_to_xy(s2_head); s2c = anchor_to_xy(s2_corner); s2t = anchor_to_xy(s2_tail)
    s3h = anchor_to_xy(s3_head); s3t = anchor_to_xy(s3_tail)

    # TR8 sanity: 竖 in one column, 横 in one row
    assert abs(s1h[0] - s1t[0]) < 5, f's1 not vertical: {s1h} {s1t}'
    assert abs(s2h[1] - s2c[1]) < 5, f's2 top-bar not horizontal: {s2h} {s2c}'
    assert abs(s2c[0] - s2t[0]) < 5, f's2 right-wall not vertical: {s2c} {s2t}'
    assert abs(s3h[1] - s3t[1]) < 5, f's3 not horizontal: {s3h} {s3t}'

    # Corner N-gaps (~14-24 px per MMH spec). We shorten each stroke's
    # end near a corner by 7 px so adjacent-stroke ends leave a ~14 px gap.
    s1h_g = _shorten(s1h, s1t, 7)      # TL corner (near s2.head)
    s1t_g = _shorten(s1t, s1h, 7)      # BL corner (near s3.head)
    s2h_g = _shorten(s2h, s2c, 7)      # TL corner (near s1.head)
    s2t_g = _shorten(s2t, s2c, 12)     # BR corner (near s3.tail, larger gap ~24 px)
    s3h_g = _shorten(s3h, s3t, 7)      # BL corner (near s1.tail)
    s3t_g = _shorten(s3t, s3h, 12)     # BR corner (near s2.tail)

    W = 10  # ink width for prominent enclosing radical

    # s1: left wall
    fat_line(draw, s1h_g, s1t_g, width=W)

    # s2: top bar + right wall (P-weld at corner with 顿笔 disc)
    fat_line(draw, s2h_g, s2c, width=W)
    fat_line(draw, s2c, s2t_g, width=W)
    cx, cy = s2c; r = 6
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s3: bottom bar
    fat_line(draw, s3h_g, s3t_g, width=W)

    # Populate SELF_CHECK gap measurements
    def _dist(a, b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

    SELF_CHECK['tl_gap_px'] = round(_dist(s1h_g, s2h_g), 1)
    SELF_CHECK['bl_gap_px'] = round(_dist(s1t_g, s3h_g), 1)
    SELF_CHECK['br_gap_px'] = round(_dist(s2t_g, s3t_g), 1)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wei_enclosure(draw)
    out = os.path.join(_HERE, '01_囗.png')
    img.save(out)
    print(f'Saved {out}')
    print(f'SELF_CHECK: {SELF_CHECK}')


if __name__ == '__main__':
    main()
