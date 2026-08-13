# BANK_DEVIATION
# skipped: (no 皮 primitive exists — fresh inline required)
# replaced: bao_char.py with local render (needed compressed for R-slot + 巳 interior)
# reason: 皰 = 皮 (LR-left) + 包 (LR-right). No 皮 in bank. bao_char occupies
#         full canvas; needs compression into right ~55% of canvas plus an
#         inline 巳 interior figure — cleaner to inline the whole 包 fresh.
# fresh_component: pi_for_LR_left, bao_full_for_LR_right (envelope + 巳)
import os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(_HERE, "01_皰.png")


def _qbez(p0, p1, p2, steps=30):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _cbez(p0, p1, p2, p3, steps=40):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        b0 = (1 - u) ** 3
        b1 = 3 * (1 - u) ** 2 * u
        b2 = 3 * (1 - u) * u * u
        b3 = u ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _stroke(d, pts, widths):
    if isinstance(widths, (int, float)):
        widths = [widths] * len(pts)
    for i in range(len(pts) - 1):
        w = max(2, int(round(widths[i])))
        a = pts[i]
        b = pts[i + 1]
        d.line([a, b], fill=(0, 0, 0), width=w)
        r = w / 2.0
        d.ellipse([b[0] - r, b[1] - r, b[0] + r, b[1] + r], fill=(0, 0, 0))
    r0 = max(2, int(round(widths[0]))) / 2.0
    d.ellipse([pts[0][0] - r0, pts[0][1] - r0,
               pts[0][0] + r0, pts[0][1] + r0], fill=(0, 0, 0))


def _taper(n, w0, w1):
    return [w0 + (w1 - w0) * (i / max(1, n - 1)) for i in range(n)]


# ---------- Left: 皮 (pí), 5 strokes ----------
def draw_pi_for_LR_left(d):
    # 1. 横 (top short horizontal) — from upper-left going right
    heng = [(55, 60), (115, 55)]
    _stroke(d, heng, _taper(2, 5, 5))

    # 2. 撇 (long) — starts at right end of top heng, curves down-left to bottom
    #    This is the long defining stroke of 皮
    pie1 = _cbez((115, 55), (95, 115), (65, 190), (25, 270), 45)
    _stroke(d, pie1, _taper(len(pie1), 6, 2))

    # 3. 竖 — short middle vertical dropping from the heng, forming top of 又
    shu = [(85, 60), (85, 115)]
    _stroke(d, shu, 5)

    # 4. 横折 forming a cross-arm connecting the shu to the pie at ~y=115
    #    Small horizontal from shu going right, then dropping — but 皮's body
    #    is really "又" so draw a short heng + small pie
    arm_h = [(55, 115), (108, 115)]
    _stroke(d, arm_h, 5)

    # 又 body: small 撇 from arm going down-left, then 捺 going down-right
    # inner 撇
    pie2 = _cbez((78, 118), (65, 160), (55, 200), (40, 245), 30)
    _stroke(d, pie2, _taper(len(pie2), 5, 2))

    # 5. 捺 (right-going tail) — from center down-right with tapered exit
    na = _cbez((85, 120), (100, 165), (120, 210), (145, 260), 35)
    _stroke(d, na, _taper(len(na), 3, 8))


# ---------- Right: 包 (bāo) = 勹 envelope + 巳 interior ----------
def draw_bao_full_for_LR_right(d):
    # ----- 勹 envelope (2 strokes) -----
    # 1. Short 撇 at top-left of envelope
    pie = _qbez((178, 45), (167, 68), (155, 92), 25)
    _stroke(d, pie, _taper(len(pie), 5, 2))
    # 2. Continuous envelope: top → shoulder → shaft → hook
    top = _qbez((172, 88), (215, 85), (258, 82), 24)
    _stroke(d, top, 6)
    shoulder = _cbez((258, 82), (272, 82), (275, 100), (272, 118), 20)
    _stroke(d, shoulder, 6)
    shaft = _cbez((272, 118), (268, 168), (256, 218), (238, 262), 40)
    _stroke(d, shaft, _taper(len(shaft), 6, 3))
    hook = _qbez((238, 262), (225, 258), (212, 244), 15)
    _stroke(d, hook, _taper(len(hook), 5, 2))

    # ----- 巳 interior (3 strokes) — sits in middle-lower of envelope -----
    # Compact 巳 occupying roughly x=180-250, y=130-225
    # Stroke 1: 横折 — top horizontal + right vertical (small box top)
    seg1a = [(180, 135), (245, 135)]
    _stroke(d, seg1a, 5)
    seg1b = [(245, 135), (245, 170)]
    _stroke(d, seg1b, 5)
    # small middle bar closing top box (part of 巳 upper 口)
    seg1c = [(180, 168), (245, 168)]
    _stroke(d, seg1c, 4)

    # Stroke 2: 竖弯钩 — left vertical dropping, curving right at bottom, hook up
    left_v = [(180, 138), (180, 200)]
    _stroke(d, left_v, 5)
    bottom_curve = _cbez((180, 200), (185, 222), (215, 228), (250, 225), 25)
    _stroke(d, bottom_curve, _taper(26, 5, 5))
    hook_up = _qbez((250, 225), (255, 213), (248, 200), 12)
    _stroke(d, hook_up, _taper(len(hook_up), 5, 2))


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_pi_for_LR_left(d)
    draw_bao_full_for_LR_right(d)
    img.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    render()
