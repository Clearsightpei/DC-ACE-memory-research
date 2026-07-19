"""p1_stroke_18_撇折 — Drawer attempt (G4 grid-bank).

撇折 (piězhé): a compound stroke — a 撇 (diagonal sweep from upper
region down-left, tapered head-to-tip) that at its bottom pivots
sharply to a 横 (short horizontal segment traveling right). Common
in 幺, 么, 公, 纟 (silk radical top), 女 (in some analyses shares
this shape logic). The turn is a hard 折 (90°-ish elbow), NOT a
curved arc, and the 横 segment has uniform width (no needle taper —
that would make it a 撇提 instead).

Distinct from neighbors:
  - 撇点  (p1_stroke_17): 撇 → 点 (down-RIGHT press that broadens)
  - 撇折  (this):         撇 → 横 (right, roughly HORIZONTAL, uniform)
  - 横撇  (p1_stroke_09): 横 first, then 撇 sweep (order reversed)

米字格 anchor plan (PIL-native: y grows DOWN within each cell,
matching p1_stroke_17_撇点 convention):
  Segment 1 (撇 part — thick TR head → thin pivot):
    head  @ ('TR', 0.30, 0.25)  — 起笔 upper-right region, biased left
    pivot @ ('BL', 0.55, 0.65)  — pivot low-left, the 折 elbow
  Segment 2 (横 part — uniform-width, rightward):
    tail  @ ('BC', 0.80, 0.65)  — travels right across the bottom row

Joint spec: single compound stroke, one internal welded pivot.
  seg1.tail @ BL (0.55, 0.65)  ⇆  seg2.head @ BL (0.55, 0.65)
  Class: P (piercing / welded, corner-cell rule).

Width profile:
  - 撇 segment: 起笔 ~13 px at TR head, tapers to ~5 px at the pivot.
  - Pivot 顿笔: small reinforcement disc (~7 px) at the elbow so the
    joint reads as welded, and to give the corner a slight kaishu
    press-bump.
  - 横 segment: uniform ~7 px (slightly thicker than the pivot
    reinforcement's outer edge so the horizontal has body). No taper
    to a needle — 撇折's horizontal ends with a squared 收笔.

No writes to success_bank/code/.
"""
import os
from PIL import Image, ImageDraw


# --- 米字格 anchor → PIL pixel coord (300x300 canvas, 9 cells 100x100) ---
_CELL_COL = {'TL': 0, 'ML': 0, 'BL': 0,
             'TC': 1, 'C':  1, 'BC': 1,
             'TR': 2, 'MR': 2, 'BR': 2}
_CELL_ROW = {'TL': 0, 'TC': 0, 'TR': 0,
             'ML': 1, 'C':  1, 'MR': 1,
             'BL': 2, 'BC': 2, 'BR': 2}
_CELL = 100  # px per cell on the 300x300 canvas


def anchor_to_xy(a):
    """(cell, x_frac, y_frac) -> (px, py) with y growing downward."""
    cell, xf, yf = a
    col = _CELL_COL[cell]
    row = _CELL_ROW[cell]
    return (col + xf) * _CELL, (row + yf) * _CELL


def _quad_bezier(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
    return x, y


def _perp_unit(p0, p2):
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    return -dy / L, dx / L


def _tapered_bezier(draw, a_head, a_tail, head_w, tail_w,
                    curve=0.0, segments=40):
    """Paint a tapered stroke along a quad-Bezier from head to tail.
    curve>0 bows toward the perpendicular of the chord (screen-y down)."""
    p0 = anchor_to_xy(a_head)
    p2 = anchor_to_xy(a_tail)
    ux, uy = _perp_unit(p0, p2)
    mid = ((p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2)
    chord = ((p2[0] - p0[0]) ** 2 + (p2[1] - p0[1]) ** 2) ** 0.5
    off = curve * chord
    p1 = (mid[0] + ux * off, mid[1] + uy * off)

    prev = None
    prev_w = None
    for i in range(segments + 1):
        t = i / segments
        x, y = _quad_bezier(p0, p1, p2, t)
        w = head_w + (tail_w - head_w) * t
        r = max(0.5, w / 2)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))
        if prev is not None:
            lw = max(1, int(round((w + prev_w) / 2)))
            draw.line((prev[0], prev[1], x, y), fill=(0, 0, 0), width=lw)
        prev = (x, y)
        prev_w = w


def _fat_line(draw, p0, p1, width, color=(0, 0, 0)):
    """Uniform-width line with rounded caps."""
    draw.line([p0, p1], fill=color, width=width)
    r = width / 2.0
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # --- Segment 1: 撇 part (thick TR → thin at pivot BL) ---
    # Slight belly curve (concave toward upper-left) matches a natural
    # 撇 sweep. curve>0 with p0=TR,p2=BL bows down-right; we want the
    # belly to bow slightly down-right (convex toward lower-right), so
    # a small positive curve.
    head_pie = ('TR', 0.30, 0.25)
    pivot    = ('BL', 0.55, 0.65)
    _tapered_bezier(d, head_pie, pivot,
                    head_w=13, tail_w=5, curve=0.07, segments=48)

    # --- Segment 2: 横 part (uniform-width, rightward, squared end) ---
    tail_heng = ('BC', 0.80, 0.65)
    p_pivot = anchor_to_xy(pivot)
    p_tail = anchor_to_xy(tail_heng)
    _fat_line(d, p_pivot, p_tail, width=7)

    # --- 顿笔 reinforcement disc at the pivot (welded joint) ---
    px, py = p_pivot
    r = 4.0  # radius ~ half of the horizontal width, so joint reads clean
    d.ellipse((px - r, py - r, px + r, py + r), fill=(0, 0, 0))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_撇折.png")
    img.save(out)
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"wrote {out} size={img.size}")


if __name__ == "__main__":
    main()
