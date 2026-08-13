"""p3_char_0368_乖 — 8 strokes.

Structure (from GT decomposition):
  - Top: short 撇 (small diagonal at top)
  - Long 横 spanning the width just below the top
  - Long 竖 going down through the center to the bottom
  - Left half (~middle): short 撇 + two short 横s (二-like)
  - Right half (~middle): a 匕-shape (short 横 + 竖折 / ヒ shape) with hook

Bank note: no direct 乖 or 北 bank entry. 千-like top exists (qian_thousand.py)
but its composition differs (仟 has 亻 radical). Inline fresh render — the
symmetric side-branches around a central 竖 don't match any bank recipe.

Thin uniform strokes per P12 (MMH GTs are thin, not calligraphic).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 5  # thin uniform width, matches MMH GT style


def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)


def poly(pts, w=LW):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)


# --- Stroke 1: top short 撇 (small diagonal from upper-right down-left)
poly([(175, 45), (140, 68)])

# --- Stroke 2: long 横 (top horizontal spanning the width)
poly([(50, 82), (255, 78)])

# --- Stroke 3: long 竖 (vertical through center, from just below top 横 to bottom)
poly([(150, 55), (150, 285)])

# --- Left half: 撇 + 二 -----------------
# Stroke 4: short 撇 on left, from near the top 横 going down-left
poly([(110, 95), (70, 135)])

# Stroke 5: upper left 横
poly([(55, 145), (140, 148)])

# Stroke 6: lower left 横
poly([(60, 200), (140, 205)])

# --- Right half: 匕-shape -------------------------------
# Stroke 7: 横折竖弯钩 style — top 横, down curving, right hook
poly([(158, 118), (220, 115)])           # short 横 top
poly([(220, 115), (222, 205), (245, 220)])  # 竖 with slight bend + hook right

# Stroke 8: right side diagonal 撇 (upper right going into interior/down-left)
poly([(232, 130), (172, 205)])

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G3_coords/attempts/p3_char_0368_乖/01_乖.png"
)
