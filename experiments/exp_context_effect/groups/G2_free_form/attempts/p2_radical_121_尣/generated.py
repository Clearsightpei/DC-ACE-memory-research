"""Render radical 尣 (4 strokes) as 300x300 PNG.

Structure observed from GT:
- Stroke 1: short 撇 upper-left (dot-like flick from ~(105,95) to ~(80,140))
- Stroke 2: short curved 折-like stroke upper-right (starts ~(180,90),
  curls down to ~(195,140) with small hook feel — like a 横折 mini)
- Stroke 3: long 撇 sweeping from upper-middle down-left,
  starts ~(140,80), ends ~(55,275). Slight rightward bow.
- Stroke 4: 竖弯钩 on right — descends from ~(165,140) down to
  ~(165,240), then curves right and hooks up ending near ~(240,215).

Top-heavy in upper third (small angled pair), bottom is inverted-V
形 legs like 儿. Overall aspect: square-ish, filling ~x=55..240,
y=80..275.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=6):
    """Draw a poly-line stroke with rounded joins."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for p in pts:
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2], fill=BLACK)


def taper_stroke(pts, w_start=4, w_end=8, steps=40):
    """Poly-line with linear width taper (thin-to-thick or thick-to-thin)."""
    # Densify the polyline
    dense = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        for t in range(steps):
            a = t / steps
            dense.append((x0 + a * (x1 - x0), y0 + a * (y1 - y0)))
    dense.append(pts[-1])
    n = len(dense)
    for i, (x, y) in enumerate(dense):
        w = w_start + (w_end - w_start) * (i / max(n - 1, 1))
        d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=BLACK)


# --- Stroke 1: short 撇 upper-left (thick to thin, down-left) ---
pie_top_left = [(110, 90), (95, 115), (78, 145)]
taper_stroke(pie_top_left, w_start=7, w_end=3, steps=30)

# --- Stroke 2: short curved stroke upper-right (横折-ish, more curved) ---
# Small horizontal top, then curves down-left like a hook/reverse pie
htop = [(172, 95), (198, 92)]
taper_stroke(htop, w_start=5, w_end=5, steps=15)
# curved drop that bends inward (toward center)
vdrop = [(198, 92), (200, 108), (195, 125), (188, 142)]
taper_stroke(vdrop, w_start=6, w_end=3, steps=30)

# --- Stroke 3: long 撇 sweeping from upper-middle down-left ---
# Starts near center-top, crosses through the body, ends lower-left.
long_pie = [(150, 80), (130, 130), (100, 190), (70, 245), (55, 275)]
taper_stroke(long_pie, w_start=8, w_end=3, steps=40)

# --- Stroke 4: 竖弯钩 on right (like 儿's right leg) ---
# Vertical portion
sv = [(170, 140), (168, 180), (168, 220)]
taper_stroke(sv, w_start=6, w_end=6, steps=30)
# Curve to the right
curve = [(168, 220), (175, 245), (200, 258), (230, 255)]
taper_stroke(curve, w_start=6, w_end=7, steps=30)
# Hook upward
hook = [(230, 255), (238, 240), (240, 225)]
taper_stroke(hook, w_start=7, w_end=3, steps=20)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_121_尣/01_尣.png"
img.save(out)
print(f"saved {out}")
