"""G1 render of 侃 (character p3_char_0410).
Layout: 亻 on left, right side = 冂 top + 口 + 儿 legs.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left radical 亻 ----
# Slanting pie (diagonal top)
stroke([(90, 80), (55, 140)], width=6)
# Long vertical stroke (slightly slanted)
stroke([(78, 110), (70, 250)], width=6)

# ---- Right component: 冂 top ----
# top horizontal (short, curving slightly)
stroke([(135, 95), (230, 92)], width=6)
# left vertical of 冂 going down
stroke([(138, 95), (135, 200)], width=6)
# right vertical of 冂 going down long with hook
stroke([(228, 92), (235, 240)], width=6)

# ---- Inner: 口 (small mouth near top) ----
stroke([(155, 125), (215, 123)], width=5)
stroke([(155, 125), (155, 170)], width=5)
stroke([(215, 123), (215, 170)], width=5)
stroke([(155, 170), (215, 170)], width=5)

# ---- Bottom right: 儿 legs ----
# Left leg (pie, curving down-left from middle of right block)
stroke([(175, 200), (140, 265)], width=6)
# Right leg: extends the right vertical of 冂, with a hook (斜钩)
stroke([(235, 240), (260, 275)], width=6)
# hook at end
stroke([(260, 275), (245, 275)], width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_侃.png")
img.save(out_path)
print(f"Wrote {out_path}")
