"""
冈 (p3_char_0127_冈)
Structure: 冂 (3-sided open-bottom bracket) enclosing 乂 (X = 撇 + 捺)
Strokes (4):
  1. 竖 — left wall, slight lean-in at bottom
  2. 横折钩 — top横 + right竖 + hook down-left at bottom-right corner
  3. 撇 — inside, from upper-right area down-left
  4. 捺 — inside, from upper-left area down-right (crosses the 撇)

Notes from memory:
- form_catalog "乂 as body-cross": 撇+捺 crossing near vertical middle
- bracket family (冂): share joints; open-bottom; legs may splay slightly
- terminal hook: 横折钩's hook flicks up-left (~15-20 px)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6  # main stroke width

def brush_line(pts, width=LW):
    """Draw a polyline with round joins."""
    d.line(pts, fill=INK, width=width, joint="curve")
    # cap ends with a small filled circle for round terminals
    r = width // 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

# --- Stroke 1: 竖 (left wall) ---
# Starts at the top-left inside corner and drops straight, no outward foot.
# GT shows this leg ending near y~265, not extending below the box.
brush_line([(70, 78), (68, 170), (70, 265)], width=LW)

# --- Stroke 2: 横折钩 (top + right wall + hook) ---
# horizontal top from ~(80,70) to (235,65); then turn (shoulder) and drop
# down the right side to about (240, 265); then hook up-left ~18 px
top_h = [(80, 72), (155, 68), (235, 65)]      # top 横 (slight rise then dip)
shoulder = (240, 78)                            # 折 shoulder joint
right_v = [(240, 78), (238, 170), (240, 262)]  # 竖 down right side
hook = [(240, 262), (222, 258)]                # small hook flick up-left

# combine into one polyline so the joins are continuous
combined = top_h + [shoulder] + right_v[1:] + [hook[1]]
brush_line(combined, width=LW)

# --- Stroke 3: 撇 (inside, upper-right down to lower-left) ---
# GT: 撇 starts near upper-right of inside, curves down-left ending near left wall.
brush_line([(195, 115), (155, 175), (100, 245)], width=LW - 1)

# --- Stroke 4: 捺 (inside, upper-left down to lower-right, crossing 撇) ---
# thin -> thick with a terminal foot; approximate with a widening line
def taper_line(pts, w0=3, w1=8):
    """Draw a tapered line from w0 to w1 by sampling segments."""
    import math
    # sample along the polyline
    total = 0
    seglens = []
    for i in range(len(pts) - 1):
        dx = pts[i+1][0] - pts[i][0]
        dy = pts[i+1][1] - pts[i][1]
        L = math.hypot(dx, dy)
        seglens.append(L)
        total += L
    N = 80  # samples
    acc = 0
    samples = []
    for i in range(len(pts) - 1):
        dx = pts[i+1][0] - pts[i][0]
        dy = pts[i+1][1] - pts[i][1]
        L = seglens[i]
        steps = max(1, int(N * L / total))
        for s in range(steps):
            t = s / steps
            x = pts[i][0] + dx * t
            y = pts[i][1] + dy * t
            frac = (acc + L * t) / total
            r = w0 / 2 + (w1 - w0) / 2 * frac
            samples.append((x, y, r))
        acc += L
    # final point
    fx, fy = pts[-1]
    samples.append((fx, fy, w1 / 2))
    for (x, y, r) in samples:
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

taper_line([(120, 130), (160, 180), (210, 235), (222, 243)], w0=4, w1=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0127_冈/01_冈.png")
print("Saved 01_冈.png")
