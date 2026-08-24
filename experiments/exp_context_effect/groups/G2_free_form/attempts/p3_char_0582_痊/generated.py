"""
Render 痊 (quan2) at 300x300, black ink on white.

Structure: 疒 canopy (LEFT/TOP wrap) + 全 interior (人 lid + 王).

疒 (frozen cohort - 14x fails):
  5 strokes: 点 (top), 横 (short crossbar), 长撇 (long down-left sweep),
             内点 + 提 (INSIDE the canopy triangle, not dangling on stem)

全 interior:
  人 lid (撇 + 捺 covering the top of body) + 王 (3 横 + 1 竖)
  Body must sit INSIDE the 疒 canopy triangle, tucked under the 撇 belly.
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


def shoulder(pt, r=6):
    x, y = pt
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# =============== 疒 canopy ================
# (1) top 点 — small tick top-center-left
dot1 = bez((95, 55), (98, 62), (102, 68), (108, 74), n=25)
stroke(dot1, (3, 8))

# (2) 横 — short crossbar just under the 点, at top of canopy
heng = bez((70, 90), (100, 88), (135, 88), (165, 92), n=40)
stroke(heng, (6, 7))
shoulder((165, 92), r=6)  # right-end shoulder dab

# (3) 长撇 — long sweeping stroke down-left from right end of 横
pie = bez((160, 90), (130, 140), (95, 195), (55, 260), n=80)
stroke(pie, (10, 3))

# (4) 内点 — dot INSIDE the canopy triangle (upper-left of interior wedge)
inner_dot = bez((85, 130), (88, 138), (92, 146), (98, 154), n=25)
stroke(inner_dot, (3, 8))

# (5) 提 — rising tick from below inner_dot, angling up-right
ti = bez((78, 175), (90, 170), (105, 162), (122, 155), n=30)
stroke(ti, (8, 3))

# =============== 全 interior (nestled under 疒 撇 belly) ================
# 全 = 人 (top cover) + 王 (3 horizontals + 1 vertical)
# center around x=195, y=100..255

# --- 人 lid ---
# 撇 of 人: from apex down-left
pie_ren = bez((195, 85), (180, 110), (165, 130), (150, 150), n=60)
stroke(pie_ren, (10, 4))

# 捺 of 人: from apex down-right, with foot flare
na_ren = bez((195, 90), (215, 115), (235, 140), (255, 158), n=60)
stroke(na_ren, (4, 12))
foot = bez((255, 158), (260, 160), (264, 162), (268, 163), n=15)
stroke(foot, (12, 4))

# --- 王 (3 横 + 1 竖) — sits under the 人 apex ---
# 横 1 (top, short)
h1 = bez((165, 175), (190, 173), (215, 173), (240, 176), n=40)
stroke(h1, (6, 6))

# 横 2 (middle, shorter)
h2 = bez((170, 210), (195, 208), (218, 208), (235, 210), n=40)
stroke(h2, (5, 5))

# 竖 (vertical, connects all three 横)
sh = bez((202, 168), (202, 200), (202, 230), (202, 252), n=50)
stroke(sh, (7, 7))

# 横 3 (bottom, longest)
h3 = bez((155, 250), (185, 248), (220, 248), (255, 252), n=50)
stroke(h3, (7, 7))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0582_痊/01_痊.png")
