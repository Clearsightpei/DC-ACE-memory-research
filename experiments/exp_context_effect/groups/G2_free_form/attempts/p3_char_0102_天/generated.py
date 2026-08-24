"""
Render 天 (heaven) to a 300x300 PNG.

SIGNATURE CHECK (per sibling_signature_checklist.md):
  target = 天
  related bit (大): 一 + 撇+捺 sharing apex ON the 一
  For 天: TOP short 横 (upper) + LONGER 横 (middle) + 撇+捺 apex
          sitting ON the middle 横. Top 横 is shorter than middle 横.
  Common wrong-render: 夫 (top 横 longer than middle) or 大 (only one 横).

Structure inspection of GT:
  - Stroke 1: top short 横, slight downward slope at right end
  - Stroke 2: middle longer 横 (wider), roughly horizontal
  - Stroke 3: 撇 — from apex on middle 横 sweeping down-left
  - Stroke 4: 捺 — from apex on middle 横 sweeping down-right with thick foot

Following G2 memory:
  - form_catalog "横 as top-lid": short lid over hanging body
  - form_catalog "撇 + 捺 apex on 一" (like 大): apex sits ON the 横
  - drawer_memory "Draw the flick" and brush-dab technique for 捺 foot
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width_start=10, width_end=10):
    """Draw a variable-width polyline by dabbing circles along it."""
    if len(points) < 2:
        return
    # compute cumulative length
    seg_lens = []
    total = 0.0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        L = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
        seg_lens.append(L)
        total += L
    steps = max(int(total * 2), 20)
    for s in range(steps + 1):
        t = s / steps
        # find which segment
        target = t * total
        acc = 0.0
        seg = 0
        for i, L in enumerate(seg_lens):
            if acc + L >= target or i == len(seg_lens) - 1:
                seg = i
                local = (target - acc) / L if L > 0 else 0
                break
            acc += L
        x1, y1 = points[seg]
        x2, y2 = points[seg+1]
        x = x1 + (x2 - x1) * local
        y = y1 + (y2 - y1) * local
        w = width_start + (width_end - width_start) * t
        r = w / 2
        d.ellipse([x-r, y-r, x+r, y+r], fill="black")

# --- Stroke 1: top short 横 ---
# Short horizontal near top, slight rightward-down slope
stroke([(105, 82), (210, 88)], width_start=7, width_end=10)

# --- Stroke 2: middle longer 横 ---
# Longer horizontal below (~1.6x top width), roughly at y=145
stroke([(45, 145), (255, 148)], width_start=8, width_end=9)

# --- Stroke 3: 撇 (down-left sweep from apex on middle 横) ---
# apex roughly at x=150, y=140 (on the middle 横), sweeps down-left
# gentle curve
pie = []
# start near apex slightly right of center to allow 捺 apex
sx, sy = 148, 148
# curve to lower-left
pts = [
    (sx, sy),
    (132, 185),
    (108, 220),
    (78, 255),
    (48, 278),
]
stroke(pts, width_start=10, width_end=4)

# --- Stroke 4: 捺 (down-right sweep with thick foot) ---
# starts at apex, sweeps down-right, thickens at foot
pts = [
    (152, 148),
    (172, 180),
    (198, 218),
    (230, 255),
    (262, 278),
]
stroke(pts, width_start=5, width_end=15)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0102_天/01_天.png")
print("saved")
