# p3_char_0241_如 — 如 = 女 (left) + 口 (right)
# G3: callable Python functions. 女 inlined fresh (no bank entry);
# 口 approximated inline at right for a clean right-hand square.
from PIL import Image, ImageDraw

W = H = 300


def draw_line(d, p0, p1, w=4):
    d.line([p0, p1], fill="black", width=w)


def draw_curve(d, pts, w=4, steps=48):
    p0, c, p1 = pts
    prev = p0
    for i in range(1, steps + 1):
        u = i / steps
        x = (1 - u) * (1 - u) * p0[0] + 2 * (1 - u) * u * c[0] + u * u * p1[0]
        y = (1 - u) * (1 - u) * p0[1] + 2 * (1 - u) * u * c[1] + u * u * p1[1]
        d.line([prev, (x, y)], fill="black", width=w)
        prev = (x, y)


def draw_nu(d, cx=105, cy=160):
    """女 — 3 strokes: 撇点, long 撇, long 横 (crosses through both pies)."""
    # Stroke 1: 撇点 — starts from upper area, curves down-left, tip near heng level;
    # then a short dian rising to the right ending near mid.
    p1_start = (cx + 8, cy - 55)
    p1_ctrl = (cx - 5, cy - 20)
    p1_end = (cx - 35, cy + 12)
    draw_curve(d, [p1_start, p1_ctrl, p1_end], w=4)
    # dian: bounces from pie's tail up-right to about mid-right of the 女.
    draw_line(d, p1_end, (cx + 2, cy + 25), w=5)

    # Stroke 2: long 撇 — starts upper-right (above stroke 1 origin), sweeps down-left,
    # crossing stroke 1 near the top-third, and ending lower-left.
    p2_start = (cx + 38, cy - 60)
    p2_ctrl = (cx + 15, cy - 15)
    p2_end = (cx - 50, cy + 55)
    draw_curve(d, [p2_start, p2_ctrl, p2_end], w=4)

    # Stroke 3: long 横 — horizontal near center, slight upward tilt, crosses through
    # the pies' intersection region.
    draw_line(d, (cx - 55, cy + 2), (cx + 50, cy - 6), w=4)


def draw_kou_inline(d, cx=225, cy=170, half_w=35, half_h=32):
    """口 — 3-stroke square: shu (left), heng+zhe (top-right corner), heng (bottom)."""
    left = cx - half_w
    right = cx + half_w
    top = cy - half_h
    bot = cy + half_h
    # left 竖
    draw_line(d, (left, top), (left, bot), w=4)
    # top 横 + right 竖 (heng_zhe) — extend both slightly to close corners cleanly
    draw_line(d, (left - 1, top), (right + 1, top), w=4)
    draw_line(d, (right, top - 1), (right, bot + 1), w=4)
    # bottom 横
    draw_line(d, (left - 2, bot), (right + 2, bot), w=4)


def main():
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    draw_nu(d, cx=95, cy=160)
    draw_kou_inline(d, cx=220, cy=175, half_w=35, half_h=32)
    img.save("01_如.png")


if __name__ == "__main__":
    main()
