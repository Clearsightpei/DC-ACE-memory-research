"""p3_char_0193_癶 retry_1 (bo, "back to back") — G3 attempt.

# VISUAL DIFF (prior 01_癶.png vs gt/phase3/癶.png)
# 1. Prior LEFT top: a single 45-deg diagonal short mark (like a mini 撇).
#    GT LEFT top: an inverted-L shape — a short horizontal going RIGHT
#    then a short hook DOWN. This is the "横撇" / heng-pie head of the
#    left radical. Missing shape → left half unrecognizable.
# 2. Prior RIGHT top: two separated tiny diagonal ticks (dot + tick).
#    GT RIGHT top: a short 撇 (down-left) + a short 横 (down-right) that
#    meet at an apex around the top of the long 捺, forming a small ∧
#    shape. Prior scattered ticks lack the apex meeting.
# 3. Prior BODY: both long strokes are nearly straight and centered too
#    tightly. GT: left long 撇 has clearer outward bow (bulges left),
#    right long 捺 flares outward more strongly. Widen splay.
# 4. Prior missing: the small horizontal "shoulder heng" that sits on
#    top of the right half's long 捺, which in GT is a distinctive
#    short mark going down-right from the apex.

# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): errata says apex convergence; but VISUAL DIFF shows the
#   two halves are SEPARATED in GT (they DON'T meet). Errata's kiss_apex
#   advice is wrong for THIS char. Trust GT (v8 B5 lesson): render each
#   half with its own top hook, no shared apex between halves.
# Q2 (form_catalog): relevant rows — 横撇 (heng-pie composite, for both
#   halves' top marks); long 撇 (left body); long 捺 (right body). Use
#   thin uniform widths (~5px) to match GT's hand-drawn look.
# Q3 (helpers): fail category = per-half compound stroke, NOT X-crossing
#   (bank #201 大_char.py X-crossing does NOT apply here — halves don't
#   cross). No helper — inline fresh per v8 posture.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=5):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=width)
    for p in pts:
        r = width / 2
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="black")


def curve(p0, p1, p2, steps=40, width=5):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    stroke(pts, width=width)


def draw_bo(d):
    # ============ LEFT HALF ============
    # Top of left = 横撇 composite: short horizontal then bend down-left.
    # Horizontal segment (goes rightward slightly downward)
    stroke([(75, 100), (115, 108)], width=5)
    # Short 撇 hook down from end of horizontal
    stroke([(115, 108), (105, 130)], width=5)

    # Main long 撇: starts near top-center-left, sweeps down and left
    # with outward (left) bow — apex around (85, 175), ending low-left.
    curve((130, 105), (85, 180), (55, 255), width=6)

    # ============ RIGHT HALF ============
    # Top of right = small ∧ apex: short 撇 (down-left) meeting short
    # heng-tick (down-right) around x~180, y~110.
    # Short 撇 going down-left
    stroke([(180, 100), (162, 128)], width=5)
    # Short heng-tick going down-right from near the same apex
    stroke([(180, 108), (210, 118)], width=5)

    # Main long 捺: from just below the apex, sweeps down and right with
    # outward (right) bow — flare at end mimicking GT's tapered ending.
    curve((180, 130), (215, 195), (265, 250), width=6)


draw_bo(d)

out = os.path.join(os.path.dirname(__file__), "01_癶.png")
img.save(out)
print("wrote", out)
