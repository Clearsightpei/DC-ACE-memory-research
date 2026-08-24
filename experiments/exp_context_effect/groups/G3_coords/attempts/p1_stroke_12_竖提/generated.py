"""p1_stroke_12_竖提 (shu ti) — vertical then flick up-right.
G3 coord-bank format: numeric offsets on a 300x300 canvas.
White background, black ink."""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# 竖 (vertical): from top-center-ish down to bottom-center-ish
# Start slightly above middle top, go down to lower area
shu_x0, shu_y0 = 150, 55
shu_x1, shu_y1 = 150, 235

# Thick vertical: draw multiple parallel lines for calligraphic weight
stroke_w = 14
for w in range(-stroke_w // 2, stroke_w // 2 + 1):
    d.line([(shu_x0 + w, shu_y0), (shu_x1 + w, shu_y1 - 6)], fill="black", width=1)

# Rounded top of 竖
d.ellipse([shu_x0 - stroke_w // 2, shu_y0 - 6, shu_x0 + stroke_w // 2, shu_y0 + 6], fill="black")

# 提 (ti / flick): from bottom of vertical, tapering up-right
# Start at the bottom of the shu, angle ~30 degrees up-right, tapering
ti_x0, ti_y0 = 150, 235
ti_x1, ti_y1 = 245, 175

# Tapered flick: width decreases from thick to thin
n_seg = 24
for i in range(n_seg):
    f0 = i / n_seg
    f1 = (i + 1) / n_seg
    x0 = ti_x0 + (ti_x1 - ti_x0) * f0
    y0 = ti_y0 + (ti_y1 - ti_y0) * f0
    x1 = ti_x0 + (ti_x1 - ti_x0) * f1
    y1 = ti_y0 + (ti_y1 - ti_y0) * f1
    w = max(1, int(round(13 * (1 - f0) + 1 * f0)))
    d.line([(x0, y0), (x1, y1)], fill="black", width=w)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_12_竖提/01_竖提.png"
img.save(out)
print(f"Wrote {out} size={img.size}")
