"""G1 render for p3_char_0374_疙 (character '疙').
Structure: 疒 radical (left+top wrap) + 乞 inside/right.
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 4  # stroke thickness

def stroke(pts, width=W):
    """Draw a polyline with rounded joints/ends for a brush feel."""
    d.line(pts, fill=BLACK, width=width, joint="curve")
    r = width // 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# --- 疒 radical ---
# stroke 1: small top-left dot / short slant  (丶)
stroke([(70, 65), (85, 80)])

# stroke 2: horizontal top bar (from just left of center going right)
stroke([(90, 100), (215, 95)])

# stroke 3: left-side dot going down-left ("丶" of 疒, top-left dot)
stroke([(78, 115), (65, 135)])

# stroke 4: another dot on left side (lower dot of 疒)
stroke([(72, 155), (58, 175)])

# stroke 5: long left-falling stroke (丿) — long curved diagonal from top-right of horiz down to lower-left
stroke([(115, 105), (100, 160), (75, 220), (55, 265)])

# --- 乞 inside (on the right within 疒) ---
# stroke 1 (乞): small slanting dot at top ("丿"-like short)
stroke([(190, 130), (215, 145)])

# stroke 2 (乞): horizontal stroke below
stroke([(140, 170), (235, 165)])

# stroke 3 (乞): 乙-like sweeping hook — starts upper-middle, sweeps down-right in a curve,
# floors out along bottom, then hooks up at the right end.
stroke([(150, 195), (155, 215), (170, 240), (200, 260),
        (235, 265), (250, 258), (252, 240), (250, 215)])

# save
out_path = os.path.join(os.path.dirname(__file__), "01_疙.png")
img.save(out_path)
print("wrote", out_path)
