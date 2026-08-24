"""Render 打 (dǎ) — 5 strokes: 扌 (horizontal, vertical-hook, rising) + 丁 (horizontal, vertical-hook)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 6  # stroke thickness


def stroke(points, width=TH):
    d.line(points, fill=INK, width=width, joint="curve")


# ---- Left radical: 扌 (hand) ----
# 1. horizontal (short, slight rise) — mid-upper area
stroke([(40, 135), (120, 128)], width=TH)

# 2. vertical hook (long descender with hook at bottom left)
stroke([(85, 95), (85, 240), (65, 250)], width=TH)

# 3. rising stroke (from lower-left up to mid-right, crosses vertical) — steeper
stroke([(45, 195), (130, 160)], width=TH)

# ---- Right side: 丁 ----
# 4. horizontal top (slight downward angle to right, as in GT)
stroke([(145, 118), (280, 122)], width=TH)

# 5. vertical hook (long descender with hook)
stroke([(215, 122), (215, 250), (195, 260)], width=TH)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0180_打/01_打.png")
print("saved")
