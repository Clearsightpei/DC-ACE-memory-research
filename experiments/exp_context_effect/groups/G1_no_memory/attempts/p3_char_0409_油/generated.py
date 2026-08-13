"""Render 油 (oil) - water radical 氵 + 由.
G1 no-memory control: cold render from GT observation.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5  # line width

def stroke(pts, width=LW):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 氵 water radical (left side) ----
# Top dot (drops from upper-left going down-right)
stroke([(60, 90), (78, 105)], width=6)
# Middle dot
stroke([(50, 130), (68, 145)], width=6)
# Bottom rising tick (提)
stroke([(50, 200), (85, 175)], width=6)

# ---- 由 (right side) ----
# Right side of 由 occupies roughly x=110..245, y=70..250

# Top horizontal (top of the box) - actually 由 starts with vertical through middle first
# Sequence: 竖(middle vertical top part), 横折(top-right corner going down), 横(inside top), 横(middle), 横(bottom)
# Standard 由 stroke order: 竖(middle upper stub), 横折(top-right), 横(middle), 竖(middle full), 横(bottom)

# The central vertical stroke that extends above the box (top stub)
stroke([(178, 70), (178, 90)], width=LW)

# Top horizontal + right vertical (横折): from top-left of box to top-right, then down
stroke([(115, 90), (240, 90), (240, 250)], width=LW)

# Left vertical of box
stroke([(115, 90), (115, 250)], width=LW)

# Bottom horizontal (closes the box)
stroke([(115, 250), (240, 250)], width=LW)

# Middle horizontal (crossbar inside)
stroke([(115, 170), (240, 170)], width=LW)

# Central vertical through the box (from top through bottom)
stroke([(178, 90), (178, 250)], width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_油.png")
img.save(out_path)
print(f"Saved {out_path}")
