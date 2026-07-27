"""
Render 仫 (Mu, minority group name).
Structure: 亻 (person radical, left) + 厶 (right).
- 亻: short 撇 (top) + long straight 竖 below the 撇 attachment
- 厶: 撇折 (a 撇 that bends into a rightward stroke) + 点

Consulted memory: TIER-0 sibling checklist — 仫 not in sibling list;
neither component (亻, 厶) is a sibling-risk target. Straightforward
left-right composition. 亻 gets ~30% width, 厶 gets ~50% width, gap ~10%.
No hooks. Follow form_catalog guidance for 撇 (top-of-radical single flick).
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_line(pts, width_start, width_end, color=(0, 0, 0)):
    """Draw a variable-width polyline by dabbing circles."""
    if len(pts) < 2:
        return
    # sample densely
    total_len = 0
    seg_lens = []
    for i in range(len(pts) - 1):
        dx = pts[i+1][0] - pts[i][0]
        dy = pts[i+1][1] - pts[i][1]
        L = math.hypot(dx, dy)
        seg_lens.append(L)
        total_len += L
    if total_len == 0:
        return
    steps = max(int(total_len * 2), 20)
    for s in range(steps + 1):
        t = s / steps
        # find segment
        target = t * total_len
        acc = 0
        seg_idx = 0
        for i, L in enumerate(seg_lens):
            if acc + L >= target or i == len(seg_lens) - 1:
                seg_idx = i
                local_t = (target - acc) / L if L > 0 else 0
                break
            acc += L
        x = pts[seg_idx][0] + (pts[seg_idx+1][0] - pts[seg_idx][0]) * local_t
        y = pts[seg_idx][1] + (pts[seg_idx+1][1] - pts[seg_idx][1]) * local_t
        w = width_start + (width_end - width_start) * t
        r = w / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=color)

# ---------- 亻 (person radical, left side) ----------
# Short 撇 at top: from upper-right down-left
pie_pts = [(95, 70), (88, 90), (75, 115), (60, 135)]
brush_line(pie_pts, 9, 5)

# Long 竖 (vertical, straight down): starts near the 撇 attachment
shu_pts = [(90, 100), (90, 245)]
brush_line(shu_pts, 10, 9)

# ---------- 厶 (right side) ----------
# 撇折 (single continuous stroke): starts upper-right, sweeps down-left (撇),
# then bends and sweeps to lower-right (折 with slight downward slope forming
# the bottom of the triangle).
# 撇 portion
p_start = (215, 110)
p_corner = (170, 195)  # bottom-left corner of the triangle
brush_line([p_start, (205, 135), (190, 165), p_corner], 7, 5)
# 折 portion — from the corner sweeping right-and-slightly-down
brush_line([p_corner, (200, 205), (235, 215)], 6, 8)

# 点 (dot): short down-right stroke at the top-right, closing the triangle top
dian_pts = [(220, 145), (240, 175), (250, 195)]
brush_line(dian_pts, 4, 10)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0191_仫/01_仫.png")
print("saved")
