# p3_char_0131_冗__retry_1 (G5)
#
# TRAJECTORY DIFF (from inspection of GT PNG + main-attempt PNG):
#   Main FAILed. Concrete visual gaps vs GT:
#     (a) The bottom of 几's right stroke (s4) did NOT wrap deep enough.
#         GT wraps down to y~=280 in BC/BR region; main topped out at
#         belly_bottom = (252, 268). Result: 冗 read as short/squat.
#     (b) The 钩 hook flick in the main was tiny (belly (252,268) → tip
#         (262, 244)) and pointed up-RIGHT with only ~24 px reach. GT
#         hook is clearly visible and finishes higher (MMH tail (262,224)
#         — 44 px above belly-bottom). Main under-reached the hook.
#     (c) s3 pie (left leg of 几) had modest bow. GT pie is a graceful
#         leftward-bowing sweep with visible arc — main's arc was OK but
#         its endpoints (98,149)→(49,284) were correct.
#     (d) Top 冖 was fine visually (mi_cover primitive rendered clean).
#
#   Fix plan for R1:
#     - Keep mi_cover for s1+s2 (top). No change.
#     - Keep draw_pie for s3; bump bow_perp from 12 → 16 for a more
#       clearly-arced left leg.
#     - Inline s4 using the sandbox candidate `heng_zhe_wan_gou` spec
#       (see G5 sandbox.md B5 bank_candidates), with:
#         heng_head=(120,151), corner=(203,148),
#         belly_bottom=(238,285) [WAS 252/268 — deeper wrap],
#         hook_tip=(258,222)     [WAS 262/244 — reach MMH tail (262,224)].
#       Continuous polyline path, tapered.
#
# BANK_DEVIATION
# skipped: (no heng_zhe_wan_gou primitive in bank as of B5 — CRITICAL missing,
#           per sandbox.md; hypothesis-driven candidate spec applied here)
# reason: The 4-segment compound 横折弯钩 has no bank primitive. Inlining
#         from the sandbox candidate spec so a PASS here can promote it.
# fresh_component: heng_zhe_wan_gou_for_几_in_冗 (retry_1 — deeper belly,
#                  MMH-aligned hook tip)

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,         # 4 primitives: mi_cover(=2) + pie + inline hzwg
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],    # s1.mid ~ s2.head N (via mi_cover geometry);
                                     # s3.head (98,149) ~ s4.head (120,151) => 22 px N-compliant
    'overall_pass': None,
    'notes': 'retry_1: deeper wrap + MMH-aligned hook tip + more bow on s3 pie'
}

import sys
import pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from mi_cover import draw_mi_cover
from pie import draw_pie

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


def _bezier3(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        pts.append((b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0],
                    b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]))
    return pts


def _bezier2(p0, p1, p2, n=30):
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0],
                    (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]))
    return pts


# --- Strokes 1 + 2: 冖 top cover via bank primitive ---
draw_mi_cover(d, ox=0, oy=0, scale=1.0)


# --- Stroke 3: 撇 (left leg of 几) ---
# MMH: head ('ML', 0.979, 0.485) = (97.9, 148.5); tail ('BL', 0.489, 0.842) = (48.9, 284.2)
s3_head = (98, 149)
s3_tail = (49, 284)
draw_pie(d, head=s3_head, tail=s3_tail, bow_perp=16, w_head=10, w_tail=2)


# --- Stroke 4: 横折弯钩 (inline; sandbox candidate spec) ---
# MMH: head ('C', 0.201, 0.509) = (120.1, 150.9); tail ('BR', 0.622, 0.238) = (262.2, 223.8)
heng_head = (120, 151)
corner = (203, 148)
belly_bottom = (238, 285)
hook_tip = (258, 222)

# (a) heng head → corner: near-horizontal top segment
heng_pts = []
for i in range(24):
    t = i / 23
    heng_pts.append((heng_head[0] + t * (corner[0] - heng_head[0]),
                     heng_head[1] + t * (corner[1] - heng_head[1])))

# (b) corner → belly_bottom: deep U-wrap via cubic bezier
#   c1 = (corner.x + small, corner.y + big-drop) → keeps line vertical after corner
#   c2 = (belly.x + large, belly.y - small)      → widens the bottom right of the U
wrap_pts = _bezier3(corner,
                    (corner[0] + 15, corner[1] + 90),   # steep drop from corner
                    (belly_bottom[0] + 22, belly_bottom[1] - 12),  # curve right at bottom
                    belly_bottom,
                    n=70)

# (c) belly_bottom → hook_tip: up-right (and slightly-back) 钩 flick
hook_pts = _bezier2(belly_bottom,
                    (belly_bottom[0] + 25, belly_bottom[1] - 20),  # control up-right of belly
                    hook_tip,
                    n=28)

all_pts = heng_pts + wrap_pts[1:] + hook_pts[1:]

# Render as tapered polyline: heavier through the shaft, taper into the hook tip.
n_total = len(all_pts)
n_heng = len(heng_pts)
n_wrap = len(wrap_pts) - 1
n_hook = len(hook_pts) - 1

for i, (x, y) in enumerate(all_pts):
    if i < n_heng:
        # thin lead-in on heng (顿笔 slightly heavier near corner)
        u = i / max(1, n_heng - 1)
        w = 5.5 + 2.0 * u
    elif i < n_heng + n_wrap:
        # shaft/wrap: full weight
        w = 7.5
    else:
        # hook flick: taper from 7 to 2
        u = (i - n_heng - n_wrap) / max(1, n_hook - 1)
        w = 7.0 - 5.0 * u
    d.ellipse([x - w, y - w, x + w, y + w], fill='black')

# 顿笔 dab at the corner for a crisp visible turn
cx, cy = corner
d.ellipse([cx - 4.5, cy - 4.5, cx + 4.5, cy + 4.5], fill='black')

# End cap at heng_head
hx, hy = heng_head
d.ellipse([hx - 4.0, hy - 4.0, hx + 4.0, hy + 4.0], fill='black')


out = pathlib.Path(__file__).parent / '01_冗.png'
img.save(out)
print(f'wrote {out}')
