"""Render 没 (méi) - water radical + top-right cap + 又 bottom."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"

def stroke(pts, width=5):
    d.line(pts, fill=INK, width=width, joint="curve")

# ---------- 氵 (three-drops water) on the left ----------
stroke([(58, 85), (82, 108)], width=6)   # top dot
stroke([(45, 130), (70, 152)], width=6)  # middle dot
stroke([(55, 210), (88, 188)], width=6)  # bottom rising tick

# ---------- Right side top: ⺈-like cap ----------
# small pie above
stroke([(135, 70), (155, 95)], width=5)
# horizontal + turn-down (㇆-like)
stroke([(140, 105), (235, 105), (240, 112), (232, 165)], width=5)

# ---------- Bottom: 又 (right hand) ----------
# 横撇 (crosses under the cap): horizontal then falling-left diagonal
stroke([(115, 175), (225, 175), (220, 182), (105, 265)], width=5)
# 捺: from mid upper going down-right
stroke([(165, 200), (260, 270)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_没.png")
img.save(out)
print("Saved", out)
