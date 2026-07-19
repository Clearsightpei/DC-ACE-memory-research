"""G1 render of 火 (radical, 4 strokes) at 300x300."""
import os
from PIL import Image, ImageDraw

W = H = 300
OUT = os.path.join(os.path.dirname(__file__), "01_火.png")


def stroke(draw, pts, widths):
    """Draw a variable-width stroke by chaining ellipses along a polyline.
    pts: list of (x, y) control points
    widths: list of widths at each point (linear interp between)
    """
    # densify with linear interpolation
    dense = []
    dense_w = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        steps = max(2, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5))
        for s in range(steps):
            t = s / steps
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
            dense_w.append(w0 + (w1 - w0) * t)
    dense.append(pts[-1])
    dense_w.append(widths[-1])
    for (x, y), w in zip(dense, dense_w):
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=0)


def main():
    img = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(img)

    # Stroke 3 (drawn first for layering): main 撇 — starts upper-center,
    # nearly vertical then curves down-left to lower-left.
    stroke(d,
           [(160, 55), (158, 100), (152, 145), (135, 195), (95, 245)],
           [5, 8, 9, 9, 3])

    # Stroke 1: left dot — short 点 stroke to the LEFT of the 撇's mid,
    # oriented down-left (小撇点).
    stroke(d, [(120, 120), (95, 145)], [4, 8])

    # Stroke 2: right dot — short 点 stroke to the RIGHT of the 撇's mid,
    # oriented down-right, hooking slightly (小撇点mirror).
    stroke(d, [(178, 130), (200, 148)], [4, 8])

    # Stroke 4: main 捺 — starts on/near the 撇 body around 1/3 down,
    # sweeps down-right to lower-right with thickening tail.
    stroke(d,
           [(150, 140), (170, 175), (200, 215), (235, 250)],
           [4, 7, 10, 13])

    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
