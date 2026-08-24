"""桃 (táo, peach) — Phase-3 character.

Composition: 木 (compressed, left) + 兆 (right).
Left 木 uses 4 strokes but with 捺 -> 点 (LR-compression rule from
form_catalog.md left-position 木).
Right 兆 uses 6 strokes: two mirrored halves.

SIGNATURE CHECK (from TIER-0 F recipe):
- teardrop taper on all 撇/捺/点 (bezier + line_dabs with r0!=r1)
- shoulder dab at hook joint
- bezier for curved sweep (竖弯钩 arcs)
- hook flick UP-and-LEFT (into body) on both 竖弯钩

Components MUST touch (TIER-0 H): 木's 横 extends right to touch/overlap
where 兆's left stroke starts. No gap.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=300, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        omt = 1 - t
        x = omt * omt * p0[0] + 2 * omt * t * p1[0] + t * t * p2[0]
        y = omt * omt * p0[1] + 2 * omt * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# =============================================================
# LEFT: 木 radical (compressed to left half; 捺 -> 点)
# =============================================================
LCX, LCY = 90, 130  # cross joint for 木

# 1. 横 — horizontal (spans left ~40 to ~135; extends slightly rightward
#    to nearly touch 兆's leftmost stroke start)
h_x0, h_y0 = 40, 133
h_x1, h_y1 = 138, 128
r_h = 4.0
dab(h_x0, h_y0, r_h + 1)
line_dabs(h_x0, h_y0, h_x1, h_y1, r_h, r_h, steps=250)
dab(h_x1, h_y1, r_h + 1)

# 2. 竖 — vertical through cross point
v_x0, v_y0 = LCX, 60
v_x1, v_y1 = LCX, 265
r_v = 4.5
dab(v_x0, v_y0, r_v + 1)
line_dabs(v_x0, v_y0, v_x1, v_y1, r_v, r_v, steps=350)
dab(v_x1, v_y1, r_v)

# 3. 撇 (left flick from cross) — thick to thin, curved
pie_p0 = (LCX, LCY + 2)
pie_p2 = (38, 245)
pie_p1 = (65, 200)
bezier_dabs(pie_p0, pie_p1, pie_p2, r0=7.0, r1=1.2, steps=350, ease=1.15)
dab(pie_p0[0], pie_p0[1], 7.5)

# 4. 点 (replaces 捺 when 木 is on the left) — short dot down-right
dot_p0 = (LCX + 2, LCY + 3)
dot_p2 = (140, 200)
dot_p1 = (120, 175)
bezier_dabs(dot_p0, dot_p1, dot_p2, r0=2.2, r1=6.5, steps=200, ease=1.3)
dab(dot_p2[0], dot_p2[1], 7.0)


# =============================================================
# RIGHT: 兆 (6 strokes)
# Left half of 兆: 撇 (upper) + 竖弯钩 (main)
# Middle: two 点/提
# Right half: 点 (upper) + 竖弯钩 (main)
# =============================================================

# 5. 撇 upper-left of 兆 — down-left flick from ~x=180 to ~x=150
b1_p0 = (185, 75)
b1_p2 = (150, 135)
b1_p1 = (168, 108)
bezier_dabs(b1_p0, b1_p1, b1_p2, r0=6.0, r1=1.4, steps=200, ease=1.2)
dab(b1_p0[0], b1_p0[1], 6.5)

# 6. 竖弯钩 (left main of 兆) — leftmost long stroke, sweeps down-right,
#    hook UP-and-LEFT into body
lm_p0 = (162, 135)
lm_p1 = (168, 220)
lm_p2 = (200, 270)
bezier_dabs(lm_p0, lm_p1, lm_p2, r0=5.5, r1=4.8, steps=320, ease=1.0)
dab(lm_p0[0], lm_p0[1], 6.0)
# shoulder dab at hook joint
dab(lm_p2[0], lm_p2[1], 6.0)
# hook flick UP-and-LEFT into body
hk_p0 = (200, 270)
hk_p1 = (192, 258)
hk_p2 = (178, 250)
bezier_dabs(hk_p0, hk_p1, hk_p2, r0=5.5, r1=1.2, steps=120, ease=1.2)

# 7. 提 middle — short up-right stroke, thick to thin
t_x0, t_y0 = 200, 200
t_x1, t_y1 = 235, 178
line_dabs(t_x0, t_y0, t_x1, t_y1, 5.5, 1.4, steps=180)
dab(t_x0, t_y0, 6.0)

# 8. 点 middle-right — small down-right dot (interior)
d_p0 = (220, 152)
d_p2 = (240, 185)
d_p1 = (232, 170)
bezier_dabs(d_p0, d_p1, d_p2, r0=2.0, r1=5.5, steps=180, ease=1.3)
dab(d_p2[0], d_p2[1], 6.0)

# 9. 点 upper-right of 兆 — dot pointing down-left
ur_p0 = (255, 80)
ur_p2 = (235, 130)
ur_p1 = (247, 105)
bezier_dabs(ur_p0, ur_p1, ur_p2, r0=6.0, r1=1.6, steps=200, ease=1.2)
dab(ur_p0[0], ur_p0[1], 6.5)

# 10. 竖弯钩 (right main of 兆) — rightmost long stroke from upper-right
#     down and hook UP-and-LEFT into body
rm_p0 = (260, 130)
rm_p1 = (263, 220)
rm_p2 = (285, 265)
bezier_dabs(rm_p0, rm_p1, rm_p2, r0=5.5, r1=5.0, steps=320, ease=1.0)
dab(rm_p0[0], rm_p0[1], 6.0)
dab(rm_p2[0], rm_p2[1], 6.5)
# hook flick UP-and-LEFT
rhk_p0 = (285, 265)
rhk_p1 = (276, 253)
rhk_p2 = (262, 244)
bezier_dabs(rhk_p0, rhk_p1, rhk_p2, r0=5.5, r1=1.2, steps=120, ease=1.2)

out = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0565_桃/01_桃.png"
)
img.save(out)
print(f"saved {out}")
