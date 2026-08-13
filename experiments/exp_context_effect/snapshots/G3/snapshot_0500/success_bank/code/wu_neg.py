# p3_char_0145_勿 (wù) — G3 attempt
# 4 strokes: (1) short 撇 (top-center, small), (2) 横折钩 envelope
# (top→shoulder→shaft→hook), (3) long inside 撇, (4) another long inside 撇.
# Recipe: adapt bao_char.py (勹 envelope) then add two long pies inside.
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
# Add success_bank/code to path so we can import bao_char
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from bao_char import draw_bao_char  # envelope + top pie
from _shared_helpers import variant_pie


def render(out_path):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # (1)+(2) Reuse bao_char (short top pie + envelope). 勿's envelope
    # is very similar to 勹's; slight downshift so we have room above
    # for the top pie and inside for the two additional 撇.
    draw_bao_char(d, ox=0, oy=0, scale=1.0)

    # variant_pie uses MATH coords (center origin, +y up).
    # (3) First long inner 撇 — starts under envelope near left-top,
    # sweeps down-left to bottom-left corner.
    # PIL (115, 115) -> math (-35, 35);  PIL (55, 250) -> math (-95, -100)
    variant_pie(d, head=(-35, 35), tail=(-95, -100),
                bow_perp=10.0, w_head=8.0, w_tail=2.0, n=48)

    # (4) Second long inner 撇 — parallel, further right, ends center-low.
    # PIL (165, 115) -> math (15, 35);  PIL (100, 265) -> math (-50, -115)
    variant_pie(d, head=(15, 35), tail=(-50, -115),
                bow_perp=10.0, w_head=8.0, w_tail=2.0, n=48)

    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_勿.png")
    render(out)
    print("wrote", out)
