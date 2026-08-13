"""p3_char_0263_她 — 女 (left) + 也 (right).

G3 rendering: callable Python functions, inline PIL. No bank primitive
exists for 女 or 也. 也 has repeatedly failed as scattered strokes;
per drawer_memory + errata, its envelope MUST read as one continuous
竖弯钩 shape with heng+shu inserted through it. Uniform thin ink
(W~4-5, per P12 MMH-thin). L/R split roughly 40/60.
"""

from PIL import Image, ImageDraw

W_THIN = 4  # P12 MMH-thin uniform width


def _bezier_pts(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] \
            + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] \
            + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
        pts.append((x, y))
    return pts


def _stroke(draw, pts, w=W_THIN):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
    for x, y in pts:
        draw.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2),
                     fill=(0, 0, 0))


def draw_nu(draw, ox=0, oy=0):
    """女 — 3 strokes: 撇点, 撇, 横. Compact into y=80..245."""
    # Stroke 1: 撇点 (compound). Descending 撇 top-right→lower-left,
    # then short 点 kicking down-right.
    pie_pts = _bezier_pts(
        (ox + 70, oy + 85),
        (ox + 55, oy + 130),
        (ox + 40, oy + 170),
        (ox + 30, oy + 190),
    )
    _stroke(draw, pie_pts)
    dian_pts = _bezier_pts(
        (ox + 35, oy + 185),
        (ox + 55, oy + 200),
        (ox + 75, oy + 215),
        (ox + 90, oy + 225),
    )
    _stroke(draw, dian_pts)

    # Stroke 2: main 撇 — from upper-right, sweeping down-left.
    pie2 = _bezier_pts(
        (ox + 100, oy + 95),
        (ox + 85, oy + 155),
        (ox + 60, oy + 210),
        (ox + 30, oy + 245),
    )
    _stroke(draw, pie2)

    # Stroke 3: 横 — horizontal across the middle
    _stroke(draw, [(ox + 20, oy + 175), (ox + 130, oy + 175)])


def draw_ye(draw, ox=0, oy=0):
    """也 — inline envelope. Wider than tall, clear upward hook on right,
    single central 竖. Per errata: envelope reads as ONE continuous
    竖弯钩 shape, not 3 disconnected primitives."""
    # Stroke 1: small top 横 (short, sits high, off-center-left)
    _stroke(draw, [(ox + 10, oy + 130), (ox + 55, oy + 130)])

    # Stroke 2: 竖弯钩 envelope — single continuous flowing stroke.
    # Combined path: left descent -> bottom curve -> right ascent -> upward hook.
    env_main = _bezier_pts(
        (ox + 18, oy + 105),    # top-left start
        (ox + 15, oy + 210),    # descend
        (ox + 40, oy + 260),    # bottom curve
        (ox + 90, oy + 258),    # bottom middle
    )
    _stroke(draw, env_main)
    env_main2 = _bezier_pts(
        (ox + 90, oy + 258),
        (ox + 120, oy + 255),
        (ox + 128, oy + 240),
        (ox + 128, oy + 215),   # right ascent
    )
    _stroke(draw, env_main2)
    # Upward hook at end (the 钩)
    hook = _bezier_pts(
        (ox + 128, oy + 215),
        (ox + 128, oy + 195),
        (ox + 122, oy + 180),
        (ox + 115, oy + 170),
    )
    _stroke(draw, hook)

    # Stroke 3: interior 竖 — central vertical through the envelope
    _stroke(draw, [(ox + 65, oy + 115), (ox + 68, oy + 245)])


def draw_ta_she(out_path):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Left 女: origin roughly (0, 0) offset so component fits x=20..135
    draw_nu(draw, ox=0, oy=0)
    # Right 也: shift right so component sits at x=145..270
    draw_ye(draw, ox=145, oy=0)
    img.save(out_path)


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_她.png")
    draw_ta_she(out)
    print(f"wrote {out}")
