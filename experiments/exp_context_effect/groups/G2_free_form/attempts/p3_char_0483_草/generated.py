"""
Render 草 (cao3) at 300x300, black ink on white.

Structural read from GT:
  Top (艹 grass radical, 3 strokes):
    - Long horizontal, slight rise, across upper third.
    - Left short vertical, tilted slightly, crossing the horizontal.
    - Right short vertical, tilted slightly, crossing the horizontal.
  Middle (日, 4 strokes): a compact box with an inner horizontal.
    - Left vertical.
    - Top-right corner (横折) as one path.
    - Middle horizontal.
    - Bottom horizontal closing the box.
  Bottom (十, 2 strokes):
    - Long horizontal extending well beyond box width.
    - Long central vertical descending to bottom edge.

Applying TIER-0 F calligraphic-weight moves:
  - Teardrop taper via `stroke(pts, widths=(a,b))`.
  - Shoulder dabs at 折 corners (extra ellipse at joint).
  - Bezier for any curved sweep (verticals mostly straight but tapered).
  - No hooks with flick required here (草 has no 钩 in main strokes).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def shoulder_dab(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# === 艹 (grass radical) ===
# 1) long horizontal across, slight up-right rise
h_top = bez((45, 72), (110, 68), (200, 65), (258, 62), n=50)
stroke(h_top, (7, 7))

# 2) left short vertical (slight tilt inward, top-to-bottom passing through h_top)
lv = bez((100, 42), (100, 58), (102, 82), (105, 100), n=40)
stroke(lv, (8, 6))

# 3) right short vertical (slight tilt inward the other way)
rv = bez((198, 42), (198, 58), (196, 82), (192, 100), n=40)
stroke(rv, (8, 6))

# === 日 (middle box) ===
box_left_x = 108
box_right_x = 192
box_top_y = 118
box_mid_y = 152
box_bot_y = 188

# 1) left vertical of the box
lv2 = bez((box_left_x, box_top_y), (box_left_x, 140),
          (box_left_x, 170), (box_left_x, box_bot_y), n=40)
stroke(lv2, (7, 7))

# 2) top-and-right (横折): horizontal across then fold down as right vertical
h_top_box = bez((box_left_x, box_top_y), (135, box_top_y - 1),
                (170, box_top_y - 1), (box_right_x, box_top_y), n=40)
stroke(h_top_box, (6, 7))
shoulder_dab(box_right_x, box_top_y, r=5)
rv2 = bez((box_right_x, box_top_y), (box_right_x, 140),
          (box_right_x, 170), (box_right_x, box_bot_y), n=40)
stroke(rv2, (7, 7))

# 3) middle horizontal inside the box
h_mid = bez((box_left_x + 3, box_mid_y), (135, box_mid_y - 1),
            (170, box_mid_y - 1), (box_right_x - 3, box_mid_y), n=40)
stroke(h_mid, (5, 5))

# 4) bottom horizontal closing the box
h_bot = bez((box_left_x, box_bot_y), (135, box_bot_y + 1),
            (170, box_bot_y + 1), (box_right_x, box_bot_y), n=40)
stroke(h_bot, (6, 6))

# === 十 (bottom) ===
# 1) long horizontal well wider than box
h_long = bez((30, 220), (110, 216), (200, 216), (275, 220), n=60)
stroke(h_long, (8, 8))

# 2) long central vertical, from just above the long horizontal to bottom
v_long = bez((152, 195), (152, 235), (152, 260), (152, 285), n=60)
stroke(v_long, (8, 7))

img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0483_草/01_草.png"
)
