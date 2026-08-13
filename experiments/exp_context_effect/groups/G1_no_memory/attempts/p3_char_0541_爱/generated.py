"""G1 render of 爱 (love) — revised, PIL 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")

# --- 爫 (top claw) - three little strokes ---
line([(105, 55), (115, 75)], 4)   # left short slash
line([(140, 50), (148, 75)], 4)   # middle
line([(180, 52), (170, 78)], 4)   # right slash

# --- 冖 cover: long horizontal with left entry and right hook ---
line([(80, 95), (85, 108)], 4)      # left dot
line([(85, 108), (220, 108)], 4)    # long horizontal
line([(220, 108), (218, 128)], 4)   # right hook down

# --- middle horizontal (part of 冖 base / small stroke) ---
line([(95, 140), (205, 140)], 4)

# --- slanted stroke crossing middle (the 一 + slant of 爱) ---
line([(155, 108), (110, 175)], 4)   # slant from top-right to lower-left

# --- 夂 bottom radical ---
# top horizontal-ish curve
line([(90, 175), (215, 175)], 4)
# left descending pie
line([(120, 175), (85, 260)], 4)
# right descending na (sweeping)
line([(150, 195), (245, 275)], 4)
# small connecting stroke inside
line([(140, 210), (170, 240)], 4)

out = os.path.join(os.path.dirname(__file__), "01_爱.png")
img.save(out)
print("saved", out)
