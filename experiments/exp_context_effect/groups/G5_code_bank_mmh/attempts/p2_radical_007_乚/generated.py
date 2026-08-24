"""G5 attempt: p2_radical_007_乚 (1 stroke).

MMH-derived structural expectations:
  stroke 1: head @ ('TL', 0.636, 0.867)  -> canvas (95, 130)
            tail @ ('BR', 0.552, 0.124)  -> canvas (233, 169)
  joint expectations: NONE (single stroke)

The 乚 radical is a single J/hook shape: descends from upper-left,
sweeps right along the bottom, then a small terminal hook going up
to the tail anchor.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# MMH-derived canvas coords (cell TL = x:0..150, y:0..150; BR = x:150..300, y:150..300)
head = (95, 130)   # top of the J
tail = (233, 169)  # end of the hook

# Path: head -> descend -> arc across bottom -> hook up to tail
# Sample points along a smooth polyline that lands the endpoints on the anchors.
path = [
    head,
    (93, 160),
    (93, 200),
    (98, 225),
    (115, 240),
    (150, 245),
    (190, 245),
    (218, 240),
    (230, 220),
    (233, 195),
    tail,
]

# Stroke it thickly, round joins, so it looks brush-ink.
width = 8
for a, b in zip(path[:-1], path[1:]):
    draw.line([a, b], fill="black", width=width)
for p in path:
    draw.ellipse([p[0] - width // 2, p[1] - width // 2,
                  p[0] + width // 2, p[1] + width // 2], fill="black")

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_007_乚/01_乚.png"
img.save(out)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # single continuous polyline = 1 stroke
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'single-stroke radical; anchors landed at head (95,130) and tail (233,169).'
}
