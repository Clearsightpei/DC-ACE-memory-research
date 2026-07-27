# generated.py — 中 (zhōng), Phase-3 character, 4 strokes.
# Composition: bank `kou` for the enclosing box + inline `shu` for the
# central vertical (drawn with deliberate length so it protrudes above
# and below the box — the defining silhouette of 中).
#
# GT observation: kou sits in the upper-middle; central vertical is
# long, protruding a short distance above the box and a long tail below.
# Horizontally the vertical passes through the box's exact center.

import os
import sys
from PIL import Image, ImageDraw

# Wire up the shared success_bank code directory so imports work.
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from kou import draw_kou   # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center, +y up) -> PIL pixel (top-left, +y down)."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_zhong(t, ox=0, oy=0, scale=1.0):
    """中 (zhong).

    kou box: centered horizontally, sitting above center (oy ≈ +5).
      At scale 0.55 the kou spans x∈[-36, +36], y∈[-23, +33].
    Central vertical: from y ≈ +55 (short protrusion above box)
      down to y ≈ -110 (long tail below box), x = 0, thickness 10.
    """
    # kou at moderate scale, shifted up slightly (box sits in upper half).
    draw_kou(t,
             ox=ox + 0 * scale,
             oy=oy + 5 * scale,
             scale=0.55 * scale)

    # Central vertical (shu) — inline for deliberate length control.
    # Top ≈ 20px above the box top (box top ≈ y=33 → shu top ≈ y=55).
    # Bottom ≈ 80px below box bottom (box bottom ≈ y=-23 → shu bottom ≈ y=-103).
    top_y = 55 * scale
    bot_y = -110 * scale
    thickness = max(1, int(round(10 * scale)))
    x_top, y_top = _to_pixel(ox + 0, oy + top_y)
    x_bot, y_bot = _to_pixel(ox + 0, oy + bot_y)
    t.line([(x_top, y_top), (x_bot, y_bot)],
           fill=(0, 0, 0), width=thickness)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_zhong(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_中.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
