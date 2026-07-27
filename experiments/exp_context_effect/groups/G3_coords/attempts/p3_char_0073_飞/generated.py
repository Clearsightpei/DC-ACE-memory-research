# p3_char_0073_飞 — 3 strokes
#   S1: 横斜钩 — long horizontal top that bends and sweeps down-left,
#              then curves down-right with a small hook flick at end.
#   S2: 小撇 — short 撇 inside the bowl (upper-mid → lower-left).
#   S3: 小点 — small dot to the right of the 撇.
#
# GT observation (300×300, PIL px, y grows DOWN):
#   S1 top-left head ~(50,110), horizontal to ~(175,115), corner-bend
#     down through ~(180,145), ~(170,175), ~(175,215), ~(190,250),
#     hook up-out to ~(200,260) with a small flick.
#   S2 short pie inside: head ~(175,150), tail ~(145,205).
#   S3 dot inside: head ~(155,195), tail ~(180,215).
#
# Rendered fresh (no bank primitive for 横斜钩 exists that matches; 乙 was
# a full envelope. 飞's main stroke is flatter on top with a longer
# horizontal, and the bowl leans right).

import sys
from pathlib import Path

_HELPERS_DIR = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(_HELPERS_DIR))

from PIL import Image, ImageDraw
from _shared_helpers import variant_pie, variant_dian, tapered_bezier, to_px  # noqa: F401

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
draw = ImageDraw.Draw(img)


def stamp(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def piecewise_path(path, widths, steps_per_seg=70):
    for i in range(len(path) - 1):
        x0, y0 = path[i]
        x1, y1 = path[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        for s in range(steps_per_seg + 1):
            u = s / steps_per_seg
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            w = w0 + (w1 - w0) * u
            stamp(x, y, w / 2.0)


# --- S1: 横斜钩 continuous sweep (PIL px directly) ---
# Flat horizontal top → corner-bend at ~(180,120) → gentle inward curve
# down through the bowl → bottom flick with small hook.
s1_path = [
    (48, 112),   # head (thin)
    (80, 106),   # rising slightly
    (118, 104),
    (152, 108),
    (176, 118),  # corner-start
    (188, 132),  # corner apex (顿笔 blob will land here)
    (188, 158),
    (188, 192),
    (196, 224),
    (208, 252),  # bottom-right (bowl bottom)
    (212, 262),  # hook base
    (205, 265),  # hook curl leftward
    (196, 262),  # hook tip up-left
]
s1_widths = [
    2.5, 4.5, 5.5, 6.0, 7.0,
    8.5,             # corner blob
    7.5, 7.0, 7.0, 7.5, 8.0,
    6.0, 2.5,
]
piecewise_path(s1_path, s1_widths, steps_per_seg=70)

# 顿笔 corner blob
stamp(188, 132, 6.0)
# hook base blob
stamp(212, 262, 5.0)

# --- S2: short 撇 inside the bowl (upper mid → lower-left of interior) ---
# PIL(170,150) → math(+20, 0); PIL(150,200) → math(0, -50)
variant_pie(
    draw,
    head=(+20, 0),
    tail=(0, -50),
    bow_perp=-3.0,
    w_head=6.0,
    w_tail=1.5,
    n=48,
)

# --- S3: small 点 to the right of 撇 (clearly separated) ---
# PIL(170,190) → math(+20, -40); PIL(190,215) → math(+40, -65)
variant_dian(
    draw,
    head=(+20, -40),
    tail=(+40, -65),
    w_head=2.0,
    w_tail=8.0,
    bow_perp=-2.0,
    n=32,
)

# Save
out_path = Path(__file__).parent / "01_飞.png"
img.save(out_path)
print(f"Wrote {out_path}")
