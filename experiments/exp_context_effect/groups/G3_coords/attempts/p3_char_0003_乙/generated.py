# p3_char_0003_乙 — the character 乙 (yǐ), 1 stroke (横折弯钩-like).
#
# The character 乙 IS the 乙 radical, shape-identical. Use bank primitive
# draw_yi_radical (PASSed at position 38 as p2_radical_006_乙) at scale=1.0,
# ox=0, oy=0 — the recorded coords already fill the canvas correctly.
#
# TR-compliant: (ox, oy, scale) deliberately chosen for THIS composition
# (standalone character = same layout as the radical). No transformation
# needed beyond the identity.

import sys
sys.path.insert(0, "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code")

from PIL import Image, ImageDraw
from yi_radical import draw_yi_radical

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Standalone character — identity transform (same as passing radical render).
draw_yi_radical(d, ox=0.0, oy=0.0, scale=1.0)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0003_乙/01_乙.png"
img.save(out_path)
print(f"Saved: {out_path}")
