# p3_char_0171_疒__retry_1 — 疒 (sickness radical), 5 strokes.
#
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): "疒 — call guang (广) explicitly; drawer omitted the whole envelope."
#   Fix: reuse draw_guang (envelope) + inline two inner dots (冫-like pair)
#   on the LEFT side of the pie belly. Prior retry code was close but the
#   two dots and pie were dwarfed. This retry keeps guang at scale 1.0 and
#   places the two inner dots larger and more centered inside the belly.
# Q2 (form_catalog): 广-envelope + inner dot pair. Uses P/T-style dot for
#   upper and a mini提 for lower. Row of interest: "envelope + interior".
# Q3 (helpers): No helpers imported — the envelope function draw_guang
#   already handles the frame; the two inner dots are inline hand-render
#   (mirror_dian_pair does not apply — 疒's pair is 冫-arranged vertically,
#   not the horizontal 丷 pair the helper models).

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from guang import draw_guang  # noqa: E402


def _px(cx, cy):
    return 150 + cx, 150 - cy


def _draw_tapered_line(draw, p0, p1, w_head, w_tail, n=24):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def _draw_inner_dot_top(draw, ox, oy):
    # Upper 冫-dot — short slash from upper-left to lower-right, thin→thick.
    # Sits inside 广's belly, well BELOW the heng roof, LEFT of pie mid.
    p0 = _px(ox + -75, oy + -10)
    p1 = _px(ox + -55, oy + -28)
    _draw_tapered_line(draw, p0, p1, w_head=3.5, w_tail=9.0, n=22)


def _draw_inner_dot_bottom(draw, ox, oy):
    # Lower 冫-mark — 提 (rising flick), thick→thin from lower-left up-right.
    # Below the upper dot, still left of pie shaft.
    p0 = _px(ox + -95, oy + -60)
    p1 = _px(ox + -68, oy + -48)
    _draw_tapered_line(draw, p0, p1, w_head=9.5, w_tail=2.5, n=22)


def draw_nechuang(t, ox=0.0, oy=0.0, scale=1.0):
    """疒 radical: 广 base + two 冫-like inner dot marks tucked on the left."""
    draw_guang(t, ox=ox, oy=oy, scale=scale)
    _draw_inner_dot_top(t, ox, oy)
    _draw_inner_dot_bottom(t, ox, oy)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Center 广 with slight up-right nudge so pie tail lands near
    # bottom-center; dots go into left half of belly.
    draw_nechuang(draw, ox=15, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疒.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
