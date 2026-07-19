"""
竖折撇 (shu-zhe-pie) — three-beat compound stroke.

Structure (per drawer_memory.md):
  1. 竖 (vertical): top → bottom, uniform width, small 顿 at start.
  2. 折 (shoulder): sharp ~90° corner at bottom of 竖 — one slightly-
     larger dab at the joint.
  3. 撇 (throw-away tail): from the shoulder, sweeps DOWN-and-LEFT with
     a gentle bow (quadratic Bezier), tapering thick→thin to a sharp tip.

Distinguish from 竖折 (which ends blunt horizontally right). Here the
secondary beat is a 撇, so after the shoulder the ink pushes down-left
(not right), tapering to a tip.

Canvas: 300×300, white background, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_line(x0, y0, x1, y1, r_start, r_end, n=400):
    """Straight segment via brush dabs, radius ramps r_start → r_end."""
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def stroke_bezier(p0, p1, p2, r_start, r_end, n=500):
    """Quadratic Bezier via brush dabs, radius ramps r_start → r_end."""
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --- 1) 竖 : vertical, top → bottom ---
# Start upper-center-left, drop straight down.  Uniform width r≈5, small
# ramp up toward the shoulder (per 折-family memory: "primary end radius
# ramps up slightly toward the corner").
v_x = 130
v_y0 = 55
v_y1 = 175  # shoulder point
dab(v_x, v_y0, 7)                      # 顿笔 at top
stroke_line(v_x, v_y0, v_x, v_y1, 5, 6)

# --- 2) 折 shoulder dab at joint ---
shoulder_x, shoulder_y = v_x, v_y1
dab(shoulder_x, shoulder_y, 8)         # slightly-larger 顿 dab (r+2..3)

# --- 3) short middle 横 running rightward before the 撇 launches ---
# In 竖折撇 the horizontal runs briefly right, then the 撇 flies down-
# left from its right end.  Keep it short so the 撇 has room to bow.
h_x1 = 190
h_y1 = shoulder_y - 2                  # slight up-tilt like standalone 横
stroke_line(shoulder_x, shoulder_y, h_x1, h_y1, 6, 6)
dab(h_x1, h_y1, 7)                     # small terminal press at 横 end

# --- 4) 撇 tail : from right-end of 横, sweeps down-and-left, bowed ---
# Bezier P0 = end-of-横, P2 = lower-left tip, control pulled toward the
# stroke's interior (below-right of the chord) to give the characteristic
# rightward bow.  Taper thick → sharp tip.
pie_p0 = (h_x1, h_y1)
pie_p2 = (65, 260)
pie_ctrl = (175, 220)                  # ctrl pulled down-and-right of chord midpoint → gentle bow
stroke_bezier(pie_p0, pie_ctrl, pie_p2, r_start=7, r_end=1.2, n=500)

img.save("01_竖折撇.png")
print("wrote 01_竖折撇.png")
