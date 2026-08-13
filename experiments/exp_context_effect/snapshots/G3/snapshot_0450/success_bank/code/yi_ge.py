# yi_ge.py — 弋 (yì), 3 strokes: 横 + 斜钩 (belly bezier) + 点.
# PASSed at p3_char_0093_弋 (B5, pos 255). Uses _shared_helpers.tapered_*
# to render thin lines and belly-preserving bezier. Fixes previous errata
# where 斜钩 lost its belly.
from _shared_helpers import tapered_bezier, tapered_line


def draw_yi_ge(t, ox=0, oy=0, scale=1.0):
    """弋 — 3 strokes on math-coord canvas (thin uniform ~4-5 px)."""
    def _sh(mx, my):
        return (mx * scale + ox, my * scale + oy)

    # Stroke 1: short heng, upper-middle.
    tapered_line(t, _sh(-58, 12), _sh(48, 20), 4, 4)

    # Stroke 2: 斜钩 belly bezier + short hook.
    tapered_bezier(
        t,
        _sh(-35, 55),
        _sh(25, -30),
        _sh(48, -95),
        w_head=4, w_tail=5,
        n=64,
    )
    tapered_line(t, _sh(48, -95), _sh(72, -78), 5, 3)

    # Stroke 3: 点 — small dot upper-right.
    tapered_line(t, _sh(32, 60), _sh(48, 45), 3, 6)
