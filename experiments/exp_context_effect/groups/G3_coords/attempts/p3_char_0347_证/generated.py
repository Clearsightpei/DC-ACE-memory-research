# BANK_DEVIATION
# skipped: (no direct bank entry for 讠 — TERMINAL per errata; no bank for 正)
# reason: 讠 is a persistent unsolved errata radical (no bank primitive); 正 also
#   in errata (0182). Fresh inline render targeted at GT proportions: narrow
#   讠 column ~22% of width, wider 正 fills remaining ~78% with 5 clean strokes.
# fresh_component: yan_speech_inline_for_zheng, zheng_5stroke_frame

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(p0, p1, w=5):
    d.line([p0, p1], fill=BLACK, width=w)
    # rounded caps
    r = w / 2
    d.ellipse([p0[0]-r, p0[1]-r, p0[0]+r, p0[1]+r], fill=BLACK)
    d.ellipse([p1[0]-r, p1[1]-r, p1[0]+r, p1[1]+r], fill=BLACK)

def polyline(pts, w=5):
    for i in range(len(pts) - 1):
        stroke(pts[i], pts[i+1], w=w)

# ---- LEFT: 讠 (yan / speech radical) ----
# 1) 点 (dot) — small diagonal dab at top of column
dot_a = (48, 78)
dot_b = (62, 96)
stroke(dot_a, dot_b, w=8)

# 2) 横折提 (heng-zhe-ti) — L with a rising flick at the bottom
#    horizontal top → sharp corner down → rising tick to upper-right
p_h0 = (32, 128)      # left start of horizontal
p_h1 = (78, 128)      # right end of horizontal (corner)
p_v1 = (60, 190)      # descend (leans slightly left, like GT)
p_t1 = (85, 178)      # 提 flick up-right
polyline([p_h0, p_h1, p_v1, p_t1], w=5)

# ---- RIGHT: 正 (zheng) — 5 strokes ----
# 1) 一 top heng (moderate width)
stroke((115, 92), (272, 90), w=5)

# 2) 丨 short left vertical (from top heng down)
stroke((138, 92), (138, 168), w=5)

# 3) 一 middle short heng (from left vertical rightward)
stroke((138, 165), (222, 162), w=5)

# 4) 丨 long vertical (from top heng middle-right down to bottom)
stroke((202, 92), (202, 252), w=5)

# 5) 一 bottom wide heng (widest of the three horizontals)
stroke((102, 252), (280, 248), w=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0347_证/01_证.png")
print("wrote 01_证.png")
