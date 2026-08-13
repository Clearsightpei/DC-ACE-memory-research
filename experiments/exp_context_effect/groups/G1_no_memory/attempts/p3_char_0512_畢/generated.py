"""G1 render of 畢 (bi4) — no memory, cold render from GT visual."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4  # stroke thickness

def line(p1, p2, w=T):
    d.line([p1, p2], fill=INK, width=w)

# 畢 has 11 strokes: top 田 (5) + 十 middle (2) + 十 bottom + two horizontal bars
# Layout: 田 on top ~ y=45..135, then middle horizontals y=155, y=180,
# vertical descender through center to y=270, small marks on sides

# --- Top 田 (square with cross) ---
# Left vertical (slight slant)
line((100, 45), (95, 135))
# Top horizontal
line((100, 45), (200, 50))
# Right vertical with hook top-right
line((200, 50), (205, 135))
# Middle horizontal inside 田
line((97, 90), (202, 92))
# Middle vertical inside 田
line((150, 48), (150, 133))
# Bottom of 田
line((95, 135), (205, 135))

# --- Middle 十-like: horizontal bar wider than 田 ---
line((60, 170), (240, 172))

# --- Second wider horizontal ---
line((70, 205), (235, 207))

# --- Vertical descender through center (from 田 through bars to bottom) ---
line((150, 133), (150, 275))

# --- Bottom horizontal (short base) ---
line((110, 245), (195, 247))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0512_畢/01_畢.png")
