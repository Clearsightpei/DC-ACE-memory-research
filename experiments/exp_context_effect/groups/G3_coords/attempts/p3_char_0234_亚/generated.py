# 亚 (yà) — Phase 3 char 0234
# Structure from GT: 6-stroke symmetric block
#   1) top horizontal (medium width, upper)
#   2) left vertical (slight outward slant at bottom)
#   3) right vertical (slight outward slant at bottom)
#   4) middle-left short mark (小撇 / small diagonal)
#   5) middle-right short mark (小捺 / small diagonal)
#   6) bottom horizontal (widest, base)
#
# GT-first render — inline PIL, no bank primitive is a natural fit
# for this Roman-numeral-II-like envelope. Widths ~4-6px (MMH thin).
from PIL import Image, ImageDraw
from pathlib import Path

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def line(a, b, w):
    d.line([a, b], fill=INK, width=w)

# 1) top horizontal (extends slightly past verticals)
line((70, 90), (230, 88), 6)

# 2) left vertical (slight outward slant bottom-left)
line((95, 92), (75, 220), 5)

# 3) right vertical (slight outward slant bottom-right)
line((205, 92), (225, 220), 5)

# 4) middle-left small diagonal (short 撇-like — down-left)
line((115, 150), (95, 185), 5)

# 5) middle-right small diagonal (short 捺-like — down-right)
line((185, 150), (205, 185), 5)

# 6) bottom horizontal (widest, right below verticals)
line((40, 232), (260, 232), 6)

out = Path(__file__).parent / "01_亚.png"
img.save(out)
print(f"wrote {out}")
