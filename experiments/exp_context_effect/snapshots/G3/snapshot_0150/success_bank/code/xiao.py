# xiao.py — 小 (xiǎo, small), 3 strokes.
# Batch B2 (position 108) — human PASSed.
# Composition: shu_gou (center) + inline-fresh left short 撇 + dian (right).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu_gou import draw_shu_gou            # noqa: E402
from dian import draw_dian                  # noqa: E402
from _shared_helpers import variant_pie      # noqa: E402


def draw_xiao(t, ox=0.0, oy=0.0, scale=1.0):
    """小 radical, 3 strokes."""
    draw_shu_gou(t, ox=ox + 0.0 * scale, oy=oy - 15.0 * scale, scale=0.65 * scale)
    # Left short 撇 — inline-fresh via variant_pie
    variant_pie(t,
                head=(ox - 12.0 * scale, oy + 10.0 * scale),
                tail=(ox - 65.0 * scale, oy - 45.0 * scale),
                bow_perp=-4.0 * scale, w_head=9.0 * scale, w_tail=1.0 * scale)
    draw_dian(t, ox=ox + 48.0 * scale, oy=oy - 5.0 * scale, scale=0.65 * scale)
