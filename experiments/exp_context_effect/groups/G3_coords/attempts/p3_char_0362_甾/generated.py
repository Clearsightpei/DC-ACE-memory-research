# BANK_DEVIATION
# skipped: chuan.py  (chuan (川) recipe is straight verticals; 巛 top of
#          甾 has the distinctive curly scoop that failed for 巛 radical
#          alone — see errata.md p2_radical_042_巛.)
# reason: 巛 top requires curly-hook scoops per vertical, not the straight
#         shu-based verticals chuan.py provides. Inline three curly shapes.
# fresh_component: chuan_scoop_for_zai (three cursive curly scoops as
#                  the 巛 top of 甾)
#
# p3_char_0362_甾 — 巛 (top, three curly scoops) + 田 (bottom, box)
# G3: callable Python. Direct PIL rendering at 300x300.

import os
from PIL import Image, ImageDraw


def _stroke(draw, pts, w_start, w_end):
    """Draw a taper-varying polyline."""
    n = len(pts) - 1
    for i in range(n):
        u = i / max(1, n)
        w = max(2, int(round(w_start + (w_end - w_start) * u)))
        ax, ay = pts[i]
        bx, by = pts[i + 1]
        draw.line([(ax, ay), (bx, by)], fill=(0, 0, 0), width=w)
        r = w / 2.0
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def _bezier_curve(cx0, cy0, cx1, cy1, cx2, cy2, n=30):
    """Quadratic bezier sampled as polyline."""
    pts = []
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * cx0 + 2 * (1 - u) * u * cx1 + u ** 2 * cx2
        y = (1 - u) ** 2 * cy0 + 2 * (1 - u) * u * cy1 + u ** 2 * cy2
        pts.append((x, y))
    return pts


def _draw_scoop(draw, top_x, top_y, bot_x, bot_y, w=5):
    """A cursive 巛-scoop: a small pronounced curl/hook at the top
    (opens rightward), then a curved descent to the bottom-left with
    a slight tail. Matches the GT's three curly verticals."""
    # Pronounced top hook: mini loop, starts upper-right, curls left-down.
    # Bezier: from (top_x+8, top_y+2) around to (top_x-6, top_y+18)
    hook = _bezier_curve(top_x + 10, top_y + 2,
                         top_x + 4, top_y - 4,
                         top_x - 4, top_y + 4, n=15)
    _stroke(draw, hook, w, w)
    hook2 = _bezier_curve(top_x - 4, top_y + 4,
                          top_x - 10, top_y + 12,
                          top_x - 2, top_y + 20, n=15)
    _stroke(draw, hook2, w, w)
    # Main descending curve: bows to the right, ends with slight left tail
    pts = _bezier_curve(top_x - 2, top_y + 20,
                        top_x + 12, (top_y + bot_y) / 2 + 10,
                        bot_x, bot_y, n=30)
    _stroke(draw, pts, w, w - 1)


def draw_zai(t):
    # === Top 巛 : three curly scoops ===
    # Left scoop
    _draw_scoop(t, top_x=85, top_y=40, bot_x=75, bot_y=130, w=5)
    # Middle scoop (slightly shorter start)
    _draw_scoop(t, top_x=150, top_y=45, bot_x=145, bot_y=130, w=5)
    # Right scoop
    _draw_scoop(t, top_x=215, top_y=40, bot_x=210, bot_y=130, w=5)

    # === Bottom 田 (box with interior +) ===
    L, R = 70, 230
    T, B = 150, 270
    MX = (L + R) // 2
    MY = (T + B) // 2

    # 左竖 (left vertical)
    _stroke(t, [(L, T), (L, B)], 6, 6)
    # 横折 (top horizontal + right vertical)
    _stroke(t, [(L, T), (R, T)], 6, 6)
    _stroke(t, [(R, T), (R, B)], 6, 6)
    # 中竖 (middle vertical, thinner)
    _stroke(t, [(MX, T), (MX, B)], 4, 4)
    # 中横 (middle horizontal)
    _stroke(t, [(L, MY), (R, MY)], 4, 4)
    # 底横 (bottom close)
    _stroke(t, [(L, B), (R, B)], 6, 6)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_zai(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "01_甾.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
