"""处 (chù/chǔ) — 5 strokes.
Structure: 夂-like top (短撇 + 横撇捺 envelope) + interior 竖 + 点.
Thin ink to match MMH GT style (P12). Inline fresh under v8.
"""
from PIL import Image, ImageDraw

W_STROKE = 5
IMG = 300

img = Image.new("RGB", (IMG, IMG), "white")
d = ImageDraw.Draw(img)


def _pts_from_bezier(p0, p1, p2, n=40):
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


def stroke_line(a, b, w=W_STROKE):
    d.line([a, b], fill="black", width=w)


def stroke_bezier(p0, p1, p2, w=W_STROKE):
    pts = _pts_from_bezier(p0, p1, p2)
    d.line(pts, fill="black", width=w)


def draw_chu(t=None, ox=0, oy=0, scale=1.0):
    # Stroke 1: 短撇 (short pie) at upper-left; tail lands ON the
    # start of the 横 (joint at ~ (95, 115)).
    stroke_bezier((125, 75), (108, 95), (93, 118))

    # Stroke 2: 横撇 — short horizontal from the pie's tail out to
    # right, then arcs down-left to the belly of the character.
    stroke_line((92, 115), (155, 112))
    stroke_bezier((155, 112), (140, 150), (95, 190))

    # Stroke 3: long 捺 (na) — the character's dominant sweep,
    # starting from the belly and sweeping out to lower-right,
    # tapering slightly at the tail.
    pts = _pts_from_bezier((95, 190), (170, 260), (275, 255), n=50)
    d.line(pts, fill="black", width=W_STROKE + 1)

    # Stroke 4: 竖 (shu) — the vertical inside/right, sitting
    # under the 横撇 opening.
    stroke_line((198, 90), (200, 215))

    # Stroke 5: 点 (dian) — a short down-right dot on the right of
    # the 竖, mid-height.
    stroke_bezier((215, 150), (225, 160), (240, 175))


draw_chu()

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0212_处/01_处.png"
img.save(out)
print("wrote", out)
