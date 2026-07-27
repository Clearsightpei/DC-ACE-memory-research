"""G1 render of 冖 (radical: cover/crown). Revised."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Stroke 1: left short dot/tick (丶-like), slanting down-left, separate
# from horizontal start
d.line([(88, 125), (72, 170)], fill="black", width=6)

# Stroke 2: 橫折 — horizontal (slightly rising) then short down-hook
# Horizontal begins a bit right of the dot's top so they're clearly separate
d.line([(95, 130), (218, 120)], fill="black", width=6)
# Right hook — slants slightly down-left (like GT)
d.line([(218, 120), (208, 165)], fill="black", width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_冖.png")
img.save(out_path)
print(f"Saved: {out_path}")
