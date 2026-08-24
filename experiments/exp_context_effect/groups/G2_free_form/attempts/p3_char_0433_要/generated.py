"""
要 (yào) — 9 strokes. Top: 覀 (西-like frame, no bottom vertical hooks).
Bottom: 女 (3 strokes: 撇点, long 撇, 横 crossbar).

Layout:
  - Top half (~y 30..145): 覀 rectangle (wider than tall, horizontal top,
    left/right verticals, two internal short verticals, closing bottom
    horizontal that BECOMES the crossbar of the top-block).
  - Bottom half (~y 145..285): 女, wide, straddling the whole width.

Stroke plan (MMH 覀 has 6 strokes: 一, 丨, 横折, 丨, 丨, 一; then 女 has 3):
  1. top 一
  2. left 丨
  3. 横折 (top right corner: horizontal + descending right side)
  4. inside-left short 丨
  5. inside-right short 丨
  6. bottom 一 seal
  7. 女 stroke 1: 撇点
  8. 女 stroke 2: long 撇
  9. 女 stroke 3: 横

# SIGNATURE CHECK: 女 has three strokes; long 撇 goes body-crossing.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def bezier(p0, p1, p2, widths, steps=80):
    w0, w1 = widths
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = w0 * (1 - t) + w1 * t
        dab(x, y, r)


def segment(p0, p1, widths, steps=60):
    w0, w1 = widths
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] * (1 - t) + p1[0] * t
        y = p0[1] * (1 - t) + p1[1] * t
        r = w0 * (1 - t) + w1 * t
        dab(x, y, r)


BW = 4.0  # base half-width

# ============================================================
# TOP: 覀 (rectangular frame with 2 internal short verticals)
# ============================================================
L, R = 70, 230
T, B = 55, 145

# 1. top 一
segment((L - 5, T), (R + 5, T), widths=(BW, BW), steps=80)

# 2. left 丨
segment((L, T - 2), (L - 4, B + 2), widths=(BW, BW), steps=60)

# 3. 横折 (upper piece + right descending side) — single connected
segment((L + 2, T - 6), (R + 4, T - 6), widths=(BW, BW), steps=70)
segment((R + 4, T - 6), (R + 6, B), widths=(BW, BW), steps=60)

# 4. inside-left short 丨
segment((L + 45, T + 12), (L + 42, B - 5), widths=(BW - 0.5, BW - 0.5), steps=40)

# 5. inside-right short 丨
segment((L + 100, T + 12), (L + 103, B - 5), widths=(BW - 0.5, BW - 0.5), steps=40)

# 6. bottom 一 seal (this doubles as the top of the 女 area's crossbar zone)
segment((L - 10, B), (R + 12, B - 3), widths=(BW + 0.5, BW + 0.5), steps=90)

# ============================================================
# BOTTOM: 女 (3 strokes) — placed lower half
# ============================================================

# Stroke 7: 撇点 (piě-diǎn) — upper-left of 女
pie_start = (145, 155)
pie_ctrl = (125, 195)
pie_tip = (95, 235)
dab(*pie_start, BW + 1)
bezier(pie_start, pie_ctrl, pie_tip, widths=(BW + 1, BW - 2), steps=70)
dab(*pie_tip, BW - 1)

# 点 (反捺): from tip, sweeps down-right, thin→thick
dian_end = (175, 285)
dian_ctrl = (130, 255)
bezier(pie_tip, dian_ctrl, dian_end, widths=(BW - 1.5, BW + 2), steps=70)
dab(*dian_end, BW + 2)

# Stroke 8: long 撇 — from upper-right down-left across full width of 女
pie2_start = (205, 160)
pie2_ctrl = (160, 220)
pie2_tip = (40, 285)
dab(*pie2_start, BW + 1)
bezier(pie2_start, pie2_ctrl, pie2_tip, widths=(BW + 1.5, BW - 2), steps=110)

# Stroke 9: 横 crossbar for 女 — a wide horizontal across mid-bottom
heng_start = (30, 235)
heng_end = (285, 225)
dab(*heng_start, BW)
segment(heng_start, heng_end, widths=(BW, BW), steps=130)
dab(*heng_end, BW + 1)


out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0433_要/01_要.png"
)
img.save(out_path)
print(f"wrote {out_path}")
