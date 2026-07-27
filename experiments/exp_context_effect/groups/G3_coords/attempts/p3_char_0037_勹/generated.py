# p3_char_0037_勹 (bao) — G3 attempt.
#
# Strategy (per sandbox lesson from p2_radical_010_勹 FAIL):
#   Draw the 横+折+钩 envelope as ONE continuous smooth bezier — NOT
#   as heng + shu with a sharp right angle. The roundedness of the
#   shoulder is exactly what makes 勹 read as 勹.
#
# Stroke 1: short 撇 starting up-left, descending to meet the top of
#           the envelope.
# Stroke 2: continuous envelope — horizontal top (short) → rounded
#           shoulder → descending shaft with slight leftward bow → tiny
#           up-left hook flick.
#
# Rendered fresh in PIL (300x300, white bg, black ink).

from PIL import Image, ImageDraw

CANVAS = 300
OUT = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0037_勹/01_勹.png"


def qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def cbez(p0, p1, p2, p3, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        b0 = (1 - u) ** 3
        b1 = 3 * (1 - u) ** 2 * u
        b2 = 3 * (1 - u) * u * u
        b3 = u ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def stroke_taper(draw, pts, w0, w1):
    n = len(pts)
    for i in range(n - 1):
        u = i / (n - 1)
        w = max(2, int(round(w0 + (w1 - w0) * u)))
        a = pts[i]
        b = pts[i + 1]
        draw.line([a, b], fill=(0, 0, 0), width=w)
        r = w / 2.0
        draw.ellipse([b[0] - r, b[1] - r, b[0] + r, b[1] + r], fill=(0, 0, 0))


def stroke_var(draw, pts, widths):
    """widths: list same length as pts (per-point width)."""
    n = len(pts)
    for i in range(n - 1):
        w = max(2, int(round(widths[i])))
        a = pts[i]
        b = pts[i + 1]
        draw.line([a, b], fill=(0, 0, 0), width=w)
        r = w / 2.0
        draw.ellipse([b[0] - r, b[1] - r, b[0] + r, b[1] + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Stroke 1: short 撇 (pie) at top-left. Placed above envelope's
    # top-left corner, descending down-left.
    # Head high-right at (95, 45), tail down-left at (60, 100).
    pie_pts = qbez((95, 45), (78, 65), (60, 100), 30)
    stroke_taper(d, pie_pts, w0=5, w1=3)

    # Stroke 2: envelope — horizontal top, rounded shoulder,
    # descending shaft with slight leftward bow, small hook at bottom.
    #
    # Segment A: horizontal top from (80, 100) → (215, 95).
    top_a = (80, 100)
    top_b = (215, 95)
    seg_a = qbez(top_a, (147, 100), top_b, 24)
    stroke_var(d, seg_a, [7] * len(seg_a))

    # Segment B: shoulder rounded turn (215, 95) → shaft top (230, 125).
    sh_start = top_b
    sh_end = (230, 125)
    seg_b = cbez(sh_start, (228, 95), (232, 110), sh_end, 18)
    stroke_var(d, seg_b, [7] * len(seg_b))

    # Segment C: descending shaft with slight leftward bow.
    # (230, 125) → (195, 255). Control points bow leftward.
    shaft_start = sh_end
    shaft_end = (195, 255)
    seg_c = cbez(shaft_start, (225, 175), (215, 225), shaft_end, 50)
    widths_c = [7 - 2 * (i / (len(seg_c) - 1)) for i in range(len(seg_c))]
    stroke_var(d, seg_c, widths_c)

    # Segment D: small up-left hook flick at bottom.
    # (195, 255) → (170, 240).
    hook_start = shaft_end
    hook_end = (168, 238)
    seg_d = qbez(hook_start, (183, 253), hook_end, 15)
    widths_d = [5 - 3 * (i / (len(seg_d) - 1)) for i in range(len(seg_d))]
    stroke_var(d, seg_d, widths_d)

    img.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
