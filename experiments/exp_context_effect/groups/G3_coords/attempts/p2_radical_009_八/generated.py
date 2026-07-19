"""p2_radical_009_八 — G3 attempt.

八 = 撇 (left, splayed down-left) + 捺 (right, splayed down-right).
Small gap between the two heads near the upper center of the canvas.

Bank primitives (TR6 comments):
- pie standalone: head (65,90) math → pixel (215,60); tail (-45,-85) → pixel (105,235).
  Standalone is too tall and too shifted right of center for 八's left stroke.
  Target left stroke: head near pixel (155, 95), tail near pixel (90, 230).
  Chosen scale 0.75. At scale 0.75:
    default head pixel = (150 + 65*0.75, 150 - 90*0.75) = (198.75, 82.5)
    default tail pixel = (150 - 45*0.75, 150 + 85*0.75) = (116.25, 213.75)
  Shift by ox=-45, oy=+5 -> head pixel = (153.75, 77.5); tail pixel = (71.25, 208.75).
  Slightly high tail — bump oy down: ox=-45, oy=-10 -> head (153.75, 92.5); tail (71.25, 223.75).

- na standalone: head (-70,80) → pixel (80,70); tail (80,-90) → pixel (230,240).
  Target right stroke: head near pixel (165, 95), tail near pixel (230, 235).
  Chosen scale 0.75. At scale 0.75:
    default head pixel = (150 - 70*0.75, 150 - 80*0.75) = (97.5, 90.0)
    default tail pixel = (150 + 80*0.75, 150 + 90*0.75) = (210, 217.5)
  Shift by ox=+65, oy=+5 -> head pixel = (162.5, 85); tail pixel = (275, 212.5).
  Tail too far right — reduce ox: ox=+50, oy=-15 -> head (147.5, 105); tail (260, 232.5).
  Better: ox=+55, oy=-10 -> head (152.5, 100); tail (265, 227.5). Still right-heavy.
  Use ox=+50, oy=-15: head (147.5, 105); tail (260, 232.5).

Eyeball sanity (TR7):
- Gap at top: pie head pixel_x 153.75, na head pixel_x 147.5 — heads nearly coincide
  which will look joined. In 八 the top should have a small V-notch. Split them:
  pie head slightly left, na head slightly right, both at similar y.
  Adjust: pie ox=-50 (head 148.75), na ox=+55 (head 152.5). Very close still.
  Actually 八's top has heads that are close but distinct; the pie head is
  slightly to the LEFT of the na head. Try: pie ox=-52 head 146.75; na ox=+58
  head 155.5. That gives ~9 px gap between the two heads. Good.
"""

from PIL import Image, ImageDraw
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # REVISION notes vs pass 1:
    # - Heads were too close (formed a caret). GT has a clear V-notch gap
    #   between the two heads. Separate them: pie head shifts LEFT
    #   (ox more negative), na head shifts RIGHT (ox more positive).
    # - na tail was too heavy (blob). scale down further so belly is
    #   less pronounced.
    # - Both strokes should read as more "splayed" not so tall.

    # 撇 — left stroke of 八. scale 0.65, head pulled further left.
    # At scale 0.65: default head pixel = (150 + 65*0.65, 150 - 90*0.65) = (192.25, 91.5)
    #                default tail pixel = (150 - 45*0.65, 150 + 85*0.65) = (120.75, 205.25)
    # ox=-40, oy=+5 -> head pixel (152.25, 86.5); tail pixel (80.75, 200.25).
    # That places the pie head near center-top, tail near bottom-left.
    draw_pie(d, ox=-40, oy=+5, scale=0.65)

    # 捺 — right stroke of 八. scale 0.65, head pulled right of pie head.
    # At scale 0.65: default head pixel = (150 - 70*0.65, 150 - 80*0.65) = (104.5, 98)
    #                default tail pixel = (150 + 80*0.65, 150 + 90*0.65) = (202, 208.5)
    # ox=+65, oy=-5 -> head pixel (169.5, 103); tail pixel (267, 213.5).
    # pie head ≈ (152, 87), na head ≈ (170, 103) → gap ~18 px horizontal, ~16 vertical.
    # Small V-notch at top, splay outward.
    draw_na(d, ox=+65, oy=-5, scale=0.65)

    out = os.path.join(os.path.dirname(__file__), "01_八.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
