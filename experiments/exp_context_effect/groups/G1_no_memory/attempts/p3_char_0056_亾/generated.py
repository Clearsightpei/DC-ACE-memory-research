"""Render 亾 as a 300x300 PNG with PIL."""
from PIL import Image, ImageDraw
from pathlib import Path

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# Layout: character occupies roughly x=[60,240], y=[60,260]
# Two parts:
# Left: L-shape (vertical + bottom horizontal), like left half of 匚
#   vertical from (80, 80) down to (80, 230), then horizontal from (80,230) to (150,230)
# Right upper: 厶 -like shape (short left diagonal + long right diagonal + tail)
#   short diagonal from (155, 90) down-left to (135, 130)
#   long diagonal from (155, 90) down-right to (240, 220), with slight sweep
# Bottom horizontal spanning the whole bottom (as seen in GT)
#   from (80, 245) to (245, 245)  -- looks like bottom of the L extends further

# Stroke 1: left vertical (goes down and connects to bottom via slight hook/turn)
d.line([(80, 85), (80, 240)], fill=INK, width=LW)

# Stroke 2: bottom horizontal (long, spans across, meets left vertical)
d.line([(78, 245), (255, 245)], fill=INK, width=LW)

# Stroke 3: short diagonal (top-right part, going down-left) - 撇
d.line([(160, 90), (140, 150)], fill=INK, width=LW)

# Stroke 4: long diagonal from top going down-right - 捺
d.line([(160, 90), (185, 140), (245, 215)], fill=INK, width=LW)

out = Path(__file__).parent / "01_亾.png"
img.save(out)
print(f"saved {out}")
