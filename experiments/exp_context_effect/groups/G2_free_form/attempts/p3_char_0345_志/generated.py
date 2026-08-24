"""
p3_char_0345_志 — 志 (zhi, "will/aspiration")

Structure: 士 (top) + 心 (bottom)

SIGNATURE CHECK (from sibling_signature_checklist.md, applied to 士 component):
| 士 | TOP 横 LONGER than bottom (~1.5x) | 土 |

Compound-character sibling bit (memory_index E): even though 士 is a
sub-glyph here, enforce top-longer-than-bottom (~1.5x) inside the
component.

心 component: 卧钩 (bowl hook) flick UP-and-LEFT (~-145 deg),
plus three 点 (left, center-inside, right).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=7):
    """Draw a polyline with rounded caps by dabbing circles at every point."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=width)
    r = width // 2
    for (x, y) in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def bezier(p0, p1, p2, n=40):
    """Quadratic Bezier sampling."""
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def dot(cx, cy, rx=6, ry=9, angle=0):
    """Simple ink dot — small ellipse."""
    d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=INK)


# ============ 士 (top) — rows y=45..135 ============

# 1. TOP 横 — LONGER (~150 wide)
stroke([(70, 60), (230, 62)], width=8)

# 2. Middle 竖 — from top横 down through bottom横
stroke([(150, 60), (150, 145)], width=8)

# 3. BOTTOM 横 — SHORTER (~100 wide), ratio ~100/160 = 0.63 (so top ~1.6x)
stroke([(100, 145), (200, 143)], width=8)


# ============ 心 (bottom) — rows y=160..270 ============

# Order in MMH: left 点, 卧钩, center 点 (inside bowl), right 点

# Left 点 — down-left tick at bottom-left of 心 (visible teardrop)
d.polygon([(72, 178), (85, 172), (96, 212), (82, 218)], fill=INK)

# 卧钩 (bowl hook) — long sweeping bowl from upper-left curving down
# and to the right, terminating with UP-and-LEFT flick.
bowl = bezier((98, 190), (150, 292), (232, 235), n=60)
for i in range(len(bowl) - 1):
    d.line([bowl[i], bowl[i + 1]], fill=INK, width=9)

# hook flick UP-and-LEFT from the bowl's right end (~-145 deg)
hook_start = bowl[-1]
hook_end = (210, 205)
stroke([hook_start, hook_end], width=9)

# Center 点 (inside bowl, teardrop shape)
d.polygon([(147, 195), (162, 195), (165, 225), (150, 228)], fill=INK)

# Right 点 — upper-right tick, down-right teardrop
d.polygon([(213, 172), (228, 170), (238, 205), (224, 210)], fill=INK)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0345_志/01_志.png")
print("saved 01_志.png")
