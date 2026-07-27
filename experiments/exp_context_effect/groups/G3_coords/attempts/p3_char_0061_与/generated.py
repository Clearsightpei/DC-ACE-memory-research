"""p3_char_0061_与 — G3 fresh derivation.

与 is a 3-stroke character:
  1. 横折 (top): short horizontal starting mid-upper, turning down at right end
     as a short vertical (the "shoulder").
  2. 横 (middle): short horizontal beneath, spanning less than stroke-1.
  3. 竖折折钩 (bottom): long horizontal at bottom, hooking up-and-right
     at the right end (small rising hook).

Coordinates are chosen fresh against 300x300 canvas.
"""
from PIL import Image, ImageDraw
from pathlib import Path


def draw_yu(img_draw, ox=0, oy=0, scale=1.0):
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    ink = "black"
    w_main = max(5, int(7 * scale))
    w_thin = max(4, int(6 * scale))

    # Stroke 1: 横折 — top short heng turning down at right
    # Small entering tick going down-right into the head
    img_draw.line([P(102, 70), P(112, 85)], fill=ink, width=w_thin)
    # Horizontal top
    img_draw.line([P(110, 85), P(210, 80)], fill=ink, width=w_main)
    # Turn down (short vertical, slight left lean)
    img_draw.line([P(208, 82), P(196, 140)], fill=ink, width=w_main)

    # Stroke 2: middle 横 — shorter horizontal beneath, tucked under shoulder
    # Small down-tick at start
    img_draw.line([P(122, 138), P(132, 148)], fill=ink, width=w_thin)
    img_draw.line([P(130, 148), P(205, 142)], fill=ink, width=w_main)

    # Stroke 3: 竖折折钩 — long bottom heng, turn down at right, hook back left
    # Long bottom horizontal
    img_draw.line([P(50, 220), P(230, 212)], fill=ink, width=w_main)
    # Turn down at right
    img_draw.line([P(228, 210), P(220, 258)], fill=ink, width=w_main)
    # Hook: small flick back up-left
    img_draw.line([P(220, 258), P(198, 250)], fill=ink, width=w_thin)


def main():
    out_dir = Path(__file__).parent
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_yu(d, ox=0, oy=0, scale=1.0)
    img.save(out_dir / "01_与.png")


if __name__ == "__main__":
    main()
