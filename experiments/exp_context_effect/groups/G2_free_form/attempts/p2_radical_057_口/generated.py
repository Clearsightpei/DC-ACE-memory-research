"""
Render 口 (kǒu) — 3-stroke radical, "mouth" square.

Three canonical strokes:
  1. 竖 (left vertical): top-left → bottom-left
  2. 横折 (top horizontal + right vertical, one compound stroke): shares
     the top-left corner with stroke 1 (adjacent, no inset), turns at
     the top-right corner with a shoulder 顿-dab, drops as 竖 to bottom-right.
  3. 横 (bottom horizontal): closes the box from bottom-left to bottom-right.

Following G2 memory principles:
- Adjacent strokes SHARE joints at corners (no inset) — top-left corner
  is shared by stroke 1 start and stroke 2 start.
- 横折 uses a shoulder 顿-dab at the top-right corner.
- The bottom 横 typically has a small gap / slight inset at bottom-right
  in traditional 楷书 rendering of 口 — the GT shows this subtle opening.
- Standalone radical: use moderate 顿-dabs (r+1 to r+2), not oversized.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        dx = x1 - x0
        dy = y1 - y0
        steps = max(50, int((dx * dx + dy * dy) ** 0.5) * 2)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- anchor points ---
# 口 is a rectangle roughly centered; slightly wider than tall in most
# calligraphy. Use a modestly-sized box centered on the canvas.
# GT shows the box occupying roughly the middle band, not full canvas.
TL = (80, 100)   # top-left
TR = (225, 95)   # top-right (slight upward tilt of top 横)
BL = (90, 240)   # bottom-left (竖 leans slightly inward at bottom -
                 # characteristic 口 shape: bottom slightly narrower than top)
BR = (215, 235)  # bottom-right

R = 5  # base stroke radius

# --- Stroke 1: 竖 (left vertical), TL → BL ---
# straight 竖 with 顿-dab at start (r+2)
dab(TL[0], TL[1], R + 2)  # 顿 press at top of 竖
line_dabs(TL[0], TL[1], BL[0], BL[1], R, R)
dab(BL[0], BL[1], R + 1)  # slight terminal press

# --- Stroke 2: 横折 (top + right vertical, single compound stroke) ---
# starts at top-left corner (SHARED with stroke 1's start), 横 rightward
# with slight up-tilt, shoulder 顿-dab at top-right corner, 竖 straight
# down to bottom-right. Blunt end (no hook — this is 横折, not 横折钩).

# top 横 leg: TL -> TR (tilts slightly up: TL.y=100, TR.y=95)
# 顿 press at start of 横 (shared with 竖's start — same corner)
dab(TL[0], TL[1], R + 2)  # reinforce the shared corner
line_dabs(TL[0], TL[1], TR[0], TR[1], R, R + 1)
# shoulder 顿-dab at top-right corner
dab(TR[0], TR[1], R + 3)
# right 竖 leg: TR -> BR (straight down)
line_dabs(TR[0], TR[1], BR[0], BR[1], R + 1, R)
dab(BR[0], BR[1], R + 1)  # slight terminal press (blunt end)

# --- Stroke 3: 横 (bottom horizontal), BL → BR ---
# closes the box. In traditional 口, the bottom 横 often leaves a tiny
# gap or slight inset at both ends — but for a clean radical rendering,
# start just inside the 竖's bottom endpoint and end just inside the
# right-vertical's bottom endpoint. Small 顿 dabs at both ends.
B_left = (BL[0] + 2, BL[1] - 2)   # tiny inset to hide seam cleanly
B_right = (BR[0] - 2, BR[1] + 2)
dab(B_left[0], B_left[1], R + 1)  # start 顿
line_dabs(B_left[0], B_left[1], B_right[0], B_right[1], R, R)
dab(B_right[0], B_right[1], R + 1)  # end 顿

out_path = __file__.rsplit("/", 1)[0] + "/01_口.png"
img.save(out_path)
print(f"saved {out_path}")
