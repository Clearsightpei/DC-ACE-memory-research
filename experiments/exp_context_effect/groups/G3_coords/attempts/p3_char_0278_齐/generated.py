"""p3_char_0278_齐 — G3 attempt.

齐 (simplified, 6 strokes):
  1. 撇 (top-left of the ^ hat)
  2. 捺 (top-right of the ^ hat)
  3. 横 (long horizontal under the hat)
  4. 撇 (long pie from top of X crossing to lower-left)
  5. 捺 (long na from top of X crossing to lower-right)
  6. 竖 (short central vertical hanging from the horizontal)

Rendered inline with PIL: uniform thin ink per P12 (GT is thin).
G3 unit constraint satisfied — this file defines a callable draw_qi().
"""
from PIL import Image, ImageDraw
from pathlib import Path


def draw_qi(img_path: Path, size: int = 300) -> None:
    img = Image.new("RGB", (size, size), "white")
    d = ImageDraw.Draw(img)
    w = 5  # thin ink to match MMH GT

    # 1. top-left pie (small hat left half)
    d.line([(155, 55), (110, 95)], fill="black", width=w)
    # 2. top-right na (small hat right half) — starts from apex, goes right-down
    d.line([(155, 55), (215, 100)], fill="black", width=w)

    # 3. long horizontal 横 across mid
    d.line([(55, 135), (250, 135)], fill="black", width=w)

    # 4. long pie 撇 — from just above horizontal center-right, sweep to lower-left
    #    curved slightly by using two-segment approximation
    d.line([(175, 125), (140, 175)], fill="black", width=w)
    d.line([(140, 175), (75, 260)], fill="black", width=w)

    # 5. long na 捺 — from just above horizontal center-left, sweep to lower-right
    d.line([(135, 125), (170, 175)], fill="black", width=w)
    d.line([(170, 175), (245, 235)], fill="black", width=w)

    # 6. central vertical 竖 hanging from the horizontal
    d.line([(150, 135), (150, 265)], fill="black", width=w)

    img.save(img_path)


if __name__ == "__main__":
    out = Path(__file__).parent / "01_齐.png"
    draw_qi(out)
    print(f"wrote {out}")
