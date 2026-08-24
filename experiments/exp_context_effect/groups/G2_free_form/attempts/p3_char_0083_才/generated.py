"""Render 才 (cai) — 3 strokes: 横, 竖钩, 撇.

Structure (from GT observation):
- 横: horizontal bar high-middle, spans ~x=45..245 at y~135, slight uptilt.
- 竖钩: vertical passing through the 横 slightly right of center,
        from ~y=95 down to ~y=250, then a small hook flicking up-left.
- 撇: body-crossing diagonal starting up-right (~x=175, y=95),
      sweeping down-left across the 横 to ~x=55, y=250. Gentle bow.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(pts, width_start=9, width_end=9, dabs=True):
    """Draw a variable-width polyline by stamping circles along it."""
    n = len(pts)
    if n < 2:
        return
    # sample interpolated points along each segment
    all_samples = []
    seg_lens = []
    for i in range(n - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        seg_lens.append(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    total = sum(seg_lens) or 1
    STEP = 1.0
    acc = 0.0
    for i in range(n - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        L = seg_lens[i]
        steps = max(2, int(L / STEP))
        for k in range(steps + 1):
            t_local = k / steps
            x = x1 + (x2 - x1) * t_local
            y = y1 + (y2 - y1) * t_local
            t_global = (acc + L * t_local) / total
            all_samples.append((x, y, t_global))
        acc += L
    for (x, y, t) in all_samples:
        w = width_start + (width_end - width_start) * t
        r = w / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# --- Stroke 1: 横 (horizontal) ---
# slight uptilt from left to right, mild bow
heng_pts = [(48, 138), (100, 134), (170, 132), (245, 130)]
brush_line(heng_pts, width_start=8, width_end=7)

# --- Stroke 2: 竖钩 (vertical with hook) ---
# vertical goes from ~ (168, 95) down to (168, 245), then hook up-left
shu_pts = [(168, 95), (168, 150), (168, 210), (168, 248)]
brush_line(shu_pts, width_start=9, width_end=10)
# hook: short flick up-left
hook_pts = [(168, 248), (158, 245), (150, 238)]
brush_line(hook_pts, width_start=10, width_end=4)

# --- Stroke 3: 撇 (body-crossing diagonal) ---
# starts up-right of the 竖钩 top, sweeps down-left, crossing the 横
# gentle rightward bow (i.e. bulges out to the right slightly)
pie_pts = [
    (180, 95),
    (160, 130),
    (135, 165),
    (105, 200),
    (75, 235),
    (55, 258),
]
brush_line(pie_pts, width_start=8, width_end=3)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0083_才/01_才.png")
