"""
Draw 横折折折钩 (heng-zhe-zhe-zhe-gou) — a five-beat compound stroke.

Beat structure (as found in characters like 乃 / 及-family):
  1) 横       : short heng going right (slight up-tilt)
  2) 折 (1)   : shoulder-dab, then vertical drop (short)
  3) 折 (2)   : shoulder-dab, then heng going right (shorter still)
  4) 折 (3)   : shoulder-dab, then vertical drop (down)
  5) 钩       : hook flick up-and-left from the bottom endpoint

Rendering uses the PIL brush-dab technique from drawer_memory.md:
uniform-radius dabs along each segment, with a slightly-larger
顿-dab at every joint / shoulder. Hook tapers to a sharp tip.

Canvas: 300x300, white background, black ink, image coords (y grows DOWN).
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

R = 5              # uniform stroke radius
R_SHOULDER = R + 3 # 顿 shoulder dab

def dab(x, y, r=R):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def line_dabs(x0, y0, x1, y1, r0=R, r1=R, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

# ---- Geometry ----------------------------------------------------------
# Anchors chosen to fit comfortably in 300x300 with margins ~40 px.
# 横1: (60, 80) -> (200, 72)          slight up-tilt
# 竖1: (200, 72) -> (200, 130)        short vertical drop
# 横2: (200, 130) -> (110, 122)       goes LEFT-ish? No — 横折折折钩's
#     middle segments alternate: after the first 折 you go down; after
#     the second 折 you go horizontally again but this beat tends to be
#     shorter. Convention (see 及, 廷 etc.) has the second heng going
#     rightward as well, but very short. We'll do a short rightward heng.
# Corrected sequence:
#   横1: (55, 80)  -> (215, 73)
#   折1 shoulder at (215, 73); 竖1 drops to (215, 128)
#   折2 shoulder at (215, 128); 横2 goes RIGHTWARD but is very short:
#         actually the canonical form has the second 横 going *leftward*
#         (retrograde) — see the stroke in 乃 (nǎi): after the drop the
#         brush kicks back left, then drops again into the hook.
#   横2: (215, 128) -> (95, 140)   left-going, slight downward drift
#   折3 shoulder at (95, 140); 竖2 drops to (95, 235)
#   钩: flick up-and-left from (95, 235) to ~(55, 210)

P_H1_START = (55,  75)
P_H1_END   = (210, 68)

P_V1_START = P_H1_END
P_V1_END   = (208, 122)

P_H2_START = P_V1_END
P_H2_END   = (90,  138)     # retrograde leftward heng, slight down drift

P_V2_START = P_H2_END
P_V2_END   = (98,  240)

# hook flick
HOOK_LEN   = 40
HOOK_ANGLE_DEG = -145        # up-and-left from bottom endpoint
hx = P_V2_END[0] + HOOK_LEN * math.cos(math.radians(HOOK_ANGLE_DEG))
hy = P_V2_END[1] + HOOK_LEN * math.sin(math.radians(HOOK_ANGLE_DEG))

# ---- Draw --------------------------------------------------------------

# 顿笔 at very start of stroke
dab(*P_H1_START, r=R + 2)

# Beat 1: 横1 (slight ramp up in radius toward the shoulder)
line_dabs(P_H1_START[0], P_H1_START[1], P_H1_END[0], P_H1_END[1],
          r0=R, r1=R + 1)

# 折1 shoulder
dab(*P_H1_END, r=R_SHOULDER)

# Beat 2: 竖1
line_dabs(P_V1_START[0], P_V1_START[1], P_V1_END[0], P_V1_END[1],
          r0=R, r1=R + 1)

# 折2 shoulder
dab(*P_V1_END, r=R_SHOULDER)

# Beat 3: 横2 (retrograde leftward, holds ~ uniform)
line_dabs(P_H2_START[0], P_H2_START[1], P_H2_END[0], P_H2_END[1],
          r0=R, r1=R + 1)

# 折3 shoulder
dab(*P_H2_END, r=R_SHOULDER)

# Beat 4: 竖2 (long vertical drop into the hook)
line_dabs(P_V2_START[0], P_V2_START[1], P_V2_END[0], P_V2_END[1],
          r0=R, r1=R)

# Beat 5: 钩 flick up-and-left, tapers thick -> thin sharp tip
line_dabs(P_V2_END[0], P_V2_END[1], hx, hy,
          r0=R + 1, r1=1.2, steps=200)

# ---- Save --------------------------------------------------------------
out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_横折折折钩.png")
img.save(out_path)
print(f"Saved: {out_path}")
