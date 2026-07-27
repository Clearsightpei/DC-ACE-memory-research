# zhao_top.py — 爫 (zhǎo, claw-top radical), 4 strokes.
# PASSed at p2_radical_131_爫 (B3 pos 158, 2026-07-22).
# Uses variant_pie + tapered_bezier from _shared_helpers.
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from _shared_helpers import variant_pie, tapered_bezier, to_px  # noqa: E402


def draw_zhao_top(draw, ox=0, oy=0, scale=1.0):
    """Compact upper claw cluster. Math coords (center origin, +y up)."""
    def P(x, y): return (ox + x * scale, oy + y * scale)
    variant_pie(draw, head=P(-18, 30), tail=P(-38, 8),
                bow_perp=-2.5 * scale, w_head=6.0 * scale, w_tail=1.5 * scale)
    variant_pie(draw, head=P(0, 32), tail=P(-10, 12),
                bow_perp=-2.0 * scale, w_head=5.5 * scale, w_tail=1.2 * scale)
    variant_pie(draw, head=P(18, 32), tail=P(10, 12),
                bow_perp=-2.0 * scale, w_head=5.5 * scale, w_tail=1.2 * scale)
    tapered_bezier(draw, P(-22, 42), P(0, 52), P(22, 46),
                   w_head=4.5 * scale, w_tail=5.5 * scale, n=40)
    cx, cy = to_px(ox + 22 * scale, oy + 46 * scale)
    r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    variant_pie(draw, head=P(22, 46), tail=P(15, 30),
                bow_perp=-1.0 * scale, w_head=5.5 * scale, w_tail=1.2 * scale)
