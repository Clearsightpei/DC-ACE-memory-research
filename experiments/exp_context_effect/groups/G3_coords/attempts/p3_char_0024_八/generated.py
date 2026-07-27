# p3_char_0024_八 — 八 (ba, "eight"), 2 strokes.
# Reuses the mastered draw_ba primitive (pie + na, splayed with V-notch).
# Called at (ox=0, oy=0, scale=1.0) — the bootstrap params PASSed.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ba import draw_ba  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw_ba(t, ox=0.0, oy=0.0, scale=1.0)
    out_path = os.path.join(os.path.dirname(__file__), "01_八.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
