"""G1 render of 传 (chuan) - simplified. Character = 亻 (left) + 专 (right)."""
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 6  # stroke width

def line(pts, width=W):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 亻 radical (person) on the left ---
# Left-falling stroke (撇)
line([(90, 70), (55, 220)])
# Vertical stroke
line([(95, 130), (95, 265)])

# --- 专 on the right ---
# Top horizontal (short, slight rise)
line([(150, 90), (230, 80)])
# Second horizontal (longer, main)
line([(130, 130), (260, 128)])
# Vertical going down with hook - the 竖折折钩 shape
# vertical segment
line([(200, 90), (200, 165)])
# from vertical bottom, horizontal then down-hook
line([(160, 165), (245, 165)])
line([(245, 165), (240, 210)])
# hook curl left
line([(240, 210), (200, 220)])

# Long bottom horizontal that sweeps down-right
line([(130, 200), (275, 195)])

# The final 点 (dot) on lower right
line([(215, 235), (235, 260)], width=W+1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0283_传/01_传.png")
