# p3_char_0257_问 — 问 (wèn), 6 strokes: 点 + 竖 + 横折钩 (门 envelope) + 竖 + 横折 + 横 (口 inside).
# Composition: reuse men_char envelope recipe; place a small 口 inline inside upper interior.
from PIL import Image, ImageDraw
import os, sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from dian import draw_dian  # noqa: E402


def _tapered_line(D, p0, p1, w0, w1, steps=24):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_men_envelope(D):
    """Draw 门 envelope: 点 + left 竖 + top-right 横折钩. Full-canvas scale."""
    # 1) top-left 点
    draw_dian(D, ox=-58, oy=68, scale=0.60)
    # 2) left 竖: top(80,110) -> bot(76,258)
    top = (80, 110); bot = (76, 258)
    _tapered_line(D, top, bot, w0=9, w1=10, steps=32)
    D.ellipse([top[0]-4, top[1]-4, top[0]+4, top[1]+4], fill=(0, 0, 0))
    D.ellipse([bot[0]-5, bot[1]-5, bot[0]+5, bot[1]+5], fill=(0, 0, 0))
    # 3) 横折钩: top horizontal + right vertical + hook
    h_left = (110, 75); h_right = (230, 72)
    _tapered_line(D, h_left, h_right, w0=9, w1=11, steps=24)
    D.ellipse([h_right[0]-6, h_right[1]-6, h_right[0]+6, h_right[1]+6], fill=(0, 0, 0))
    v_top = (230, 72); v_bot = (228, 250)
    _tapered_line(D, v_top, v_bot, w0=11, w1=10, steps=32)
    D.ellipse([v_bot[0]-6, v_bot[1]-6, v_bot[0]+6, v_bot[1]+6], fill=(0, 0, 0))
    hook_end = (v_bot[0] - 26, v_bot[1] - 20)
    _tapered_line(D, (v_bot[0]+1, v_bot[1]+2), hook_end, w0=10, w1=2, steps=16)


def draw_inner_kou(D, cx, cy, half_w, half_h):
    """口 inside the 门, drawn inline as 3 strokes:
       left 竖 | top-right 横折 | bottom 横.
       Bounding: [cx-half_w, cx+half_w] × [cy-half_h, cy+half_h]."""
    x_l = cx - half_w; x_r = cx + half_w
    y_t = cy - half_h; y_b = cy + half_h
    w = 5
    # left 竖
    _tapered_line(D, (x_l, y_t + 4), (x_l, y_b), w0=w, w1=w+1, steps=16)
    # top 横 (from just left of x_l to x_r+2)
    _tapered_line(D, (x_l - 1, y_t), (x_r, y_t), w0=w, w1=w+1, steps=16)
    # right 竖 (part of 横折)
    _tapered_line(D, (x_r, y_t), (x_r - 1, y_b), w0=w+1, w1=w, steps=16)
    # bottom 横
    _tapered_line(D, (x_l - 1, y_b), (x_r + 2, y_b), w0=w, w1=w+1, steps=16)


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_men_envelope(D)
    # 口 inside the 门 upper-interior. GT shows kou ~ x:130-195, y:145-215.
    draw_inner_kou(D, cx=163, cy=180, half_w=33, half_h=35)
    out = os.path.join(_HERE, "01_问.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
