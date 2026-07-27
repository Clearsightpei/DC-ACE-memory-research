# p3_char_0078_艹 — identity alias to mastered radical cao_zi_tou.
# Character version 艹 has the same shape as the Phase-2 radical entry.
# Per memory_index step 3: try IDENTITY alias for Phase-3 char with matching radical bank entry.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.abspath(os.path.dirname(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from cao_zi_tou import draw_cao_zi_tou  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    # Identity alias: character-vs-radical scale = 1.0, no offset.
    draw_cao_zi_tou(t, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(_HERE, "01_艹.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
