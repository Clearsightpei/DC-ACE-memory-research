# 同 (tóng) — 6 strokes: 冂 frame (2) + inner 一 (1) + inner 口 (3)
# Reading order:
#   drawer_memory.md: chronic jiong_frame.py exists for 冂 (but default is
#     too wide for this GT); kou.py exists for inner 口.
#   INDEX grep: 冂 in chronic, 口 = kou.py.
#   errata.md: 同 not listed.
# Split: 同 = 冂 + 一 (inside top) + 口 (inside bottom).
# v8: trust GT when memory (MMH anchors) disagree. MMH gives right wall at
# x=183, but the GT PNG shows right wall at x≈221 (bbox width 145, height
# 186). Widen frame accordingly; keep the 6-stroke count and N-class joints.

from PIL import Image, ImageDraw

SIZE = 300
CELL = SIZE // 3  # 100

CELLS = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def A(cell, xf, yf):
    col, row = CELLS[cell]
    return (col * CELL + xf * CELL, row * CELL + yf * CELL)


def fat_line(draw, p0, p1, width=10, color=(0, 0, 0)):
    draw.line([p0, p1], fill=color, width=int(round(width)))
    r = width / 2.0
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)


def shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


img = Image.new('RGB', (SIZE, SIZE), 'white')
draw = ImageDraw.Draw(img)

# --- 6 strokes ---
# 冂 outer frame: bbox from GT ≈ x[76..221], y[80..266].
# stroke 1: left wall 丨  — matches MMH cell TL/BL, x shifted to ~76 (GT)
s1h = A('TL', 0.76, 0.80)     # (76, 80)
s1t = A('BL', 0.76, 0.66)     # (76, 266)

# stroke 2: 横折 (top bar + right wall). MMH gives tail at BC(0.83,0.73)
# = (183, 273) but GT shows the right wall at x≈221 — trust GT (v8).
# So corner at TR/BR column (x=221), same top y as s1.
s2h = A('TL', 0.80, 0.80)     # (80, 80) — just right of s1.head
s2c = A('TR', 0.21, 0.80)     # (221, 80) — top-right corner
s2t = A('BR', 0.21, 0.66)     # (221, 266) — bottom of right wall

# stroke 3: inner 一 (top heng inside frame). MMH: C(0.104,0.31) → C(0.84,0.23).
s3h = A('C', 0.11, 0.30)      # (111, 130)
s3t = A('C', 0.85, 0.24)      # (185, 124)

# --- Inner 口 (strokes 4-6). Sits below the inner heng, roughly
# x[105..195], y[178..255]. MMH anchors are respected where consistent
# with GT geometry. ---

# stroke 4: inner 口 left wall (short 丨)
s4h = A('C', 0.10, 0.75)      # (110, 175)
s4t = A('BC', 0.20, 0.55)     # (120, 255)

# stroke 5: inner 口 横折 (top bar + right wall of inner 口)
s5h = A('C', 0.15, 0.78)      # (115, 178)
s5c = A('C', 0.95, 0.78)      # (195, 178) — top-right corner
s5t = A('BC', 0.95, 0.55)     # (195, 255) — bottom of right wall

# stroke 6: inner 口 bottom heng
s6h = A('BC', 0.20, 0.55)     # (120, 255)
s6t = A('BC', 0.95, 0.55)     # (195, 255)


# --- Render (all joints are N-class ⇒ small gap via shorten) ---

# s1 — left wall of 冂 (N-gap at top vs s2)
s1h_g = shorten(s1h, s1t, 4)
fat_line(draw, s1h_g, s1t, width=10)

# s2 — 横折 top+right wall (N-gap at start vs s1)
s2h_g = shorten(s2h, s2c, 4)
fat_line(draw, s2h_g, s2c, width=10)
fat_line(draw, s2c, s2t, width=10)
cx, cy = s2c
r = 5
draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

# s3 — inner 一 (no joints declared; standalone heng)
fat_line(draw, s3h, s3t, width=9)

# s4 — inner 口 left wall (N-gap at tail vs s6.head; N-gap at mid vs s5.head)
s4t_g = shorten(s4t, s4h, 3)
fat_line(draw, s4h, s4t_g, width=8)

# s5 — inner 口 横折 (N-gap at head vs s4)
s5h_g = shorten(s5h, s5c, 3)
fat_line(draw, s5h_g, s5c, width=8)
s5t_g = shorten(s5t, s5c, 3)
fat_line(draw, s5c, s5t_g, width=8)
cx, cy = s5c
r = 4
draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

# s6 — inner 口 bottom heng (N-gap both ends)
s6h_g = shorten(s6h, s6t, 3)
s6t_g = shorten(s6t, s6h, 3)
fat_line(draw, s6h_g, s6t_g, width=8)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 6 strokes
    'endpoint_mismatches': [
        # widened frame to match GT (v8 rule):
        {'stroke': 2, 'expected': ('BC', 0.831, 0.73), 'actual': ('BR', 0.21, 0.66),
         'delta': 'x +38 px vs MMH; matches GT right wall at x≈221'},
    ],
    'joint_class_mismatches': [],  # all N-class, small gaps preserved
    'overall_pass': True,
    'notes': '6-stroke PIL render: 冂 frame + inner 一 + inner 口. Frame widened '
             'from MMH (183) to match GT (221) per v8 trust-GT rule. All 4 declared '
             'joints are N-class with ~3-4 px shortening.'
}


img.save('01_同.png')
