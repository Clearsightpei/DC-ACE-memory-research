# kou.py — 口 (kou) radical, 3 strokes (竖 + 横折 + 横).
# Batch B1 (position 89) — human PASSed.
#
# Pure composition: bank shu (left) + bank heng_zhe (top+right) +
# bank heng (bottom).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from shu import draw_shu            # noqa: E402
from heng import draw_heng          # noqa: E402
from heng_zhe import draw_heng_zhe  # noqa: E402


def draw_kou(t, ox=0.0, oy=0.0, scale=1.0):
    """口 radical: 3-stroke enclosing box."""
    # Left 竖: TL(-65,50) → BL(-65,-50).
    draw_shu(t, ox=ox + (-65) * scale, oy=oy + 0, scale=0.50 * scale)
    # Top + right 横折 at scale 0.75.
    draw_heng_zhe(t, ox=ox + 5 * scale, oy=oy + 5 * scale, scale=0.75 * scale)
    # Bottom 横 at y=-50.
    draw_heng(t, ox=ox + 0, oy=oy + (-50) * scale, scale=0.65 * scale)
