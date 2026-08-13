"""G1 render for 通 (tōng) — 辶 + 甬. Revision 2."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

def poly(pts, w=LW):
    for i in range(len(pts) - 1):
        line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], w)

# ---------- 甬 (top-right component) ----------
# top: マ-shape — dot + 横折/撇
line(158, 40, 172, 55)                     # 丶 dot
poly([(130, 68), (220, 68), (220, 95)])    # 横折
line(178, 68, 165, 100)                    # inner 撇 slanting down-left

# 用-body: outer frame
poly([(135, 105), (135, 215), (225, 215), (225, 105), (135, 105)])
# middle vertical extends downward as tail
line(180, 105, 180, 240)
# only two inner horizontals (top-mid and mid-bottom → gives 3 rows)
line(135, 145, 225, 145)
line(135, 180, 225, 180)

# ---------- 辶 (walking radical) ----------
# 点 top-left
line(55, 50, 70, 68)
# 横折折撇 — cleaner shape
poly([(48, 88), (95, 88)])                 # 横
poly([(95, 88), (68, 115)])                # 折 down-left
poly([(68, 115), (100, 115)])              # short 横
poly([(100, 115), (70, 150)])              # 撇 down-left
# 平捺 — long sweeping bottom curve, rises at right tail
poly([(35, 230), (75, 258), (170, 265), (240, 245), (270, 220)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0513_通/01_通.png")
print("saved")
