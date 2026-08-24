"""p2_radical_129_曰 — 曰 (yuē, 'to say'), 4 strokes.

曰 vs 日: same 4-stroke box+middle-heng structure, but 曰 is squatter
(wider than tall, aspect ~1.15:1) while 日 is tall (~1:1.7). Reuses the
`ri.py` inline-tall-rectangle template but with reshaped x/y bounds:
wider x-span, shorter y-span, centered on canvas mid.

Reference: form_catalog.md — 日 tall-rectangle recipe; box-aspect
lesson (never force kou for non-1:1). This is the same lesson applied
to a squat-rectangle case.
"""
from PIL import Image, ImageDraw


def draw_yue(t, ox=0, oy=0, scale=1.0):
    """曰 radical, 4 strokes — squat rectangle with middle 横."""
    # 曰 is squatter than 日. Canvas 300x300; center at 150.
    # Width ~140 (wider than 日's 115), height ~120 (shorter than 日's 200).
    x_left = 80 + ox
    x_right = 220 + ox
    y_top = 90 + oy
    y_bot = 210 + oy
    y_mid = 150 + oy  # roughly centered vertically
    w = max(1, int(round(11 * scale)))
    w_mid = max(1, int(round(9 * scale)))
    # Stroke 1: left 竖
    t.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top heng + right shu)
    t.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    t.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 横 (thinner; small right-side gap to break from wall)
    t.line([(x_left + 2, y_mid), (x_right - 5, y_mid)],
           fill=(0, 0, 0), width=w_mid)
    # Stroke 4: bottom 横
    t.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_yue(t)
    img.save(
        "<REPO_ROOT>/experiments/"
        "exp_context_effect/groups/G3_coords/attempts/"
        "p2_radical_129_曰/01_曰.png"
    )


if __name__ == "__main__":
    main()
