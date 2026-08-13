"""G1 render of 线 (thread/line) at 300x300. Revision 1."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ===== Left radical 纟 =====
# top "ㄥ" loop
line([(70, 60), (100, 50), (110, 75), (80, 90)], width=5)
# middle "ㄥ" loop
line([(65, 100), (105, 95), (115, 120), (75, 138)], width=5)
# bottom horizontal 提 (three dots merged, ends with an upward tick)
line([(50, 190), (135, 180)], width=6)

# ===== Right side 戋 =====
# 1st horizontal (short, upper)
line([(155, 75), (220, 70)], width=5)
# 2nd horizontal (longer, mid)
line([(140, 130), (240, 125)], width=5)
# 撇 (short diagonal from top-right down-left, crossing horizontals)
line([(215, 60), (150, 145)], width=5)
# 斜钩 (long diagonal down-right ending in a hook)
line([(175, 105), (275, 260)], width=6)
# hook tick at the bottom-right end
line([(275, 260), (255, 255)], width=5)
# 点 (dot at upper right)
line([(240, 90), (258, 108)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0427_线/01_线.png")
print("wrote 01_线.png")
