"""
Render 油 (oil) at 300x300, black ink on white.
Structure:
  Left: 氵 (three-dots water radical) — three short 点 in top-to-bottom
        diagonal, occupying left ~30% column.
  Right: 由 — a rectangle 冂-body with vertical 竖 that extends ABOVE
         the top, plus interior horizontal(s). Right side ~60% width.
Sibling check for 由: distinguishing from 甲/申/田/由:
  - 由: vertical extends UP above rectangle (protrudes on top only).
  - Interior: one horizontal midway + one short vertical through it,
    forming a + inside the box; but really 由 = 田 with the middle
    vertical protruding UPWARD.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # standard line width

def stroke(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")

def brush(x, y, r=3):
    d.ellipse((x-r, y-r, x+r, y+r), fill=BLACK)

# ---- 氵 water radical (left column, roughly x = 40..85) ----
# top dot (点): short diagonal from upper-left to lower-right
stroke([(48, 85), (78, 105)], width=7)
# middle dot: similar
stroke([(35, 130), (68, 152)], width=7)
# bottom dot (提): rises left-to-right (flick upward)
stroke([(48, 210), (85, 190)], width=7)

# ---- 由 on the right (roughly x = 110..255) ----
# Box coordinates
BOX_L = 130
BOX_R = 245
BOX_T = 80
BOX_B = 250

# The vertical 竖 that protrudes above the top edge
V_X = (BOX_L + BOX_R) // 2  # centered
V_TOP = 50    # protrudes above box top
V_BOT = BOX_B - 5
stroke([(V_X, V_TOP), (V_X, V_BOT)], width=7)

# Top horizontal (top of 冂 body); 横
stroke([(BOX_L, BOX_T), (BOX_R, BOX_T)], width=7)

# Left vertical of box (drops from top-left)
stroke([(BOX_L, BOX_T), (BOX_L, BOX_B)], width=7)

# Right vertical of box - typically slightly angled (竖折)
stroke([(BOX_R, BOX_T), (BOX_R, BOX_B)], width=7)

# Bottom horizontal (closes the box)
stroke([(BOX_L, BOX_B), (BOX_R, BOX_B)], width=7)

# Middle horizontal (interior) - divides box in half
MID_Y = (BOX_T + BOX_B) // 2
stroke([(BOX_L, MID_Y), (BOX_R, MID_Y)], width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_油.png")
img.save(out_path)
print(f"Wrote {out_path}")
