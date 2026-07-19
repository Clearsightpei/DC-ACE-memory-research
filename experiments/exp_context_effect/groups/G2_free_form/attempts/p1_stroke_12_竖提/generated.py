"""
G2 free-form Drawer — p1_stroke_12_竖提
竖提 = a straight vertical (top -> bottom) followed by a rising flick
      (bottom endpoint -> upper right), thick->thin on the flick.
Rendered with PIL brush-dabs per drawer_memory.md guidance.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_line(p0, p1, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- 竖 (vertical): top -> bottom, roughly uniform, tiny end-swell at joint ---
shu_top = (140, 55)      # top-left-ish area
shu_bot = (140, 210)     # bottom endpoint (turn point)

# initial 顿笔: one larger dab at the top press-in
draw.ellipse((shu_top[0] - 8, shu_top[1] - 8, shu_top[0] + 8, shu_top[1] + 8), fill="black")

# vertical body: slight swell toward the joint (per 折/turn guidance —
# ramp up radius toward corner so the shoulder reads)
dab_line(shu_top, shu_bot, r_start=6.5, r_end=8.0, steps=450)

# shoulder dab at the joint
jx, jy = shu_bot
draw.ellipse((jx - 9.5, jy - 9.5, jx + 9.5, jy + 9.5), fill="black")

# --- 提 (rising flick): joint -> upper right, thick -> sharp tip ---
# angle ~28° above horizontal, length ~85 px
# start at joint, end up-right
ti_end = (235, 165)  # rises up-right (y decreases in image coords)
dab_line(shu_bot, ti_end, r_start=8.0, r_end=1.2, steps=380)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p1_stroke_12_竖提/01_竖提.png"
)
print("done")
