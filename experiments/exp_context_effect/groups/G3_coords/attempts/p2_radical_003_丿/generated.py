# p2_radical_003_丿 — G3 attempt
# Per P10: pie primitive is TOO diagonal for 丿 radical.
# 丿 has (a) shallower slope (nearly vertical top, gentle curve),
# (b) thicker head, (c) softer curl — reads as "gentle scoop".
# GT observation: starts near top-center (~x=145,y=75 PIL),
# nearly vertical for the first ~30%, then arcs down-left to end
# at lower-left (~x=90, y=245 PIL). Uniformly-tapered ink,
# thicker at top, needle tail at bottom.
#
# Inline recipe (NOT calling draw_pie — see TR5: primitive would need
# extreme reshape). Numeric quadratic bezier in math-coords.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_pie_radical(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw 丿 radical: gentle scoop, near-vertical head, softer curl than 撇.

    Math coords, +y up.
      REVISION 1: first pass was too diagonal (read as 撇, not 丿).
      Move head RIGHT (+15) so it's near canvas center-top; move tail
      slightly RIGHT (-35) so full stroke is more vertical. Push control
      point DOWN so the top ~40% stays nearly vertical, then curves.
      p0 (head, thick): (+15, +85)  — top, slightly right of center axis
      ctrl:             (+10, +5)   — nearly on-axis for vertical top run
      p1 (tail, thin):  (-45, -100) — bottom-left, further down than pie
    Head width 14 (thicker than pie's 10) tapering to 1.
    """
    x0, y0 = 15.0 * scale, 85.0 * scale
    x1, y1 = -45.0 * scale, -100.0 * scale
    # Control point: nearly on x0's axis => top of stroke stays vertical.
    # Then bends smoothly down-left toward the tail.
    mx = 10.0 * scale
    my = 5.0 * scale

    n_segments = 80
    w_head = max(1, 14.0 * scale)
    w_tail = 1.0

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        # Width profile: hold head width for first 15%, then taper.
        if u < 0.15:
            w = w_head
        else:
            u2 = (u - 0.15) / 0.85
            w = w_head + (w_tail - w_head) * u2
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_pie_radical(t, ox=0, oy=0, scale=1.0)
    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_003_丿/01_丿.png"
    img.save(out)


if __name__ == "__main__":
    main()
