# p3_char_0173_仔__retry_1 — 仔 (zǐ), 5 strokes: 亻 + 子.
#
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): errata.md says "use `zi_char` (bank #122) verbatim on the
#   right, at scale ~0.65, ox=+40" — prior retry_0 inlined 子 and the
#   hook/heng disconnected from the crossing. This retry applies the fix.
# Q2 (form_catalog): 亻-family rows say ren_pang identity-alias on left,
#   fail is always in the right component. Bank has zi_char (#122) —
#   direct reuse is the recipe form_catalog prescribes.
# Q3 (helpers): fail category was "right component missing" (composition
#   content gap, not a joint-weld gap), so kiss_apex / mirror_dian_pair
#   don't apply. The lever is bank-primitive reuse (zi_char), not a
#   variant helper.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from liao import draw_liao          # noqa: E402
from wan_gou import draw_wan_gou    # noqa: E402


def _short_heng(t, x_l, y_l, x_r, y_r, ink=9):
    """Simple crossing 横 with slight taper — used to weld across the 弯钩."""
    steps = 20
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x_l + (x_r - x_l) * t0
        ya = y_l + (y_r - y_l) * t0
        xb = x_l + (x_r - x_l) * t1
        yb = y_l + (y_r - y_l) * t1
        t.line([(xa, ya), (xb, yb)], fill="black", width=ink)


def draw(t, ox=0, oy=0, scale=1.0):
    # Left 亻 — same numbers that PASSed in prior 亻-family renders.
    # ren_pang uses math coords (center origin, +y up).
    draw_ren_pang(t, ox=ox + (-70) * scale, oy=oy + 10 * scale,
                  scale=0.75 * scale)

    # Right 子 — errata fix idea says "zi_char verbatim @ scale 0.65,
    # ox=+40" but that leaves zi_char's crossing heng too long AND
    # dipping into the 亻 territory (retry_0 self-check confirms).
    # Compose from the same sub-primitives (liao's hengou+wan_gou
    # skeleton + custom shorter crossing heng shifted right).
    s = 0.72 * scale
    # liao at ox=+35 shifts hengou to pixel (95..240) at y=(85+oy..80+oy).
    # wan_gou inside liao is scale=0.85*s ~ 0.61, larger than the
    # retry_0 attempt (0.55) — matches GT's prominent descender.
    draw_liao(t, ox=35 + ox, oy=oy, scale=s)

    # Custom crossing 横 — spans right-half only, centered on wan_gou
    # shaft (~pixel x=190). Sits at y ~ 165 to weld the descender at
    # mid-height, per GT.
    _short_heng(t, 145, 168, 265, 165, ink=9)


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw(t)
    out = os.path.join(os.path.dirname(__file__), "01_仔.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
