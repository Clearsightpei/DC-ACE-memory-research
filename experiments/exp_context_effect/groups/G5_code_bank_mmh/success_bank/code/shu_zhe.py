"""Bank primitive: 竖折 (shu-zhe — vertical then rightward horizontal, one stroke).

Extracted from p2_radical_063_山 s2 (PASS 2026-08-08, B1) via BANK_DEVIATION.
Signature: (head, corner, tail) — 3-point path with 顿笔 dab at corner.
Useful for the base of 山, 凵, 匚, 匸 (with orientation flip), and any
compound whose middle piece is a down-then-right L.
"""

from PIL import ImageDraw


def draw_shu_zhe(draw: ImageDraw.ImageDraw, head, corner, tail, width=7):
    """Draw 竖折 as a single continuous stroke: vertical head→corner, then
    horizontal corner→tail. Small 顿笔 dab at the corner; caps at endpoints.
    """
    hx, hy = head
    cx, cy = corner
    tx, ty = tail
    # vertical body
    draw.line([head, corner], fill='black', width=width)
    # small 顿笔 dab at the corner
    r = width / 2 + 1
    draw.ellipse([cx - r, cy - r, cx + r + 1, cy + r + 1], fill='black')
    # horizontal body
    draw.line([corner, tail], fill='black', width=width)
    # end caps
    rh = width / 2
    draw.ellipse([hx - rh + 1, hy - rh, hx + rh - 1, hy + rh], fill='black')
    rt = width / 2 + 1
    draw.ellipse([tx - rt, ty - rt, tx + rt, ty + rt], fill='black')
