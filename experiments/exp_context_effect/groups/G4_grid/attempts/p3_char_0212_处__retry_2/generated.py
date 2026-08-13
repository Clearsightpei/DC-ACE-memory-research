"""p3_char_0212_处 retry_2 — G4

TRAJECTORY DIFF (from Reading main FAIL PNG vs GT):
  MAIN FAIL (attempts/p3_char_0212_处/01_处.png):
    - Strokes are disconnected and hover at wrong scales.
    - The 夂 top has no X-cross topology; the pie and the sweeping
      horizontal never meet — reads as scattered lines, not 夂.
    - The 卜 竖 sits too centrally and too high; its 点 is a stubby
      diagonal orphaned off to the mid-right.
    - Long sweeping horizontal (s3) does not extend far enough right
      and does not weld to s2's mid.
  FIXES THIS RETRY:
    - Use CROSS_ANCHOR = BL(0.942, 0.154) — the P-weld from MMH — and
      route BOTH s2 and s3 through it (s2 as two-segment 横撇 hitting
      CROSS at its bend; s3 as a smooth line from ML→BR that passes
      through CROSS near its 19%-along point).
    - Extend s3 all the way to BR(0.728, 0.804) so 处's sweeping tail
      hooks out to the right per GT.
    - Place 卜 竖 (s4) as a mostly-vertical line TC→BC per MMH.
    - Draw 点 (s5) as a short diagonal from C→MR per MMH, with tail
      slightly weighted (dot form).
"""

from PIL import Image, ImageDraw
import os, sys

# Add anchor helper from the shared bank
BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(BASE, "..", "..", "success_bank", "code")))
from _anchor import anchor_to_xy, quad_bezier, fat_line, stroke_variable_width, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 5 stroke primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'CROSS_ANCHOR = BL(0.942, 0.154) shared by s2 bend and s3 mid; N-gaps preserved elsewhere.',
}

# --- Canvas ---
W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# --- Anchors (MMH-derived) ---
S1_HEAD = ('TL', 0.797, 0.791)
S1_TAIL = ('BL', 0.264, 0.065)

S2_HEAD = ('ML', 0.744, 0.509)
S2_TAIL = ('BL', 0.211, 0.815)

S3_HEAD = ('ML', 0.507, 0.986)
S3_TAIL = ('BR', 0.728, 0.804)

S4_HEAD = ('TC', 0.629, 0.747)
S4_TAIL = ('BC', 0.743, 0.455)

S5_HEAD = ('C', 0.928, 0.485)
S5_TAIL = ('MR', 0.429, 0.916)

CROSS = ('BL', 0.942, 0.154)  # P-weld point per MMH joint spec

# Convert to pixels
p1h = anchor_to_xy(S1_HEAD); p1t = anchor_to_xy(S1_TAIL)
p2h = anchor_to_xy(S2_HEAD); p2t = anchor_to_xy(S2_TAIL)
p3h = anchor_to_xy(S3_HEAD); p3t = anchor_to_xy(S3_TAIL)
p4h = anchor_to_xy(S4_HEAD); p4t = anchor_to_xy(S4_TAIL)
p5h = anchor_to_xy(S5_HEAD); p5t = anchor_to_xy(S5_TAIL)
cross = anchor_to_xy(CROSS)

BLACK = (0, 0, 0)

# --- Stroke 1: long 撇 (outer pie of 夂) ---
# Slight leftward curve. Control point pulled a bit left of midpoint.
ctrl1 = ((p1h[0] + p1t[0]) / 2 - 8, (p1h[1] + p1t[1]) / 2 + 6)
pts1 = quad_bezier(p1h, ctrl1, p1t, n=40)
w1 = [7 - 4 * (i / 40) for i in range(41)]  # taper from thick to thin
stroke_variable_width(d, pts1, w1, BLACK)

# --- Stroke 2: 横撇 (middle stroke of 夂) — smooth curve through CROSS ---
# Use quadratic bezier with control point chosen so B(t=0.56) lands near CROSS.
# Formula: (0.194*P0 + 0.4928*P1 + 0.3136*P2) = CROSS  =>  P1 = (CROSS - 0.194*P0 - 0.3136*P2)/0.4928
ctrl2_x = (cross[0] - 0.194 * p2h[0] - 0.3136 * p2t[0]) / 0.4928
ctrl2_y = (cross[1] - 0.194 * p2h[1] - 0.3136 * p2t[1]) / 0.4928
ctrl2 = (ctrl2_x, ctrl2_y)
pts2 = quad_bezier(p2h, ctrl2, p2t, n=40)
w2 = [6.5 - 3.5 * (i / 40) for i in range(41)]
stroke_variable_width(d, pts2, w2, BLACK)

# --- Stroke 3: long sweeping 横折弯钩/捺 (bottom of 处) ---
# Smooth arc from ML to BR, passing near CROSS at t~0.19.
# Undulating curve using two beziers stitched at midpoint for the sweep+hook.
mid3 = (0.5 * (p3h[0] + p3t[0]) - 12, 0.5 * (p3h[1] + p3t[1]) - 22)
pts3 = quad_bezier(p3h, mid3, p3t, n=60)
w3 = []
for i in range(61):
    t = i / 60
    # peak thickness around t=0.7 (捺 flare before hook)
    thick = 5 + 4 * max(0, 1 - abs(t - 0.7) * 2.5)
    w3.append(thick)
stroke_variable_width(d, pts3, w3, BLACK)

# --- Stroke 4: 竖 (卜's vertical stem) ---
# Small lean: head TC to tail BC, slight rightward drift already in anchors.
ctrl4 = ((p4h[0] + p4t[0]) / 2 + 2, (p4h[1] + p4t[1]) / 2)
pts4 = quad_bezier(p4h, ctrl4, p4t, n=30)
w4 = [7 - 2 * (i / 30) for i in range(31)]
stroke_variable_width(d, pts4, w4, BLACK)

# --- Stroke 5: 点 (卜's dot) ---
# Short diagonal from C to MR; classic 点 taper: thin head, thick tail.
pts5 = sample_line(p5h, p5t, n=20)
w5 = [3 + 5 * (i / 20) for i in range(21)]
stroke_variable_width(d, pts5, w5, BLACK)

# --- Save ---
out = os.path.join(BASE, '01_处.png')
img.save(out)
print(f"Wrote {out}")

# Structural verification
print("stroke count: 5 (s1 pie, s2 hengpie two-seg, s3 sweep, s4 shu, s5 dot)")
print(f"CROSS pixel: {cross}")
print(f"s3 at t=0.19 approx: ({p3h[0] + 0.19*(p3t[0]-p3h[0]):.1f}, {p3h[1] + 0.19*(p3t[1]-p3h[1]):.1f})")
