# p3_char_0028_冖 — G3 render.
# 冖 (mi, "cover" / 秃宝盖) — 2 strokes: small 点 top-left + 横钩.
# Same graphic as the p2 radical; bank has a mastered mi_radical.py.
# Standalone character occupies full canvas — deliberate (ox=0, oy=0, scale=1.0)
# per TR1-TR3 (character is at canvas-natural scale, no compositional shrink).

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from mi_radical import draw_mi_radical  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    # Standalone character at canvas natural scale (deliberate — not defaults).
    draw_mi_radical(draw, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(_HERE, "01_冖.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
