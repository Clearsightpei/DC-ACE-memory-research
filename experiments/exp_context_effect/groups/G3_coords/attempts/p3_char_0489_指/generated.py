# BANK_DEVIATION
# skipped: shou_pang.py
# reason: GT is uniform thin lines (MMH style) across whole char; turtle-based shou_pang mixes badly with inline PIL right-side (匕+日) at these thin widths. Better to inline all strokes at consistent width.
# fresh_component: zhi_finger_inline (扌 + 旨 all inline PIL)

# p3_char_0489_指 (zhǐ, "finger") — 9 strokes.
# Left: 扌 (3 strokes: heng, shu-gou, ti)
# Right: 旨 = 匕 top (2 strokes: pie, shu-wan) + 日 bottom (4 strokes)

from PIL import Image, ImageDraw

CANVAS = 300
W = 5

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


def line(p0, p1, w=W):
    d.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def polyline(pts, w=W):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)


# ==== LEFT: 扌 (x-range ~35..115) ====
# Stroke 1: 横 (short, slightly rising)
line((40, 105), (110, 100))

# Stroke 2: 竖钩 (long vertical shaft with small hook at bottom)
line((75, 70), (75, 240))
# hook at bottom, small tick to the upper-left
line((75, 240), (60, 225))

# Stroke 3: 提 (rising tick across shaft from lower-left to upper-right)
line((45, 175), (115, 155))

# ==== RIGHT: 旨 (x-range ~130..260) ====
# --- Top: 匕 (compressed, small) ---
# Stroke 4: 撇 (short, from upper-right to lower-left)
line((205, 55), (155, 105))

# Stroke 5: 竖弯钩 / 竖弯 (vertical down, curves right, small hook up)
line((175, 75), (175, 115))
polyline([(175, 115), (185, 125), (210, 128), (240, 118)])
# small hook up at end
line((240, 118), (240, 100))

# --- Bottom: 日 (rectangle with middle heng) ---
x_left = 150
x_right = 240
y_top = 150
y_bot = 250
y_mid = 205

# Stroke 6: 竖 (left vertical)
line((x_left, y_top), (x_left, y_bot))
# Stroke 7: 横折 (top heng + right shu)
line((x_left, y_top), (x_right, y_top))
line((x_right, y_top), (x_right, y_bot))
# Stroke 8: middle 横
line((x_left + 3, y_mid), (x_right - 3, y_mid))
# Stroke 9: bottom 横
line((x_left, y_bot), (x_right, y_bot))

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0489_指/01_指.png"
img.save(out)
print("saved", out)
