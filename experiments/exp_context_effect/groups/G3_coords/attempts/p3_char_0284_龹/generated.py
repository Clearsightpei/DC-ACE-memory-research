"""p3_char_0284_龹 — inline fresh (no bank primitive fits)

GT decomposition (from visual inspection of gt/phase3/龹.png):
- Top: 丷-style pair — left slanted pie (from upper-right to lower-left,
  short), right mirrored dian (from upper-left to lower-right, short).
- Middle: two hengs with a central shu piercing them; the upper heng
  is shorter and narrower, the lower heng is wider.
- Bottom: 人 — a long 撇 sweeping down-left and a 捺 sweeping down-right
  from the lower heng's centre area.

Rendering: inline PIL with uniform thin ink (P12 / trust-GT posture).
The MMH GT uses thin near-uniform widths; no calligraphic taper here.
"""
from PIL import Image, ImageDraw

W = 300
H = 300
INK_W = 5  # thin, MMH-style

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def line(p, q, w=INK_W):
    d.line([p, q], fill="black", width=w)


def curve(points, w=INK_W):
    # smooth-ish polyline via many segments
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill="black", width=w)


def draw_long(t, ox=0, oy=0, scale=1.0):
    """龹 rendered by inline strokes; kept as a callable per G3 rule."""

    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    # --- top 丷 (mirror-dot pair) ---
    # left pie: from upper-right to lower-left, short
    line(P(120, 60), P(105, 95))
    # right dian: from upper-left to lower-right, short
    line(P(180, 60), P(195, 95))

    # central shu (the vertical mast; drawn first, caps under hengs)
    line(P(150, 90), P(150, 175))

    # upper heng (shorter, sits mid-height)
    line(P(110, 130), P(190, 130))

    # lower heng (wider, forms the crossbar for 人)
    line(P(75, 170), P(225, 170))

    # --- bottom 人 ---
    # long pie sweeping down-left from centre
    curve([
        P(150, 170),
        P(125, 200),
        P(100, 230),
        P(70, 265),
    ])
    # long na sweeping down-right from centre
    curve([
        P(150, 170),
        P(180, 205),
        P(210, 240),
        P(240, 275),
    ])


draw_long(None)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G3_coords/attempts/p3_char_0284_龹/01_龹.png"
)
