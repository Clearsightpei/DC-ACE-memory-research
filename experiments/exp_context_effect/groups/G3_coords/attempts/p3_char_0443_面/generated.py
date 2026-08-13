# BANK_DEVIATION
# skipped: you_frame_up.py / bai_char.py
# reason: 面 has a top 一 that spans wider than the frame plus a leftward-descending 丿 through the top; neither bank frame recipe captures that top+pie geometry, and the inner element is 目-like (two horizontals + short vert), not a single central shu.
# fresh_component: mian_frame_with_top_heng_and_pie
#
# 面 (miàn) — 9 strokes.
# Composition: top 一 spanning wide + 丿 descending from near left of top heng,
# then a large rectangular frame (left 竖 + 横折 + bottom 横) enclosing a
# 目-like inner block (short left 竖 + two short 横).

from PIL import Image, ImageDraw


def draw_mian(canvas):
    # Top 一 — long, spans across
    canvas.line([(45, 55), (250, 58)], fill=(0, 0, 0), width=8)

    # 丿 — starts near top heng (a bit right of frame's left edge), descends down-left
    canvas.line([(95, 50), (35, 275)], fill=(0, 0, 0), width=8)

    # Frame — left 竖
    x_left, x_right = 78, 245
    y_top, y_bot = 90, 265
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=8)

    # Frame — 横折 (top heng of frame + right 竖)
    canvas.line([(x_left - 3, y_top), (x_right, y_top)], fill=(0, 0, 0), width=8)
    canvas.line([(x_right, y_top), (x_right + 2, y_bot)], fill=(0, 0, 0), width=8)

    # Frame — bottom 横 (closes)
    canvas.line([(x_left - 2, y_bot), (x_right + 3, y_bot + 2)], fill=(0, 0, 0), width=8)

    # Inner block (目-like but compact): short left 竖 + upper 横 + lower 横
    # Positioned in the upper-middle region of the frame, NOT reaching bottom.
    ix_left, ix_right = 128, 205
    iy_top, iy_bot = 140, 215
    iy_mid = (iy_top + iy_bot) // 2
    # short left vertical of inner block
    canvas.line([(ix_left, iy_top), (ix_left, iy_bot)], fill=(0, 0, 0), width=5)
    # upper inner heng
    canvas.line([(ix_left, iy_top), (ix_right, iy_top)], fill=(0, 0, 0), width=5)
    # lower inner heng
    canvas.line([(ix_left + 2, iy_bot), (ix_right - 3, iy_bot)], fill=(0, 0, 0), width=5)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_mian(d)
    img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0443_面/01_面.png")
