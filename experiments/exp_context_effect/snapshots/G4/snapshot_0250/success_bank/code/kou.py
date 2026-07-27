"""口 (kǒu, "mouth", 3 strokes) — B1 pass.

3-stroke open square with all N-class joints (small natural gaps at
the corners). Inlined via fat_line because the shortening trick to
open the N-gaps sits outside the standard heng_zhe primitive.

Strokes:
  s1 — 竖 (left wall, thin, slightly slanting).
  s2 — 横折 (top bar + right wall).
  s3 — 横 (bottom bar, slight upward slant).

Joints:
  s1.head ⇆ s2.head → N (top-left, ~15 px gap).
  s1.tail ⇆ s3.head → N (bottom-left, ~15 px gap).
  s2.tail ⇆ s3.tail-region → N (bottom-right, ~15 px gap).
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


def draw_kou(draw,
             s1_head=('ML', 0.671, 0.289), s1_tail=('BC', 0.02, 0.555),
             s2_head=('ML', 0.891, 0.333),
             s2_corner=('C', 0.93, 0.33),
             s2_tail=('BC', 0.937, 0.2),
             s3_head=('BC', 0.081, 0.458),
             s3_tail=('BR', 0.18, 0.344)):
    s1h = anchor_to_xy(s1_head); s1t = anchor_to_xy(s1_tail)
    s2h = anchor_to_xy(s2_head); s2c = anchor_to_xy(s2_corner); s2t = anchor_to_xy(s2_tail)
    s3h = anchor_to_xy(s3_head); s3t = anchor_to_xy(s3_tail)

    s1h_g = _shorten(s1h, s1t, 4)
    s1t_g = _shorten(s1t, s1h, 4)
    s2h_g = _shorten(s2h, s2c, 4)
    s2t_g = _shorten(s2t, s2c, 4)
    s3h_g = _shorten(s3h, s3t, 4)

    fat_line(draw, s1h_g, s1t_g, width=9)
    fat_line(draw, s2h_g, s2c, width=9)
    fat_line(draw, s2c, s2t_g, width=9)
    cx, cy = s2c; r = 6
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    fat_line(draw, s3h_g, s3t, width=9)
