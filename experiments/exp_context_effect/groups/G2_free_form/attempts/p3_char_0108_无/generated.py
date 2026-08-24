"""
无 (wu2) — 4 strokes. REVISION 1.

Consult (per memory_index.md):
- form_catalog "二 as top-of-radical stacked pair (无/旡/云-top)":
  two 横 stacked, top slightly SHORTER than bottom.
- form_catalog "撇 + 竖弯钩 as leg-pair under a lid (无/旡/兀/尢)":
  撇 from lid area throws down-left; 竖弯钩 from right descends,
  arcs rightward at baseline, hooks UP-and-LEFT.

# FLICK CHECK (per sibling_signature_checklist.md):
#   竖弯钩 flick: UP-and-LEFT after the arc (~-105° to -115°).

Revision notes: attempt-1 竖弯钩 too small and cramped. Extend descent
deeper and give the horizontal arc more sweep so the right leg has
proper 竖弯钩 presence (roughly baseline-parallel bottom).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(pts, w=8):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=w)
    for p in pts:
        r = w / 2
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=BLACK)


def bezier(ctrl, n=41):
    out = []
    for t in [i / (n - 1) for i in range(n)]:
        a = list(ctrl)
        while len(a) > 1:
            a = [((1 - t) * a[i][0] + t * a[i + 1][0],
                  (1 - t) * a[i][1] + t * a[i + 1][1]) for i in range(len(a) - 1)]
        out.append(a[0])
    return out


# ---- Stroke 1: top 横 (shorter, slight up-right tilt) ----
line([(105, 82), (215, 74)], w=8)

# ---- Stroke 2: bottom 横 (longer, slight up-right tilt) ----
line([(55, 132), (245, 120)], w=8)

# ---- Stroke 3: 撇 — starts upper-right ABOVE the top 横,
# pierces down through both 横 on the right side, curves down-left
# and sweeps to the lower-left corner ----
撇_ctrl = [(175, 55), (150, 130), (110, 210), (55, 280)]
pts = bezier(撇_ctrl, n=50)
# taper: thick to thin
for i in range(len(pts) - 1):
    w = max(3, 9 - int(6 * (i / len(pts))))
    d.line([pts[i], pts[i + 1]], fill=BLACK, width=w)
# start cap
d.ellipse([172, 51, 178, 57], fill=BLACK)

# ---- Stroke 4: 竖弯钩 — starts on the bottom 横 around x=175,
# descends nearly vertically to y~230, arcs rightward along the
# baseline to about x=245, then hooks UP-and-LEFT ~-110° ----

# The 竖弯钩 as a continuous Bezier:
#   Start (top): (180, 125)  — meets bottom 横
#   Descent bottom: (180, 235)
#   Arc curl-corner: (195, 260)
#   Arc end (rightward): (250, 258)
弯钩_ctrl = [(180, 125), (180, 210), (183, 250), (215, 262), (250, 258)]
pts = bezier(弯钩_ctrl, n=60)
for i in range(len(pts) - 1):
    d.line([pts[i], pts[i + 1]], fill=BLACK, width=8)

# Hook: from (250, 258) flick UP-and-LEFT (~-110°)
# length ~20 px
end = (250, 258)
angle = math.radians(-110)  # image coords: -110° means up-and-slightly-left
hook_end = (end[0] + 22 * math.cos(angle), end[1] + 22 * math.sin(angle))
d.line([end, hook_end], fill=BLACK, width=7)

# Caps
for p in [(180, 125), end, hook_end]:
    r = 4
    d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=BLACK)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0108_无/01_无.png"
img.save(out)
print(f"wrote {out}")
