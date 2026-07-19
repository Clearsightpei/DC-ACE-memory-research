"""
Draw 横折折折钩 (heng-zhe-zhe-zhe-gou) — a 5-segment compound stroke
composed of: horizontal, down-turn, horizontal, down-turn, horizontal, hook.
Found in characters such as 乃, 奶, 仍 (right component).

Output: 300x300 PNG, white background, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
T = 10  # stroke thickness

def line(p0, p1, w=T):
    draw.line([p0, p1], fill=INK, width=w)
    # rounded joins
    r = w // 2
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)

# Layout (image coords, y grows DOWN):
# Segment 1: horizontal top       (60, 70) -> (230, 70)
# Segment 2: short vertical down  (230, 70) -> (230, 110)
# Segment 3: horizontal left      (230, 110) -> (90, 110)
# Segment 4: vertical down        (90, 110) -> (90, 175)
# Segment 5: horizontal right     (90, 175) -> (230, 175)
# Hook: upward-left tick from end (230, 175) -> (205, 150)

p1 = (60, 70)
p2 = (230, 70)
p3 = (230, 110)
p4 = (90, 110)
p5 = (90, 175)
p6 = (230, 175)
p7 = (205, 148)  # hook tip pointing up-left

line(p1, p2)
line(p2, p3)
line(p3, p4)
line(p4, p5)
line(p5, p6)
# hook (slightly thicker tick that tapers — approximate with a line)
line(p6, p7, w=T)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p1_stroke_32_横折折折钩/01_横折折折钩.png"
img.save(out_path)
print(f"Saved {out_path} ({W}x{H})")
