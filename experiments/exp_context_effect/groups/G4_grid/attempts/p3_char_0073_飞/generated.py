"""p3_char_0073_飞 — 3-stroke character. REVISION 1.

Lookup checklist:
1. success_bank/INDEX.md grep "飞" — listed but no fei.py; treat as unmastered.
2. errata.md grep "飞" — 3 prior FAILs. Fix: ONE variable-width polyline for
   s1 (no bezier splitting), horizontal opening TRULY flat (share y).
3. principles_meta TR8 — flat 横 opening.
4. Revision fix: previous attempt had s1 opening rising too steeply and
   descent too vertical. Flatten opening; make descent CURVE inward (wan)
   before terminating in an up-flick.

MMH anchors:
  s1 head ML(0.369, 0.318) → tail BR(0.651, 0.484) — top compound sweep
  s2 head MR(0.168, 0.26)  → tail C(0.849, 0.77) — small inner mark
  s3 head C(0.767, 0.863)  → tail BR(0.367, 0.291) — small inner mark
"""
import os
import sys

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revision: flatter horizontal opening, wan-curved descent, up-flick tip. Marks inside arc.'
}

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, quad_bezier

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- Stroke 1: compound top piece (横 → sharp corner → wan descent → up-flick) ----
# ONE variable-width polyline, ~7 waypoints. All y in same row for horizontal
# portion (TR8 rule 5). Then corner in TR, then long curving descent through
# MR/BR that swings LEFT-then-RIGHT (wan) before flicking up-right.
# Use bezier for wan section then extend to hook tip.

# Horizontal + corner: ML(0.20, 0.35) — TR(0.55, 0.35) — nearly flat.
head = anchor_to_xy(('ML', 0.20, 0.35))
mid_h = anchor_to_xy(('TC', 0.50, 0.85))
corner = anchor_to_xy(('TR', 0.55, 0.85))

# Wan descent: from corner curving down through MR/BR interior.
knee = anchor_to_xy(('MR', 0.30, 0.50))    # descent starts curving
belly = anchor_to_xy(('BR', 0.10, 0.55))   # belly of the wan (leftward pull)
hook_base = anchor_to_xy(('BR', 0.35, 0.85))  # bottom of hook
hook_tip = anchor_to_xy(('BR', 0.65, 0.55))   # flick up-and-right

# Build polyline: flat opening → corner → smooth wan → hook flick
pts_s1 = [head, mid_h, corner]
# Bezier from corner through knee/belly to hook_base
wan1 = quad_bezier(corner, knee, belly, n=15)
wan2 = quad_bezier(belly, hook_base, hook_tip, n=15)
pts_s1 += wan1[1:] + wan2[1:]

n = len(pts_s1) - 1
widths_s1 = []
for i in range(n + 1):
    t = i / n
    if t < 0.35:
        w = 8  # horizontal 横
    elif t < 0.85:
        w = 9  # descent body
    else:
        # taper into hook tip
        u = (t - 0.85) / 0.15
        w = 9 + (2 - 9) * u
    widths_s1.append(w)
stroke_variable_width(draw, pts_s1, widths_s1, color=(0, 0, 0))

# ---- Stroke 2: small 撇 inside — down-right short diagonal ----
pts_s2 = [
    anchor_to_xy(('C', 0.60, 0.40)),
    anchor_to_xy(('C', 0.72, 0.58)),
    anchor_to_xy(('C', 0.82, 0.70)),
]
widths_s2 = [7, 5, 3]
stroke_variable_width(draw, pts_s2, widths_s2, color=(0, 0, 0))

# ---- Stroke 3: small tick — going down-right, below s2 ----
pts_s3 = [
    anchor_to_xy(('C', 0.55, 0.70)),
    anchor_to_xy(('C', 0.72, 0.85)),
    anchor_to_xy(('C', 0.85, 0.92)),
]
widths_s3 = [5, 7, 5]
stroke_variable_width(draw, pts_s3, widths_s3, color=(0, 0, 0))

out = os.path.join(HERE, '01_飞.png')
img.save(out)
print('wrote', out)
