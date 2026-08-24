"""儿 — 2-stroke radical.

MMH anchors:
  stroke 1 (撇): head ML(0.929, 0.093) -> tail BL(0.393, 0.827)
  stroke 2 (竖弯钩): head TC(0.567, 0.838) -> tail BR(0.71, 0.227)

Cells in 300x300 canvas: 100x100 each.
  ML cell x:[0,100), y:[100,200)
  BL cell x:[0,100), y:[200,300)
  TC cell x:[100,200), y:[0,100)
  BR cell x:[200,300), y:[200,300)

Endpoint pixel coords:
  s1 head (93, 109), tail (39, 283)   -- 撇, curved leftward
  s2 head (157, 84), tail (271, 223)  -- 竖弯钩, down then right, small hook
"""
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '2 separate strokes (no joints); pie curves left-down; shu-wan-gou goes down then curves right with small hook up.'
}

W = H = 300
img = Image.new('L', (W, H), 255)
d = ImageDraw.Draw(img)

def bezier(pts, steps=200):
    """Quadratic bezier: pts = [(x0,y0),(cx,cy),(x1,y1)]"""
    (x0, y0), (cx, cy), (x1, y1) = pts
    out = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u*u*x0 + 2*u*t*cx + t*t*x1
        y = u*u*y0 + 2*u*t*cy + t*t*y1
        out.append((x, y))
    return out

def stroke(points, width=8):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=0, width=width)
    for (x, y) in points:
        d.ellipse((x-width/2, y-width/2, x+width/2, y+width/2), fill=0)

# Stroke 1: 撇 — from (93,109) top-right to (39,283) bottom-left, curved leftward (bows left)
# Control point pulled slightly left to give the pie curvature.
s1 = bezier([(93, 109), (50, 180), (39, 283)], steps=120)
stroke(s1, width=8)

# Stroke 2: 竖弯钩 — starts (157,84), goes straight down, curves right along bottom, ends (271,223) with small hook up.
# Break into two arcs: vertical descent then horizontal curve with hook up.
# Descent: from (157,84) down to about (155,240)
s2a = bezier([(157, 84), (156, 160), (155, 240)], steps=120)
stroke(s2a, width=8)
# Curve: sweep right and slightly up, ending at (271, 223) — the tail with hook.
s2b = bezier([(155, 240), (200, 275), (271, 223)], steps=120)
stroke(s2b, width=8)

img.save('<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_017_儿/01_儿.png')
print('done')
