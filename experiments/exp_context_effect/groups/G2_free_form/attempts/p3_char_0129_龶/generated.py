"""
Item: p3_char_0129_龶
4 strokes: three horizontals + one through-going vertical.
Structure like 主 minus the top dot: 短横 / 中横 / 长横 with 竖 crossing top two.
GT observation: 竖 sits slightly left-of-center; bottom 横 clearly longest;
top 横 shortest; middle 横 medium. All in upper half of canvas.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def hline(x1, x2, y, w=6):
    d.line([(x1, y), (x2, y)], fill=INK, width=w)
    # small brush-end dabs
    d.ellipse([x1 - w//2, y - w//2, x1 + w//2, y + w//2], fill=INK)
    d.ellipse([x2 - w//2, y - w//2, x2 + w//2, y + w//2], fill=INK)

def vline(x, y1, y2, w=6):
    d.line([(x, y1), (x, y2)], fill=INK, width=w)
    d.ellipse([x - w//2, y1 - w//2, x + w//2, y1 + w//2], fill=INK)
    d.ellipse([x - w//2, y2 - w//2, x + w//2, y2 + w//2], fill=INK)

# Layout in upper half of canvas (bottom third empty like GT)
# Vertical axis center-ish, slightly left of center
CX = 140

# Top short 横 - shortest, near top
hline(110, 175, 105, w=5)

# Middle 横 - medium length
hline(95, 195, 155, w=5)

# Bottom long 横 - longest, forms base
hline(60, 260, 205, w=6)

# Through 竖 - crosses top and middle 横 only (stops at bottom 横)
vline(CX, 90, 205, w=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0129_龶/01_龶.png")
print("saved")
