# generated.py — p1_stroke_01_横
# Renders a single 横 (horizontal stroke) to a 300x300 PNG.

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Make the shared primitive importable.
_BANK_CODE = Path("/Users/peilinwu/Documents/AI memory research/experiments/"
                  "exp_context_effect/groups/G3_coords/success_bank/code")
sys.path.insert(0, str(_BANK_CODE))

from heng import draw_heng  # noqa: E402

OUT_PATH = Path("/Users/peilinwu/Documents/AI memory research/experiments/"
                "exp_context_effect/groups/G3_coords/attempts/"
                "p1_stroke_01_横/01_横.png")


def main() -> None:
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Coordinate-format placement: centered horizontal stroke.
    # (ox, oy, scale) = (0, 0, 1.0) draws a 200x12 px 横 at canvas center.
    draw_heng(draw, ox=0, oy=0, scale=1.0)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH, "PNG")


if __name__ == "__main__":
    main()
