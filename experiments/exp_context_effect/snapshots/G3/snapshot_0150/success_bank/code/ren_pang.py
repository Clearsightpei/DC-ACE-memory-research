# ren_pang.py — 亻 (ren-pang, "person" side radical), 2 strokes.
# Batch B1 (position 61) — human PASSed.
#
# Composition: bank pie (compressed) + bank shu (short) with shu head
# touching pie's mid-shaft.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402


def draw_ren_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """亻 radical: pie (top, sweeping down-left) + short shu (right)."""
    # pie at scale 0.80, offset (-23, +20) — compressed sweep.
    draw_pie(t, ox=ox + (-23) * scale, oy=oy + 20 * scale, scale=0.80 * scale)
    # shu at scale 0.50, offset (+20, -40) — short vertical on the right.
    draw_shu(t, ox=ox + 20 * scale, oy=oy + (-40) * scale, scale=0.50 * scale)
