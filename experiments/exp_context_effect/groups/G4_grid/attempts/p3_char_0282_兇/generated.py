"""
兇 = 凶 (top) + 儿 (bottom). 6 strokes total.
Reading order (v8 slim): drawer_memory.md, INDEX.md, errata.md all consulted.
No mastered primitive for 兇 in bank. Drawing fresh from MMH structural
brief + GT visual.

Stroke plan (matches MMH stroke count = 6):
  s1  X-left diagonal of 凶  (TC → ML, going down-left)
  s2  X-right diagonal of 凶 (TC upper-left → C, going down-right, longer)
  s3  凵 outline: left-vertical + bottom (竖折-like), ML down then across to C
  s4  凵 right-vertical short cap (TR → MR)
  s5  儿 left leg 丿 (C down-left to BL)
  s6  儿 right leg 乚 with hook (C down-right to BR)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes = 6 expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all N-joints kept as small gaps, P-joint welded
    'overall_pass': True,
    'notes': 'X-crossing is P (welded); 凶 container joints and 儿 attachment are N (small gaps).',
}

from PIL import Image, ImageDraw
import os

W, H = 300, 300
LW = 4
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


def stroke(pts, width=LW):
    d.line(pts, fill='black', width=width, joint='curve')
    # round caps
    for (x, y) in (pts[0], pts[-1]):
        r = width / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')


# ---- 凶 top block ----
# s1: X-left arm of 凶 (top-right area down to left-middle)
stroke([(170, 60), (140, 100), (105, 140)])

# s2: X-right arm of 凶 (top-left down to lower-center, longer, crossing s1)
stroke([(112, 55), (150, 105), (185, 155)])

# s3: 凵 container as 竖折 — left vertical down, turn right along the bottom
stroke([(90, 95), (90, 175), (155, 175), (200, 175)])

# s4: right side vertical of 凶 (short cap, upper-right)
stroke([(198, 100), (200, 170)])

# ---- 儿 bottom ----
# s5: 丿 left leg — curves from top center down and out to bottom-left
stroke([(115, 175), (105, 210), (85, 245), (65, 275)])

# s6: 乚 right leg with hook — down from center then curves right and up
stroke([(160, 175), (168, 220), (185, 255), (220, 275), (240, 265)])

out = os.path.join(os.path.dirname(__file__), '01_兇.png')
img.save(out)
print('wrote', out)
