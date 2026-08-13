"""
步 (bu) — 7 strokes. Top: 止 compact. Bottom: 少-like without the dot.
Revision 2:
 - Tighten top 止 so pieces read as one radical.
 - Short 撇 (stroke 5) originates ABOVE the long 横, crosses it, sweeps down-left.
 - Extend the sweeping 撇 further to lower-right with graceful curve.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = (0, 0, 0)

def line(p0, p1, w=6):
    d.line([p0, p1], fill=INK, width=w)

def bezier(pts, w=6, n=60, taper=None):
    def B(t):
        u = 1 - t
        x = u**3*pts[0][0] + 3*u**2*t*pts[1][0] + 3*u*t*t*pts[2][0] + t**3*pts[3][0]
        y = u**3*pts[0][1] + 3*u**2*t*pts[1][1] + 3*u*t*t*pts[2][1] + t**3*pts[3][1]
        return (x, y)
    prev = B(0)
    for i in range(1, n+1):
        t = i/n
        cur = B(t)
        if taper:
            w0, w1 = taper
            ww = int(round(w0 + (w1-w0)*t))
        else:
            ww = w
        d.line([prev, cur], fill=INK, width=max(1, ww))
        d.ellipse([cur[0]-ww/2, cur[1]-ww/2, cur[0]+ww/2, cur[1]+ww/2], fill=INK)
        prev = cur

# ---- Top 止 (compact) ----
# Stroke 1: middle vertical (tall) of 止
line((115, 70), (115, 135), w=8)

# Stroke 2: short horizontal tick from mid vertical going right (upper area)
line((115, 95), (155, 92), w=6)

# Stroke 3: short vertical dropping from right end of tick
line((155, 92), (155, 135), w=7)

# Stroke 4: LONG horizontal — the middle base of 步, extends far right
bezier([(55, 145), (130, 143), (215, 143), (255, 148)], w=7, n=50)

# ---- Bottom part ----
# Stroke 5: short 撇 originating above-left of the horizontal, sweeping down-left crossing it
bezier([(105, 128), (95, 155), (82, 180), (65, 210)], w=7, n=45, taper=(8,3))

# Stroke 6: vertical stem in middle (from just below horizontal, going down)
line((150, 148), (150, 215), w=7)

# Stroke 7: long sweeping 撇, from mid area, curving down-right
bezier([(170, 155), (185, 205), (210, 245), (260, 275)], w=8, n=70, taper=(10,3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0351_步/01_步.png")
