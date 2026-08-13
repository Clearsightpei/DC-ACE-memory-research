"""
伪 (wěi) — left 亻 + right 为
Revision: emphasize 为's sweeping 撇 and curved 横折钩;
avoid it reading as a plain rectangle.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def brush(pts, width=6):
    if len(pts) < 2:
        return
    d.line(pts, fill=INK, width=width, joint="curve")
    for p in pts:
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2], fill=INK)


def bezier(p0, p1, p2, n=40):
    return [
        ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0],
         (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1])
        for t in [i / n for i in range(n + 1)]
    ]


# --- Left 亻 (person radical) ---
# 撇 (top going down-left, curved)
pie = bezier((115, 78), (100, 135), (65, 225), n=48)
brush(pie, width=7)

# 竖 (vertical stem, starting from where 撇 begins)
brush([(112, 118), (115, 265)], width=7)


# --- Right 为 ---
# 1) top 点 (small tick upper-left of 为 region)
dot1 = bezier((150, 72), (162, 82), (172, 96), n=20)
brush(dot1, width=7)

# 2) 撇 — long sweeping diagonal from upper-right down to lower-left
pie2 = bezier((205, 90), (170, 165), (130, 250), n=52)
brush(pie2, width=7)

# 3) 横折钩 with curve — start at top-middle, go right, curve down
#    Horizontal top
brush([(178, 118), (240, 108)], width=7)
#    Right-side curve (bowed slightly outward)
right_curve = bezier((240, 108), (252, 175), (232, 245), n=44)
brush(right_curve, width=7)
#    Hook: flick UP-and-LEFT (TIER-0)
hook = bezier((232, 245), (222, 250), (198, 232), n=22)
brush(hook, width=7)

# 4) inner 点 (small dot inside 为)
dot2 = bezier((178, 175), (188, 188), (200, 205), n=20)
brush(dot2, width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0272_伪/01_伪.png")
