# BANK_DEVIATION
# skipped: mu.py
# reason: 亲's bottom is 朩 nested tight under 立's lower heng — 木's own
#   heng is absent (shared with 立's long heng), so mu.py can't be dropped
#   in as-is; pie/na cross at the shu near the top rather than at a fresh
#   木-heng, giving a tighter vertical stack than mu.py encodes.
# fresh_component: xin_zhu_bottom_for_亲 (heng + hooked shu + pie + na
#   sharing 立's long heng as the top rail)
#
# No 立 primitive in bank — inlined 立 fresh (dot + 丷 pair + long heng
# forming top block).

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=5):
    d.line([p0, p1], fill="black", width=w)

def tapered(p0, p1, w0=6, w1=6, steps=24):
    x0, y0 = p0; x1, y1 = p1
    for i in range(steps):
        t0 = i / steps; t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0; ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1; yb = y0 + (y1 - y0) * t1
        w = w0 + (w1 - w0) * t0
        d.line([(xa, ya), (xb, yb)], fill="black", width=max(1, int(round(w))))

def curve(pts, w=5):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)

# --- 立 top block ---
# 1) top dot (slanting down-right), centered
tapered((148, 32), (164, 52), w0=4, w1=8)

# 2) left dot 丷-left (slants down-left) — spaced away from heng
tapered((115, 68), (100, 92), w0=5, w1=7)

# 3) right dot 丷-right (slants down-right)
tapered((180, 68), (196, 92), w0=5, w1=7)

# 4) long heng of 立 (also serves as top rail of 朩 below)
tapered((55, 118), (245, 116), w0=5, w1=6)

# --- 朩 bottom block ---
# 5) second heng (木's own heng, above pie/na)
tapered((75, 162), (225, 160), w0=5, w1=6)

# 6) shu going down from the top heng, straight down to bottom
#    (in 亲 the shu spans full lower half from 立-heng to bottom;
#    slight hook (gou) at bottom-left is optional but visible in GT)
tapered((150, 122), (150, 262), w0=6, w1=5)
# small hook to lower-left
line((150, 262), (138, 258), w=5)

# 7) pie (left descending curve from shu-heng crossing area)
pie_pts = [(148, 175), (130, 200), (108, 228), (78, 258)]
curve(pie_pts, w=5)

# 8) na (right descending, thickening)
na_steps = [(152, 175), (172, 202), (196, 232), (224, 260)]
for i in range(len(na_steps) - 1):
    w = 4 + int(i * 1.5)
    d.line([na_steps[i], na_steps[i+1]], fill="black", width=w+2)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0461_亲/01_亲.png"
img.save(out)
print("wrote", out)
