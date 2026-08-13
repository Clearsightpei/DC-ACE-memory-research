"""G1 render of 亳 (háo)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)

def line(p1, p2, w=5):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(pts, w=5):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i+1], w)

# --- 亠 top ---
# dot 丶 (top-center, angled)
poly([(150, 25), (162, 42)], w=6)
# horizontal 一
line((70, 55), (225, 55), w=6)

# --- 口 (small mouth) ---
line((115, 72), (115, 105), w=5)     # left vertical
poly([(113, 72), (188, 72), (188, 105)], w=5)  # top + right down
line((113, 105), (190, 105), w=5)    # bottom

# --- long horizontal (waist of the character) ---
line((45, 128), (255, 128), w=6)

# --- 冖 shape: horizontal roof with hook down on right ---
poly([(85, 150), (215, 150), (200, 178)], w=6)

# --- 乇 bottom ---
# top short horizontal inside
line((110, 178), (200, 178), w=6)
# slanted 丿 from top-mid going down-left
poly([(150, 178), (85, 265)], w=6)
# vertical + right-hook (竖弯钩 style)
poly([(175, 178), (175, 260), (225, 260), (225, 240)], w=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0532_亳/01_亳.png")
print("saved")
