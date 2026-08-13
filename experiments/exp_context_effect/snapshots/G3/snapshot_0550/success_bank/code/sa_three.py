# 仨 (sā) — bank entry (B7 curator promotion, main PASS)
# Source: groups/G3_coords/attempts/p3_char_0189_仨/generated.py
# Note: 5 (ren_pang left + 三 right inline thin)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

# p3_char_0189_仨 — 仨 (sā), 5 strokes: 亻 (left) + 三 (right, 3 hengs).
# Revision: san_char.py uses fixed length_px (not scaled), causing the
# bottom heng to run off canvas at scale=0.55. Inline three draw_yi calls
# with hand-scaled length_px + oy offsets, and raise the whole char.
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from yi import draw_yi  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left — compressed, positioned in left ~35%. Raise so it
    # spans roughly the vertical extent of the char.
    draw_ren_pang(d, ox=-55.0, oy=25.0, scale=0.65)

    # 三 on right (~55–58% width). Three hengs: short top / short mid /
    # longer bottom, hand-scaled lengths so nothing runs off canvas.
    ox_r = 50.0
    draw_yi(d, ox=ox_r,        oy=60.0,  length_px=55, scale=0.7)
    draw_yi(d, ox=ox_r,        oy=15.0,  length_px=60, scale=0.7)
    draw_yi(d, ox=ox_r - 5.0,  oy=-40.0, length_px=105, scale=0.9)

    out = os.path.join(os.path.dirname(__file__), "01_仨.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
