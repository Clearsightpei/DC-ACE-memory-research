# si.py — 巳 (sì), 3 strokes (横折 + 横 + 竖弯钩).
# Batch B2 (position 104) — human PASSed.
# Fully inline-fresh (TR8) — 巳 shape close to 己 which failed via
# force-fit. PIL-pixel coords (not math coords) for direct GT match.

INK = (0, 0, 0)


def _tapered_line(draw, p0, p1, w0, w1, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def _dot_blob(draw, cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=INK)


def draw_si(t, ox=0.0, oy=0.0, scale=1.0):
    """巳 radical (PIL pixel coords). ox/oy/scale for API parity only."""
    _tapered_line(t, (70, 85), (200, 85), 9, 12)
    _dot_blob(t, 200, 87, 7)
    _tapered_line(t, (200, 87), (200, 130), 12, 10)
    _tapered_bezier(t, (95, 130), (145, 128), (200, 130), 9, 11)
    _tapered_line(t, (70, 85), (70, 210), 11, 12)
    _tapered_bezier(t, (70, 210), (95, 228), (180, 220), 12, 11)
    _tapered_line(t, (180, 220), (215, 217), 11, 9)
    _dot_blob(t, 215, 217, 6)
    _tapered_line(t, (215, 217), (208, 197), 9, 2)
