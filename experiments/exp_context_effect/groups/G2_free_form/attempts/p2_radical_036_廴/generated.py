"""
p2_radical_036_廴  (yǐn, "long stride")  — 2画 radical

Composition (canonical, 2 strokes):
  1. 横折折撇 (heng-zhe-zhe-pie): a compact zigzag in the upper-left.
     Reads like a small "3": short 横 → shoulder → short down-slant →
     shoulder → short rightward 横 → long bowed 撇 down-left. Sits
     in the upper-left ~1/3 of the canvas.
  2. 捺 (na, press-down, "平捺" horizontal variant): a long sweeping
     press-down that starts at (or near) the tip of stroke 1's 撇,
     bows gently downward, then presses out to the RIGHT with a
     broad flat foot extending well past the right edge of stroke 1.
     This 平捺 is the visual signature of 廴 — it's the "stride."

Renderer: PIL brush-dabs, 300×300 white canvas, black ink.

Design notes (from drawer_memory.md + GT observation):
  - Two beats share a joint at the 撇 tip → 捺 start (small joining
    dab, no visible gap).
  - Standalone radical scale — hooks/curves must be pronounced; use
    small start-press (r=6-7), avoid balloon dots.
  - The 平捺's foot dominates the lower half of the canvas — its
    length is the identity signature.
"""

from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(30, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(P0, P1, P2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: 横折折撇 (compact zigzag in upper-left) ---------------
# Anchors (image coords, y grows DOWN):
#   A: top-left start of the first 横
#   B: end of first 横 (shoulder 1)
#   C: end of short down-slant (shoulder 2)
#   D: end of short rightward 横 — this is where the 撇 launches
#   E: tip of the 撇 (goes down-and-left; belly on lower-right)

A = (55, 65)
B = (140, 58)
C = (95, 115)
D = (175, 108)
E = (55, 220)  # 撇 tip — lower-left; this is the joint with stroke 2

r_body = 5.5

# 顿笔 press at start of stroke 1
dab(A[0], A[1], r_body + 2)

# Beat 1: short 横 (slight up-tilt), uniform radius
line_dabs(A[0], A[1], B[0], B[1], r_body, r_body)

# Shoulder 1 at B
dab(B[0], B[1], r_body + 2.5)

# Beat 2: short down-slant (going down-and-left slightly) B → C
line_dabs(B[0], B[1], C[0], C[1], r_body, r_body)

# Shoulder 2 at C
dab(C[0], C[1], r_body + 2.5)

# Beat 3: short rightward 横 (slight up-tilt) C → D
line_dabs(C[0], C[1], D[0], D[1], r_body, r_body)

# Shoulder / launch dab at D (where 撇 springs off)
dab(D[0], D[1], r_body + 2.5)

# Beat 4: long bowed 撇 from D down-and-left to E. Bezier with control
# pulled toward primary interior (upper-right side of the D→E chord) so
# the 撇 has a gentle rightward bow (belly on lower-right).
bez_ctrl_1 = (175, 175)  # pulled right-and-down of chord midpoint
bezier_dabs(D, bez_ctrl_1, E, r_body + 1.5, 1.4, steps=250)


# ---- Stroke 2: 平捺 (horizontal press-down) --------------------------
# Starts at joint E (the 撇 tip) with a small joining 顿-dab, sweeps
# down-and-right in a gentle concave-up bow, then presses out flat
# to the right with a broad terminal foot. This is the identity
# stroke of 廴.
#
# Path: E → gentle-bow midpoint → F (start of flat foot) → G (tip of
# broad terminal). Foot extends far to the right.

F = (210, 265)  # bottom of the bow, where the ramp-up-and-out begins
G = (290, 245)  # broad terminal — foot's tip, well to the right

# Joining dab at E (hides seam between 撇 tip and 捺 start) — kept small
# so it doesn't read as a balloon; the 撇 tip taper is already thin.
dab(E[0], E[1], r_body)

# Body of the 平捺 as a bezier from E to F, thin→thick (捺 gets
# progressively thicker toward the foot). Control point pulled DOWN
# and slightly LEFT of chord midpoint to give the belly a
# concave-up bow (the 捺 dips down before rising into the foot).
na_ctrl = (115, 285)  # below-and-left of E→F chord midpoint
bezier_dabs(E, na_ctrl, F, 3.0, 10.5, steps=260)

# Broad terminal foot F → G: this is the flat sweep-out. Ramps up
# slightly (foot rises), thick body then tapers to a rounded tip.
foot_ctrl = (255, 260)
bezier_dabs(F, foot_ctrl, G, 11.0, 2.5, steps=200)

# Small terminal press at G to give a rounded (not needle-sharp) tip
dab(G[0], G[1], 2.8)


# ---- Save ----------------------------------------------------------
out = (
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_036_廴/01_廴.png"
)
img.save(out)
print(f"wrote {out}")
