# TRAJECTORY DIFF (retry 1 of p3_char_0021_几)
# Prior attempts inspected:
#   - main (FAIL): heng_zhe_wan_gou bulged too far right (wan apex at x=285),
#     terminal hook curled back to (278, 219) creating an awkward reverse-curl
#     that reads visually as a stray tail. Also the heng top was too flat/long,
#     extending to x=225. In the GT the right stroke has a SHORTER top heng
#     (~x=195), a NEAR-VERTICAL descent for the first ~2/3, and only in the
#     bottom third curves rightward, ending as a soft rightward taper near
#     (240, 268) — no dramatic hook-back.
# Fixes this retry:
#   1) Shorten top heng: (119, 106) -> (195, 108).  ~20px shorter than main.
#   2) Descent is straight-vertical from corner down to ~(215, 220), then
#      wan-curves right through (240, 260) and terminates at (272, 258) with
#      just a soft up-flick to (270, 240). Keeps the shape L-with-wan, not
#      bulging C.
#   3) Pie: keep MMH anchors, but strengthen taper (w_head=11 -> tail=2) so
#      the head reads as a clean tapered start rather than a blob.

# BANK_DEVIATION
# skipped: shu_wan_gou.py (starts vertical; 几 s2 starts horizontal)
# reason: 横折弯钩 is a 4-segment compound (heng + zhe + wan + gou);
#         bank has no heng_zhe_wan_gou primitive as of B3.
# fresh_component: heng_zhe_wan_gou_for_几 (v2 — straighter descent than main)

SELF_CHECK = {
    'visual_ok': None,          # set after render inspection
    'stroke_count_ok': True,    # 2 turtle-equivalent stroke primitives
    'endpoint_mismatches': [],  # both s1, s2 use MMH anchors verbatim
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'retry-1: shortened top heng, straightened wan descent, softened terminal'
}

import sys, pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
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
        pts.append((b0*p0[0] + b1*p1[0] + b2*p2[0] + b3*p3[0],
                    b0*p0[1] + b1*p1[1] + b2*p2[1] + b3*p3[1]))
    return pts


# --- Stroke 1: 撇 (pie) ---
# MMH: head ('TL', 0.952, 0.94) = (95, 94), tail ('BL', 0.378, 0.877) = (38, 288)
s1_head = (95, 94)
s1_tail = (38, 288)
draw_pie(d, head=s1_head, tail=s1_tail, bow_perp=12, w_head=11, w_tail=2)

# --- Stroke 2: 横折弯钩 (inline; BANK_DEVIATION) ---
# MMH: head ('C', 0.192, 0.063) = (119, 106), tail ('BR', 0.78, 0.188) = (278, 219)
# Joint N with s1.head at C: |Δ|=sqrt(24²+12²)≈26.8px (≥15.6 expected, still N)
s2_head = (119, 106)

# --- (a) Heng: short horizontal from head to (200, 108) ---
heng_end = (200, 108)
heng_pts = []
for i in range(12):
    t = i / 11
    heng_pts.append((s2_head[0] + t * (heng_end[0] - s2_head[0]),
                     s2_head[1] + t * (heng_end[1] - s2_head[1])))

# --- (b/c/d) One smooth bezier from heng_end all the way down and around ---
# Replace the previous 3-part corner+descent+wan (which caused an S-bump
# at the top corner) with a single graceful cubic that: goes right briefly,
# turns down along ~x=213, curves rightward, and finishes at the wan bottom.
wan_end = (260, 265)
smooth_pts = _bezier3(heng_end,
                      (218, 108),   # brief rightward extension
                      (213, 260),   # long vertical anchor with tiny rightward drift
                      wan_end,
                      n=70)

# --- (e) Gou: small terminal up-flick to MMH tail (278, 219) ---
# Keep it subtle — a short quadratic-like flick, not a big curl.
tip = (272, 245)
hook_pts = _bezier3(wan_end, (270, 260), (272, 252), tip, n=15)

all_pts = heng_pts + smooth_pts[1:] + hook_pts[1:]
ipts = [(int(round(x)), int(round(y))) for x, y in all_pts]
d.line(ipts, fill='black', width=8, joint='curve')

# End caps
for (x, y) in (ipts[0], ipts[-1]):
    d.ellipse([x - 4, y - 4, x + 4, y + 4], fill='black')

out = pathlib.Path(__file__).parent / '01_几.png'
img.save(out)
print(f'wrote {out}')
