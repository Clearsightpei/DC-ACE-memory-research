"""Attempt: p1_stroke_01_横 (G4 — grid-bank memory).

Target: 横 — a single horizontal stroke, left → right.

Composition (米字格 anchors):
  draw_heng(('ML', 0.15, 0.5), ('MR', 0.85, 0.5))

Rationale:
  - Runs along the horizontal mid-band of the character region.
  - Starts near the left edge of the ML cell (x_frac=0.15) and ends
    near the right edge of the MR cell (x_frac=0.85), giving a stroke
    that spans ~70% of the canvas width. That matches the visual
    weight of an isolated 横 in a printed dictionary rendering
    (占中间行, 两端留白).
  - Vertically centered in the mid row (y_frac=0.5 in both ML and MR).
  - Stroke width 10 px (~3.3% of canvas, ~10% of cell) — typical
    printed kaishu weight.
  - Single stroke → no joint list needed.
"""

import sys
from pathlib import Path

# Import from this G4 group's success bank.
SUCCESS_BANK_CODE = Path(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G4_grid/success_bank/code"
)
sys.path.insert(0, str(SUCCESS_BANK_CODE))

from PIL import Image, ImageDraw
from heng import draw_heng


OUT_PATH = Path(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G4_grid/attempts/p1_stroke_01_横/01_横.png"
)


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # 米字格 anchors: horizontal mid-band, spanning ML left → MR right.
    draw_heng(draw,
              start_anchor=('ML', 0.15, 0.5),
              end_anchor=('MR', 0.85, 0.5),
              width=10,
              color=(0, 0, 0))
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
