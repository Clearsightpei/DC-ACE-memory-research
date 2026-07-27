"""p3_char_0032_凵 — G3 attempt.

凵 (qu/kan) as a standalone character. The mastered radical primitive
`qu_radical.draw_qu_radical` already produces the U-shape (inlined
竖折 + short right 竖). The character is orthographically identical
to the radical — call the bank primitive with a modest scale bump so
the character reads as prominent on the 300x300 canvas.

Deliberate transform per TR1-TR3:
  ox=0, oy=0 — centered on canvas midpoint. GT places the U in the
    lower half; the primitive itself extends further down than up
    from origin (v_top=+10, v_bot=-80) so the natural centering
    already skews the ink toward the bottom half, matching GT.
  scale=1.05 — character context vs radical context: a standalone
    character should occupy slightly more of the canvas than a
    left/right/embedded radical. 1.0 was mastered for the radical;
    +5% bump gives character-scale presence without exceeding the GT
    envelope (GT U spans ~130px wide, primitive at s=1.05 spans
    (80-(-80))*1.05 = 168px which sits well inside 300px canvas).
"""

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from qu_radical import draw_qu_radical  # noqa: E402


def render(out_path: str) -> None:
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_qu_radical(draw, ox=0, oy=-15, scale=1.05)
    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_凵.png")
    render(out)
    print(f"wrote {out}")
