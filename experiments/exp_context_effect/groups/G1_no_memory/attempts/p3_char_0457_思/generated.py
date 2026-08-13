"""G1 render of 思 (si) = 田 (top) + 心 (bottom)."""
from PIL import Image, ImageDraw
import os, math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 6

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

def curve(pts, w=LW):
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)

# --- 田 (top, x:95..205, y:40..145) ---
line((95, 45), (208, 40))                 # top
line((100, 45), (93, 148))                # left vertical
line((208, 45), (203, 152))               # right vertical
line((100, 148), (203, 152))              # bottom
line((150, 55), (147, 145))               # inner vertical
line((100, 98), (205, 98))                # inner horizontal

# --- 心 (bottom, y:175..280) ---
# stroke 1: left dot (点)
line((75, 200), (60, 240), w=LW)

# stroke 2: 卧钩 (lying hook) — main bowl, curves down then up with hook at end
bowl = []
for t in range(0, 21):
    u = t / 20.0
    # parametric curve: starts x=95,y=205 -> dips to bottom -> rises to x=235,y=205
    x = 95 + 140 * u
    # y forms a shallow U
    y = 205 + 75 * math.sin(math.pi * u)
    bowl.append((x, y))
curve(bowl)
# hook at end (upward flick)
line(bowl[-1], (245, 190), w=LW)

# stroke 3: middle dot (inside bowl)
line((150, 245), (168, 265), w=LW)

# stroke 4: right dot (upper right)
line((215, 195), (245, 220), w=LW)

out = os.path.join(os.path.dirname(__file__), "01_思.png")
img.save(out)
print("wrote", out)
