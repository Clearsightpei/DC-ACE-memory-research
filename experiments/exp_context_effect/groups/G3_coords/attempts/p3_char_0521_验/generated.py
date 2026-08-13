# BANK_DEVIATION
# skipped: (no bank entry for 马 or 佥)
# reason: 马 radical and 佥 right-component both absent from bank; inline fresh
# fresh_component: ma_left_radical (3-stroke simplified 马), qian_right_composite (人-cap + heng + 从 bottom)

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
w_main = 5
w_thin = 4


def line(p1, p2, width=w_main):
    d.line([p1, p2], fill=INK, width=width)


def draw_ma_left():
    """Simplified 马 (3 strokes) in left column x ~ 25..130, y ~ 70..255.

    Stroke 1 (横折): short heng across the top-right, then shu down —
      forms the top-right corner of the small box (like フ).
    Stroke 2 (竖折折钩): the left-column of the box goes down from top,
      then heng across the middle, then shu down, then hook left.
    Stroke 3 (提): rising heng across the bottom.
    """
    # --- Stroke 1: 横折 (top-right corner) ---
    # heng from (55, 80) to (120, 80)
    line((55, 80), (120, 80), w_main)
    # shu down from (120, 80) to (120, 145)
    line((120, 80), (120, 145), w_main)

    # --- Stroke 2: 竖折折钩 ---
    # left shu from (55, 80) going down to (55, 145) — sharing top-left
    line((55, 80), (55, 145), w_main)
    # heng across at y=145 to close middle bar
    line((55, 145), (120, 145), w_main)
    # continues shu down from right side
    line((120, 145), (115, 220), w_main)
    # hook: swings left-up at the bottom
    line((115, 220), (75, 215), w_main)

    # --- Stroke 3: 提 (rising heng) across the bottom ---
    line((20, 255), (135, 240), w_main)


def draw_qian_right():
    """Right-side 佥 in x ~ 155..290, y ~ 60..270.
    Components:
      - 人 top cap (pie + na crossing near apex).
      - Horizontal 一 below the cap.
      - Small 从-like pattern at the bottom (two short pie+dian pairs).
    """
    apex_x, apex_y = 225, 60

    # Top 人: pie sweeping down-left, na sweeping down-right
    line((apex_x, apex_y), (168, 135), w_main)
    line((apex_x, apex_y), (285, 135), w_main)

    # 一 heng below the cap (spans full right column)
    line((162, 165), (285, 165), w_main)

    # 从 at bottom: left pair (pie + dian)
    line((198, 195), (175, 260), w_thin)   # left pie
    line((205, 205), (225, 260), w_thin)   # left dian/short-na

    # 从 at bottom: right pair (pie + dian)
    line((250, 195), (232, 260), w_thin)   # right pie
    line((255, 205), (278, 260), w_thin)   # right dian/short-na


draw_ma_left()
draw_qian_right()

img.save("01_验.png")
