"""
实 (shí) — Phase 3 char, 8 strokes.
Structure: 宀 (roof) on top + 头 (dot, dot, 横, 撇, 捺) below.

Stroke plan (order):
1. 点 (top small dot on 宀 crown, right-leaning)
2. 点 (left inner of 宀, small slash)
3. 横钩 (roof horizontal ending in short down-left hook)
4. 点 (upper left of 头)
5. 点 (upper right of 头)
6. 横 (middle horizontal, spans wide)
7. 撇 (long left-down sweep from center)
8. 捺 (long right-down sweep from same center)

Silhouette: tall square, roof upper 40%, body lower 60%.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def line(p1, p2, w=6):
    d.line([p1, p2], fill=INK, width=w)


def bezier(pts, w=6, steps=60):
    # simple quadratic/cubic bezier polyline
    n = len(pts) - 1
    from math import comb
    out = []
    for i in range(steps + 1):
        t = i / steps
        x = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][0] for k in range(n + 1))
        y = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][1] for k in range(n + 1))
        out.append((x, y))
    for a, b in zip(out, out[1:]):
        d.line([a, b], fill=INK, width=w)


# ---- 宀 (roof) — upper 40% ----
# 1. top dot: small mark at very top center
bezier([(148, 40), (152, 46), (158, 55)], w=7, steps=20)

# 2. left inner dot of 宀 (short slash down-left, at left edge of roof)
bezier([(78, 90), (75, 100), (72, 112)], w=7, steps=20)

# 3. 横钩 — long horizontal across, ending in short hook down-left
bezier([(72, 92), (110, 88), (170, 88), (220, 92)], w=7, steps=60)
# hook flick: from end going down-left slightly (roof hook goes down-left)
bezier([(220, 92), (218, 100), (212, 108)], w=7, steps=20)

# ---- 头 body — lower 60% ----
# 4. upper-left dot of 头 (short slash)
bezier([(100, 130), (105, 138), (112, 148)], w=7, steps=20)

# 5. upper-right dot of 头 (short slash)
bezier([(190, 130), (185, 138), (178, 148)], w=7, steps=20)

# 6. 横 — wide horizontal across, middle-lower
bezier([(55, 190), (110, 188), (180, 188), (245, 192)], w=7, steps=60)

# 7. 撇 — long left-down sweep from center-upper to lower-left
bezier([(150, 165), (135, 210), (110, 250), (80, 278)], w=7, steps=60)

# 8. 捺 — long right-down sweep from same center, thicker terminal
bezier([(150, 165), (170, 205), (195, 240), (225, 268)], w=7, steps=60)
# small tail widening at end of 捺
bezier([(225, 268), (232, 270), (240, 270)], w=7, steps=20)


out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0393_实/01_实.png"
img.save(out_path)
print("Saved:", out_path)
