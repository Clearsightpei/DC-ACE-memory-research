"""G1 render of 家 (jiā, home) — roof radical 宀 over 豕 (pig)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=6):
    d.line(pts, fill="black", width=w, joint="curve")

# --- Roof radical 宀 ---
# Top dot 丶 (small down-right dot near top center)
line([(148, 30), (158, 48)], w=7)

# Left downstroke of roof (short slant down-left, 点)
line([(100, 68), (78, 92)], w=6)

# Horizontal top of roof with hook on the right (横钩)
line([(72, 68), (232, 68)], w=6)
line([(232, 68), (224, 92)], w=6)  # small hook down-left at right end

# --- Body 豕 ---
# Top short horizontal (一)
line([(120, 118), (185, 118)], w=6)

# Long left-descending stroke 丿 from top-center down through body
line([(155, 100), (95, 265)], w=7)

# Right-side 横折 (small horizontal turning down)
line([(155, 145), (200, 145)], w=6)
line([(200, 145), (185, 175)], w=6)

# Central short 撇 (left slant)
line([(160, 175), (135, 205)], w=5)

# Second short 撇 lower
line([(155, 210), (125, 240)], w=5)

# Long right 捺 (falling stroke down-right)
line([(160, 165), (245, 270)], w=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0501_家/01_家.png")
print("saved")
