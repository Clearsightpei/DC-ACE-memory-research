"""
p3_char_0487 孩 — left 子 + right 亥 (LR compound, 9 strokes)

Revision 2: tightened 亥 vertical stack (亠 dot must sit close above 一).
Components touch (rule H): 子's 一 extends under 亥's left edge.
Hook flick UP-LEFT for 子's 竖钩.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")
    for (x, y) in (pts[0], pts[-1]):
        r = width / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def dot(cx, cy, rx=5, ry=8):
    d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill="black")

# ============ LEFT 子 ============
# 1) 横撇 (top horizontal with hook down-left)
stroke([(35, 88), (108, 82), (112, 100), (58, 118)], width=6)

# 2) 竖钩 through center, hook flicks UP-LEFT
stroke([(78, 82), (80, 215), (74, 230), (60, 224)], width=6)

# 3) 一 (bottom horizontal of 子), extends toward 亥
stroke([(30, 168), (165, 165)], width=6)

# ============ RIGHT 亥 (compact vertical stack) ============
# 1) 丶 top dot — center of 亥
dot(205, 62, rx=5, ry=9)

# 2) 一 (short horizontal, just below the dot)
stroke([(160, 88), (260, 84)], width=6)

# 3) 乛 (small 横折) — starts left, hook down
stroke([(170, 112), (215, 110), (215, 130)], width=6)

# 4) 丿 short — down from mid
stroke([(220, 108), (185, 155)], width=6)

# 5) 丿 long sweeping down-left through body
stroke([(210, 135), (150, 260)], width=6)

# 6) 乀 press-and-sweep down-right
stroke([(200, 165), (245, 215), (280, 258)], width=7)

# Tiny inner mark near center of 亥 body (small 人-like touches suggested by GT)
stroke([(195, 175), (215, 195)], width=5)
stroke([(215, 175), (200, 200)], width=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0487_孩/01_孩.png")
