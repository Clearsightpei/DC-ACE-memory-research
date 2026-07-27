"""囗 (wéi, "enclosure", 3 strokes) — B2 pass.

Standalone enclosing radical. TR9 mandatory (MMH cramps to lower-right);
frame occupies x_frac 0.30–0.85, y_frac 0.15–0.90.

Strokes:
  s1 — 竖 (left wall).
  s2 — 横折 (top bar + right wall).
  s3 — 横 (bottom bar).

Joints: 3 × N (all four corners are natural gaps; open-frame style like 口).
"""
from _anchor import anchor_to_xy, fat_line


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_wei_enclose(draw,
                     s1_head=('TL', 0.30, 0.15), s1_tail=('BL', 0.30, 0.90),
                     s2_head=('TL', 0.35, 0.15),
                     s2_corner=('TR', 0.85, 0.15),
                     s2_tail=('BR', 0.85, 0.90),
                     s3_head=('BL', 0.35, 0.90), s3_tail=('BR', 0.85, 0.90),
                     width=10):
    s1h = anchor_to_xy(s1_head); s1t = anchor_to_xy(s1_tail)
    s2h = anchor_to_xy(s2_head); s2c = anchor_to_xy(s2_corner); s2t = anchor_to_xy(s2_tail)
    s3h = anchor_to_xy(s3_head); s3t = anchor_to_xy(s3_tail)

    # N-gap shortening at all four corners.
    s1h_g = _shorten(s1h, s1t, 7)
    s1t_g = _shorten(s1t, s1h, 7)
    s2h_g = _shorten(s2h, s2c, 7)
    s2t_g = _shorten(s2t, s2c, 12)
    s3h_g = _shorten(s3h, s3t, 7)
    s3t_g = _shorten(s3t, s3h, 12)

    fat_line(draw, s1h_g, s1t_g, width=width)
    fat_line(draw, s2h_g, s2c, width=width)
    fat_line(draw, s2c, s2t_g, width=width)
    r = 6
    draw.ellipse([s2c[0]-r, s2c[1]-r, s2c[0]+r, s2c[1]+r], fill=(0, 0, 0))
    fat_line(draw, s3h_g, s3t_g, width=width)
