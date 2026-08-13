"""p2_radical_129_曰 — 曰 (yuē, "to say", 4画).

口-family enclosure + inner middle 横 that DOES NOT reach right wall
(distinct from 日 which needs middle 横 wall-to-wall).

Joints (all N — 口-family open-corner):
  s1.head ⇆ s2.head : N top-left
  s1.mid  ⇆ s3.head : N inner left
  s1.tail ⇆ s4.head : N bottom-left
  s2.tail ⇆ s4.tail : N bottom-right
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from _anchor import anchor_to_xy, fat_line


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6: return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


DEFAULTS = {
    's1_h': ('TL', 0.30, 0.15), 's1_t': ('BL', 0.30, 0.90),
    's2_h': ('TL', 0.36, 0.15), 's2_c': ('TR', 0.90, 0.15), 's2_t': ('BR', 0.90, 0.90),
    's3_h': ('ML', 0.36, 0.50), 's3_t': ('C',  0.60, 0.50),
    's4_h': ('BL', 0.36, 0.90), 's4_t': ('BR', 0.90, 0.90),
}


def draw_yue(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    s1h = anchor_to_xy(p['s1_h']); s1t = anchor_to_xy(p['s1_t'])
    s2h = anchor_to_xy(p['s2_h']); s2c = anchor_to_xy(p['s2_c']); s2t = anchor_to_xy(p['s2_t'])
    s3h = anchor_to_xy(p['s3_h']); s3t = anchor_to_xy(p['s3_t'])
    s4h = anchor_to_xy(p['s4_h']); s4t = anchor_to_xy(p['s4_t'])
    w = 10
    fat_line(draw, _shorten(s1h, s1t, 6), _shorten(s1t, s1h, 6), width=w)
    fat_line(draw, _shorten(s2h, s2c, 6), s2c, width=w)
    fat_line(draw, s2c, _shorten(s2t, s2c, 10), width=w)
    r = 6
    draw.ellipse([s2c[0]-r, s2c[1]-r, s2c[0]+r, s2c[1]+r], fill=(0, 0, 0))
    fat_line(draw, _shorten(s3h, s3t, 5), s3t, width=w)
    fat_line(draw, _shorten(s4h, s4t, 6), _shorten(s4t, s4h, 10), width=w)
