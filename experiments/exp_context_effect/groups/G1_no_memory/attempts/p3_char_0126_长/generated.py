"""G1 draw of 长 — 4 strokes: short pie, horizontal, vertical, long na."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 5  # stroke thickness

def line(pts, width=TH):
    d.line(pts, fill=INK, width=width, joint="curve")

# Stroke 1: short 撇 at top — small down-left stroke starting near center-upper
line([(140, 60), (130, 80), (118, 105), (108, 130)], width=TH)

# Stroke 2: long horizontal (一) through middle, slight upward slant
line([(45, 140), (110, 135), (180, 130), (245, 128)], width=TH)

# Stroke 3: vertical (竖) descending from just above horizontal down through
# to a 提 flick at the bottom (up-right little foot)
line([(115, 108), (115, 160), (115, 220), (118, 255)], width=TH)
# 提 flick from bottom of vertical up-right
line([(118, 255), (150, 240), (175, 228)], width=TH)

# Stroke 4: long 捺 (na) — from crossing area, sweep down-right with tail
line([(130, 140), (160, 170), (195, 205), (230, 235), (265, 260)], width=TH)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0126_长/01_长.png"
img.save(out)
print(f"Saved {out}")
