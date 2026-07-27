# p3_char_0135_刅 — 刅 (chuang, "wound/cut", variant of 创)
# Structure: 刀 (dao) base + small 点 inside upper + right-side 点/捺 mark
# ~4 strokes: 撇 (crossing pie), 横折钩 (dao's main envelope),
#             小点 (inside upper), 捺/点 (right-side blade mark)
# Bank note: 刀 primitive was FAIL/errata; deriving fresh with thin
# calligraphic widths per B5 lesson (respect GT proportions).

from PIL import Image, ImageDraw

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


def to_px(x, y):
    """Math coords (center origin, +y up) -> PIL pixel."""
    return CANVAS / 2 + x, CANVAS / 2 - y


def tapered_bezier(p0, p1, p2, w_head, w_tail, steps=48):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        px, py = to_px(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def tapered_line(p0, p1, w_head, w_tail, steps=24):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        px, py = to_px(x, y)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


# ============================================================
# The character is rendered small/centered per GT (~60% canvas)
# GT shows compact form roughly in middle of canvas.
# ============================================================

# Revised (pass 2): smaller/tighter per GT, character sized ~45% canvas,
# positioned slightly above center. Thinner MMH-style widths.

# Stroke 1: 撇 — long left-falling from upper-center to lower-left
# Crosses the horizontal shaft at ~40% mark
tapered_bezier(
    p0=(-5, 30),     # upper head, meets top-bar left area
    p1=(-20, 5),     # bow slightly left
    p2=(-40, -35),   # thin tail lower-left
    w_head=4, w_tail=1, steps=40,
)

# Stroke 2: 横折钩 — top horizontal + right vertical + hook of 刀
h_start = (-15, 32)
h_end = (25, 32)
tapered_line(h_start, h_end, w_head=3, w_tail=4, steps=20)

# Zhe corner (small filled joint)
cx, cy = to_px(*h_end)
d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(0, 0, 0))

# Vertical descent
v_start = h_end
v_end = (25, -25)
tapered_line(v_start, v_end, w_head=4, w_tail=4, steps=22)

# Hook (钩) — short up-left flick at the base
gou_start = v_end
gou_end = (12, -10)
tapered_line(gou_start, gou_end, w_head=4, w_tail=1, steps=16)

# Stroke 3: 撇/点 inside upper-middle (small pie inside)
tapered_bezier(
    p0=(0, 15),
    p1=(-5, 5),
    p2=(-12, -8),
    w_head=3, w_tail=1, steps=24,
)

# Stroke 4: 点/捺 on the right (blade mark)
# Small diagonal falling stroke, positioned close-right of the hook
tapered_bezier(
    p0=(35, 15),
    p1=(45, 5),
    p2=(58, -12),
    w_head=2, w_tail=5, steps=24,
)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0135_刅/01_刅.png")
print("wrote 01_刅.png")
