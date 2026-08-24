"""
p3_char_0180_打 — hand-radical 扌 + 丁

Structure:
  Left: 扌 (raise-hand radical) — 3 strokes
    1. 短横 (short horizontal), slight upward tilt
    2. 长竖钩 (long vertical with hook flick up-left at bottom)
    3. 提 (rising stroke from lower-left to mid, crossing the 竖)
  Right: 丁 — 2 strokes
    4. 一 (horizontal top)
    5. 亅 (vertical hook, terminal flicks UP-and-LEFT ~ -105°)

TIER-0 hook rule (memory_index.md B): all 亅 hooks flick UP-LEFT.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
INK = 8  # brush width


def line(p0, p1, w=INK):
    d.line([p0, p1], fill=BLACK, width=w)
    # round the joints so the ink looks continuous
    r = w // 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ---- Left: 扌 (roughly x=40..130, y=105..265) ----

# 1. Short horizontal (短横), slight upward tilt
line((45, 145), (128, 132))

# 2. Long vertical with hook (长竖钩): starts just above the 短横,
#    ends at bottom with hook UP-and-LEFT
line((100, 118), (100, 255))
# hook flick: from (100,255) go up-and-left
line((100, 255), (82, 240))

# 3. 提 (rising stroke): from lower-left up through the vertical
line((48, 215), (128, 188))


# ---- Right: 丁 (roughly x=145..275, y=105..265) ----

# 4. 一 (horizontal top): long, slight upward tilt
line((145, 148), (275, 138))

# 5. 亅 (vertical hook): starts from middle of 一, goes down,
#    hook flicks UP-and-LEFT
line((208, 138), (208, 258))
line((208, 258), (188, 242))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0180_打/01_打.png")
