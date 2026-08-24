"""Render 运 (yun, 7 strokes) at 300x300 PNG, PIL brush-dabs.

运 = 辶 (semi-enclosure, bottom-left wrap) + 云 (upper-right inside).

Structure (visible in gt/phase3/运.png):
- 云 sits in the UPPER-RIGHT quadrant, compact.
  云 = 4 strokes:
    (1) 短横 (top short 横)
    (2) 长横 (bottom longer 横)
    (3) 撇折 of 厶 (short bowed 撇 down-left, then a rightward stub)
    (4) 点 (small dot ending the 厶)
- 辶 wraps under-left, drawn LAST (per stroke order):
    (5) 点 (small dot upper-left)
    (6) 横折折撇 z-body on left side, below the dot
    (7) 平捺 long shallow smile sweeping under 云, right foot.

Reference PASS: p2_radical_044_辶 (dab technique reused).

# SIGNATURE CHECK: 云 has TWO horizontals stacked (short-over-long)
# with a ム (撇折+点) under them — NOT a single 一 (would look like 元).
# 辶's 捺 must flick RIGHT with a broad flat foot; the hook of nothing
# here — 辶 has no upward hook, its 捺 ends flat.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy)
    if steps is None:
        steps = max(30, int(L * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200, ease=None):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        te = ease(t) if ease else t
        r = r0 + (r1 - r0) * te
        dab(x, y, r)


# ============ 云 (upper-right) ============
# Compact. x roughly [125, 235], y roughly [60, 175].

# Stroke 1: 短横 (top short 横) — slightly rising
def stroke_top_heng():
    x0, y0 = 148, 78
    x1, y1 = 210, 72
    r = 3.2
    dab(x0, y0, r + 1.0)
    line_dabs(x0, y0, x1, y1, r, r)
    dab(x1, y1, r + 1.5)  # slight press at right end


# Stroke 2: 长横 (bottom longer 横) — spans wider
def stroke_bottom_heng():
    x0, y0 = 128, 112
    x1, y1 = 232, 108
    r = 3.4
    dab(x0, y0, r + 1.0)
    line_dabs(x0, y0, x1, y1, r, r)
    dab(x1, y1, r + 1.7)


# Stroke 3: 撇折 of 厶 — short 撇 down-left then a rightward stub
def stroke_pie_zhe():
    # 撇 portion (bowed down-left)
    p0 = (172, 128)
    p1 = (158, 148)
    p2 = (146, 168)
    bezier_dabs(p0, p1, p2, 3.2, 2.6, steps=140)
    # zhe stub going down-right (the 折 of 撇折 continues right)
    x0, y0 = p2
    x1, y1 = 190, 172
    line_dabs(x0, y0, x1, y1, 3.0, 3.4)
    dab(x1, y1, 4.0)


# Stroke 4: 点 (small dot of 厶 — upper-right of the ム enclosure)
def stroke_dot_yun():
    # small teardrop pointing down-left, ending near where zhe-stub ended
    p0 = (208, 145)
    p1 = (200, 158)
    p2 = (194, 172)
    steps = 90
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = 1.6 + (4.2 - 1.6) * (t ** 1.3)
        dab(x, y, r)
    dab(p2[0], p2[1], 4.2)


# ============ 辶 (wraps under-left) ============
# Drawn AFTER 云 per stroke order. Dot upper-left, body lower-left, 捺 across bottom.

# Stroke 5: 点 of 辶 (small teardrop upper-left)
def stroke_chuo_dot():
    p0 = (92, 62)
    p1 = (98, 75)
    p2 = (108, 88)
    steps = 100
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = 1.5 + (4.5 - 1.5) * (t ** 1.4)
        dab(x, y, r)
    dab(p2[0], p2[1], 4.5)


# Stroke 6: 横折折撇 body of 辶 (compact z on the left)
def stroke_chuo_body():
    a = (72, 128)   # start of small 横
    b = (118, 122)  # end of 横 / first fold
    c = (88, 158)   # after first fold going down-left
    e = (128, 155)  # after second short 横
    tail_tip = (72, 218)  # bowed 撇 down-left tail
    r_body = 3.2
    dab(a[0], a[1], r_body + 1.2)
    line_dabs(a[0], a[1], b[0], b[1], r_body, r_body)
    dab(b[0], b[1], r_body + 1.4)
    line_dabs(b[0], b[1], c[0], c[1], r_body, r_body)
    dab(c[0], c[1], r_body + 1.2)
    line_dabs(c[0], c[1], e[0], e[1], r_body, r_body)
    dab(e[0], e[1], r_body + 1.2)
    ctrl = (118, 190)
    bezier_dabs(e, ctrl, tail_tip, r_body + 0.5, 1.2, steps=220)


# Stroke 7: 平捺 (flat sweeping press) — long shallow smile
def stroke_chuo_pina():
    p0 = (58, 232)
    p2 = (268, 238)
    p1 = (162, 278)  # control pulls down → concave-up belly
    steps = 340
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        if t < 0.85:
            r = 1.5 + (6.8 - 1.5) * (t / 0.85)
        else:
            r = 6.8 - (6.8 - 5.2) * ((t - 0.85) / 0.15)
        dab(x, y, r)
    # broad flat foot
    fx, fy = p2
    for k in range(0, 14):
        dab(fx + k * 0.7, fy + k * 0.15, 5.5 - k * 0.15)
    dab(p0[0], p0[1], 3)


# ---- render in stroke order ----
stroke_top_heng()
stroke_bottom_heng()
stroke_pie_zhe()
stroke_dot_yun()
stroke_chuo_dot()
stroke_chuo_body()
stroke_chuo_pina()

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0329_运/01_运.png"
img.save(out)
print("Saved:", out)
