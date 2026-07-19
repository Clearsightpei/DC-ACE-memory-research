"""G1 render of 车 (radical, 4 strokes, simplified) — 300x300 PNG.

Simplified 车 stroke order (4 strokes):
  1. 横 — a top short horizontal
  2. 撇折 — down-left slant then up-right (forms the 'shoulder' under top 横)
  3. 横 — a middle horizontal crossing the vertical
  4. 竖 — a long vertical going down through, with tiny top hook

The GT shape shows: top short horizontal, then an angled 'V'-ish
figure under it (the 撇折), a middle horizontal, a long vertical,
and a bottom horizontal on the base.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    d.line(pts, fill="black", width=width, joint="curve")
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse((x - width/2, y - width/2, x + width/2, y + width/2), fill="black")

# 1) top short horizontal (a bit slanted, like GT's small top piece)
stroke([(135, 78), (185, 72)], width=7)

# 2) 撇折 — starts at right end of top横, goes down-left, then折 up-right slightly
#    forming a small 'shoulder' shape under the top horizontal
stroke([(180, 75), (150, 108), (178, 118)], width=7)

# 3) middle horizontal — long, spanning most of the width
stroke([(78, 138), (225, 130)], width=8)

# 4) vertical (long) with the bottom horizontal integrated as another stroke —
#    the char has: middle横 + 竖(with small top hook) + bottom横
#    But 车 is 4 strokes total. The bottom horizontal is actually part of
#    the last stroke in some analyses; canonical simplified 车 = 4 strokes:
#    横, 撇折, 横, 竖. So bottom horizontal is NOT separate.
#    Looking at GT: bottom horizontal IS present distinctly. In simplified
#    车 the bottom "horizontal" is actually the 提 tail of the 竖. So:
#    the last stroke is a long 竖 that ends by pushing out to the right
#    (the base). But GT clearly shows a full bottom horizontal.
#    So: 4-stroke breakdown of GT: 横, 撇折, 横(middle), 竖 — and the
#    bottom horizontal in GT is likely part of stroke 3 (middle横 extends
#    to become bottom) — no, they are visually distinct.
#    Simpler: render what GT looks like faithfully with 4 clear strokes:
#      strokes 1,2 above (top+shoulder), stroke 3 middle横, stroke 4 长竖
#    Add a subtle bottom horizontal as the 提 out of the 竖.

# vertical descending through center; ends with a slight rightward tail
stroke([(158, 82), (156, 235), (245, 220)], width=8)

# separate bottom horizontal (visually present in GT) — draw as extension
stroke([(55, 228), (250, 218)], width=8)

out = os.path.join(os.path.dirname(__file__), "01_车.png")
img.save(out)
print("wrote", out)
