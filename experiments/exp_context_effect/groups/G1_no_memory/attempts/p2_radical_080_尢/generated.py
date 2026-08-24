"""G1 render of 尢 (3-stroke radical) — revised."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5


def stroke(points, width=LW):
    d.line(points, fill=INK, width=width, joint="curve")


# Stroke 1: 撇 (long left-falling curve) drawn first
# Starts higher-middle and sweeps down to lower-left corner
p_pts = []
for i in range(51):
    t = i / 50
    # start upper (around x=150,y=80), sweep down-left ending near (55,265)
    x0, y0 = 155, 82
    x1, y1 = 120, 175   # control
    x2, y2 = 55, 268
    x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t * t * x2
    y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t * t * y2
    p_pts.append((x, y))
stroke(p_pts)

# Stroke 2: 横 (horizontal) — crosses the 撇, slight down slope
h_pts = []
for i in range(21):
    t = i / 20
    x = 80 + t * 135
    y = 138 + t * 8
    h_pts.append((x, y))
stroke(h_pts)

# Stroke 3: 竖弯钩 — small rising top tick, then vertical, curve right, small hook up
# The top tick begins near where the 横 meets it on the right, angling up-right briefly
# Then main body plunges down and curves right into a hook

# Combined top tick + vertical body as one polyline (tick is short)
top_tick = [(198, 140), (208, 128), (218, 118)]
stroke(top_tick)

# Vertical body from ~(210,132) going down to ~(215,250), slight rightward drift
body = []
for i in range(31):
    t = i / 30
    x = 210 + 3 * t
    y = 132 + t * 118
    body.append((x, y))
stroke(body)

# Bottom curve turning right (竖弯)
curve = []
for i in range(21):
    t = i / 20
    # arc from (213,250) sweeping down-right to (250,268)
    x = 213 + t * 40
    y = 250 + (t ** 0.6) * 18
    curve.append((x, y))
stroke(curve)

# Small hook up-right at the end (钩)
hook = [(253, 268), (255, 260), (256, 253)]
stroke(hook)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p2_radical_080_尢/01_尢.png"
)
