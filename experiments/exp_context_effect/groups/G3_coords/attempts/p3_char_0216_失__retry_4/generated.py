# TRAJECTORY DIFF for p3_char_0216_失 (retry_4)
#
# FAILED attempts (main, r1, r2, r3):
#   - top small pie sits ON TOP of the horizontal line like a "+", not as a
#     separate tick above it. In GT the small 撇 lives clearly above the
#     top 横, offset slightly left.
#   - top 横 is placed too close to (or on) the long 横 making the two
#     horizontals visually merge; GT shows a clear vertical gap of ~50px
#     between the two horizontals.
#   - long 撇 is too diagonal; in GT it starts near vertical from the top
#     and curves left near the bottom (the trunk of 大 must be visible as
#     a mostly-vertical descent through both horizontals).
#   - overall the char reads as 矢, not 失. The distinguishing move: the
#     long pie should extend UPWARD past the top 横, and the small pie sits
#     above/left of the top 横 rather than crossing it.
#
# FIXES this attempt:
#   - clearly separate the small top pie: sits ABOVE the top 横, slanted
#     from upper-right to lower-left, no crossing.
#   - top 横 shorter (~55px), positioned at y=95.
#   - long 横 at y=150 (55px below top 横), spans 200px wide.
#   - long 撇 starts high at (~155, 55), descends near-vertically to
#     (~150, 150) crossing point, then curves left to (~55, 278).
#   - 捺 starts at crossing (~150, 150), sweeps down-right to (~258, 278).
#
# BANK_DEVIATION
# skipped: shi.py / relevant compound bank entries
# reason: prior 4 attempts using componentized layout kept producing 矢 not 失;
#         the top small-pie + top-横 relationship needs precise inline placement
#         that bank primitives don't parameterize.
# fresh_component: shi_failed_char_r4_layout

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

WIDTH = 5

# Stroke 1: short 撇 at top-left (small tick, upper-right to lower-left).
# Sits ABOVE the top 横, offset slightly left of center.
d.line([(148, 62), (118, 92)], fill='black', width=WIDTH)

# Stroke 2: top short 横. Placed at y=95, spans from ~125 to ~185.
d.line([(122, 96), (188, 92)], fill='black', width=WIDTH)

# Stroke 3: long 横. y=150, spans ~50 to ~250.
d.line([(50, 152), (252, 146)], fill='black', width=WIDTH)

# Stroke 4: long 撇. Starts near top center (155, 55), descends near-vertical
# to the crossing (150, 150), then curves down-left to (55, 278).
pie_pts = []
# Upper segment: mostly vertical from (155, 55) to (150, 150)
for i in range(15):
    t = i / 14.0
    x = 155 - 5 * t
    y = 55 + 95 * t
    pie_pts.append((x, y))
# Lower segment: curves down-left from (150, 150) to (55, 278) with bow
for i in range(1, 35):
    t = i / 34.0
    # Quadratic Bezier-ish: start (150,150), control (135, 235), end (55, 278)
    x = (1 - t) * (1 - t) * 150 + 2 * (1 - t) * t * 115 + t * t * 55
    y = (1 - t) * (1 - t) * 150 + 2 * (1 - t) * t * 225 + t * t * 278
    pie_pts.append((x, y))
d.line(pie_pts, fill='black', width=WIDTH)

# Stroke 5: 捺 from crossing (150, 150) down-right to (258, 278).
# Slight curve outward (belly to the lower-left).
na_pts = []
for i in range(35):
    t = i / 34.0
    # Quadratic: start (150,150), control (195, 200), end (258, 278)
    x = (1 - t) * (1 - t) * 150 + 2 * (1 - t) * t * 195 + t * t * 258
    y = (1 - t) * (1 - t) * 150 + 2 * (1 - t) * t * 210 + t * t * 278
    na_pts.append((x, y))
# Taper: draw with widening effect near end
for i in range(len(na_pts) - 1):
    w = WIDTH + int(2 * (i / (len(na_pts) - 1)))
    d.line([na_pts[i], na_pts[i + 1]], fill='black', width=w)

img.save('<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0216_失__retry_4/01_失.png')
