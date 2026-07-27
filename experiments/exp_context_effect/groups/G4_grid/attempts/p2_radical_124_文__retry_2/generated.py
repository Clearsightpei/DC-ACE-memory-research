"""p2_radical_124_文 — retry_2.

Fix per errata (retry_n=2): define APEX = ('BC', 0.50, 0.30) and pass
IDENTICAL tuple to both pie head and na head so the X-cross shares
pixels (no fragmentation).

Strokes (4):
  1. dot 点   (top)
  2. heng 一  (upper middle)
  3. pie 撇   (from APEX down-left)
  4. na 捺    (from APEX down-right)
"""
import os
import sys
from PIL import Image, ImageDraw

CODE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(CODE_DIR))

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


# --- shared apex tuple (the fix) -----------------------------------
# APEX sits just below the 一; both pie and na start from this IDENTICAL
# tuple so their heads share pixels at the X-cross (retry_n=2 fix).
APEX = ('C', 0.50, 0.55)


def draw_dot(draw, anchor, size=14):
    x, y = anchor_to_xy(anchor)
    # small teardrop-like dot: short slanted fat line
    dx, dy = 10, 10
    p0 = (x - dx * 0.4, y - dy * 0.4)
    p1 = (x + dx * 0.6, y + dy * 0.6)
    fat_line(draw, p0, p1, width=8)


def draw_heng(draw, from_anchor, to_anchor, width=8):
    p0 = anchor_to_xy(from_anchor)
    p1 = anchor_to_xy(to_anchor)
    fat_line(draw, p0, p1, width=width)


def draw_pie_from_apex(draw, apex_anchor, tail_anchor,
                       head_width=10, tail_width=1, curve=0.10, segments=48):
    p0 = anchor_to_xy(apex_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_na_from_apex(draw, apex_anchor, tail_anchor,
                      head_width=4, mid_width=10, tail_width=2, curve=-0.08,
                      segments=48):
    """na (捺) — thin head at apex, swells mid, tapers at tail."""
    p0 = anchor_to_xy(apex_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = []
    for i in range(segments + 1):
        t = i / segments
        # swell to mid_width at t≈0.7, then taper
        if t < 0.7:
            w = head_width + (mid_width - head_width) * (t / 0.7)
        else:
            w = mid_width + (tail_width - mid_width) * ((t - 0.7) / 0.3)
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 1. dot: top center, slightly right of center
    draw_dot(draw, ('TC', 0.55, 0.55))

    # 2. heng: upper middle across ML→MR
    draw_heng(draw, ('ML', 0.35, 0.55), ('MR', 0.55, 0.55), width=7)

    # 3. pie: from APEX down-left to BL region
    draw_pie_from_apex(draw, APEX, ('BL', 0.30, 0.85), curve=0.08)

    # 4. na: from APEX down-right to BR region
    draw_na_from_apex(draw, APEX, ('BR', 0.75, 0.80), curve=-0.05)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_文.png")
    img.save(out)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
