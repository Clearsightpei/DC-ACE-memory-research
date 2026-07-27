# p2_radical_081_夂 (zhǐ) — 3 strokes.
# Retry #1. Prior attempt: top pie was ok, but body 撇/捺 didn't share an
# apex — the pie/na diverged and the heng-turn-pie for stroke 2 read as two
# separate strokes. Fresh approach: mirror the fu.py (父) X-crossing recipe
# but with a single top pie (no top dot), and treat the 横撇 (stroke 2) as a
# short heng cap that flows into the big 撇, sharing its start-pixel with the
# 捺's head (apex weld).
#
# GT reading: canvas ~300x300; top short pie sits near (150, 105) angled
# down-left; the main body is an inverted-V (V-shape apex near (150, 128))
# with a short horizontal bar just above the apex on the right — the 横撇's
# heng — followed by a big 撇 sweeping to lower-left (75, 245) and a big 捺
# sweeping to lower-right (245, 240).
#
# PIL coords (top-left origin, y grows DOWN).

import os
from PIL import Image, ImageDraw

CANVAS = 300


def _tb(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
        w_head=8, w_tail=1, belly_pos=1.0, w_belly=None, n=60):
    """Tapered quadratic bezier from (x0,y0) to (x1,y1), PIL pixel coords."""
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = max(1e-6, (dx * dx + dy * dy) ** 0.5)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    cx = mx + nx * ctrl_perp + ux * ctrl_along
    cy = my + ny * ctrl_perp + uy * ctrl_along
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def _tapered_line(draw, x0, y0, x1, y1, w_head=6, w_tail=6, n=24):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_zhi(t):
    """夂 — 3 strokes. Inline-fresh per errata fix idea (apex-weld like 父)."""

    # ---- Stroke 1: short 撇 at top (a small tick above the body). ----
    # Head upper-right around (158, 92), tail lower-left around (140, 118).
    _tb(t, 158, 92, 140, 118, ctrl_perp=-2, w_head=6, w_tail=1, n=30)

    # ---- Stroke 2: 横撇 (short heng that turns into the long left-arm 撇). ----
    # The heng runs from left of apex (110, 130) to the apex-right (180, 128).
    # Small "顿笔" turn at the right end, then the long 撇 dives down-left
    # from (180, 128) to (70, 250), bowing slightly leftward (perp -8).
    _tapered_line(t, 110, 130, 180, 128, w_head=5, w_tail=6, n=24)
    # small 顿笔 blob at the turn
    r = 5
    t.ellipse([180 - r, 128 - r, 180 + r, 128 + r], fill=(0, 0, 0))
    # Long 撇 from the turn down to lower-left. Head thick, needle tail.
    _tb(t, 180, 130, 72, 248, ctrl_perp=-8, w_head=9, w_tail=1, n=70)

    # ---- Stroke 3: 捺 sweeping from apex (near stroke-2 heng start) down-right.
    # Starts at (128, 132) — just below+left of the heng — thin head, belly
    # around 0.75 along, longer flatter foot ending at (262, 232).
    _tb(t, 128, 132, 262, 232, ctrl_perp=14, w_head=2, w_tail=4,
        belly_pos=0.78, w_belly=15, n=80)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_zhi(t)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_夂.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
