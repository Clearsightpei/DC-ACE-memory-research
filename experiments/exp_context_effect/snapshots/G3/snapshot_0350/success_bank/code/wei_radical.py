# wei_radical.py — 囗 (wéi), 3-stroke enclosing box.
# Batch B2 (position 105) — human PASSed.
# Larger sibling of 口 (kou): enclosing radical role, scale ~0.90+.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu import draw_shu            # noqa: E402
from heng import draw_heng          # noqa: E402
from heng_zhe import draw_heng_zhe  # noqa: E402


def draw_wei_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """囗 radical: 3-stroke enclosing box (large)."""
    draw_shu(t, ox=ox + (-80) * scale, oy=oy + 7 * scale, scale=0.875 * scale)
    draw_heng_zhe(t, ox=ox + (-8.5) * scale, oy=oy + 47.4 * scale, scale=0.794 * scale)
    # right-side extension (heng_zhe's right vertical is too short)
    if scale == 1.0 and ox == 0 and oy == 0:
        t.line([(205, 162), (205, 230)], fill=(0, 0, 0), width=8)
    else:
        # scaled/offset extension
        x_r = 150 + (55) * scale + ox
        y_top = 150 - ((-12.1) * scale + oy)
        y_bot = 150 - ((-80) * scale + oy)
        t.line([(x_r, y_top), (x_r, y_bot)],
               fill=(0, 0, 0), width=max(2, int(round(8 * scale))))
    draw_heng(t, ox=ox + (-12.5) * scale, oy=oy + (-80) * scale, scale=0.675 * scale)
