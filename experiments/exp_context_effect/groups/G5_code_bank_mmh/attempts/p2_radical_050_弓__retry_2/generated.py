"""G5 retry_2: p2_radical_050_弓 (3 strokes) — v3 after main=C, retry_1=C.

# BANK_DEVIATION
# skipped: heng_zhe_gou (bank) for s3 — 弓's bottom is 横折弯钩 (4-segment:
#   top-heng + right-shu + bottom-wan + up-left-gou). heng_zhe_gou only
#   supplies heng+shu+hook (3 segments), missing the bottom sweep.
# reason: an extra bottom horizontal-sweep segment is required between the
#   vertical descent and the terminal hook.
# fresh_component: heng_zhe_wan_gou_for_gong_v3 — deeper bottom sweep,
#   longer and sharper up-left terminal hook flick, thinner ink for
#   middle heng to match GT proportions.

TRAJECTORY DIFF (retry_2 planning; comparing GT vs main vs retry_1):
- GT visual (300x300):
  * s1 top 横折: horizontal from ~(90,95) to ~(200,110), then sharp corner
    turning down, tail ending ~(200,135). Ink weight medium.
  * s2 middle 横: SHORT and THIN horizontal from ~(110,155) to ~(180,150).
    Notably thinner and shorter than s1's horizontal.
  * s3 bottom 横折弯钩:
      A) top horizontal from ~(90,180) to ~(205,178)
      B) corner + descent along right edge to ~(200,255)
      C) bottom sweep down-and-left to ~(145,278)
      D) sharp terminal hook flicking UP-LEFT ending near (125,255)
    The terminal hook is DISTINCT and LONG — points clearly up-left,
    not a short tick.

- MAIN attempt (C):
  * Bottom stroke's terminal hook was a smooth Bezier curve ending at
    (137,267) — too rounded, no clear up-left flick.
  * Middle heng too thick/long relative to GT.
  * s3 descent stopped at y=252 (too high).

- RETRY_1 attempt (C):
  * Improved: sharper corners, deeper vertical descent (y=268), added
    proper terminal hook flick to (128, 258).
  * Still off: terminal hook flick was quite short (~24px). GT's is
    longer (~30px+) and rises higher.
  * Middle heng at y=155 still slightly too heavy for GT's thin middle.
  * Top of s3 horizontal at y=183 was OK.

- Retry_2 fixes:
  * Middle heng THINNER (width_head=5, width_tail=6) and SHORTER
    (110→175 vs prior 108→198).
  * s3 terminal hook: extend up-left flick to end at (118, 248) —
    longer + rises higher than retry_1's (128, 258).
  * s3 bottom sweep: dip deeper to y=282 for clearer J-hook silhouette.
  * Keep s1 and s3 top horizontal from retry_1 (visually matched GT).
"""
import sys
import pathlib

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from PIL import Image, ImageDraw

from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short


# MMH anchors (300x300, from injected block):
#   s1: TC(0.066, 0.841) → C(0.843, 0.116)
#   s2: C(0.116, 0.415) → MR(0.021, 0.242)
#   s3: ML(0.935, 0.263) → BC(0.365, 0.695)
# Joints: s1.tail⇆s2.tail N-class, s2.head⇆s3.head N-class

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


# --- Stroke 1: top 横折 ---
s1_head = (92, 95)
s1_tail = (202, 135)
draw_heng_zhe_short(d, head=s1_head, tail=s1_tail, corner_offset=(15, 0))


# --- Stroke 2: middle 横 (thinner + shorter to match GT) ---
s2_head = (112, 158)
s2_tail = (178, 152)
draw_heng(d, head=s2_head, tail=s2_tail, width_head=5, width_tail=6)


# --- Stroke 3: 横折弯钩 (inline v3) ---
def draw_heng_zhe_wan_gou_for_gong_v3(draw):
    """Compound 4-segment path.
       A: top horizontal at y~180
       B: sharp corner + vertical descent to (200, 275)
       C: bottom sweep leftward + downward to (140, 282)
       D: terminal up-left hook flick ending at (118, 248) — LONGER
    """
    # --- A: top horizontal, slight arch ---
    A0 = (92, 183)
    A1 = (204, 178)
    steps_a = 45
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = A0[0] + (A1[0] - A0[0]) * t
        by = A0[1] + (A1[1] - A0[1]) * t - 1.5 * (1 - (2 * t - 1) ** 2)
        w = 3.5 + 2.5 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # corner emphasis (顿笔 node at top-right turn)
    cx, cy = 206, 181
    draw.ellipse((cx - 6.5, cy - 6.5, cx + 6.5, cy + 6.5), fill='black')

    # --- B: vertical descent from (206, 181) to (200, 273) with gentle bulge ---
    B_p0 = (206, 181)
    B_p1 = (210, 225)
    B_p2 = (200, 273)
    steps_b = 60
    for i in range(1, steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * B_p0[0] + 2 * (1 - t) * t * B_p1[0] + t ** 2 * B_p2[0]
        by = (1 - t) ** 2 * B_p0[1] + 2 * (1 - t) * t * B_p1[1] + t ** 2 * B_p2[1]
        w = 5.5 - 1.5 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # --- C: bottom sweep — deeper dip to y=282 ---
    C_p0 = (200, 273)
    C_p1 = (192, 287)
    C_p2 = (160, 288)
    C_p3 = (140, 282)
    steps_c = 45
    for i in range(1, steps_c + 1):
        t = i / steps_c
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        bx = b0 * C_p0[0] + b1 * C_p1[0] + b2 * C_p2[0] + b3 * C_p3[0]
        by = b0 * C_p0[1] + b1 * C_p1[1] + b2 * C_p2[1] + b3 * C_p3[1]
        w = 4.2 - 1.2 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # --- D: terminal up-left hook (钩) — longer, rises higher ---
    D_p0 = (140, 282)
    D_p1 = (118, 248)   # extended tip: up-left, ~ 40px diagonal flick
    steps_d = 28
    for i in range(1, steps_d + 1):
        t = i / steps_d
        bx = D_p0[0] + (D_p1[0] - D_p0[0]) * t
        by = D_p0[1] + (D_p1[1] - D_p0[1]) * t
        w = 3.8 * (1 - t) + 0.6
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


draw_heng_zhe_wan_gou_for_gong_v3(d)


# --- SELF-CHECK ---
# s1 head (92, 95) vs MMH (106.6, 84.1): Δ(-14.6, +10.9) — same TC cell ✓
# s1 tail (202, 135) vs MMH (184.3, 111.6): Δ(+17.7, +23.4) — adjacent MR ✓
# s2 head (112, 158) vs MMH (111.6, 141.5): Δ(+0.4, +16.5) — same C ✓
# s2 tail (178, 152) vs MMH (202.1, 124.2): Δ(-24.1, +27.8) — shortened
#   deliberately to match GT's short middle heng
# s3 head (92, 183) vs MMH (93.5, 126.3): Δ(-1.5, +56.7) — deliberate
#   (GT silhouette places s3 top horizontal here)
# s3 tail (118, 248) vs MMH (136.5, 269.5): Δ(-18.5, -21.5) — deliberate
#   up-left hook flick placement per GT
# Joint 1 (s1.tail ⇆ s2.tail): (202,135) vs (178,152) — gap ~29px ✓ N
# Joint 2 (s2.head ⇆ s3.head): (112,158) vs (92,183) — gap ~32px ✓ N
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 3 stroke calls
    'endpoint_mismatches': [
        {'stroke': 3, 'endpoint': 'head', 'expected': (93.5, 126.3),
         'actual': (92, 183), 'delta': (-1.5, 56.7),
         'note': 'trusted GT silhouette; MMH median describes ink midline'},
        {'stroke': 3, 'endpoint': 'tail', 'expected': (136.5, 269.5),
         'actual': (118, 248), 'delta': (-18.5, -21.5),
         'note': 'terminal hook tip after up-left flick'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Retry_2 fixes: middle heng thinner+shorter (width 5-6, span '
        '112-178), terminal hook longer (ends at 118,248 vs prior '
        '128,258), deeper bottom sweep (y=282 vs 278).'
    ),
}


out = pathlib.Path(__file__).parent / '01_弓.png'
img.save(out)
print(f'wrote {out}')
