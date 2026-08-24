"""G1 attempt: 复 (fu) — revised.
Top: 丿+一 (small pie above a long horizontal)
Middle: small 日-like box with two inner horizontals
Bottom: 夂 (short slanted + long 撇 + 捺)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
T = 5


def polyline(pts, w=T):
    d.line(pts, fill=INK, width=w)


# ---- Top ----
# 1) small slanted 丿 above the horizontal
polyline([(130, 30), (115, 55)], w=T)

# 2) top horizontal 一 (long, slightly slanted up-right)
polyline([(60, 65), (240, 60)], w=T)

# ---- Middle box (日) ----
# Left vertical of box
polyline([(105, 65), (105, 175)], w=T)

# Top+right: 横折 (top-right corner from ~ (105,90) to (195,90) then down to (195,175))
polyline([(105, 90), (195, 90), (195, 175)], w=T)

# Inner horizontal 1
polyline([(108, 128), (192, 128)], w=T)

# Bottom horizontal (closes box)
polyline([(105, 175), (195, 175)], w=T)

# ---- Bottom (夂) ----
# small slant at top-right of bottom section
polyline([(150, 180), (170, 200)], w=T)

# long 撇 from upper-right sweeping down-left
polyline([(190, 190), (55, 285)], w=T)

# 捺 right-falling stroke (starts mid, sweeps down-right)
polyline([(115, 235), (265, 285)], w=T)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0495_复/01_复.png")
print("saved")
