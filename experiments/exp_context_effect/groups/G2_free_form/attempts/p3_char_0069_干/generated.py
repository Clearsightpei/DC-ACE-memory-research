"""Draw 干 at 300x300 using PIL.

Structure (from form_catalog):
- Top 横: SHORT (~110 px), high on canvas
- Bottom 横: LONGER (~170 px), middle-lower on canvas
- Through-going 竖: STRAIGHT, no hook, passes through both 横,
  extending ~15 px above top and well below bottom.

Sibling bit (HARD RULE): 干 vs 千 — 干 has TWO straight 横 + straight 竖
(no 撇-lid, no hook). Keep the top 横 straight.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
STROKE = 10  # brush width

# Center x-axis
cx = 150

# --- Top 横 (short, ~110 px) ---
top_y = 95
top_len = 110
top_x0 = cx - top_len // 2
top_x1 = cx + top_len // 2
d.line([(top_x0, top_y), (top_x1, top_y)], fill=INK, width=STROKE)

# --- Bottom 横 (longer, ~170 px) ---
bot_y = 165
bot_len = 175
bot_x0 = cx - bot_len // 2
bot_x1 = cx + bot_len // 2
d.line([(bot_x0, bot_y), (bot_x1, bot_y)], fill=INK, width=STROKE)

# --- Through-going 竖 (straight, no hook) ---
# Extend ~15 px above top 横 and well below bottom 横
shu_top = top_y - 15
shu_bot = 265
d.line([(cx, shu_top), (cx, shu_bot)], fill=INK, width=STROKE)

out = os.path.join(os.path.dirname(__file__), "01_干.png")
img.save(out)
print(f"wrote {out}")
