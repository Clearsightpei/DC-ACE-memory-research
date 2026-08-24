# BANK_DEVIATION
# skipped: min_dish.py (module-level script, not callable — cannot slot into stacked composition)
# reason: 盅 stacks 中 (top) over 皿 (bottom); 皿 must sit in lower ~40% of canvas at compressed height
# fresh_component: min_bottom_for_zhong (inline 皿 sized for bottom-stack slot)
#
# 盅 (zhōng) — 中 stacked on 皿, 9 strokes. 中 occupies upper half,
# 皿 the lower ~40%. zhong.py bank primitive uses centered math coords;
# adapting via scale + oy shift would be fine, but for a clean top/bottom
# stacked composition it's simpler to render both fresh inline.
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6


def draw_zhong_top(d):
    """中 in upper half: kou box + central shu protruding above and below."""
    # kou box (slightly narrower than full width, upper region)
    left, right = 105, 200
    top, bot = 45, 115
    # left vertical
    d.line([(left, top), (left, bot)], fill=INK, width=LW)
    # top horizontal + right vertical (横折)
    d.line([(left, top), (right, top)], fill=INK, width=LW)
    d.line([(right, top), (right, bot)], fill=INK, width=LW)
    # bottom horizontal (closes box)
    d.line([(left, bot), (right, bot)], fill=INK, width=LW)
    # central shu (protrudes above top and below bottom)
    cx = (left + right) // 2
    d.line([(cx, 15), (cx, 165)], fill=INK, width=LW + 1)


def draw_min_bottom(d):
    """皿 in lower ~40%: 3 shus + top-right corner (横折) + long base heng.
    5 strokes; wide shallow basin, base extends beyond box."""
    # box region
    top = 185
    bot = 245
    left = 75
    right = 225
    # stroke 1: left vertical (slight inward slant)
    d.line([(left, top), (left + 6, bot)], fill=INK, width=LW)
    # stroke 2: first inner short vertical
    d.line([(125, top + 5), (127, bot)], fill=INK, width=LW)
    # stroke 3: second inner short vertical
    d.line([(175, top + 5), (175, bot)], fill=INK, width=LW)
    # stroke 4: 横折 top cap (short horizontal to right, then vertical down)
    d.line([(left + 6, top), (right, top)], fill=INK, width=LW)
    d.line([(right, top), (right - 6, bot)], fill=INK, width=LW)
    # stroke 5: long base heng (extends beyond box on both sides)
    d.line([(45, 262), (270, 260)], fill=INK, width=LW + 1)


draw_zhong_top(d)
draw_min_bottom(d)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0468_盅/01_盅.png")
print("saved")
