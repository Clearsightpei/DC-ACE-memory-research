"""G1 render of 紧 — top-left 臣, top-right 又, bottom 糸.
PIL polylines at 300x300, black on white, matches GT cursive style."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=3):
    d.line(pts, fill="black", width=w)

# ---------------- TOP-LEFT: 臣 (compressed) ----------------
# left tall vertical
line([(60, 55), (65, 165)], w=4)
# top horizontal (short)
line([(65, 55), (115, 62)], w=3)
# inner top box: short horizontal + return
line([(80, 80), (115, 85)], w=3)
line([(115, 85), (113, 110)], w=3)
# middle horizontal
line([(80, 110), (115, 113)], w=3)
# bottom hook: horizontal + returning vertical to close
line([(65, 165), (125, 168)], w=3)
line([(125, 168), (122, 145)], w=3)

# ---------------- TOP-RIGHT: 又 ----------------
# heng-pie (top horizontal turning into left-falling)
line([(150, 55), (235, 70)], w=3)
line([(235, 70), (170, 165)], w=3)
# na (right-falling from mid)
line([(180, 95), (255, 175)], w=4)

# ---------------- BOTTOM: 糸 ----------------
# top small mark (short slash — 撇)
line([(115, 175), (100, 195)], w=3)
# small triangle 幺 (two short curves)
line([(105, 195), (140, 200)], w=3)
line([(140, 200), (135, 220)], w=3)
line([(105, 220), (140, 220)], w=3)

# 小 base
# center vertical with hook
line([(135, 225), (135, 285)], w=4)
line([(135, 282), (122, 288)], w=3)
# left dot/slash
line([(105, 235), (85, 275)], w=3)
# right dot/slash (long na)
line([(165, 235), (215, 285)], w=4)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_紧.png"))
print("wrote 01_紧.png")
