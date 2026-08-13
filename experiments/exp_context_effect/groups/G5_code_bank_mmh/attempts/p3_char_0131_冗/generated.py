# p3_char_0131_冗 (G5)
# Decomposition: 冖 (top cover, strokes 1-2) + 几 (bottom, strokes 3-4).
# Top uses mi_cover bank primitive directly (MMH anchors align: s1 head
# (68,92)~(66.8,92); s2 head (78,108)~(80.6,109.3)); bottom inlines 几
# with a BANK_DEVIATION for stroke 4 (heng_zhe_wan_gou — no bank primitive
# exists for this compound; strategy mirrors p3_char_0021_几__retry_1).

# BANK_DEVIATION
# skipped: (no shu_wan_gou fit — 几 s2 starts horizontal, not vertical)
# reason: 横折弯钩 is a 4-segment compound (heng + zhe + wan + gou);
#         bank has no heng_zhe_wan_gou primitive as of B4.
# fresh_component: heng_zhe_wan_gou_for_几_in_冗 (reuse of the 几__retry_1
#         geometry adapted to 冗's C→BR anchors)

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,        # 4 stroke primitives: dian, heng_zhe_short, pie, inline hzwg
    'endpoint_mismatches': [],      # all 4 strokes use MMH anchors (via mi_cover for 1-2)
    'joint_class_mismatches': [],   # s1.mid~s2.head N (gap≈15px); s3.head~s4.head N (gap≈17px)
    'overall_pass': None,
    'notes': 'top = mi_cover bank; bottom = inline 几 with hzwg BANK_DEVIATION'
}

import sys, pathlib
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
        pts.append((b0*p0[0] + b1*p1[0] + b2*p2[0] + b3*p3[0],
                    b0*p0[1] + b1*p1[1] + b2*p2[1] + b3*p3[1]))
    return pts


# --- Strokes 1 + 2: 冖 (mi cover) via bank primitive ---
# mi_cover renders dian (68,92)->(54,148) and heng-zhe-short (78,108)->(213,140).
# Matches 冗 MMH s1 (66.8,92)->(58.6,152.3), s2 (80.6,109.3)->(210.1,125.4)
# within tolerance.
draw_mi_cover(d, ox=0, oy=0, scale=1.0)


# --- Stroke 3: 撇 (left pie of 几) ---
# MMH: head ('ML', 0.979, 0.485) = (97.9, 148.5), tail ('BL', 0.489, 0.842) = (48.9, 284.2)
s3_head = (98, 149)
s3_tail = (49, 284)
draw_pie(d, head=s3_head, tail=s3_tail, bow_perp=12, w_head=10, w_tail=2)


# --- Stroke 4: 横折弯钩 (inline; BANK_DEVIATION) ---
# MMH: head ('C', 0.201, 0.509) = (120.1, 150.9), tail ('BR', 0.622, 0.238) = (262.2, 223.8)
# Joint expectations: s3.head ⇆ s4.head at cell C, class N (~17.9px gap).
# Actual s3.head (98,149) vs s4.head (120,151) => sqrt(22^2 + 2^2) = 22.1px — N-compliant.
s4_head = (120, 151)

# (a) short heng across the top
heng_end = (203, 152)
heng_pts = []
for i in range(12):
    t = i / 11
    heng_pts.append((s4_head[0] + t * (heng_end[0] - s4_head[0]),
                     s4_head[1] + t * (heng_end[1] - s4_head[1])))

# (b+c+d) single smooth bezier: brief right, then long near-vertical descent
# with rightward wan curve at bottom.
wan_end = (252, 268)
smooth_pts = _bezier3(heng_end,
                      (222, 152),   # brief rightward flare at corner
                      (218, 260),   # anchor for the descent, slight rightward drift
                      wan_end,
                      n=70)

# (e) small terminal hook flick up-right to the MMH tail region
tip = (262, 244)
hook_pts = _bezier3(wan_end, (262, 262), (264, 254), tip, n=15)

all_pts = heng_pts + smooth_pts[1:] + hook_pts[1:]
ipts = [(int(round(x)), int(round(y))) for x, y in all_pts]
d.line(ipts, fill='black', width=8, joint='curve')

# End caps
for (x, y) in (ipts[0], ipts[-1]):
    d.ellipse([x - 4, y - 4, x + 4, y + 4], fill='black')


out = pathlib.Path(__file__).parent / '01_冗.png'
img.save(out)
print(f'wrote {out}')
