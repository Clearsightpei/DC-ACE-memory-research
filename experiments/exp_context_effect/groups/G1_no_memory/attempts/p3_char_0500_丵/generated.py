"""G1 render for 丵.

Character has two zones:
  - top: a "业"-like cluster of short diagonals + a small horizontal cap,
         sitting on a long horizontal.
  - bottom: "羊"-like: two upper dots, three horizontals, one long vertical.

Rendered with PIL at 300x300, black ink on white.
"""

from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=6):
    d.line([p1, p2], fill="black", width=w)

# ---- Top cluster (业-like array of short strokes) ----
# left-side pair of diagonals
line((70, 55),  (85, 85),   w=5)   # \
line((95, 55),  (85, 85),   w=5)   # /  small chevron
line((110, 60), (100, 90),  w=5)   # \
line((130, 60), (140, 90),  w=5)   # /

# center pair
line((150, 45), (140, 90),  w=5)
line((150, 45), (165, 90),  w=5)

# right diagonals
line((175, 60), (185, 90),  w=5)
line((205, 60), (195, 90),  w=5)
line((215, 65), (225, 95),  w=5)

# small horizontal cap under the cluster (short)
line((105, 95),  (200, 95), w=5)

# ---- Long horizontal separating top from bottom ----
line((40, 130), (260, 130), w=7)

# ---- Bottom (羊-like) ----
# two upper dots slanting inward
line((115, 145), (125, 165), w=5)   # left dot \
line((190, 145), (180, 165), w=5)   # right dot /

# upper short horizontal
line((115, 175), (190, 175), w=6)
# middle horizontal
line((95, 215),  (210, 215), w=6)

# long central vertical
line((150, 150), (150, 285), w=7)

out = os.path.join(os.path.dirname(__file__), "01_丵.png")
img.save(out)
print("wrote", out)
