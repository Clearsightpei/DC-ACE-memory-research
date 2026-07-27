# p3_char_0067_山 — character 山.
# Identity alias to the mastered radical shan (bank entry #61).
# Per memory_index v7: character-vs-radical, same shape → try IDENTITY first.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shan import draw_shan  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_shan(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_山.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
