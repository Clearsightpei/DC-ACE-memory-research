"""G1 render of 还 (huán) — 不 on upper-right, 辶 wrapping from left/bottom."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=6):
    d.line(pts, fill="black", width=w, joint="curve")

# --- 辶 dot (top-left) ---
line([(65, 60), (95, 85)], 6)

# --- 不 (upper portion, right-center) ---
# horizontal top bar
line([(110, 115), (255, 115)], 7)
# vertical stem down
line([(185, 115), (185, 215)], 7)
# left falling stroke (from just under top bar, going down-left)
line([(175, 140), (125, 210)], 6)
# right dot (from just under top bar, going down-right)
line([(210, 140), (245, 190)], 6)

# --- 辶 lower body (三点 + 平捺) ---
# second short slant, below the top dot
line([(60, 130), (95, 160)], 6)
# curved descending stroke into the sweep (like ㄥ shape)
line([(85, 175), (70, 210), (95, 240)], 6)
# long horizontal 捺 sweep across the bottom, gently rising to the right
line([(70, 250), (275, 235)], 7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0305_还/01_还.png")
