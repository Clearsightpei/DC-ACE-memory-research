# p3_char_0015_二 — 二 ("two"), 2 strokes (short 横 on top + long 横 on bottom).
# Reuse of Success Bank primitive draw_er (bootstrap-batch PASS at p2_radical_018_二).
# The radical form and character form of 二 are visually identical, so the
# same coord recipe applies. Deliberate (ox, oy, scale) chosen for THIS
# composition: the character 二 fills the whole cell (300x300), so no
# further downscaling from the radical baseline; center at canvas midpoint.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from er import draw_er  # noqa: E402


def render(output_path: str) -> None:
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # 二 as a standalone character occupies the full 米字格. draw_er's
    # canonical form places upper heng at y=+45 (math) and lower at y=-80
    # (math), which pushes the lower heng near the bottom edge. Nudge the
    # whole composition upward by ~15px so both strokes sit inside the
    # visual cell more comfortably.
    draw_er(t, ox=0.0, oy=10.0, scale=1.0)

    img.save(output_path)


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_二.png")
    render(out)
    print(f"wrote {out}")
