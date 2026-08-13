"""G1 render of 当 (dāng) — simplified, 6 strokes.
Top: 3 small slanting strokes (like 小).
Bottom: 彐-like — three horizontals stacked with a right-side vertical
descending from the top横折; left side is OPEN."""
from PIL import Image, ImageDraw
from pathlib import Path

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4  # stroke thickness

def line(pts, width=T):
    d.line(pts, fill=INK, width=width, joint="curve")

# --- Top three strokes (like 小 shape sitting on the body) ---
# 1) Left slant ("丿"): upper-left, slants down-left
line([(110, 70), (85, 110)], width=T)

# 2) Middle short vertical (slight lean)
line([(150, 60), (152, 105)], width=T)

# 3) Right slant ("乀"-like): upper-right, slants down-right
line([(195, 70), (220, 110)], width=T)

# --- Body: 彐-like (三 with right vertical) ---
# 4) 横折 — top horizontal then turn down (top + right side of the 彐 shape)
line([(70, 140), (230, 140), (230, 250)], width=T)

# 5) Middle horizontal — inside, spans nearly full width, touches right vertical
line([(75, 195), (230, 195)], width=T)

# 6) Bottom horizontal — the base; extends across, slight rise on the left
line([(60, 250), (230, 250)], width=T)

out = Path(__file__).parent / "01_当.png"
img.save(out)
print(f"wrote {out}")
