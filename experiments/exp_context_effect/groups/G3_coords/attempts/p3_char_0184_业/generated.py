# 业 — 5 strokes (thin GT: MMH ink)
# Order: left-pie, left-vert, right-dian, right-vert, bottom-heng
# Trust GT posture (v8): bank not required.
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
WID = 5

def line(p0, p1, w=WID):
    d.line([p0, p1], fill=INK, width=w)


def draw_ye(d):
    # Left vertical (nearly straight) — top ~ y=95, bottom ~ y=240
    line((115, 95), (120, 240))
    # Right vertical — a bit taller, top ~ y=75
    line((185, 75), (183, 240))
    # Left inner pie (between the verticals, going from upper-right to lower-left)
    line((150, 145), (132, 180))
    # Right inner dian (between the verticals, going from upper-left to lower-right)
    line((160, 145), (178, 180))
    # Bottom heng — spans across
    line((55, 253), (255, 250))


draw_ye(d)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0184_业/01_业.png"
img.save(out)
print("saved", out)
