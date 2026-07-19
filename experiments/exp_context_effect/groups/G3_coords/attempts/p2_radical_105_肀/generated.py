"""肀 (yu) — 4-stroke radical.

Decomposition (from GT observation):
  1. 横折 (heng-zhe) at top: short horizontal top-bar with a downward
     right shoulder (small right-side down-tick), positioned upper-center.
  2. 横 (short) upper-middle: shorter horizontal crossing the vertical
     around y=+35 (math coords).
  3. 横 (wider) lower-middle: wider horizontal crossing the vertical
     around y=-15.
  4. 竖 (long) vertical: runs from top (y~+70) all the way down to
     y~-125 (extends below both hengs, long tail).

INLINE-FRESH decisions (TR8):
- Vertical is a plain 竖 shape — reuse `draw_shu` primitive with a
  shifted (ox, oy) and larger scale (long vertical). Pure translation
  of the standalone shape, no re-anchoring → primitive fits (TR8-1/2/3).
- Two middle hengs are plain horizontals — reuse `draw_heng` with
  chosen (ox, oy) and scale (short). Pure translation, primitive fits.
- Top 横折: reuse `draw_heng_zhe`? Its default aspect is a wide box.
  In 肀 the top element is a short bar with a small right-side tick.
  Extreme scale would flatten. INLINE-FRESH it as a short heng + a
  small vertical stub with a corner blob (P6).
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw

# Import G3 bank primitives from the group's success_bank
BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402


CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def draw_yu_radical(t):
    # --- Stroke 4: long vertical spine (drawn first for layering) ---
    # Shu default: 200 px @ scale=1.0. Extend UP through top hz.
    # Target top y ≈ +85, bottom y ≈ -125. Length = 210 px. scale=1.05.
    # Center of shaft at y = (-125 + 85)/2 = -20. ox=0, oy=-20.
    draw_shu(t, ox=0, oy=-20, scale=1.05)

    # --- Stroke 1: 横折 at top ---
    # Short horizontal top bar (~55 px wide) with a small downward
    # vertical stub on the right (~14 px). Top bar sits AT the top of
    # the vertical shaft (y ~ +80) so the shaft pokes through it.
    ink_w = 8
    hz_x_left, hz_y_top = _to_pixel(-28, 78)
    hz_x_right, hz_y_right = _to_pixel(28, 78)
    hz_x_stub, hz_y_stub = _to_pixel(28, 62)
    t.line([(hz_x_left, hz_y_top), (hz_x_right, hz_y_right)],
           fill=(0, 0, 0), width=ink_w)
    t.line([(hz_x_right, hz_y_right), (hz_x_stub, hz_y_stub)],
           fill=(0, 0, 0), width=ink_w)
    # Corner blob (顿笔) — small filled ellipse at the corner.
    r = 5
    t.ellipse([hz_x_right - r, hz_y_right - r,
               hz_x_right + r, hz_y_right + r], fill=(0, 0, 0))

    # --- Stroke 2: upper 横 (shorter) ---
    # Target width ~ 110 px, oy = +30. scale = 0.55.
    draw_heng(t, ox=3, oy=30, scale=0.55)

    # --- Stroke 3: lower 横 (wider) ---
    # Target width ~ 156 px, oy = -20. scale = 0.78.
    draw_heng(t, ox=0, oy=-20, scale=0.78)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_yu_radical(t)
    out = Path(__file__).parent / "01_肀.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
