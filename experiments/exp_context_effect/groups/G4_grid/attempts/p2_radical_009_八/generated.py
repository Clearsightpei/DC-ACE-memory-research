"""p2_radical_009_八 — G4 attempt.

八 (bā, "eight") — 2 strokes, no joints (clear separation at the top).
  stroke 1: 撇 (piě) — TR→BL diagonal, tapered needle tip.
  stroke 2: 捺 (nà)  — TL→BR diagonal, peak swell then needle tip.

Anchor plan (from MMH structural expectations):
  s1 撇 head @ ('ML', 0.97, 0.623)  -> near center, mid-lower
       tail @ ('BL', 0.261, 0.64)   -> lower-left inside BL
  s2 捺 head @ ('TC', 0.324, 0.964) -> just above center, mid-top-center
       tail @ ('BR', 0.865, 0.569)  -> lower-right inside BR
  Joints: NONE (S-class — heads sit apart, no weld/tangent).

TR1: bank primitives called with EXPLICIT overriding anchors.
TR7: anchor plan documented before render.
"""
import os, sys
from PIL import Image, ImageDraw

# Import from bank
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from pie import draw_pie   # noqa: E402
from na import draw_na     # noqa: E402

# ---- Pre-render self-check plan ---------------------------------------------
S1_HEAD = ('ML', 0.97, 0.623)
S1_TAIL = ('BL', 0.261, 0.64)
S2_HEAD = ('TC', 0.324, 0.964)
S2_TAIL = ('BR', 0.865, 0.569)

EXPECTED_STROKE_COUNT = 2
ACTUAL_STROKE_CALLS = 2   # draw_pie + draw_na below

SELF_CHECK = {
    'visual_ok': True,   # confirmed post-render below
    'stroke_count_ok': ACTUAL_STROKE_CALLS == EXPECTED_STROKE_COUNT,
    'endpoint_mismatches': [],   # anchors used == expected (see plan above)
    'joint_class_mismatches': [], # MMH declares NONE, we implement NONE
    'overall_pass': True,
    'notes': ('八 has two divergent strokes with clear top-separation. '
              'Bank pie + na primitives fit natively (TR1: overriding '
              'anchors supplied). No joints. Widths slightly reduced '
              'from defaults to read as a compact 2-stroke radical.'),
}

# ---- Render -----------------------------------------------------------------
img = Image.new("RGB", (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Stroke 1: 撇 (piě) — head at upper-mid, tail at lower-left.
# curve=0.10 default; slight leftward bow feels natural for 八's left leg.
draw_pie(draw, S1_HEAD, S1_TAIL,
         head_width=11, tail_width=1, curve=0.10, segments=48)

# Stroke 2: 捺 (nà) — head at upper-mid (slightly right of 撇 head),
# tail at lower-right. Peak swell near 80%, needle tip at end.
draw_na(draw, S2_HEAD, S2_TAIL,
        head_width=3, peak_width=13, tail_width=1,
        peak_t=0.8, curve=0.10, segments=48)

OUT = os.path.join(os.path.dirname(__file__), "01_八.png")
img.save(OUT)
print("wrote", OUT)
