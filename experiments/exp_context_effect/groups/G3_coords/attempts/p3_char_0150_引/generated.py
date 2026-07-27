# p3_char_0150_引 — main attempt (G3, retry disabled per B5 evolution)
# 引 = 弓 (left, 3 strokes: 横折, 横折钩折(with bottom sweep), 竖折折钩)
#        + 丨 (right, tall vertical, MMH thin)
#
# GT observation: uniform thin lines (MMH style, P12 → thin widths).
# Left 弓 is compact top-left area; right 丨 spans nearly full canvas height.
# Silhouette:
#   - 弓 sits in x∈[~60, ~150], y∈[~80, ~240]
#   - 丨 vertical at x≈210, y∈[~55, ~275]
#
# No 弓 primitive in bank → inline PIL polylines for the three 弓 strokes.
# Use thin uniform width per P12 (MMH GT is thin ~4-5 px).

from PIL import Image, ImageDraw

CANVAS = 300
W = 4  # thin uniform stroke width per P12 (MMH GT style)


def draw_polyline(draw, pts, w=W):
    draw.line(pts, fill=(0, 0, 0), width=w)
    # round caps at each joint
    for x, y in pts:
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def draw_yin(img):
    d = ImageDraw.Draw(img)

    # --- 弓 (left side) ---
    # Stroke 1: 横折 — top horizontal then vertical down (upper cap of 弓)
    draw_polyline(d, [(70, 90), (155, 85), (148, 135)])

    # Stroke 2: 横 — the middle horizontal spanning from left to right vertical
    draw_polyline(d, [(75, 138), (150, 135)])

    # Stroke 3: 竖折折钩 — left vertical top, across, down-left sweep, right hook
    # Start at top-left of the lower loop, across right, then diagonal sweep
    # down and left, ending with a small hook that turns up-right.
    draw_polyline(d,
                  [(80, 140), (150, 140), (145, 180), (75, 250),
                   (130, 260), (128, 245)])

    # --- 丨 (right side) — tall vertical (slightly bowed left at top like GT)
    draw_polyline(d, [(215, 55), (213, 280)])


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw_yin(img)
    out = __file__.rsplit("/", 1)[0] + "/01_引.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
