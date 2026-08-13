"""G1 render of 多 (duo) — two stacked 夕 with smoother curves."""
from PIL import Image, ImageDraw
from pathlib import Path

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 5

def smooth_curve(points, width=LW):
    # Draw a Catmull-Rom-ish smoothed polyline by subdividing.
    # Simple approach: draw line with joint='curve' at more points.
    d.line(points, fill=INK, width=width, joint="curve")

def dot(cx, cy, r=5):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=INK)

# --- Top 夕 ---
# Stroke 1: 撇 — starts upper, curves down-left
smooth_curve([
    (158, 32), (152, 45), (144, 62), (132, 82),
    (115, 105), (95, 130), (78, 150)
])

# Stroke 2: 横折钩 — short horizontal turning into hook down-left
smooth_curve([
    (120, 72), (145, 68), (170, 70), (180, 78),
    (178, 95), (168, 118), (150, 140), (118, 155)
])

# Stroke 3: 撇 (small inner) inside the 夕
smooth_curve([(128, 108), (138, 122), (140, 130)])

# --- Bottom 夕 (larger, shifted slightly) ---
# Stroke 4: 撇
smooth_curve([
    (172, 148), (165, 165), (155, 185), (140, 210),
    (118, 240), (92, 265), (68, 282)
])

# Stroke 5: 横折钩
smooth_curve([
    (135, 188), (170, 184), (200, 186), (212, 195),
    (210, 215), (198, 240), (178, 262), (140, 278)
])

# Stroke 6: 撇 (small inner)
smooth_curve([(148, 225), (159, 240), (162, 248)])

out = Path(__file__).parent / "01_多.png"
img.save(out)
print(f"wrote {out}")
