# san_dian_shui.py — 氵 (three-drops-water radical), 3 strokes.
# Batch B2 (position 101) — human PASSed.
# Two dian + one ti — all from bank at deliberate (ox, oy, scale).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from dian import draw_dian  # noqa: E402
from ti import draw_ti      # noqa: E402


def draw_san_dian_shui(t, ox=0.0, oy=0.0, scale=1.0):
    """氵 radical, 3 strokes."""
    draw_dian(t, ox=ox + 5 * scale, oy=oy + 54 * scale, scale=0.55 * scale)
    draw_dian(t, ox=ox - 26 * scale, oy=oy - 6 * scale, scale=0.55 * scale)
    draw_ti(t, ox=ox - 10 * scale, oy=oy - 69 * scale, scale=0.35 * scale)
