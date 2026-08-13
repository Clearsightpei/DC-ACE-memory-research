"""
p3_char_0403_放 (fàng) — 8 strokes = 方 (left) + 攵 (right)

REVISION 2: fixed 方's box (removed stray bottom line, cleaner 横折钩),
better 攵 (horizontal connects to top 撇, body 撇 and 捺 cross properly).

方 (left half): 丶 一 丿 横折钩(with hook)
攵 (right half): 丿 一 丿 ㇏
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def stroke(pts, width=6):
    draw.line(pts, fill=BLACK, width=width, joint="curve")


def dot_dab(x, y, angle_deg=45, length=12, width=6):
    """Slanted dot 丶 — short stroke."""
    import math
    rad = math.radians(angle_deg)
    x2 = x + length * math.cos(rad)
    y2 = y + length * math.sin(rad)
    draw.line([(x, y), (x2, y2)], fill=BLACK, width=width, joint="curve")
    r = width // 2 + 1
    draw.ellipse([x2 - r, y2 - r, x2 + r, y2 + r], fill=BLACK)


def bezier(p0, p1, p2, width=6, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    draw.line(pts, fill=BLACK, width=width, joint="curve")


def taper_line(p0, p1, w0=8, w1=3, steps=16):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = int(w0 + (w1 - w0) * t0)
        draw.line([(xa, ya), (xb, yb)], fill=BLACK, width=max(1, w))
        draw.ellipse([xb - w / 2, yb - w / 2, xb + w / 2, yb + w / 2], fill=BLACK)


# ------------------- 方 (left half, x ~30-140) -------------------
# 1. 丶 dot at top-center of left half
dot_dab(88, 45, angle_deg=55, length=13, width=7)

# 2. 一 long horizontal beneath dot
stroke([(35, 90), (145, 88)], width=7)

# 3. 丿 long 撇 from just right-of-center of horizontal, sweeping down-left
bezier((100, 95), (75, 165), (28, 240), width=6)

# 4. 横折钩 — the right side box of 方 that gives it its enclosed feel.
#    Down from just below the horizontal's right end, curving in, hook LEFT-UP.
# Down stroke (slightly bowed left as in 力)
bezier((128, 95), (118, 160), (95, 215), width=6)
# hook flick UP-and-LEFT per memory hook rules (~-115°)
draw.line([(95, 215), (78, 200)], fill=BLACK, width=6)

# ------------------- 攵 (right half, x ~155-285) -------------------
# 5. 短 撇 top-left of 攵  (starts high, ends at horizontal's start)
bezier((215, 80), (200, 100), (180, 125), width=6)

# 6. 一 short horizontal — LEFT end meets the tail of stroke 5
stroke([(178, 128), (255, 118)], width=7)

# 7. 丿 body 撇 sweeps down-left through the horizontal
bezier((230, 138), (200, 200), (160, 265), width=6)

# 8. 捺 long tapered down-right — starts near crossing of 6/7
taper_line((215, 158), (285, 262), w0=4, w1=11, steps=26)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0403_放/01_放.png"
)
print("wrote 01_放.png (revision 2)")
