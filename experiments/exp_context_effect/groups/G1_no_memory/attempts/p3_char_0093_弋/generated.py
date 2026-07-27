"""G1 render of 弋 (yi4) — 3 strokes: 横 (rising short), 斜钩 (long diagonal with hook), 点 (dot upper right)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

def stroke(points, width=LW):
    d.line(points, fill=BLACK, width=width, joint="curve")
    # round caps
    for (x, y) in points:
        d.ellipse((x - width/2 + 0.5, y - width/2 + 0.5,
                   x + width/2 - 0.5, y + width/2 - 0.5), fill=BLACK)

# Stroke 1: short 横 — starts left of center, rises slightly to the right.
# In GT it's around y=140, from x~55 to x~175
s1 = [(55, 148), (105, 143), (175, 138)]
stroke(s1, LW)

# Stroke 2: 斜钩 (xie gou) — the big backbone
# starts upper-left (near top around x=95, y=90), curves down-right through center,
# swings to lower-right corner then hooks up.
s2 = [(95, 90), (110, 110), (130, 140), (160, 180), (195, 225), (215, 250), (225, 245), (232, 230)]
stroke(s2, LW + 1)

# Stroke 3: 点 (dot) — small stroke at upper right
# short diagonal from ~ (175, 78) to (200, 100)
s3 = [(178, 82), (188, 92), (200, 102)]
stroke(s3, LW)

out_path = os.path.join(os.path.dirname(__file__), "01_弋.png")
img.save(out_path)
print(f"Saved {out_path}")
