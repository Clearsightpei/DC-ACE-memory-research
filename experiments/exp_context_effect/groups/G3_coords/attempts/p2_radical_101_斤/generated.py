"""
p2_radical_101_斤 (jīn, 4 strokes)

Stroke breakdown (from GT inspection):
  1. Short 撇 (pie) at upper-left: head high-mid-left, sweeps down-left, short.
  2. Short 横 (heng) at upper-right, near top: nearly horizontal, gentle rise.
  3. Long 撇 (pie): head starts near left-end of heng (touches top of vertical
     axis), curves down and sweeps far to bottom-left. This is the dominant
     stroke of 斤.
  4. 竖 (shu): straight vertical, starts at right end of heng, descends
     through mid-canvas down to bottom.

Applying TR8 (inline-fresh test): every stroke here has custom geometry
(the two 撇 have very different lengths/slopes; the 竖 is thin and
comparatively short; the 横 rises slightly and is short). Bank pie is too
diagonal (P10) and would fight both 撇 shapes. So: INLINE all four fresh
as tapered beziers with matched ink widths (~7-9 px), no primitive calls.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
CX, CY = W // 2, H // 2  # (150, 150)


def _to_pixel(x, y):
    """Math coords (center origin, +y up) -> PIL pixel."""
    return (CX + x, CY - y)


def _bezier(p0, p1, p2, steps=80):
    """Quadratic bezier -> list of (x, y) sample points in pixel space."""
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        out.append((x, y))
    return out


def _stamp_tapered(draw, points, w0, w1):
    """Stamp filled circles along `points` with width tapering w0 -> w1."""
    n = len(points)
    for i, (x, y) in enumerate(points):
        u = i / max(n - 1, 1)
        w = w0 + (w1 - w0) * u
        r = max(w / 2.0, 0.5)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=0)


def draw_jin(img):
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: SHORT 撇 (upper-left short tick) ----
    # In GT it's a small tick that meets the heng's left end. Head upper-right,
    # tail down-left, very short. Head thick (~8), taper to ~2.
    p0 = _to_pixel(-18, +72)   # head upper (slightly right of shaft top)
    p1 = _to_pixel(-30, +58)
    p2 = _to_pixel(-42, +42)   # tail down-left, meets heng's left end
    _stamp_tapered(d, _bezier(p0, p1, p2), w0=8, w1=2)

    # ---- Stroke 2: SHORT 横 (upper heng, roughly at pie-tail level) ----
    # Starts from where the short pie ended (weld). Slight upward tilt.
    # Uniform-ish width ~7.
    p0 = _to_pixel(-42, +42)
    p1 = _to_pixel(-8, +48)
    p2 = _to_pixel(+38, +52)
    _stamp_tapered(d, _bezier(p0, p1, p2), w0=7, w1=6)

    # ---- Stroke 3: LONG 撇 (dominant, sweeps down-left with tail curl) ----
    # Head starts at heng's left area (touches top of vertical shaft region).
    # Descends nearly straight-vertical then curls LEFT at the bottom (like 厂's
    # pie). Head thick (~9), tail thin (~2). Control point CLOSE to chord
    # midpoint but slightly left to induce the terminal curl.
    p0 = _to_pixel(-30, +48)   # head near heng-left/pie-tail region
    p1 = _to_pixel(-40, -30)   # belly control - mostly vertical shaft
    p2 = _to_pixel(-90, -95)   # tail bottom-left with leftward curl
    _stamp_tapered(d, _bezier(p0, p1, p2), w0=9, w1=2)

    # ---- Stroke 4: 竖 (shu, vertical descender from right end of heng) ----
    # Starts at right end of heng (+38, +52) descends straight down to bottom.
    # Uniform width ~7.
    p0 = _to_pixel(+38, +45)
    p1 = _to_pixel(+38, -20)
    p2 = _to_pixel(+38, -95)
    _stamp_tapered(d, _bezier(p0, p1, p2), w0=7, w1=6)


def main():
    img = Image.new("L", (W, H), color=255)
    draw_jin(img)
    out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_101_斤/01_斤.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
