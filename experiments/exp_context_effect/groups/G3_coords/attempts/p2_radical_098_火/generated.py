"""
火 (huǒ) — 4-stroke radical
Per TR8 (INLINE-FRESH TEST): 火's central two strokes are a 人-shape
(pie + na apex-crossing) and B1 documented that bank pie/na force-fit
fails on 人/入/大 because their default chord angles fight the target.
So: inline all 4 strokes as tapered polylines / beziers with hand-
picked endpoints. No bank primitive calls.

Stroke plan (from GT visual):
  1. Left dot (short 点 slanting down-left):  small tapered stroke,
     high-left region, thick head → thin tail. Sits around x=110, y=140.
  2. Right dot (short 撇 slanting down-left): mirror-ish, in the
     upper-middle-right region around x=190, y=140. Thick head at
     upper-right, tapers down-left.
  3. Central 撇 (long): starts near top-center (150, 70), sweeps
     down-left with a slight scoop to bottom-left (95, 250). Thick
     head (~10) → needle tip (~1).
  4. 捺 (long): starts near top-center where 撇 originates (~155, 90),
     sweeps down-right with belly at u=0.7, tapers to a foot at
     bottom-right (~230, 240). Thin head (~2) → belly (~15) → foot (~3).

Canvas: 300x300, white bg, black ink. PIL only (P2).
Convention: PIL pixel coords (y grows DOWN in PIL).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _bezier_pts(p0, p1, p2, n=80):
    """Quadratic bezier sample."""
    pts = []
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _tapered_polyline(pts, widths):
    """Stamp circles along pts with per-point radii from widths list.
    widths is list same length as pts (each = full width, radius = w/2).
    """
    for (x, y), w in zip(pts, widths):
        r = max(0.5, w / 2)
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def _width_ramp(n, w_start, w_mid, w_end, mid_u=0.5):
    """Linear interp start→mid at u=mid_u, mid→end at u=1."""
    ws = []
    for i in range(n):
        u = i / (n - 1) if n > 1 else 0
        if u <= mid_u:
            t = u / mid_u
            ws.append(w_start + (w_mid - w_start) * t)
        else:
            t = (u - mid_u) / (1 - mid_u)
            ws.append(w_mid + (w_end - w_mid) * t)
    return ws


# --- Stroke 1: left dot (short 撇-dot slanting down-LEFT) ---
# In GT: sits mid-left, thick head at upper-right, tapers down-left.
# Position it well left of the central pie, roughly mid-height.
s1_pts = _bezier_pts((115, 138), (105, 152), (90, 165), n=30)
s1_widths = _width_ramp(len(s1_pts), 5, 4, 1)
_tapered_polyline(s1_pts, s1_widths)

# --- Stroke 2: right dot (short 点/捺-like, slanting down-RIGHT) ---
# In GT: mirror-flank, thick head at upper-left, tapers down-RIGHT.
# Small short stroke, right of pie shaft, above the na body.
s2_pts = _bezier_pts((178, 138), (190, 148), (203, 158), n=30)
s2_widths = _width_ramp(len(s2_pts), 4, 5, 1)
_tapered_polyline(s2_pts, s2_widths)

# --- Stroke 3: central long 撇 ---
# From top-center down-left with scoop; thick head → needle tip.
# Slightly thinner overall than v1.
s3_pts = _bezier_pts((152, 60), (135, 155), (80, 258), n=90)
s3_widths = _width_ramp(len(s3_pts), 8, 5, 1, mid_u=0.55)
_tapered_polyline(s3_pts, s3_widths)

# --- Stroke 4: 捺 ---
# From near pie's apex sweeping down-right with belly u≈0.7.
# Thinner belly than v1 (was too heavy).
s4_pts = _bezier_pts((160, 80), (185, 170), (235, 255), n=90)
s4_widths = []
n4 = len(s4_pts)
for i in range(n4):
    u = i / (n4 - 1)
    if u <= 0.7:
        t = u / 0.7
        # 2 → 12
        s4_widths.append(2 + (12 - 2) * t)
    else:
        t = (u - 0.7) / 0.3
        # 12 → 3
        s4_widths.append(12 + (3 - 12) * t)
_tapered_polyline(s4_pts, s4_widths)


out_path = os.path.join(os.path.dirname(__file__), "01_火.png")
img.save(out_path)
print(f"Wrote {out_path}")
