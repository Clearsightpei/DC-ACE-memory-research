# BANK_DEVIATION
# skipped: ren_pang.py
# reason: bank primitive's pie+shu geometry rendered with the shu detached
#   from the pie mid-shaft at this scale, breaking the 亻 joint visually.
# fresh_component: ren_pang_inline_for_lao
#
# generated.py — p3_char_0390_佬 (lǎo, "old man") — 8 strokes.
# Composition: 亻 (left, inline) + 老 (right, inline).

from PIL import Image, ImageDraw

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)

W = 5


def line(p0, p1, w=W):
    d.line([p0, p1], fill=(0, 0, 0), width=w)


def polyline(pts, w=W):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)


def tapered_bezier(p0, p1, p2, w0=6, w1=2, steps=60):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            d.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
        prev = (bx, by)


# ---- LEFT: 亻 (inline) — x range 40..110 ----
# Stroke 1: 撇 — sweeps from upper-center down-left
tapered_bezier((90, 85), (75, 130), (45, 195), w0=6, w1=3)
# Stroke 2: 竖 — drops from mid-pie straight down
line((88, 140), (88, 265), w=W)

# ---- RIGHT: 老 — x range 125..280 ----
# Stroke 3: top heng (long)
line((130, 105), (275, 100), w=W)

# Stroke 4: short shu — vertical crossing hengs
line((200, 80), (200, 165), w=W)

# Stroke 5: middle heng (tilted slightly, shorter than top)
line((150, 140), (270, 138), w=W)

# Stroke 6: long sweeping pie — from upper right, sweeps down-left,
# ending at bottom of right column (does NOT invade left column)
tapered_bezier((260, 95), (215, 195), (150, 275), w0=7, w1=2)

# ---- 匕 at bottom right ----
# Stroke 7: short pie of 匕 — small sweep down-left, sits between
# the middle heng and the 竖弯钩 shaft
line((235, 170), (200, 210), w=W)

# Stroke 8: 竖弯钩 — vertical shaft, curve right, hook up
polyline([(215, 160), (215, 245)], w=W)  # vertical shaft
polyline([(215, 245), (230, 265), (255, 268), (275, 260)], w=W)  # curve
line((275, 260), (277, 235), w=W)  # hook up

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0390_佬/01_佬.png"
img.save(out)
print("saved", out)
