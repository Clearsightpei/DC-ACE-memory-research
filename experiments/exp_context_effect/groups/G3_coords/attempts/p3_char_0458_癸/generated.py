# BANK_DEVIATION
# skipped: (no bank entry attempted; 癸 is a unique compound of 癶+天 with
#          no close bank alias — 大 crossing is TERMINAL_FROZEN, 天 fails
#          same X-crossing family, and 癶 has no bank entry)
# reason: MMH GT is thin-uniform and 癸's stroke geometry is idiosyncratic
#         (asymmetric top 癶 + bottom 天-like cross); fresh inline avoids
#         the X-crossing bank pitfalls documented for 大-family
# fresh_component: gui_char_inline (癶-top + heng + pie/na cross + dian)

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5  # MMH-thin uniform width per P12

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)

def curve(pts, w=LW):
    # polyline through a list of points (approximates a curved stroke)
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=INK, width=w)

# ---------- TOP: 癶 radical (two feet, asymmetric) ----------
# Stroke 1: short 横撇 at top-left (small hook coming down)
curve([(58, 62), (95, 60), (85, 82)])

# Stroke 2: long 撇 — left leg of 癶, sweeps from upper-center down to lower-left
curve([(110, 55), (95, 95), (75, 135), (48, 175)])

# Stroke 3: short dian on the middle-left (small mark near the pie's midpoint)
curve([(100, 108), (118, 122)])

# Stroke 4: short 横 / dian at top-right (small horizontal element)
curve([(170, 70), (200, 68), (200, 88)])

# Stroke 5: short dian below that horizontal (small tick)
curve([(178, 92), (192, 108)])

# Stroke 6: long 捺 — right leg of 癶, sweeps from upper-center down to lower-right
curve([(150, 60), (170, 100), (200, 140), (240, 175)])

# ---------- BOTTOM: 天-like (heng + pie/na cross) ----------
# Stroke 7: 一 (horizontal), middle-bottom
line((70, 195), (230, 195), w=LW)

# Stroke 8: 撇 — bottom-left descender from heng
curve([(148, 200), (125, 230), (95, 265)])

# Stroke 9: 捺 — bottom-right descender from heng
curve([(155, 200), (185, 235), (220, 270)])

img.save("01_癸.png")
