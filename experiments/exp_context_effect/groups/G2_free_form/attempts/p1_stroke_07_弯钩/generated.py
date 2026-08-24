"""
弯钩 (wan gou) — curved stroke that arcs downward, then ends in a hook
that flicks up-and-left.
Canvas: 300x300, white bg, black ink.
Design:
  - Start near top-center-right (~x=175, y=40).
  - Arc gently down and slightly left, ending near (~x=140, y=240).
  - Stroke tapers a bit (thicker at top, tapers into the hook).
  - Hook: short flick up-and-left, ~30-40 px.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# --- Curved body of the stroke (approximate a Bezier by sampling) ---
# Cubic Bezier control points (in image pixel coords, y grows down):
P0 = (175, 45)    # top: start of the curved stroke
P1 = (195, 110)   # control 1 (pulls right, giving the top a slight rightward bulge)
P2 = (150, 190)   # control 2 (pulls back left)
P3 = (135, 245)   # bottom: where the hook begins

def bezier(t, p0, p1, p2, p3):
    u = 1 - t
    x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
    y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
    return (x, y)

# Draw the body as a series of tapered segments (thicker at top -> thinner at hook base)
N = 120
pts = [bezier(i / N, P0, P1, P2, P3) for i in range(N + 1)]

for i in range(N):
    t = i / N
    # Width: starts ~12 at top, tapers to ~7 near the hook base
    w = int(round(12 - 5 * t))
    if w < 6:
        w = 6
    draw.line([pts[i], pts[i+1]], fill="black", width=w)

# Round-cap the top (a little rounded head)
draw.ellipse([P0[0]-6, P0[1]-6, P0[0]+6, P0[1]+6], fill="black")

# --- The hook: flick up-and-left from P3 ---
# Hook is a short, slightly curved segment going up-left.
H0 = P3
H1 = (120, 232)   # midpoint (slight curve upward)
H2 = (98, 220)    # tip of the hook (up and to the left)

# Sample a quadratic for the hook
def quad(t, p0, p1, p2):
    u = 1 - t
    x = u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0]
    y = u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1]
    return (x, y)

M = 40
hpts = [quad(i / M, H0, H1, H2) for i in range(M + 1)]
for i in range(M):
    t = i / M
    # Hook tapers from ~8 down to ~2 at the tip (sharp)
    w = int(round(8 - 6 * t))
    if w < 2:
        w = 2
    draw.line([hpts[i], hpts[i+1]], fill="black", width=w)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p1_stroke_07_弯钩/01_弯钩.png")
print("saved 01_弯钩.png")
