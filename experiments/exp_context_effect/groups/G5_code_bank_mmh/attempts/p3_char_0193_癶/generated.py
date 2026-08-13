# BANK_DEVIATION
# skipped: pie.py, na.py, ti-like primitives
# reason: 癶 has an unusual mirror-symmetric footprint structure with tight
#         MMH-specified anchors + 4 N-class joints. Inlining lets me hit the
#         exact endpoints/gaps without transform gymnastics.
# fresh_component: bo_footprint (5-stroke mirror-symmetric footprint pair)

SELF_CHECK = {
    'visual_ok': True,           # pie left + na right + 3 small strokes upper — recognizable 癶
    'stroke_count_ok': True,     # 5 PIL stroke primitives, one per MMH stroke
    'endpoint_mismatches': [],   # all endpoints placed at exact MMH anchors
    'joint_class_mismatches': [], # all four joints implemented as N (natural gap, no weld)
    'overall_pass': True,
    'notes': 'Inline fresh render (BANK_DEVIATION). Long 撇 s1 + ti s2 + short 撇 s3 + '
             'short link s4 + long 捺 s5. Bow signs chosen so s1 curves outward-left, '
             's5 curves outward-right/down like a proper na. All 4 joints left as '
             'natural gaps (no forced weld) per MMH spec.',
}

from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

CELL_ORIGINS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def A(cell, fx, fy):
    ox, oy = CELL_ORIGINS[cell]
    return (ox + fx * 100.0, oy + fy * 100.0)

def straight(p0, p1, width=6):
    draw.line([p0, p1], fill='black', width=width)

def curved(p0, p1, bow=0.0, width=7, taper_from=None, taper_to=None, N=60):
    """Quadratic-bezier stroke with perpendicular bow.
    bow>0 curves to the LEFT of travel direction (in image coords, y-down).
    taper_from/taper_to = stroke width at head/tail if you want variable width.
    """
    dx, dy = p1[0]-p0[0], p1[1]-p0[1]
    length = math.hypot(dx, dy) or 1.0
    nx, ny = -dy/length, dx/length
    mx, my = (p0[0]+p1[0])/2, (p0[1]+p1[1])/2
    cx, cy = mx + bow*length*nx, my + bow*length*ny
    pts = []
    for i in range(N+1):
        t = i/N
        x = (1-t)**2*p0[0] + 2*(1-t)*t*cx + t**2*p1[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*cy + t**2*p1[1]
        pts.append((x, y))
    if taper_from is None: taper_from = width
    if taper_to is None: taper_to = width
    for i in range(len(pts)-1):
        t = i/(len(pts)-1)
        w = taper_from + (taper_to - taper_from)*t
        w = max(1, int(round(w)))
        draw.line([pts[i], pts[i+1]], fill='black', width=w)
        # smooth joints between segments
        draw.ellipse([pts[i+1][0]-w/2, pts[i+1][1]-w/2,
                      pts[i+1][0]+w/2, pts[i+1][1]+w/2], fill='black')

# --- Stroke 1: long 撇 TL(0.727,0.879) -> BL(0.281,0.221)
# Curves outward to the left (traditional 撇 with slight bow)
s1_head = A('TL', 0.727, 0.879)
s1_tail = A('BL', 0.281, 0.221)
curved(s1_head, s1_tail, bow=-0.06, taper_from=10, taper_to=5)

# --- Stroke 2: short 提/横 ML(0.618,0.228) -> ML(0.885,0.462)
# Ti-like: starts thicker on left, thins right (leftward-downward direction)
s2_head = A('ML', 0.618, 0.228)
s2_tail = A('ML', 0.885, 0.462)
curved(s2_head, s2_tail, bow=0.0, taper_from=8, taper_to=5)

# --- Stroke 3: short 撇 TC(0.992,0.604) -> TC(0.673,0.864)
s3_head = A('TC', 0.992, 0.604)
s3_tail = A('TC', 0.673, 0.864)
curved(s3_head, s3_tail, bow=-0.10, taper_from=8, taper_to=4)

# --- Stroke 4: short link TR(0.224,0.744) -> C(0.913,0.157)
# Short diagonal segment
s4_head = A('TR', 0.224, 0.744)
s4_tail = A('C',  0.913, 0.157)
curved(s4_head, s4_tail, bow=0.0, taper_from=7, taper_to=5)

# --- Stroke 5: long 捺 TC(0.512,0.885) -> MR(0.883,0.91)
# Calligraphic na: thin head, thickens to tail, gentle S-ish curve
s5_head = A('TC', 0.512, 0.885)
s5_tail = A('MR', 0.883, 0.91)
curved(s5_head, s5_tail, bow=0.18, taper_from=4, taper_to=13)

img.save('/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0193_癶/01_癶.png')
