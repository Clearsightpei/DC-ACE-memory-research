# p3_char_0021_几 — Phase 3 character 几.
# Orthographically identical to the mastered radical 几 (bank #41, ji.py).
# Reusing the mastered draw_ji primitive with modest recentering for the
# clean (regenerated) GT which shows 几 centered in the 300x300 canvas
# at moderate fill.

import os
import sys
from PIL import Image, ImageDraw

# Add success_bank/code to path so we can import draw_ji.
_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from ji import draw_ji  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Bank recipe's natural bbox roughly x=[75,245], y=[95,262],
    # center approx (160, 178). To recenter on canvas (150, 150) with
    # some breathing room, translate ox=-10, oy=+28 (oy positive = up
    # in the _apply convention), and keep scale=1.0 to match GT fill.
    draw_ji(draw, ox=-10.0, oy=28.0, scale=1.0)

    out = os.path.join(os.path.dirname(__file__), "01_几.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
