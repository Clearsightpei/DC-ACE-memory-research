"""
乔 (qiao) — 6 strokes: 丿, 一, 丿, 一, 丿, 亅
Layout:
  - Top 丿: long left-falling from upper-right to lower-left
  - 一 (top horizontal): under the top 丿, medium width
  - 丿 (short): small left-falling nested under the top 横 near center
  - 一 (second horizontal): wider than first, lower down
  - 丿 (lower left): long sweep going down-left
  - 亅 (vertical hook): from the right of the 2nd 横 straight down, flick UP-LEFT at bottom
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

# 1) top 丿 — from upper-right (~200,55) sweeping to lower-left (~70,155)
stroke([(200,55),(175,80),(140,110),(105,135),(70,158)], width=8)

# 2) top 一 — from left of 丿 to right, mid-upper
stroke([(95,110),(140,105),(190,102),(225,108)], width=8)

# 3) short 丿 under top 横 — small tick going down-left
stroke([(160,115),(148,140),(138,160)], width=7)

# 4) second 一 — wider horizontal, lower
stroke([(55,170),(120,165),(200,163),(250,168)], width=8)

# 5) lower-left 丿 — long sweep from mid to bottom-left
stroke([(130,175),(115,200),(95,230),(70,260)], width=8)

# 6) 亅 — vertical then hook UP-LEFT at bottom
stroke([(175,175),(172,210),(170,245),(168,265)], width=8)
# hook flick UP-LEFT
stroke([(168,265),(158,258),(148,250)], width=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0226_乔/01_乔.png")
