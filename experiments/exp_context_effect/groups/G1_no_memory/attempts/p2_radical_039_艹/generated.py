"""G1 render for radical 艹 (grass radical, 3 strokes).

Structure (per GT):
- One long horizontal (横) crossing the full width, slightly tilted up-right.
- Two short verticals/slanted strokes crossing it:
    - Left stroke: nearly vertical, slight lean (like a short 竖 or 撇).
    - Right stroke: slight lean rightward (like a short 竖 or 撇).
Both cross-strokes pierce the horizontal (extend above and below it).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
STROKE = 6

# 1. Long horizontal (横) — slight upward tilt to the right, as in GT.
#    Runs roughly x=35..270, y drifting from ~175 down to ~165 (slight tilt).
d.line([(35, 178), (270, 168)], fill=INK, width=STROKE)

# 2. Left vertical/slant — mostly vertical, tiny lean left.
#    Crosses horizontal near x≈115. Top a bit above line, bottom well below.
d.line([(118, 140), (110, 230)], fill=INK, width=STROKE)

# 3. Right vertical/slant — leans slightly right/down.
#    Crosses horizontal near x≈180. Top a bit above line, bottom below.
d.line([(178, 140), (188, 232)], fill=INK, width=STROKE)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_039_艹/01_艹.png"
img.save(out)
print(f"Wrote {out}")
