"""G1 render of 教 (jiao) - Phase 3. Revised once."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# 教 = 耂/孝-like left component + 攵 right radical
# Layout: left roughly x=30..160, right roughly x=160..280

# --- LEFT SIDE (孝 component: 土 above + 子 below) ---
# Top short horizontal (top of 土)
stroke([(60, 70), (135, 68)], width=5)
# Vertical stroke through both horizontals, slight left slant
stroke([(100, 50), (92, 130)], width=5)
# Second (longer) horizontal - extends further left and right
stroke([(35, 110), (165, 105)], width=5)
# Left-falling diagonal from right end of horizontals sweeping down-left (丿)
stroke([(155, 105), (55, 185)], width=5)

# 子 component below
# Top horizontal (top of 子, slightly curved right)
stroke([(65, 165), (150, 160)], width=5)
# Vertical hook: down then hook to the left at bottom
stroke([(118, 150), (118, 225), (75, 240)], width=5)
# Middle horizontal of 子
stroke([(70, 200), (155, 195)], width=5)

# --- RIGHT SIDE (攵 radical) ---
# Top short left-falling (short 丿 at top)
stroke([(210, 70), (188, 100)], width=5)
# Short horizontal
stroke([(180, 108), (245, 105)], width=5)
# Long left-falling diagonal from upper right down to lower left (丿)
stroke([(220, 90), (170, 240)], width=5)
# Right falling (捺) crossing the 丿
stroke([(195, 160), (275, 250)], width=5)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_教.png")
img.save(out_path)
print(f"Saved {out_path}")
