"""Attempt: p1_stroke_02_竖 — vertical stroke (垂直笔画从上到下).

Uses the G4 米字格 anchor primitive `draw_shu`.
Canvas: 300×300, white background, black ink.
"""

import os, sys
from PIL import Image, ImageDraw

# Make the shared success_bank/code importable.
BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from shu import draw_shu  # noqa: E402

OUT_PNG = os.path.join(os.path.dirname(__file__), "01_竖.png")


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    # 竖 spans vertically down the center column: TC → BC, with a small
    # inset from the very top and bottom so the terminals sit within the
    # frame. This is the canonical single-stroke demo.
    draw_shu(
        d,
        start_anchor=('TC', 0.5, 0.15),  # top, centered horizontally
        end_anchor=('BC', 0.5, 0.85),    # bottom, centered horizontally
        width=10,
    )
    img.save(OUT_PNG)
    print(f"saved {OUT_PNG} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
