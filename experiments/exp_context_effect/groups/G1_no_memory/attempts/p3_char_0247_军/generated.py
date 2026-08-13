"""Render 军 (jun) - 冖 (cover) over 车 (cart)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=3):
    d.line([p1, p2], fill="black", width=w)

# --- 冖 (top cover) ---
# left dot / small slanted stroke
line((78, 68), (92, 82))
# long horizontal top
line((78, 80), (222, 82))
# right hook (down then small tick left)
line((222, 82), (215, 122))
line((215, 122), (205, 128))

# --- 车 (bottom) ---
# top horizontal of 车 (short)
line((108, 122), (198, 124))
# small diagonal tick (upper-left to lower-right)
line((115, 108), (170, 138))
# middle-left short vertical
line((115, 138), (115, 175))
# middle-right short vertical
line((195, 138), (195, 175))
# middle horizontal (inside box)
line((115, 175), (195, 175))
# long bottom horizontal
line((60, 218), (238, 220))
# central long vertical descender (through the whole char)
line((150, 100), (150, 270))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0247_军/01_军.png")
