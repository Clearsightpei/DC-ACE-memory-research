"""G1 attempt (revision): radical 廴 (2 strokes)
Looking at GT more carefully:
- Stroke 1: upper-left, looks like a smooth "3"-shape / 横折折 (top hook opening right,
  then curls back)
- Stroke 2: long 平捺 - starts from upper-left area near stroke 1 end, sweeps down-left
  (as 撇), then extends far right with slight upward tail (as 捺).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 5

def line(pts, width=TH):
    d.line(pts, fill=BLACK, width=width, joint="curve")

# ---- Stroke 1: the "3"-like upper hook ----
# Trace: top starts around (65, 85), curves right and down to (105, 100),
# curls back left to (75, 118), then curls right-down to (110, 138)
s1 = []
# First curl (top of "3"): p0=(60,90) p1=(115,80) p2=(105, 115)
for t in range(0, 21):
    u = t / 20.0
    x = (1-u)**2 * 60 + 2*(1-u)*u * 120 + u**2 * 100
    y = (1-u)**2 * 92 + 2*(1-u)*u * 88  + u**2 * 118
    s1.append((x, y))
# Middle curve back to left: p0=(100,118) p1=(60, 122) p2=(80, 138)
for t in range(1, 21):
    u = t / 20.0
    x = (1-u)**2 * 100 + 2*(1-u)*u * 60  + u**2 * 82
    y = (1-u)**2 * 118 + 2*(1-u)*u * 122 + u**2 * 138
    s1.append((x, y))
# Bottom curl right: p0=(82,138) p1=(105, 140) p2=(118, 150)
for t in range(1, 16):
    u = t / 15.0
    x = (1-u)**2 * 82  + 2*(1-u)*u * 108 + u**2 * 120
    y = (1-u)**2 * 138 + 2*(1-u)*u * 145 + u**2 * 152
    s1.append((x, y))

line(s1, width=TH)

# ---- Stroke 2: the long 平捺 (走之/廴 base) ----
# In GT: starts near top-middle (~110, 130), goes down-left to (~75, 215),
# then sweeps far right to (~275, 220) with slight lift
s2 = []
# Segment A: 撇 part - from (115, 125) down-left to (80, 220)
# Bezier: p0=(115,125), p1=(90, 175), p2=(80, 220)
for t in range(0, 26):
    u = t / 25.0
    x = (1-u)**2 * 115 + 2*(1-u)*u * 90  + u**2 * 80
    y = (1-u)**2 * 125 + 2*(1-u)*u * 175 + u**2 * 220
    s2.append((x, y))
# Segment B: 捺 sweep right - from (80, 220) through (180, 245) up to (280, 215)
# Bezier: p0=(80,220), p1=(180, 250), p2=(280, 215)
for t in range(1, 41):
    u = t / 40.0
    x = (1-u)**2 * 80  + 2*(1-u)*u * 180 + u**2 * 280
    y = (1-u)**2 * 220 + 2*(1-u)*u * 250 + u**2 * 215
    s2.append((x, y))

line(s2, width=TH+1)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_036_廴/01_廴.png"
img.save(out)
print("saved", out)
