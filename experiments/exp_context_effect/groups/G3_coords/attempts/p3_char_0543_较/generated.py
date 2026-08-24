# BANK_DEVIATION
# skipped: (no 车 or 交 bank entry exists)
# reason: 较 = 车 (left) + 交 (right); neither radical has a bank
#   primitive and no close alias exists — inline fresh in PIL px,
#   MMH-thin lines, LR-slot compression for 车 (left ~45%).
# fresh_component: che_left_for_LR / jiao_right_for_LR
"""
Render 较 (jiào) — Left-Right composition.
Left  ~45%: 车 (chē) — 4 strokes (top 横, 折/横, 竖 with hook, bottom 提)
Right ~55%: 交 (jiāo) — 6 strokes (top 点, 横, 撇, 捺-dot, big 撇, big 捺)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 4  # MMH-style thin uniform stroke width


def stroke(pts, w=LW):
    """Draw a piecewise-linear stroke with rounded joints."""
    d.line(pts, fill=BLACK, width=w, joint="curve")
    # cap ends
    r = w // 2
    for (x, y) in (pts[0], pts[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def bezier(p0, p1, p2, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


# ============================================================
# LEFT: 车 — compressed into x ~ [15, 140]
# ============================================================
# Stroke 1: top short 横
stroke([(45, 55), (120, 55)])

# Stroke 2: 横折 — short 横 then down (upper closure of the "日"-like body)
stroke([(50, 90), (125, 90), (125, 140)])

# Stroke 3: long middle 横 (spans full left half, crossbar)
stroke([(15, 175), (140, 175)])

# Stroke 4: 竖 with subtle bottom hook/提
stroke([(80, 55), (80, 245)])
# small 提 exit at bottom of the 竖 (rising right)
stroke([(80, 245), (115, 235)])


# ============================================================
# RIGHT: 交 — occupies x ~ [150, 290], center ~ 220
# ============================================================
# Stroke 1: top 点 (short slanted dot, centered above 横)
stroke([(218, 50), (228, 68)])

# Stroke 2: long 横 (below the top dot, spans right slot)
stroke([(160, 100), (280, 100)])

# Stroke 3: short 撇 (upper-left arm — starts below 横, angles down-left)
stroke(bezier((210, 115), (198, 132), (185, 152)))

# Stroke 4: short 捺/点 (upper-right arm — mirrors, angles down-right)
stroke(bezier((232, 115), (247, 132), (262, 152)))

# Stroke 5: long 撇 (major left-diagonal from center down-left)
stroke(bezier((222, 155), (195, 205), (155, 265)))

# Stroke 6: long 捺 (major right-diagonal from center down-right)
stroke(bezier((222, 155), (252, 210), (290, 268)))


out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0543_较/01_较.png"
img.save(out)
print("wrote", out)
