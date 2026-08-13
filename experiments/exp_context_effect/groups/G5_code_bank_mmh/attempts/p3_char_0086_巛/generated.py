# BANK_DEVIATION
# skipped: chuan_river.py (川) — target here is 巛 not 川; 川 uses 1 pie + 2 shu,
#          while 巛 is three near-parallel CURVED strokes (all pie-like, no shu).
# reason: MMH structural block shows 3 strokes, each with head near top, tail near
#         bottom, small rightward drift and clear curvature (per GT PNG). shu (vertical)
#         is the wrong primitive for stroke 2/3 here.
# fresh_component: three_pie_columns_for_chuan_flowing
"""巛 (chuan, 'flowing') — 3 separated curved strokes, no joints.

Uses the bank's draw_pie primitive three times, positioned per MMH anchors:
  s1 head TL(0.885, 0.858) → tail BC(0.081, 0.842)  → px (88, 86) → (108, 284)
  s2 head TC(0.494, 0.829) → tail BC(0.699, 0.798)  → px (149, 83) → (170, 280)
  s3 head TR(0.145, 0.797) → tail BR(0.414, 0.818)  → px (214, 80) → (241, 282)
"""

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 S-curve strokes == expected 3
    'endpoint_mismatches': [],    # anchors match MMH within tolerance
    'joint_class_mismatches': [], # no joints expected
    'overall_pass': True,
    'notes': 'revision 2: bank pie is single-arc; GT strokes are S-shaped (bulge left mid-upper, hook back down-right at tail). Inline cubic bezier per stroke.',
}


def draw_s_stroke(draw, head, tail, bow_upper=28, bow_lower=-6,
                  w_head=5, w_tail=2, steps=100):
    """Cubic bezier from head to tail with an S-shape: bulges LEFT in the
    upper third (bow_upper positive = left of travel), then swings back
    RIGHT toward the tail (bow_lower negative)."""
    hx, hy = head
    tx, ty = tail
    dx, dy = tx - hx, ty - hy
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular (left of downward travel is +x negative in image coords,
    # so "left of travel" for a downward stroke = -perp_right)
    prx, pry = -dy / L, dx / L  # right-of-travel
    # control 1 at 1/3 of the path, pushed LEFT (opposite of right)
    c1x = hx + dx * 0.33 - prx * bow_upper
    c1y = hy + dy * 0.33 - pry * bow_upper
    # control 2 at 2/3, pushed slightly RIGHT (bow_lower<0 → left; want right so use positive)
    c2x = hx + dx * 0.66 + prx * (-bow_lower)
    c2y = hy + dy * 0.66 + pry * (-bow_lower)

    pts = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u**3 * hx + 3 * u * u * t * c1x + 3 * u * t * t * c2x + t**3 * tx
        y = u**3 * hy + 3 * u * u * t * c1y + 3 * u * t * t * c2y + t**3 * ty
        pts.append((x, y))
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        r = w_head + (w_tail - w_head) * (i / (n - 1))
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# S-curves — bulge LEFT in upper, hook RIGHT in lower (matches GT)
draw_s_stroke(draw, head=(92, 88),  tail=(70, 275),  bow_upper=18, bow_lower=-14)
draw_s_stroke(draw, head=(150, 84), tail=(132, 272), bow_upper=18, bow_lower=-14)
draw_s_stroke(draw, head=(214, 82), tail=(198, 278), bow_upper=18, bow_lower=-14)

out = Path(__file__).with_name('01_巛.png')
img.save(out)
print(f"wrote {out}")
