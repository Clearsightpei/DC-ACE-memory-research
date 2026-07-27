"""乓 (pāng) — ping-pong char. Revised once vs GT.

Structure per GT: 丘-style top (short pie, left shu, short upper heng,
mid heng) sitting above a long base heng, with a ㇏ sweeping down-right
from ~the right third of the base heng.

Inline fresh (P12 thin ink ~5px). Trust GT posture (v8).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 5

def poly(pts, w=TH):
    d.line(pts, fill=INK, width=w, joint="curve")

# 1. Top 丿 short pie: from (155, 45) sweeping down-left to (108, 100)
poly([(155, 45), (145, 60), (128, 78), (110, 100)], w=TH)

# 2. Left 竖 short shu: from (118, 90) down to (108, 165)
poly([(118, 90), (114, 125), (108, 165)], w=TH)

# 3. Upper short 一 (heng), slight downward: from (140, 88) to (215, 92)
poly([(140, 88), (180, 90), (215, 92)], w=TH)

# 4. Mid heng (short): from (105, 158) to (200, 152) — slight upward
poly([(105, 158), (155, 155), (200, 152)], w=TH)

# 5. Long base 一 (heng): from (35, 205) to (275, 210)
poly([(35, 205), (100, 207), (180, 209), (245, 210), (275, 210)], w=TH)

# 6. ㇏ na sweeping down-right: from ~(210, 208) to (245, 285)
poly([(210, 208), (220, 232), (232, 258), (245, 285)], w=TH)

out = os.path.join(os.path.dirname(__file__), "01_乓.png")
img.save(out)
print("wrote", out)
