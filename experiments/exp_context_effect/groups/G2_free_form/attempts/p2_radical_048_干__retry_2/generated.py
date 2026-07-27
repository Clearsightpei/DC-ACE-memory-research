"""
干 (radical p2_radical_048) — retry 2

Prior retry_1: proportions correct (top ~65% of bottom) but glyph sat
too high on canvas and 竖 did not protrude below the bottom 横 clearly.

Fix (from errata + form_catalog "竖 as through-going axis"):
- Top 横 centered around y ~ 95 (shorter, ~110 px)
- Bottom 横 around y ~ 165 (longer, ~180 px)
- 竖 starts ~10 px ABOVE top 横 (dab), passes THROUGH both, and extends
  ~40 px BELOW bottom 横 (matches GT which shows a clear protrusion)
- No hook on 竖.
- 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

# Center x of the whole glyph
CX = 150

# --- top 横 (shorter) ---
# Slight up-tilt (about 3°), small end dabs
top_y = 95
top_len = 108  # ~65% of bottom
top_x0 = CX - top_len // 2 - 4
top_x1 = CX + top_len // 2 - 4
# start dab
d.ellipse([top_x0 - 5, top_y - 5, top_x0 + 5, top_y + 5], fill=BLACK)
# line with slight up-tilt (right end higher)
d.line([(top_x0, top_y + 2), (top_x1, top_y - 3)], fill=BLACK, width=8)
# end dab
d.ellipse([top_x1 - 6, top_y - 8, top_x1 + 6, top_y + 2], fill=BLACK)

# --- bottom 横 (longer) ---
bot_y = 165
bot_len = 180
bot_x0 = CX - bot_len // 2
bot_x1 = CX + bot_len // 2
# start dab (left)
d.ellipse([bot_x0 - 6, bot_y - 6, bot_x0 + 6, bot_y + 6], fill=BLACK)
# main line, slight up-tilt
d.line([(bot_x0, bot_y + 3), (bot_x1, bot_y - 3)], fill=BLACK, width=9)
# end dab
d.ellipse([bot_x1 - 7, bot_y - 8, bot_x1 + 7, bot_y + 4], fill=BLACK)

# --- 竖 (through-going axis, no hook) ---
# Starts ~10 px above top 横, ends well below bottom 横 (~75 px)
shu_top = top_y - 12
shu_bot = bot_y + 80
shu_x = CX - 2  # slight left of center to feel natural
# top 顿 dab
d.ellipse([shu_x - 6, shu_top - 3, shu_x + 6, shu_top + 7], fill=BLACK)
# main vertical
d.line([(shu_x, shu_top), (shu_x, shu_bot)], fill=BLACK, width=9)
# small terminal press at bottom (blunt, no hook)
d.ellipse([shu_x - 5, shu_bot - 5, shu_x + 5, shu_bot + 5], fill=BLACK)

out_path = __file__.rsplit("/", 1)[0] + "/01_干.png"
img.save(out_path)
print(f"Saved: {out_path}")
