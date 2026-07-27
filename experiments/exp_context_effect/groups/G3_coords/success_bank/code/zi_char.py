# zi_char.py — 子 (zǐ, "child"), 3 strokes.
# PASSed at p3_char_0049_子 (B4) AS THE MAIN-CURRICULUM CHAR,
# and independently GRADUATED via p2_radical_082_子__retry_1 PASS.
# Recipe: 了's skeleton (top 横钩 + wan_gou descender) + crossing 横.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from liao import draw_liao  # noqa: E402
from heng import draw_heng  # noqa: E402


def draw_zi_char(t, ox=0, oy=0, scale=1.0):
    draw_liao(t, ox=ox, oy=oy, scale=scale)
    draw_heng(t, ox=ox + 15 * scale, oy=oy - 20 * scale, scale=1.0 * scale)


# Alias for the radical form (子 also passes standalone as radical after
# the B4 retry). Same recipe.
def draw_zi(t, ox=0, oy=0, scale=1.0):
    draw_zi_char(t, ox=ox, oy=oy, scale=scale)
