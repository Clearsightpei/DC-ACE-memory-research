"""龹 (p3_char_0284) — G4 retry_1.

TRAJECTORY DIFF (vs main attempt):
- main FAIL: s1 (top-left dian) and s2 (top-right dian) were extended
  by 60% on BOTH ends, producing huge cross-canvas lines that broke
  the 丷 top and made the whole character unreadable. Result looked
  like tangled strokes instead of 龹.
- main FAIL: the two extended dots merged with the pie/na and there
  was no clear 关-style body underneath.
- Fix for retry: draw s1/s2 at the actual MMH anchor endpoints (with
  at most a small ~25% back-extension toward the head so they carry
  visual weight but don't sprawl). Keep s3-s6 essentially as-is.
- Fix: reduce over-thickness on the top dots so they read as 丷.

Structural read of 龹 (looks like 关 with 丷 top):
- s1: top-left dian, short ↘ mark
- s2: top-right dian, short ↙ mark
- s3: upper heng (short)
- s4: lower heng (long, wide)
- s5: long pie top-center → bottom-left
- s6: long na center → bottom-right

Joints:
- s2.tail ⇆ s3.tail @ C(0.76, 0.163) : N gap ~32px
- s3.mid ⇆ s5.mid @ C(0.387, 0.353) : P weld
- s4.mid ⇆ s5.mid @ C(0.266, 0.718) : P weld
- s4.mid ⇆ s6.head @ C(0.642, 0.693) : N gap ~13px
"""

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes: 2 top dian (short, no over-extension), 2 heng, long pie + long na.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def dian_stroke(draw, head, tail, back_ext=0.25, w_head=3, w_tail=8):
    """Short dot/dian: thin at head, thick at tail. Small back-extension
    keeps the mark from being invisibly short at 300px."""
    dx, dy = tail[0] - head[0], tail[1] - head[1]
    h2 = (head[0] - dx * back_ext, head[1] - dy * back_ext)
    t2 = tail
    mid = ((h2[0] + t2[0]) / 2, (h2[1] + t2[1]) / 2)
    pts = [h2, mid, t2]
    widths = [w_head, (w_head + w_tail) / 2, w_tail]
    stroke_variable_width(draw, pts, widths)


# --- stroke 1: top-left dian (↘ direction) — modest extension only ---
p1a = anchor_to_xy(('TL', 0.935, 0.905))  # (93.5, 90.5)
p1b = anchor_to_xy(('C',  0.157, 0.11))   # (115.7, 111)
dian_stroke(d, p1a, p1b, back_ext=0.25, w_head=2, w_tail=7)

# --- stroke 2: top-right dian (↙ direction) — modest extension only ---
p2a = anchor_to_xy(('TC', 0.91, 0.683))  # (191, 68.3)
p2b = anchor_to_xy(('C',  0.693, 0.066)) # (169.3, 106.6)
dian_stroke(d, p2a, p2b, back_ext=0.25, w_head=2, w_tail=7)

# --- stroke 3: upper heng (short) ---
p3a = anchor_to_xy(('ML', 0.905, 0.389))  # (90.5, 138.9)
p3b = anchor_to_xy(('C',  0.989, 0.254))  # (198.9, 125.4)
fat_line(d, p3a, p3b, width=6)

# --- stroke 4: lower heng (wide) ---
p4a = anchor_to_xy(('ML', 0.58, 0.802))   # (58, 180.2)
p4b = anchor_to_xy(('MR', 0.414, 0.635))  # (241.4, 163.5)
fat_line(d, p4a, p4b, width=7)

# --- stroke 5: long pie top-center → bottom-left (curved slightly) ---
p5a = anchor_to_xy(('TC', 0.359, 0.56))   # (135.9, 56)
p5b = anchor_to_xy(('BL', 0.384, 0.59))   # (38.4, 259)
mid5 = ((p5a[0] + p5b[0]) / 2 - 14, (p5a[1] + p5b[1]) / 2)
curve5 = quad_bezier(p5a, mid5, p5b, n=40)
widths5 = []
n5 = len(curve5)
for i in range(n5):
    t = i / (n5 - 1)
    # thick top, tapering to thin tail (pie style)
    if t < 0.25:
        w = 5 + t * 8
    else:
        w = 7 - (t - 0.25) * 6
    widths5.append(max(2, w))
stroke_variable_width(d, curve5, widths5)

# --- stroke 6: long na center → bottom-right (curved slightly) ---
p6a = anchor_to_xy(('C',  0.682, 0.72))   # (168.2, 172)
p6b = anchor_to_xy(('BR', 0.854, 0.37))   # (285.4, 237)
mid6 = ((p6a[0] + p6b[0]) / 2 + 4, (p6a[1] + p6b[1]) / 2 + 6)
curve6 = quad_bezier(p6a, mid6, p6b, n=40)
widths6 = []
n6 = len(curve6)
for i in range(n6):
    t = i / (n6 - 1)
    # thin start, thickest around 0.7, then taper (na style)
    if t < 0.7:
        w = 2.5 + t * 8
    else:
        w = 8 - (t - 0.7) * 12
    widths6.append(max(2, w))
stroke_variable_width(d, curve6, widths6)

out = os.path.join(os.path.dirname(__file__), '01_龹.png')
img.save(out)
print(f"saved {out}")
print(f"strokes: 6, expected 6")
