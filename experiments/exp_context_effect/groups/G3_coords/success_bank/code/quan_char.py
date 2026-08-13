# quan_char.py — 畎 (quǎn) — promoted from p3_char_0434_畎 (B12 main verdict: A)
# Curator B12 (2026-08-04, position 601).
#
# ★★★ FIRST-EVER A VERDICT FOR G3 ★★★
# After 600 items across 12 batches / 4 format-freedom unlocks with ZERO
# A verdicts, 畎 broke through. This wrapper composes the two variants
# extracted from the passing render:
#   - quan_tian_for_LR_left (compressed 田, left ~40% of canvas)
#   - quan_dog_for_LR_right (犬 = 大 + upper-right dot, right ~55%)
#
# What made 畎 A-tier (see P-DEV4 in principle_bank.md):
# 1. Explicit x-slot decomposition (30..125 / 150..275) — hard boundaries
#    between the two halves.
# 2. Thin uniform ink (w=4-5px) matching MMH GT.
# 3. Cross-apex weld computed explicitly — pie and na share the same
#    (215, 143) crossing pixel on heng.
# 4. Two-cubic pie form (head + body) — continuous curve through cross.
# 5. Small dian upper-right (this is what makes 犬 not 大).
# 6. X-crossing family COMPRESSED into L-R right slot rather than
#    occupying full canvas — this is the mechanism P-DEV4 codifies.
#
# The 大-family standalone (人/入/大/矢/失) are TERMINAL_FROZEN. 犬 works
# BECAUSE it's compressed. Do not read this as unfreezing standalone 大.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.dirname(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from quan_tian_for_LR_left import draw_quan_tian_for_LR_left  # noqa: E402
from quan_dog_for_LR_right import draw_quan_dog_for_LR_right  # noqa: E402


def draw_quan(d):
    """Compose 畎 = 田-left + 犬-right in a 300x300 canvas."""
    draw_quan_tian_for_LR_left(d)
    draw_quan_dog_for_LR_right(d)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_quan(d)
    out = os.path.join(os.path.dirname(__file__), "01_畎.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
