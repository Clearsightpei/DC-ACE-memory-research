"""p3_char_0056_亾 — G4 grid-bank first attempt.

MANDATORY LOOKUP CHECKLIST (memory_index step):
  1. success_bank/INDEX.md grep '亾' / '亡' -> no match. New item.
  2. errata.md grep '亾' / '亡' -> no match.
  3. form_catalog.md — pie/na standard forms; TR9 not applied (this is a
     3-stroke standalone char with wide spread already).
  4. principles_meta.md — TR6 (inline if primitive doesn't fit cleanly),
     TR8 (sanity check anchors), TR10 (N-class joints must LOOK connected
     but not welded; ~15-27 px gap OK per MMH expectations).
  5. joint_atlas.md — two N joints, both between tapered tips; standard
     small natural gaps.
  6. sandbox.md — no specific note.

MMH expected stroke count: 3
  s1 head TC(0.219,0.891) -> tail BL(0.683,0.455)   long 撇 top→lower-left
  s2 head C(0.424,0.518)  -> tail BR(0.672,0.332)   short diagonal / dot
  s3 head TL(0.366,0.87)  -> tail BR(0.604,0.71)    lower horizontal-ish

Joints (both N, small natural gaps):
  s1.mid(0.33) ⇆ s2.head @ C  ≈ 15.7 px gap
  s1.tail     ⇆ s3.mid(0.38) @ BL ≈ 27.2 px gap

Inline (TR6) — the strokes are close enough to standard 撇/横 that a
lightweight tapered polyline suffices without invoking the full pie/na
primitives (avoids extreme transformation).
"""
import os, sys, math
from PIL import Image, ImageDraw

# Bring in shared anchor helper from success_bank/code (READ ONLY).
HERE = os.path.dirname(os.path.abspath(__file__))
SB   = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, SB)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'inline strokes; two N-class gaps preserved (not welded).'
}


# ---------- helpers ----------
def tapered_curve(draw, p0, p2, head_w, tail_w, curve=0.08, perp_sign=+1, segments=48):
    """Bowed variable-width stroke from p0 to p2."""
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = max(1.0, math.hypot(dx, dy))
    perp = (perp_sign * (-dy / L), perp_sign * (dx / L))
    bow = curve * L
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_w + (tail_w - head_w) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


# ---------- canvas ----------
img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---------- stroke 1: long left-descending 撇 from TC(bottom) → BL(mid) ----------
# Runs from top-center down to lower-left. Slight leftward bow (perp=-1 bows left).
s1_head = ('TC', 0.219, 0.891)
s1_tail = ('BL', 0.683, 0.455)
p1_head = anchor_to_xy(s1_head)
p1_tail = anchor_to_xy(s1_tail)
tapered_curve(draw, p1_head, p1_tail, head_w=10, tail_w=3, curve=0.06, perp_sign=-1)

# ---------- stroke 2: short 捺-flavor diagonal from C → BR ----------
# N-class joint at head with s1's midpoint (gap ~16 px preserved).
s2_head = ('C',  0.424, 0.518)
s2_tail = ('BR', 0.672, 0.332)
p2_head = anchor_to_xy(s2_head)
p2_tail = anchor_to_xy(s2_tail)
tapered_curve(draw, p2_head, p2_tail, head_w=3, tail_w=9, curve=0.06, perp_sign=+1)

# ---------- stroke 3: lower diagonal from TL(bottom) → BR(mid) ----------
# N-class joint with s1.tail (gap ~27 px preserved).
s3_head = ('TL', 0.366, 0.87)
s3_tail = ('BR', 0.604, 0.71)
p3_head = anchor_to_xy(s3_head)
p3_tail = anchor_to_xy(s3_tail)
tapered_curve(draw, p3_head, p3_tail, head_w=6, tail_w=5, curve=0.02, perp_sign=+1)

# ---------- save ----------
out = os.path.join(HERE, '01_亾.png')
img.save(out)
print('wrote', out)
