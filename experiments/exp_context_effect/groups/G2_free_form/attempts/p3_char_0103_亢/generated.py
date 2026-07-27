"""
亢 — 4 strokes: 点 (top dot), 横 (long lid), 撇 (left leg), 竖弯钩 (right leg with hook)
Structure: 亠 top-lid + leg-pair (per form_catalog "撇+竖弯钩 as leg-pair under a lid")
Siblings by structure: 无, 旡, 兀, 尢 (all leg-pair under lid).
GT check: dot is small tick above lid slightly right-of-center; 横 spans wide;
legs splay outward under the lid; 竖弯钩 arcs right at baseline and hooks up-left.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

# 1) 点 — small dot/tick above the lid, slightly right of center (GT shows a small arc tick)
dot = [(155, 70), (170, 88)]
stroke(dot, width=8)

# 2) 横 — long horizontal lid, spans wide (from ~x=55 to ~x=250) at y~=112
heng = [(55, 112), (250, 112)]
stroke(heng, width=8)

# 3) 撇 — left leg: starts inside the lid at left-middle (~x=110, y=115),
#    throws down-left curving to (~x=55, y=260)
pie_pts = []
p0 = (115, 118)
p1 = (95, 175)
p2 = (75, 220)
p3 = (55, 265)
# quadratic-ish sampling via segments with slight curve
for t_int in range(0, 21):
    t = t_int / 20.0
    # cubic bezier-ish
    x = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t)*t*t * p2[0] + t**3 * p3[0]
    y = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t)*t*t * p2[1] + t**3 * p3[1]
    pie_pts.append((x, y))
stroke(pie_pts, width=8)

# 4) 竖弯钩 — right leg: starts at right-middle of lid (~x=185, y=115),
#    descends nearly vertical, arcs rightward at baseline, terminal hook up-left
shu = []
# vertical descent from (185,115) to (190, 235)
for t_int in range(0, 15):
    t = t_int / 14.0
    x = 185 + 5 * t
    y = 115 + (235 - 115) * t
    shu.append((x, y))
# arc rightward: from (190,235) sweeping to (245,268)
cx, cy = 245, 235
r = 55
# arc from angle 180deg to ~80deg
for a_deg in range(180, 79, -5):
    a = math.radians(a_deg)
    x = cx + r * math.cos(a)
    y = cy + r * math.sin(a) + 0  # sin(180)=0, sin(90)=1 so grows to cy+r
    shu.append((x, y))
# terminal hook: up-and-left from arc end
end = shu[-1]
hook_end = (end[0] - 10, end[1] - 22)
shu.append(hook_end)
stroke(shu, width=8)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0103_亢/01_亢.png"
img.save(out)
print("saved", out, img.size)
