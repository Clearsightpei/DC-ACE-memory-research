# p2_radical_031_十 — G3 coord-bank drawer attempt
# Target: 十 radical (2画): 横 crossing 竖.
#
# TR4 (十 crossing): both heng and shu cross at canvas center. Pass the
# SAME (ox, oy) so they share the joint pixel.
# GT observation: crossing sits slightly above center (竖 extends more
# below than above); 横 spans ~70% width; 竖 spans ~85% height.
# Chosen transform:
#   - shared crossing point: (ox=0, oy=+10) in math coords (a bit above center)
#   - 横: scale = 0.75 -> length 150 px (fits ~60% width, matches GT)
#   - 竖: scale = 0.90 -> length 180 px (longer arm below center)
#     shu is centered at oy=+10 so tail lands at oy=+10-90=-80 (well below),
#     top at oy=+10+90=+100 (well above). Symmetric arms from crossing not
#     required — GT already asymmetric with more length below.
# Actually 竖 primitive draws symmetric arms around its (ox,oy). For asymmetry
# we shift the whole shu DOWN so crossing is above its midpoint.
#   crossing goal in math coords: (0, +10)
#   shu default draws centered on its oy. Want top at oy=+90, bottom at oy=-95.
#   -> center of shu at oy=(-95+90)/2 = -2.5, half-length = 92.5 -> scale ~0.925
#   For crossing to be at oy=+10, but shu center at oy=-2.5 -- crossing above center.
#   Set shu ox=0, oy=-2.5, scale=0.925.
#   heng: at oy=+10, scale=0.75.

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from heng import draw_heng
from shu import draw_shu

img = Image.new("RGB", (300, 300), (255, 255, 255))
t = ImageDraw.Draw(img)

# 横: at crossing y = +10 (slightly above center), narrower than standalone.
# default heng: length 200 px centered at (0,0). scale 0.75 -> length 150.
draw_heng(t, ox=0, oy=+10, scale=0.75)

# 竖: crossing at (0, +10). shu is symmetric around its (ox, oy). To make the
# lower arm longer than the upper arm, shift shu's center down.
# shu center at oy=-2.5, half_len = 100*0.925 = 92.5
#   -> top at oy = -2.5 + 92.5 = +90
#   -> bot at oy = -2.5 - 92.5 = -95
# Crossing at oy=+10 lies between top(+90) and bot(-95): upper arm 80, lower arm 105.
draw_shu(t, ox=0, oy=-2.5, scale=0.925)

img.save(os.path.join(HERE, "01_十.png"))
