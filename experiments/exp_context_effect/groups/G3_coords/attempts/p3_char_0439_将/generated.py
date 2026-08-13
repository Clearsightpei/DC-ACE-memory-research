# BANK_DEVIATION
# skipped: cun.py, xi.py (夕)
# reason: bank primitives are turtle-drawn with (ox,oy,scale) that don't fit
#   the 将 composition where 丬-left is narrow, 夕 tops the right column,
#   and 寸 sits below sharing the same right column with tight L-R budget.
# fresh_component: jiang_char_LR (丬 + 夕-top + 寸-bottom, PIL inline)

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)

def bezier(pts, w=LW, steps=48):
    (x0,y0),(x1,y1),(x2,y2) = pts
    prev = (x0,y0)
    for i in range(1, steps+1):
        t = i/steps
        u = 1-t
        x = u*u*x0 + 2*u*t*x1 + t*t*x2
        y = u*u*y0 + 2*u*t*y1 + t*t*y2
        d.line([prev,(x,y)], fill=INK, width=w)
        prev = (x,y)

# ============================================================
# 丬 (left) — narrow, ~ x in [40, 105], y in [55, 260]
# 3 strokes: top 点 (short slant), middle 提 (upward), long 竖
# ============================================================
# Top 点 — a short dot near top of vertical, slanting up-right
bezier([(55, 90), (68, 78), (82, 68)], w=LW)
# Middle 提 — a short rising stroke crossing the vertical from lower-left to upper-right
bezier([(48, 165), (68, 158), (92, 148)], w=LW)
# Long 竖 (vertical) — from just above 点's start down to lower area
line((82, 68), (82, 258), w=LW+1)

# ============================================================
# 夕 (top-right) — ~ x in [130, 265], y in [55, 160]
# 3 strokes: 撇 (long down-left curve), 横折撇 (top heng folding then pie), inner 点
# ============================================================
# 撇 — long curved stroke starting upper-mid, sweeping down and left
bezier([(210, 60), (180, 100), (150, 155)], w=LW)
# 横折撇: horizontal top (heng) then fold and pie down-left
# heng from junction with pie going right
line((196, 82), (245, 78), w=LW)
# fold+pie continuation: from right end of heng down and left curving
bezier([(245, 78), (240, 115), (200, 158)], w=LW)
# inner dot inside 夕
bezier([(200, 118), (212, 125), (222, 132)], w=LW)

# ============================================================
# 寸 (bottom-right) — ~ x in [130, 275], y in [170, 275]
# 3 strokes: 横 long, 竖钩 vertical with left hook, 点 to right of vertical
# ============================================================
# 横 (long horizontal, slight rise)
line((130, 195), (270, 190), w=LW)
# 竖钩: long vertical then small hook at bottom to the left
line((200, 190), (200, 258), w=LW+1)
bezier([(200, 258), (192, 268), (175, 268)], w=LW)
# 点 — dot to right of vertical, mid-height
bezier([(212, 218), (228, 226), (242, 238)], w=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0439_将/01_将.png")
print("saved")
