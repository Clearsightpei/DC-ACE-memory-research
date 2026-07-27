"""p3_char_0081_女 — 女 (nǚ, "woman"), 3 strokes.

GT is MMH-median style (thin uniform lines). Per P12, use thin widths
(~4 head, ~2 tail) rather than calligraphic brush profile.

Structural decomposition (from GT):
  Stroke 1 — 撇点 (pie-dian, zigzag): starts upper-mid, pie goes
             down-and-left to a joint, then dian goes down-and-right.
  Stroke 2 — 撇 (long sweeping pie): from upper-right, crosses through
             the character, ends lower-left. Crosses the 横 at midpoint.
  Stroke 3 — 横 (horizontal): long horizontal, slight upward tilt,
             spans nearly full width across the middle.

Written fresh with variant_* helpers (no existing 女 bank primitive).
"""

import os
import sys
from PIL import Image, ImageDraw

# Make _shared_helpers importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                "..", "..", "success_bank", "code"))
from _shared_helpers import variant_pie, variant_na, tapered_line, to_px

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
draw = ImageDraw.Draw(img)

# --- Stroke 1: 撇点 (pie-dian zigzag) — sits in upper-left region ---
# Pie portion: starts high (upper-mid), goes down-and-left to joint
# Head around (x=-15, y=+95), joint at (x=-55, y=+10)
pie1_head = (-15, +95)
pie1_joint = (-55, +10)
variant_pie(draw, head=pie1_head, tail=pie1_joint,
            bow_perp=-4.0, w_head=4.0, w_tail=2.5)

# Dian portion: from joint, going down-and-right (short thick-tail)
# Ends around (x=+5, y=-35)
dian_tail = (+5, -35)
variant_na(draw, head=pie1_joint, tail=dian_tail,
           bow_perp=+4.0, w_head=2.5, w_belly=5.5, w_tail=4.5,
           belly_u=0.7)

# --- Stroke 2: 撇 (long sweeping pie, upper-right to lower-left) ---
# Starts high-right around (x=+60, y=+75), sweeps down to (x=-110, y=-115)
pie2_head = (+60, +75)
pie2_tail = (-110, -115)
variant_pie(draw, head=pie2_head, tail=pie2_tail,
            bow_perp=-10.0, w_head=4.5, w_tail=2.0)

# --- Stroke 3: 横 (horizontal across middle, slight upward tilt right) ---
# Spans from far left to far right, at y ~ -15 (just below center)
heng_head = (-130, -20)
heng_tail = (+125, -10)  # slight rise
tapered_line(draw, heng_head, heng_tail, w0=3.5, w1=3.5)

img.save(os.path.join(os.path.dirname(__file__), "01_女.png"))
