"""Render 习 (Phase 3, item p3_char_0077) as a 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
TH = 6  # stroke thickness


def line(pts, width=TH):
    draw.line(pts, fill=INK, width=width, joint="curve")


# Stroke 1: 横折钩 (horizontal-fold-hook) — the outer frame
# Slight upward slope on top, straight down on right, small hook back-left at bottom
h_start = (70, 95)
h_end = (205, 82)      # slight upward slope, as in GT
v_end = (210, 235)     # downward vertical (slightly bowed right)
hook_end = (178, 245)  # short hook curving back-left
line([h_start, h_end, v_end, hook_end])

# Stroke 2: small short stroke (short slash) inside, upper region
line([(92, 135), (130, 143)])

# Stroke 3: 提 (rising diagonal) — from lower-left up to upper-right, inside the frame
line([(78, 200), (170, 148)])

out_path = os.path.join(os.path.dirname(__file__), "01_习.png")
img.save(out_path)
print(f"Saved {out_path}")
