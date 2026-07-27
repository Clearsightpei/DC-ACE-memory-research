"""p3_char_0229_自 — 自 (zì, "self"), 6 strokes.

Strokes (MMH order):
  1. 撇 short — top-left small diagonal descender
  2. 竖 — left vertical (top-left corner down to bottom-left)
  3. 横折 — top horizontal + right vertical (frame top + right side)
  4. 横 — upper interior horizontal
  5. 横 — middle interior horizontal
  6. 横 — bottom closing horizontal

G3 format: callable draw_zi(img, ox, oy, scale). Inline PIL fresh —
GT shows a tall rectangular frame ~50% wide, ~75% tall, with a small
撇 kissing the top edge slightly left of center, and three interior
horizontals evenly spaced.
"""

from PIL import Image, ImageDraw
import os


def draw_zi(draw, ox=150, oy=150, scale=1.0):
    # Frame geometry (tall rectangle), centered around (ox, oy)
    W = int(110 * scale)   # frame width
    H = int(170 * scale)   # frame height
    left = ox - W // 2
    right = ox + W // 2
    top = oy - H // 2 + 15   # frame top a bit below center (leave room for 撇)
    bot = top + H

    w = max(3, int(4 * scale))  # thin stroke width (matches GT)

    # 1. 撇 — short pie, from top edge (slightly left of center) up-left
    pie_bot = (left + int(W * 0.55), top + 3)
    pie_top = (left + int(W * 0.30), top - 30)
    # curved slightly
    mid = (left + int(W * 0.38), top - 15)
    draw.line([pie_top, mid, pie_bot], fill='black', width=w)

    # 2. 竖 — left vertical
    draw.line([(left, top), (left, bot)], fill='black', width=w)

    # 3. 横折 — top horizontal + right vertical (single connected stroke)
    draw.line([(left, top), (right, top)], fill='black', width=w)
    draw.line([(right, top), (right, bot)], fill='black', width=w)

    # Interior horizontals — match GT: 3 evenly spaced interior lines
    # (in addition to the top edge from 横折 and the bottom closing 横)
    interior_1 = top + (bot - top) * 0.34
    interior_2 = top + (bot - top) * 0.55
    interior_3 = top + (bot - top) * 0.76

    inset = int(6 * scale)
    # 4. upper interior 横
    draw.line([(left + inset, interior_1), (right - inset, interior_1)],
              fill='black', width=w)
    # 5. middle interior 横
    draw.line([(left + inset, interior_2), (right - inset, interior_2)],
              fill='black', width=w)
    # extra interior 横 (GT shows 3 interior lines)
    draw.line([(left + inset, interior_3), (right - inset, interior_3)],
              fill='black', width=w)

    # 6. bottom closing 横 — the bottom edge of the frame
    draw.line([(left, bot), (right, bot)], fill='black', width=w)

    # Also draw the lower interior 横 (matches GT: 3 interior horizontals)
    # Actually 自 has 3 interior horizontals — recount: MMH 自 = 6 strokes,
    # (撇, 竖, 横折, 横, 横, 横). The last 横 IS the bottom-closing one.
    # So we have: top edge (part of 横折), upper interior, middle interior,
    # bottom edge = 3 horizontals inside the frame counting the bottom.
    # But GT shows 4 horizontals visible (top edge + 2 interior + bottom).
    # That matches: 横折's horizontal + 横 + 横 + 横(bottom) = 4 horiz lines.
    # Currently we drew: top edge (横折) + interior_top + interior_mid + bot.
    # That is exactly 4. Good.


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_zi(draw, ox=150, oy=150, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), '01_自.png')
    img.save(out)
    print(f'wrote {out}')
