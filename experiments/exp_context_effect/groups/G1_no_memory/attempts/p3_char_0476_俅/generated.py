"""G1 render of 俅 = 亻 (person radical) + 求 (seek).
300x300 white bg, black ink, PIL. Revision 1."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 亻 (left person radical, upper-left area) ----
# 撇: slanted from upper-right down to lower-left
line([(90, 70), (78, 130), (55, 220)], width=5)
# 竖: vertical from mid-撇 downward
line([(85, 130), (90, 265)], width=5)

# ---- 求 (right side, occupies right ~2/3) ----
# top horizontal (slightly rising)
line([(135, 95), (245, 88)], width=5)
# center vertical with hook (竖钩)
line([(190, 65), (190, 215)], width=5)
line([(190, 215), (175, 225)], width=5)
# top-right dot (点)
line([(220, 62), (235, 85)], width=5)
# small dot upper-left of vertical (点)
line([(160, 108), (148, 130)], width=5)
# middle short horizontal / 提 crossing the vertical
line([(150, 150), (230, 145)], width=5)
# long left-falling 撇 from just below middle down to lower-left
line([(180, 155), (135, 215), (105, 265)], width=5)
# long right-falling 捺 from just below middle down to lower-right
line([(200, 160), (245, 220), (275, 265)], width=5)
# small dot lower-right (点)
line([(245, 180), (262, 205)], width=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0476_俅/01_俅.png")
print("saved")
