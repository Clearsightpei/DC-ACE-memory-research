from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 5  # stroke thickness

def line(p1, p2, w=TH):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(pts, w=TH):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# 带 has these components (top to bottom):
# 1) Three short vertical strokes at top
# 2) Long horizontal across the top
# 3) 冖-like cover with tick on left and hook on right
# 4) Two small verticals inside the cover
# 5) 巾 at the bottom (small horizontal + box + long central vertical)

# --- Top three verticals ---
line((110, 55), (110, 95))
line((150, 55), (150, 95))
line((190, 55), (190, 95))

# --- Long top horizontal ---
line((55, 100), (250, 95), w=6)

# --- Second horizontal (middle band, forming top of 冖) with left tick and right hook ---
# Left small tick going down-left
line((78, 130), (65, 145))
# Main horizontal cover
poly([(78, 130), (240, 132), (245, 155)], w=6)
# Right hook - already appended

# --- Two small marks inside upper region (between the two horizontals) ---
# Small angled strokes
line((120, 108), (128, 128))
line((175, 108), (185, 128))

# --- Middle horizontal (top of 巾) ---
line((95, 175), (225, 175), w=6)

# --- 巾 box (left vertical, right vertical with hook) ---
# Left vertical (short, of the mouth part)
line((110, 175), (110, 235))
# Bottom of mouth
line((110, 235), (180, 235))
# Right vertical of mouth with small hook
poly([(180, 175), (180, 235), (170, 240)], w=5)

# --- Long central vertical (through the 巾, extending down) ---
line((150, 130), (150, 285), w=6)

img.save(os.path.join(os.path.dirname(__file__), "01_带.png"))
print("saved")
