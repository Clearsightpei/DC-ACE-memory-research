"""
Render 度 (du4) at 300x300, black ink on white.

Structural read from GT (9 strokes):
  广 radical (top-outer, 3 strokes):
    1. 点 (short dot, top center)
    2. 横 (long horizontal, upper, extends right)
    3. 撇 (long sweep down-left from horizontal's left end)
  廿 (middle-interior, 3 strokes):
    4. 横 (top horizontal of the 廿-shape)
    5. 竖 (left vertical of 廿)
    6. 竖 (right vertical of 廿)
  廿-base + 又 (bottom, 3 strokes):
    7. 横 (base horizontal, longer than the 廿 top, spans wider)
    8. 横撇 (top-left of 又: short horizontal then pie down-left)
    9. 捺 (long S-curve sweep down-right, foot flare at end)

Applies TIER-0 F rule: teardrop taper, bezier curves, no uniform width.
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

# --- 广 radical ---
# 1. 点 (dot on top)
dot = bez((150, 30), (152, 35), (155, 42), (158, 50), n=20)
stroke(dot, (4, 9))

# 2. 横 (long horizontal top of 广) - slight rise to the right
h_top = bez((90, 68), (140, 66), (200, 66), (255, 70), n=60)
stroke(h_top, (7, 7))
# shoulder dab at right end where the horizontal would break
d.ellipse((250, 65, 262, 77), fill="black")

# 3. 撇 (long sweep down-left of 广)
pie = bez((100, 66), (85, 130), (65, 180), (35, 240), n=80)
stroke(pie, (11, 4))

# --- interior 廿 ---
# 4. 横 (top horizontal of 廿)
h_mid = bez((110, 120), (140, 118), (175, 118), (200, 120), n=40)
stroke(h_mid, (6, 6))

# 5. 竖 (left vertical of 廿)
v_left = bez((118, 120), (117, 145), (117, 165), (117, 185), n=40)
stroke(v_left, (6, 5))

# 6. 竖 (right vertical of 廿)
v_right = bez((195, 120), (196, 145), (197, 165), (198, 185), n=40)
stroke(v_right, (6, 5))

# 7. 横 (base horizontal — contained within 广, spans slightly beyond 廿)
h_base = bez((85, 185), (135, 183), (195, 183), (240, 187), n=60)
stroke(h_base, (7, 7))

# --- 又 at bottom (centered under interior) ---
# 8. 横撇: short horizontal then pie sweeping down-left
hp_h = bez((115, 215), (135, 213), (155, 213), (170, 216), n=30)
stroke(hp_h, (6, 7))
# shoulder dab at corner
d.ellipse((165, 210, 179, 224), fill="black")
# pie portion sweeping down-left, curving outward
hp_pie = bez((172, 217), (150, 240), (115, 260), (78, 280), n=60)
stroke(hp_pie, (9, 3))

# 9. 捺 (long S-curve sweep down-right from mid of 又 stem)
na = bez((155, 220), (180, 240), (210, 258), (240, 273), n=70)
stroke(na, (5, 12))
# foot flare
foot = bez((240, 273), (248, 275), (254, 277), (260, 278), n=15)
stroke(foot, (12, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0453_度/01_度.png")
