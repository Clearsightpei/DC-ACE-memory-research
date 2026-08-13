# niu.py — 牛 (niú, ox), 4 strokes.
# Batch B2 (position 138) — human PASSed.
# Pure bank composition: pie + heng + heng + shu.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402
from pie import draw_pie    # noqa: E402


def draw_niu(t, ox=0.0, oy=0.0, scale=1.0):
    """牛 radical, 4 strokes."""
    draw_pie(t, ox=ox + (-25) * scale, oy=oy + 43 * scale, scale=0.45 * scale)
    draw_heng(t, ox=ox + 15 * scale, oy=oy + 45 * scale, scale=0.325 * scale)
    draw_heng(t, ox=ox + 10 * scale, oy=oy + 0 * scale, scale=0.9 * scale)
    draw_shu(t, ox=ox + 3 * scale, oy=oy - 17.5 * scale, scale=0.925 * scale)
