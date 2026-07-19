"""p1_stroke_05_点 — Phase-1 primitive #05 rendering attempt.

Draws a single 点 (short diagonal dot) centered on the 米字格.

Anchor plan:
  head @ ('C', 0.40, 0.30)  — upper-left, fine 起笔
  tail @ ('C', 0.60, 0.60)  — lower-right, rounded 顿笔 press
  Both anchors inside the central cell → keeps the dot short and
  compact per the 点画，短小的斜点 description.

Joint spec: single stroke, no joints.
"""
import sys
from pathlib import Path

# Make the shared bank importable (draw_dian + _anchor).
BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from dian import draw_dian


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    draw_dian(
        d,
        start_anchor=('C', 0.40, 0.30),   # head, upper-left, fine
        end_anchor=('C', 0.60, 0.60),     # tail, lower-right, rounded press
        head_width=2,
        peak_width=11,
        curve=0.08,
        segments=24,
    )

    out = Path(__file__).with_name("01_点.png")
    img.save(out)
    # Confirm dimensions.
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"wrote {out} size={img.size}")


if __name__ == "__main__":
    main()
