"""p2_radical_114_日 — 日 (rì, "sun/day", 4画). B3 retry PASS.

口-family enclosure with middle 横 EXTENDING wall-to-wall (distinct
from 曰 where middle bar stops short). Retry-1 fix: extend s3 to
kiss right wall (ML→MR), extend s4 wall-to-wall (BL→BR).

Joints (all N, small 8-12 px gap):
  s1.head ⇆ s2.head; s1.mid ⇆ s3.head; s2.rightwall ⇆ s3.tail;
  s1.tail ⇆ s4.head; s2.tail ⇆ s4.tail.
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
    's1_h': ('TL', 0.80, 0.15), 's1_t': ('BL', 0.80, 0.92),
    's2_h': ('TL', 0.85, 0.15), 's2_c': ('TR', 0.50, 0.15), 's2_t': ('BR', 0.50, 0.92),
    's3_h': ('ML', 0.85, 0.55), 's3_t': ('MR', 0.50, 0.55),  # wall-to-wall
    's4_h': ('BL', 0.85, 0.88), 's4_t': ('BR', 0.50, 0.88),  # wall-to-wall
}


def draw_ri(draw, **overrides):
    p = {**DEFAULTS, **overrides}
    s1h = anchor_to_xy(p['s1_h']); s1t = anchor_to_xy(p['s1_t'])
    s2h = anchor_to_xy(p['s2_h']); s2c = anchor_to_xy(p['s2_c']); s2t = anchor_to_xy(p['s2_t'])
    s3h = anchor_to_xy(p['s3_h']); s3t = anchor_to_xy(p['s3_t'])
    s4h = anchor_to_xy(p['s4_h']); s4t = anchor_to_xy(p['s4_t'])
    w = 10
    fat_line(draw, _shorten(s1h, s1t, 5), _shorten(s1t, s1h, 5), width=w)
    fat_line(draw, _shorten(s2h, s2c, 5), s2c, width=w)
    fat_line(draw, s2c, _shorten(s2t, s2c, 5), width=w)
    r = 5
    draw.ellipse([s2c[0]-r, s2c[1]-r, s2c[0]+r, s2c[1]+r], fill=(0, 0, 0))
    fat_line(draw, _shorten(s3h, s3t, 5), _shorten(s3t, s3h, 8), width=w)
    fat_line(draw, _shorten(s4h, s4t, 5), _shorten(s4t, s4h, 8), width=w)
