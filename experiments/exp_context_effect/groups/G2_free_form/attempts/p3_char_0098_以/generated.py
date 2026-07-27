"""
p3_char_0098_以 — 4 strokes: 竖提, 点, 撇, 捺
Layout (300x300):
  Left component ~ x in [55, 130], center around x=95.
    Stroke 1 (竖提): a vertical descending from (~80, 95) to (~85, 200),
                      then flicking up-right to (~135, 175).
    Stroke 2 (点): a short downward dot between the two components,
                    around (~130, 115) to (~140, 145).
  Right component (人-like) ~ x in [150, 260]:
    Stroke 3 (撇): from (~185, 90) curving down-left to (~130, 265).
    Stroke 4 (捺): from (~180, 130) sweeping down-right to (~255, 245),
                    thin→thick foot.

# SIGNATURE CHECK: not on sibling-signature list; but right half is
# 人-like (撇+捺). Use sibling table row for 人: apex NOT shared here
# because 捺 emerges from mid-撇, not the top. Standard 以 form: 捺
# starts at ~1/3 down the 撇, not at the 撇's apex.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def brush_line(pts, w_start=8, w_end=8):
    """Draw a tapered line by dabbing circles along interpolated points."""
    if len(pts) < 2:
        return
    # accumulate arc lengths
    seg_lens = []
    total = 0.0
    for i in range(len(pts) - 1):
        dx = pts[i+1][0] - pts[i][0]
        dy = pts[i+1][1] - pts[i][1]
        L = (dx*dx + dy*dy) ** 0.5
        seg_lens.append(L)
        total += L
    if total == 0:
        return
    n_dabs = max(int(total * 2), 20)
    for k in range(n_dabs + 1):
        t = k / n_dabs
        # find which segment
        target = t * total
        acc = 0.0
        seg_i = 0
        for i, L in enumerate(seg_lens):
            if acc + L >= target or i == len(seg_lens) - 1:
                seg_i = i
                local_t = (target - acc) / L if L > 0 else 0
                break
            acc += L
        x = pts[seg_i][0] + local_t * (pts[seg_i+1][0] - pts[seg_i][0])
        y = pts[seg_i][1] + local_t * (pts[seg_i+1][1] - pts[seg_i][1])
        r = (w_start + (w_end - w_start) * t) / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

# ---------- Stroke 1: 竖提 (vertical then flick up-right) ----------
# Vertical descending body with slight left drift then rightward at bottom,
# then flicks up-right.
vertical = [(85, 95), (82, 130), (82, 170), (88, 200), (100, 210)]
flick = [(100, 210), (115, 200), (135, 180)]
brush_line(vertical, w_start=8, w_end=9)
brush_line(flick, w_start=9, w_end=3)  # taper on the flick

# ---------- Stroke 2: 点 (small dot between the two halves) ----------
dot = [(130, 115), (140, 135), (142, 148)]
brush_line(dot, w_start=4, w_end=10)  # thin→thick 点

# ---------- Stroke 3: 撇 (long curved down-left from upper right) ----------
pie = [(200, 85), (190, 120), (175, 160), (155, 200), (130, 245), (115, 270)]
brush_line(pie, w_start=9, w_end=3)  # taper to fine tip

# ---------- Stroke 4: 捺 (from mid-撇 down-right, thin→thick foot) ----------
na = [(180, 135), (200, 170), (225, 210), (250, 240), (260, 245)]
brush_line(na, w_start=4, w_end=12)  # thin→thick foot

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0098_以/01_以.png")
print("saved")
