"""
p1_stroke_15_竖折 — 竖折 (shu-zhe): vertical down, then turns right.

Following drawer_memory.md 折 corner family rules:
- Vertical primary drops straight down (no slant).
- End of vertical ramps slightly UP in radius approaching the joint (visualise 顿).
- ONE slightly-larger dab at the corner (the 顿 press / squared shoulder).
- Horizontal secondary starts at ~joint radius, holds roughly uniform.
- Blunt terminal press at right endpoint (no flick — that would be a 钩).
- Image coords, y grows DOWN.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Geometry — leave visual margin, tuck vertical to upper-left area
# vertical: top-left area, drops down
V_TOP = (110, 60)      # top of vertical
CORNER = (110, 210)    # bottom of vertical / start of horizontal (the joint)
H_END = (245, 210)     # right end of horizontal

# Widths (radii of brush-dabs)
R_UNIFORM = 5.5        # main uniform stroke half-width
R_JOINT = 8.0          # 顿 press at the shoulder (slightly larger)
R_TERMINAL = 6.5       # blunt round terminal at right end

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def stroke_segment(p0, p1, r0, r1, steps=500):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

# 1) Small 顿笔 (initial press) at the top of the vertical
dab(V_TOP[0], V_TOP[1], R_UNIFORM + 1.2)

# 2) Vertical primary: uniform, then ramp UP slightly to R_JOINT approaching corner
#    (per memory: end radius ramps up toward the corner to visualise the press)
stroke_segment(V_TOP, CORNER, R_UNIFORM, R_JOINT, steps=520)

# 3) One slightly-larger dab at the joint — the squared shoulder / 顿
dab(CORNER[0], CORNER[1], R_JOINT + 1.0)

# 4) Horizontal secondary: starts at joint radius, holds roughly uniform,
#    ends with terminal press (blunt, no flick)
stroke_segment(CORNER, H_END, R_JOINT, R_UNIFORM, steps=520)

# 5) Blunt terminal press at right endpoint (round end, no hook)
dab(H_END[0], H_END[1], R_TERMINAL)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p1_stroke_15_竖折/01_竖折.png"
img.save(out_path)
print(f"Saved {out_path}")
