"""
p2_radical_067_士 — retry #2

# SIGNATURE CHECK (per sibling_signature_checklist.md):
#   target = 士
#   bit    = TOP 横 LONGER than bottom (~1.5×)
#   wrong  = 土 (bottom longer)

Errata guidance (retry_1 FAILED because ratio was only ~140 vs ~120 —
still read as ambiguous). Push the ratio to ~1.6× per "move the knob
further" rule. Target: top ~180 px, bottom ~110 px. Vertical passes
through both. 3 strokes total: top 一 (long), central 丨 (through),
bottom 一 (short).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
WIDTH = 11

# Vertical centerline
cx = 150

# TOP 横 — LONG (~180 px). Slight upward tilt on right end for calligraphy feel.
top_y = 130
top_x1 = cx - 92   # 58
top_x2 = cx + 92   # 242
# Length = 184 px
d.line([(top_x1, top_y + 2), (cx, top_y), (top_x2, top_y - 2)], fill=INK, width=WIDTH)

# CENTRAL 竖 — through both 横. Starts a bit above top 横, ends just below bottom 横.
vert_top = 95
vert_bot = 215
d.line([(cx, vert_top), (cx, vert_bot)], fill=INK, width=WIDTH)

# BOTTOM 横 — SHORT (~110 px). Ratio: 184/110 ≈ 1.67× — exaggerated per fix note.
bot_y = 210
bot_x1 = cx - 55   # 95
bot_x2 = cx + 55   # 205
d.line([(bot_x1, bot_y + 2), (cx, bot_y), (bot_x2, bot_y - 2)], fill=INK, width=WIDTH)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_067_士__retry_2/01_士.png")
