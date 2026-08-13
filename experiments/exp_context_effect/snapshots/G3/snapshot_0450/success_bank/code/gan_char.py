# gan_char.py — 干 (gān), 3 strokes. Identity alias of gan radical.
# PASSed at p3_char_0069_干 (B4).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from gan import draw_gan  # noqa: E402


def draw_gan_char(t, ox=0, oy=0, scale=1.0):
    draw_gan(t, ox=ox, oy=oy, scale=scale)
