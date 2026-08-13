"""Bank primitive: 横折钩 (heng-zhe-gou — horizontal, corner, vertical, hook).

Extracted from p2_radical_025_力 s1 (PASS 2026-08-08, B1) via BANK_DEVIATION.
Signature: (heng_head, corner, gou_tail, hook_tip) — 4 anchors describing
the full 3-segment compound stroke. Used for 力/月/内/为 and other characters
whose right side is a full 横折钩.
"""

from PIL import ImageDraw


def draw_heng_zhe_gou(draw: ImageDraw.ImageDraw,
                      heng_head, corner, gou_tail, hook_tip):
    """Draw a compound 横折钩: horizontal (heng_head->corner),
    vertical/curved-vertical (corner->gou_tail), small upward hook flick
    (gou_tail->hook_tip). Chain-of-ellipses ink for natural corner weld.
    """
    # --- Segment A: 横 (slight upward arch, thin lead-in, swell to corner) ---
    steps_a = 60
    x0, y0 = heng_head
    x1, y1 = corner
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t - 2.0 * (1 - (2 * t - 1) ** 2)
        w = 3.5 + 2.2 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # --- Corner emphasis (小 顿笔 node at the turn) ---
    cx, cy = corner
    draw.ellipse((cx - 6.5, cy - 6.0, cx + 6.5, cy + 6.0), fill='black')

    # --- Segment B: 竖 (curves gently leftward as it descends) ---
    steps_b = 70
    x2, y2 = gou_tail
    ctrl_x = cx - 6
    ctrl_y = (cy + y2) / 2
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * cx + 2 * (1 - t) * t * ctrl_x + t ** 2 * x2
        by = (1 - t) ** 2 * cy + 2 * (1 - t) * t * ctrl_y + t ** 2 * y2
        w = 5.3 - 1.6 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # --- Segment C: 钩 (small upward-left hook flick, tapering to point) ---
    steps_c = 22
    hx, hy = hook_tip
    for i in range(steps_c):
        t = i / (steps_c - 1)
        bx = x2 + (hx - x2) * t
        by = y2 + (hy - y2) * t
        w = 4.0 * (1 - t) + 0.8
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
