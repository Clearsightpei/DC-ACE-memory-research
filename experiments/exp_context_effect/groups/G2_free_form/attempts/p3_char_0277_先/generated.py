"""
先 (xiān) — 6 strokes: 丿, 一, 一, 丨, 丿, 乚(竖弯钩)
Top: a 牛-like cluster (short 丿 + short 一 + long 一 + short 丨)
Bottom: 儿 (long 丿 + 竖弯钩)

Hook rule (memory_index TIER-0 B): 竖弯钩 terminal flicks UP-and-LEFT.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bezier(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t*t*p2[0] + t**3*p3[0]
        y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t*t*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts

def brush(points, widths):
    """draw variable-width stroke by dabbing circles"""
    n = len(points)
    for i, (x, y) in enumerate(points):
        t = i / max(1, n - 1)
        # interpolate width
        if isinstance(widths, (int, float)):
            w = widths
        else:
            # widths is list of (t, w) or just [w_start, w_end]
            if len(widths) == 2:
                w = widths[0] * (1 - t) + widths[1] * t
            else:
                w = widths[int(t * (len(widths) - 1))]
        r = w / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

def line(a, b, w=6):
    pts = bezier(a, ((a[0]+b[0])/2, (a[1]+b[1])/2), ((a[0]+b[0])/2, (a[1]+b[1])/2), b, n=40)
    brush(pts, w)

# --- Stroke 1: 丿 (short top-left slant) ---
s1 = bezier((155, 55), (150, 70), (140, 88), (120, 105), n=50)
brush(s1, [7, 3])

# --- Stroke 2: 一 (short top horizontal) ---
s2 = bezier((155, 95), (170, 93), (185, 92), (200, 92), n=30)
brush(s2, [4, 7])

# --- Stroke 3: 一 (middle long horizontal, slight rise) ---
s3 = bezier((60, 140), (110, 135), (170, 132), (240, 128), n=60)
brush(s3, [5, 8])
# small terminal dab (顿笔)
d.ellipse([236, 124, 248, 136], fill="black")

# --- Stroke 4: 丨 (short vertical connecting the two horizontals) ---
s4 = bezier((160, 95), (160, 110), (160, 125), (160, 140), n=30)
brush(s4, [6, 6])

# --- Stroke 5: 丿 (bottom-left long slant, part of 儿) ---
s5 = bezier((135, 140), (125, 175), (110, 215), (70, 265), n=70)
brush(s5, [8, 3])

# --- Stroke 6: 竖弯钩 (right leg of 儿) ---
# vertical down, curve right, hook up-left
s6a = bezier((180, 140), (178, 175), (176, 205), (180, 230), n=50)
brush(s6a, [7, 8])
s6b = bezier((180, 230), (188, 250), (205, 258), (235, 250), n=50)
brush(s6b, [8, 6])
# hook flicking UP-and-LEFT
s6c = bezier((235, 250), (238, 244), (236, 236), (228, 228), n=30)
brush(s6c, [6, 2])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0277_先/01_先.png")
print("saved")
