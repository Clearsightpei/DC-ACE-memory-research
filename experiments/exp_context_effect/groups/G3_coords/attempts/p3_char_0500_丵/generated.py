# BANK_DEVIATION
# skipped: (no direct bank entry for 丵 or its top pattern)
# reason: 丵 is rare — no bank primitive for its cluster-of-shorts top;
#   the closest siblings (业, 業 top) are not in the bank. Render fresh
#   in PIL with thin uniform ink to match the GT's hand-drawn thin lines.
# fresh_component: zhuo_shrub_top (multi-short-stroke cluster) + shu-heng base

from PIL import Image, ImageDraw

W, H = 300, 300
INK = 4  # thin per P12

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=INK):
    d.line([p0, p1], fill="black", width=w)

# --- Top cluster of scattered short strokes (丵 signature: 丵 crown) ---
# Central pair (丷): two short strokes leaning outward at very top
line((138, 55), (130, 78))   # left pie (leaning down-left)
line((162, 55), (172, 78))   # right na (leaning down-right)

# Outer scattered shorts flanking the central pair, wider spread
line((95, 68), (108, 92))    # far-left na-ish (leans down-right)
line((122, 78), (115, 100))  # inner-left short pie
line((178, 78), (188, 100))  # inner-right short na
line((208, 68), (198, 92))   # far-right pie-ish (leans down-left)

# --- First long heng (upper horizontal) ---
line((60, 118), (240, 115), w=INK)

# --- Middle row of short verticals under heng (业-like) ---
line((92, 128), (90, 158))
line((125, 128), (123, 158))
line((175, 128), (177, 158))
line((208, 128), (210, 158))

# --- Second long heng (lower horizontal) ---
line((55, 175), (245, 172), w=INK)

# --- Long central shu descender ---
line((150, 175), (150, 275), w=INK)

# --- Small heng near lower portion of shu (半-like waist) ---
line((105, 235), (200, 233), w=INK)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0500_丵/01_丵.png")
