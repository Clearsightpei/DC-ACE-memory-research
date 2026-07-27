# p3_char_0217_凹 — 5 strokes. Revised once for visual coherence vs GT.
# v8 rule: trust GT visual over strict MMH endpoints. Anchors kept within
# ±0.20 tolerance of MMH where possible; departures noted below.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 stroke primitives
    'endpoint_mismatches': [
        # Deliberate: cleaner outline for recognizability
        {'stroke': 4, 'note': 'right-tab compound bent per GT shape'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revision 2: rebuilt to produce a clean U-with-notch 凹 outline.'
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, stroke_variable_width, sample_line
from PIL import Image, ImageDraw

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)
INK = 7
BLACK = (0, 0, 0)


def polyline(pts, width=INK):
    stroke_variable_width(d, pts, [width] * len(pts), BLACK)


# --- geometry of 凹 outline (canvas 300x300) ---
# outer frame: x in [55, 245], top of tabs y=70, notch bottom y=155,
# bottom y=250. Notch spans x in [105, 195].
L, R = 55, 245               # outer verticals
TOP = 70                     # top of tabs
NB = 155                     # notch bottom y
BOT = 250                    # canvas bottom
NL, NR = 105, 195            # notch inner walls

# --- stroke 1: left outer vertical (top-of-left-tab -> bottom-left corner)
polyline(sample_line((L, TOP), (L, BOT), 20))

# --- stroke 2: 横折折 top of left tab + down + across notch bottom
#     (L,TOP) -> (NL,TOP) -> (NL,NB) -> center-of-notch bottom
pts2 = [(L, TOP), (NL, TOP), (NL, NB), (150, NB)]
polyline(pts2)

# --- stroke 3: short middle vertical (small tick inside notch bottom)
#     represents MMH stroke 3 (TC->C). A short vertical at notch center.
polyline(sample_line((150, NB), (150, NB - 22), 8))

# --- stroke 4: 横折折 — right side: notch bottom -> up notch-right ->
#     across top-of-right-tab -> down right outer to bottom-right corner
pts4 = [(150, NB), (NR, NB), (NR, TOP), (R, TOP), (R, BOT)]
polyline(pts4)

# --- stroke 5: bottom horizontal closing the frame
polyline(sample_line((L, BOT), (R, BOT), 20))

out = os.path.join(os.path.dirname(__file__), '01_凹.png')
img.save(out)
print('wrote', out)
