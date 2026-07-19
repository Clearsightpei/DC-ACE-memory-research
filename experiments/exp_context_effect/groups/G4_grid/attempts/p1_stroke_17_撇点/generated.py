"""p1_stroke_17_撇点 — Drawer attempt (G4 grid-bank).

撇点 (piědiǎn): a compound stroke — a 撇 sweep from upper region
diagonally down-left, then a sharp turn at the bottom into a 点
(short diagonal press) heading down-right. Common in 女, 巡, 巛.

米字格 anchor plan (PIL-native: y grows DOWN within each cell):
  Segment 1 (撇 part):
    head @ ('TC', 0.75, 0.30)  — thick 起笔 in upper-center, biased right
    turn @ ('C',  0.30, 0.80)  — pivot in central cell, lower-left
  Segment 2 (点 part):
    tail @ ('BC', 0.60, 0.60)  — down-right press with a rounded 顿笔 foot

Joint spec:
  seg1.tail @ C  ⇆  seg2.head @ C   (welded — same pivot point,
                                     compound-stroke bend, corner-cell)

Single logical stroke composed of two tapered arcs sharing the pivot.
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
            # fat line between consecutive samples to avoid gaps
            lw = max(1, int(round((w + prev_w) / 2)))
            draw.line((prev[0], prev[1], x, y), fill=(0, 0, 0), width=lw)
        prev = (x, y)
        prev_w = w


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # --- Segment 1: 撇 part (thick head TC → thin at pivot in C) ---
    # Slight leftward-belly curve for the 撇 sweep.
    head_pie = ('TC', 0.75, 0.30)
    pivot    = ('C',  0.30, 0.80)
    _tapered_bezier(d, head_pie, pivot,
                    head_w=13, tail_w=4, curve=0.08, segments=44)

    # --- Segment 2: 点 part (thin at pivot → thick rounded foot BC) ---
    # The 点 broadens toward the tail (顿笔 press), then a small
    # rounded cap terminates it.
    tail_dian = ('BC', 0.60, 0.60)
    _tapered_bezier(d, pivot, tail_dian,
                    head_w=4, tail_w=11, curve=-0.06, segments=32)

    # Rounded 顿笔 cap at the tail of the 点.
    tx, ty = anchor_to_xy(tail_dian)
    cap_r = 6
    d.ellipse((tx - cap_r, ty - cap_r, tx + cap_r, ty + cap_r),
              fill=(0, 0, 0))

    # Reinforce the pivot so the two segments read as one welded joint.
    px, py = anchor_to_xy(pivot)
    d.ellipse((px - 3, py - 3, px + 3, py + 3), fill=(0, 0, 0))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_撇点.png")
    img.save(out)
    assert img.size == (300, 300), f"expected 300x300, got {img.size}"
    print(f"wrote {out} size={img.size}")


if __name__ == "__main__":
    main()
