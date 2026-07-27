# yi_pron.py — 以 (yǐ), 4 strokes: left 竖提 + 短点 + right 撇 + 点.
# PASSed at p3_char_0098_以 (B5, pos 258). Inline PIL bezier recipe;
# ox/oy/scale ignored — PIL-pixel recipe kept as-authored.

import math  # noqa: F401


def draw_yi_pron(t, ox=0, oy=0, scale=1.0):
    """以 — 4 strokes. NOTE: ox/oy/scale ignored (PIL-pixel recipe)."""
    CANVAS = 300
    CX = CY = CANVAS // 2

    def to_px(x, y):
        return (CX + x, CY - y)

    def bezier_stroke(p0, p1, p2, w_head, w_tail, n=40):
        prev = None
        for i in range(n + 1):
            u = i / n
            bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
            by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
            cur = (bx, by)
            w = w_head + (w_tail - w_head) * u
            wi = max(1, int(round(w)))
            if prev is not None:
                t.line([prev, cur], fill=(0, 0, 0), width=wi)
                r = w / 2.0
                t.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
            prev = cur

    # Stroke 1: 竖提 shu descending + hook.
    bezier_stroke(to_px(-70, 55), to_px(-78, -10), to_px(-70, -55),
                  w_head=6, w_tail=5, n=40)
    bezier_stroke(to_px(-70, -55), to_px(-55, -50), to_px(-30, -30),
                  w_head=5, w_tail=2, n=30)

    # Stroke 2: 短点
    bezier_stroke(to_px(-30, 40), to_px(-20, 32), to_px(-8, 20),
                  w_head=3, w_tail=8, n=25)

    # Stroke 3: 撇 (long right sweep down-left).
    bezier_stroke(to_px(45, 70), to_px(15, 0), to_px(-5, -75),
                  w_head=6, w_tail=2, n=50)

    # Stroke 4: 点 (heavy right dot).
    bezier_stroke(to_px(20, 15), to_px(45, -25), to_px(75, -70),
                  w_head=3, w_tail=8, n=40)
