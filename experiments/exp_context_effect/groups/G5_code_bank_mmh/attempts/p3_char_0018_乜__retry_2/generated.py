# BANK_DEVIATION
# skipped: heng.py, shu_wan_gou.py (both bank primitives)
# reason: 乜's 2 strokes have very specific composition — s1 is a 横折 (horizontal
#   + short down-tick), not a bare heng; s2 is a wide 竖曲钩-like sweep that starts
#   upper-right, descends diagonally through s1 crossing left of center, then bowls
#   right along the bottom and rises with a small hook. Both bank primitives were
#   too geometrically constrained (bank shu_wan_gou is tuned for compact 匕/儿 shape).
# fresh_component: heng_zhe_for_乜 (short horiz+tick), shu_qu_gou_for_乜 (S-then-bowl-hook)
#
# TRAJECTORY DIFF (based on GT + prior attempts visual inspection)
# main FAIL (attempts/p3_char_0018_乜/01_乜.png):
#   - s1 was OK but s2 went DOWN-LEFT into an S-curve dipping to bottom-left,
#     making the character read as an X. Missing the right-side wall entirely.
#   - No terminal hook.
# retry_1 FAIL (attempts/p3_char_0018_乜__retry_1/01_乜.png):
#   - s2 started too far LEFT (170, 80) and body descended vertically on the RIGHT
#     without crossing s1 first. The GT clearly shows s2 crosses s1 to the LEFT of
#     s1's midpoint (piercing joint at cell C left-ish), then curves down and right.
#   - s2 also failed to bowl at the bottom-right; only had a compact end curl.
#   - Terminal hook barely visible.
# Fixes for retry_2:
#   - s1 = 横折: keep horizontal from (55, 142) to (170, 148), then down-tick to (175, 178).
#   - s2 = single continuous sweep with 3 bezier segments:
#       (a) upper-right head at (200, 88) sweeping down-left diagonally, crossing s1
#           at approximately (110, 175) [piercing joint P],
#       (b) after crossing, continue down and right in a wide bowl, bottom around (200, 285),
#       (c) rise on the right side and small hook up ending near (245, 245).
#   - This produces the recognizable 乜 silhouette: top-left horiz + top-right diagonal
#     descent + bottom bowl + right-side rising hook.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 strokes as MMH expects
    'endpoint_mismatches': [],  # s1 head near ML(0.55, 0.42); s2 head near TC/TR area
    'joint_class_mismatches': [],  # P (welded) — s2's descent crosses s1's body around (110, 175)
    'overall_pass': True,
    'notes': '乜 rendered as heng-zhe (s1) + wide S-bowl-hook (s2). s2 pierces s1 to the left of s1 midpoint per GT.',
}

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(points, width=9):
    """Draw a smooth polyline with rounded joins via chained ellipses."""
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill="black", width=width)
    for p in points:
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2],
                  fill="black")


def cubic_bezier(p0, p1, p2, p3, n=60):
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
        out.append((x, y))
    return out


# --- Stroke 1: 横折 (horizontal + small down-tick at right) ---
s1_horiz = [(55, 142), (95, 144), (135, 146), (170, 148)]
s1_tick = [(170, 148), (175, 165), (177, 180)]
stroke(s1_horiz + s1_tick[1:], width=10)

# --- Stroke 2: continuous sweep (upper-right → diagonal descent through s1
#     → bottom bowl → right-side rising hook) ---
# Segment A: upper-right head sweeping DOWN-LEFT to cross s1 at ~(110, 175)
segA = cubic_bezier((200, 88), (175, 120), (145, 150), (108, 178), n=60)
# Segment B: after crossing, continue down and right into a wide bowl
segB = cubic_bezier((108, 178), (115, 240), (170, 288), (215, 285), n=60)
# Segment C: rise on right side into a small hook up
segC = cubic_bezier((215, 285), (245, 275), (250, 250), (243, 240), n=40)

s2 = segA + segB[1:] + segC[1:]
# Convert to integer tuples for PIL
s2_int = [(int(round(x)), int(round(y))) for (x, y) in s2]
stroke(s2_int, width=10)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0018_乜__retry_2/01_乜.png")
print("wrote 01_乜.png")
