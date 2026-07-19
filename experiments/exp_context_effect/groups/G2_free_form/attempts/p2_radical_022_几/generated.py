"""
几 (jǐ) - 2 strokes radical.

Structure per GT:
- Stroke 1: 撇 (pie) — starts at the upper-left corner (SHARED joint with
  the 横's left endpoint) and curves gracefully down-left to a tapered tip.
- Stroke 2: 横折弯钩 (heng-zhe-wan-gou) — 横 tilts slightly up going right;
  折 shoulder; 竖 descends with a slight inward (leftward) lean; 弯 arc
  curves smoothly rightward at the bottom (no shoulder); small hook flicks
  up-and-left.

Revision fixes from pass 1:
- Share the top-left joint between 撇 start and 横 start (per memory
  principle: "adjacent strokes SHARE joints, no inset").
- Give 撇 a more pronounced curve and start it slightly right so its tip
  lands well left of center.
- 竖 leans slightly left in its middle for a natural bow.
- Reduced overall vertical range to match GT proportions.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=200):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=250):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# Shared top-left joint
JOINT_TL = (108, 100)

# ---------- Stroke 1: 撇 ----------
# Start AT the shared joint. Bow leftward, tip lands lower-left.
p0_pie = JOINT_TL
ctrl_pie = (85, 175)
p2_pie = (65, 250)
# subtle 顿 dab at start (standalone-scale)
dab(p0_pie[0], p0_pie[1], 7)
bezier_dabs(p0_pie, ctrl_pie, p2_pie, r0=7.0, r1=1.5, steps=320)


# ---------- Stroke 2: 横折弯钩 ----------
# Beat 1: 横 — starts at shared joint, tilts up slightly rightward.
heng_start = JOINT_TL
heng_end = (215, 88)
dab(heng_start[0], heng_start[1], 7)
line_dabs(heng_start, heng_end, r0=6.5, r1=6.2, steps=180)

# Shoulder dab at 折 corner
shoulder = heng_end
dab(shoulder[0], shoulder[1], 8)

# Beat 2: 竖 — bezier with slight leftward bow (belly on left / concave right).
# Descend from shoulder toward the point where the 弯 arc will begin.
shu_end_x = 205
shu_end_y = 205
shu_ctrl = (198, 150)  # pull left of chord midpoint for slight inward lean
bezier_dabs(shoulder, shu_ctrl, (shu_end_x, shu_end_y),
            r0=6.5, r1=6.0, steps=220)

# Beat 3: 弯 — tangent-continuous quarter arc into rightward horizontal.
# Uses the KEY PRIMITIVE from memory.
R = 28
x0, y0 = shu_end_x, shu_end_y
arc_end_x = x0 + R
arc_end_y = y0 + R
arc_steps = 80
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, 6.0)

# Beat 4: very short 横 rightward from arc endpoint (base of hook)
tail_end = (arc_end_x + 12, arc_end_y - 2)
line_dabs((arc_end_x, arc_end_y), tail_end, r0=6.0, r1=5.5, steps=60)

# ---------- Hook (钩) — small up-left flick ----------
hook_len = 24
hook_angle_deg = -120
rad = math.radians(hook_angle_deg)
hook_end = (tail_end[0] + hook_len * math.cos(rad),
            tail_end[1] + hook_len * math.sin(rad))
hook_ctrl = (tail_end[0] + 0.45 * hook_len * math.cos(rad) + 1,
             tail_end[1] + 0.45 * hook_len * math.sin(rad) + 2)
bezier_dabs(tail_end, hook_ctrl, hook_end, r0=5.5, r1=1.2, steps=120)


# Save
out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_022_几/01_几.png"
img.save(out_path)
print(f"Saved {out_path}")
