"""
p2_radical_110_攵 (pū / 反文旁) — 4 strokes.

Composition analysis of the GT:
- Stroke 1: short 撇 at top — starts upper-right of the top area, curves
  down-left. Head roughly mid-canvas x, tail down-left.
- Stroke 2: short 横 crossing the 撇 slightly below the head. Runs
  left-to-right, roughly horizontal, quite short. In the GT it is more
  a slanted short bar.
- Stroke 3: long 撇 — starts near the intersection of strokes 1 & 2 (or
  slightly to their right), sweeps down and left through most of the
  canvas to the lower-left corner.
- Stroke 4: 捺 — starts near where the long 撇 begins (upper region,
  right of shape center), sweeps down and RIGHT to the lower-right
  corner. Together, strokes 3 & 4 form the X-shaped 又-like bottom.

INLINE-FRESH TEST (TR8): the bank has pie / na / heng primitives, but
this composition needs specific crossing geometry (like 又 / 大 which
FAILED B1 via primitive force-fit). Following the B1 lesson, ALL FOUR
strokes are inlined fresh as tapered beziers with hand-picked control
points to get the crossings right.

Canvas: 300x300, white bg, black ink.
Uses PIL only (per P2).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
CX, CY = W // 2, H // 2  # 150, 150

img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _bezier_point(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
    return (x, y)


def tapered_bezier(p0, p1, p2, w_head, w_tail, steps=140):
    """Draw a quadratic bezier with a linear width ramp from w_head->w_tail."""
    prev = None
    for i in range(steps + 1):
        t = i / steps
        pt = _bezier_point(p0, p1, p2, t)
        w = w_head * (1 - t) + w_tail * t
        r = max(0.5, w / 2)
        draw.ellipse((pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r), fill="black")
        prev = pt


def tapered_bezier_profile(p0, p1, p2, profile, steps=160):
    """profile: list of (t, width) sorted by t; interpolates linearly."""
    def w_at(t):
        for i in range(1, len(profile)):
            t0, w0 = profile[i - 1]
            t1, w1 = profile[i]
            if t <= t1:
                if t1 == t0:
                    return w0
                a = (t - t0) / (t1 - t0)
                return w0 * (1 - a) + w1 * a
        return profile[-1][1]

    for i in range(steps + 1):
        t = i / steps
        pt = _bezier_point(p0, p1, p2, t)
        w = w_at(t)
        r = max(0.5, w / 2)
        draw.ellipse((pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r), fill="black")


# REVISION 1: original was too vertically stretched (X extended to
# bottom corners); GT is more compact and centered with roomier bottom
# margin. Shifted the crossing point down slightly and pulled the tails
# in from the corners. Also toned down top-stroke crossing so it reads
# as two separate strokes like the GT.

# --- Stroke 1: short 撇 at top ---
# Head high-mid (~145, 65), tail down-left (~112, 108).
# Width: thick head (~9) tapering to needle (~1). (per P4)
p1_head = (150, 62)
p1_ctrl = (132, 88)
p1_tail = (110, 115)
tapered_bezier(p1_head, p1_ctrl, p1_tail, w_head=9, w_tail=1)

# --- Stroke 2: short 横 slightly rising to the right ---
# Starts on the pie shaft (~123, 100) and ends up-right (~185, 82).
# Short, uniform-ish width ~7.
p2_left = (120, 100)
p2_ctrl = (152, 90)
p2_right = (188, 82)
tapered_bezier(p2_left, p2_ctrl, p2_right, w_head=7, w_tail=6)

# --- Stroke 3: long 撇 — from upper-mid area to lower-LEFT ---
# Start near (162, 115) (below intersection region), curve down-left
# through belly at (115, 175), tail at (72, 240) (pulled IN from corner).
p3_head = (162, 115)
p3_ctrl = (112, 178)
p3_tail = (72, 245)
tapered_bezier_profile(
    p3_head, p3_ctrl, p3_tail,
    profile=[(0.0, 10), (0.3, 9), (0.7, 5), (1.0, 1.5)],
)

# --- Stroke 4: 捺 — from upper-mid area to lower-RIGHT ---
# Starts near (162, 118) — same launch as stroke 3 (they form X).
# Belly at (208, 190), tail at (235, 245) (pulled IN from corner).
p4_head = (162, 118)
p4_ctrl = (205, 188)
p4_tail = (238, 248)
tapered_bezier_profile(
    p4_head, p4_ctrl, p4_tail,
    profile=[(0.0, 2), (0.3, 5), (0.7, 14), (0.9, 10), (1.0, 4)],
)


out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G3_coords/attempts/p2_radical_110_攵/01_攵.png"
)
img.save(out_path)
print(f"wrote {out_path}")
