"""
夊 (suī) — 3 strokes, similar to 夂.
Stroke 1: short 撇 at top-left (small diagonal tick).
Stroke 2: 横撇 — starts upper (right of stroke 1), a short horizontal into
          a shoulder, then sweeps down-left as a long 撇 flick.
Stroke 3: 捺 — starts near the shoulder/joint area, sweeps down-right,
          then flattens into a long horizontal tail at the bottom (the
          signature of 夊 vs 夂 — the extended flat foot).

Revision 1: centered the character better on canvas, made stroke 2's
horizontal segment more visible, extended the 捺 tail further right
to emphasize the 夊 signature (flat bottom foot).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def bezier(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = ((1 - t) ** 3) * p0[0] + 3 * ((1 - t) ** 2) * t * p1[0] + 3 * (1 - t) * (t ** 2) * p2[0] + (t ** 3) * p3[0]
        y = ((1 - t) ** 3) * p0[1] + 3 * ((1 - t) ** 2) * t * p1[1] + 3 * (1 - t) * (t ** 2) * p2[1] + (t ** 3) * p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        if callable(widths):
            w = widths(i / (n - 1))
        else:
            w = widths[i]
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ----- Stroke 1: short 撇 (top-left tick) -----
s1 = bezier((150, 62), (144, 74), (134, 90), (120, 108), n=40)
stroke(s1, lambda t: 6 - 2 * t)

# ----- Stroke 2: 横撇 -----
# Short horizontal top segment, then a shoulder, then a long 撇 down-left.
h_top = bezier((138, 92), (158, 90), (180, 92), (192, 100), n=30)
stroke(h_top, lambda t: 5 + 1.5 * t)

# shoulder 顿笔
draw.ellipse((186, 92, 200, 106), fill="black")

pie_body = bezier((192, 100), (165, 145), (115, 195), (60, 245), n=90)
stroke(pie_body, lambda t: 8 - 6 * t)

# ----- Stroke 3: 捺 with long flat foot -----
# Starts around the joint (crossing the 撇 body ~mid), sweeps down-right,
# then the terminal flattens right into a long extended tail.
na_main = bezier((130, 150), (162, 195), (200, 235), (232, 260), n=80)
stroke(na_main, lambda t: 3 + 7 * t)

# terminal flat tail — extend well to the right for the 夊 foot signature
tail = bezier((232, 260), (250, 262), (265, 262), (278, 258), n=50)
stroke(tail, lambda t: 10 - 7 * t)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0072_夊/01_夊.png")
