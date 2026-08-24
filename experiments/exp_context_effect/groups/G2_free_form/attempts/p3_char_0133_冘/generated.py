"""Render 冘 (p3_char_0133) — 4 strokes.

Structure (from GT):
  Top: a small 撇 flick on the upper-left, and a 横撇 (horizontal
       turning into a short down-right stroke) that together form
       a low hat with a dot-like flick under it.
  Bottom: 几-like base — a long left 撇 curving down-left, and a
       right 横折弯钩/竖弯钩 forming the right leg with terminal hook.

Actually 冘 = ⺈ (top hat) + 几 (bottom frame). The GT shows:
  - short 撇 top-left of hat
  - horizontal top with a short dot-like drop under middle
  - long left curve (撇) from under hat down to bottom-left
  - right vertical curving into a bottom-right hook

We use PIL with brush-dab strokes for calligraphic feel.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_stroke(pts, widths):
    """Draw a variable-width stroke by dabbing circles along a polyline."""
    if len(pts) < 2:
        return
    # sample densely
    total = 0.0
    seglens = []
    for i in range(len(pts) - 1):
        dx = pts[i+1][0] - pts[i][0]
        dy = pts[i+1][1] - pts[i][1]
        d = math.hypot(dx, dy)
        seglens.append(d)
        total += d
    if total < 1e-6:
        return
    n_samples = max(int(total * 2), 20)
    for k in range(n_samples + 1):
        t = k / n_samples
        # find segment
        target = t * total
        acc = 0.0
        seg_i = 0
        for i, sl in enumerate(seglens):
            if acc + sl >= target or i == len(seglens) - 1:
                seg_i = i
                seg_t = (target - acc) / sl if sl > 0 else 0
                break
            acc += sl
        x = pts[seg_i][0] + (pts[seg_i+1][0] - pts[seg_i][0]) * seg_t
        y = pts[seg_i][1] + (pts[seg_i+1][1] - pts[seg_i][1]) * seg_t
        # interpolate width
        w = widths[0] + (widths[1] - widths[0]) * t
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_pts(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0]
        y = u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1]
        pts.append((x, y))
    return pts


def bezier3_pts(p0, p1, p2, p3, n=50):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0]
        y = u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts


# --- Stroke 1: short 撇 top-left of hat ---
s1 = [(110, 85), (90, 115)]
dab_stroke(s1, (8, 4))

# --- Stroke 2: 横钩 hat — long horizontal, then a short downward-left hook at right end ---
s2_horiz = bezier_pts((95, 115), (155, 108), (215, 115), n=40)
dab_stroke(s2_horiz, (7, 9))
# Right-end 横钩 hook: short down-left flick
s2_hook = [(215, 115), (205, 140)]
dab_stroke(s2_hook, (9, 4))

# --- Small under-flick: dot-like drop under the middle of the hat (part of hat visual) ---
# GT shows a small "丿" under the horizontal, slightly right of center
s_dot = [(150, 125), (140, 150)]
dab_stroke(s_dot, (6, 3))

# --- Stroke 3: long left 撇 — from just under hat down to bottom-left ---
s3 = bezier3_pts((135, 130), (110, 185), (80, 230), (50, 280), n=60)
dab_stroke(s3, (10, 5))

# --- Stroke 4: right 竖弯钩 — down from upper right, sweeping right along bottom, ending in up-hook ---
s4 = bezier3_pts((200, 130), (210, 210), (225, 265), (255, 265), n=60)
dab_stroke(s4, (10, 9))
# Terminal hook: upward flick at end
s4_hook = [(255, 265), (253, 240)]
dab_stroke(s4_hook, (9, 4))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0133_冘/01_冘.png")
