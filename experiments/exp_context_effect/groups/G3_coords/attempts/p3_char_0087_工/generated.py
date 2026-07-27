# p3_char_0087_工 — character 工 (gong, "work").
# 3 strokes: top 横 (shorter), middle 竖 (short), bottom 横 (wider).
#
# Recipe: identity alias of the PASSing gong.py radical primitive
# (batch B1 pos 81). The character 工 and the radical 工 are the same
# glyph. Per memory_index "Char-vs-radical Character-vs-radical scaling"
# guidance and TR1: prefer identity alias when shape matches. Called
# with (ox=0, oy=0, scale=1.0) — deliberate: canvas-centered at the
# primitive's canonical size (GT is ~200px tall, matches unit).

import os
import sys

from PIL import Image, ImageDraw

# Make success_bank/code importable.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from gong import draw_gong  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Identity alias — the radical's canonical size fits the 300x300 canvas
    # for the character 工 (GT shows top ~110-190 wide heng, bottom ~30-270).
    draw_gong(draw, ox=0.0, oy=0.0, scale=1.0)

    out_path = os.path.join(_HERE, "01_工.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
