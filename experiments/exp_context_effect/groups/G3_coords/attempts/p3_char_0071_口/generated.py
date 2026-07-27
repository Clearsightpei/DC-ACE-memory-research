# p3_char_0071_口 — 口 (kou, "mouth"), 3 strokes.
# Identity alias for the mastered kou radical primitive (B1 PASS).
# Per memory_index step 3: character == radical shape → identity alias
# call at (ox=0, oy=0, scale=1.0).

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from kou import draw_kou  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw_kou(t, ox=0.0, oy=0.0, scale=1.0)
    out_path = os.path.join(os.path.dirname(__file__), "01_口.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
