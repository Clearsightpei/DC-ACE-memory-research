# 的 (de) — 8 strokes. Left: 白 (5) compressed. Right: 勺 (3): 撇 + 横折钩 + 点.
# BANK_DEVIATION
# skipped: bai_char.py
# reason: bank 白 body is 120px wide (95-215); need it compressed to ~80px on left half for 白+勺 L/R composition.
# fresh_component: bai_compressed_for_de
from PIL import Image, ImageDraw


def draw_de(canvas):
    """8-stroke 的 into a PIL ImageDraw canvas (300x300)."""
    # ---------- LEFT: 白 (compressed) ----------
    x_left = 42
    x_right = 122
    y_top = 92
    y_bot = 252
    y_mid = 172
    w = 9
    w_mid = 7

    # Stroke 1: top 撇 (short pie, tail lands at top-left of body)
    canvas.line([(88, 65), (x_left + 6, y_top + 2)], fill=(0, 0, 0), width=7)

    # Stroke 2: left 竖
    canvas.line([(x_left, y_top), (x_left + 2, y_bot)], fill=(0, 0, 0), width=w)

    # Stroke 3: 横折 (top 横 + right 竖)
    canvas.line([(x_left, y_top), (x_right, y_top + 3)], fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top + 3), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)

    # Stroke 4: middle 横 (with small gap to right)
    canvas.line([(x_left + 4, y_mid), (x_right - 6, y_mid)], fill=(0, 0, 0), width=w_mid)

    # Stroke 5: bottom 横 (closes body)
    canvas.line([(x_left + 2, y_bot), (x_right + 2, y_bot + 2)], fill=(0, 0, 0), width=w)

    # ---------- RIGHT: 勺 ----------
    # Envelope: top-left ~ (155, 75), top-right ~ (255, 78),
    # right vertical down to ~ (250, 250), hook curls left+up to ~ (200, 240).

    # Stroke 6: 撇 — starts near top-middle of the 勺 area, curves down-left
    # Tail should touch/kiss the top-left corner of the envelope.
    # Head near (200, 45), tail near (157, 82).
    # Use a small polyline for gentle curve.
    canvas.line([(195, 60), (180, 70), (168, 78), (158, 82)],
                fill=(0, 0, 0), width=8)

    # Stroke 7: 横折钩 (envelope with hook)
    # Top 横: (155, 80) -> (255, 82)
    canvas.line([(155, 80), (255, 82)], fill=(0, 0, 0), width=w)
    # Right 竖: (255, 82) -> (250, 245)   (minimal lean)
    canvas.line([(255, 82), (250, 245)], fill=(0, 0, 0), width=w)
    # Hook: curl left+up from (245, 245) to (210, 232)
    canvas.line([(250, 245), (235, 246), (220, 240), (210, 230)],
                fill=(0, 0, 0), width=w)

    # Stroke 8: 点 inside the envelope (small dot, lower-middle-left of envelope interior)
    # Draw as a short thick line for calligraphic dot
    canvas.line([(188, 158), (205, 175)], fill=(0, 0, 0), width=10)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_de(d)
    img.save("01_的.png")
    print("saved 01_的.png")
