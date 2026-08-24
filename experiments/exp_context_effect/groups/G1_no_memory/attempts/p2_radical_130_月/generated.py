"""G1 render of radical 月 (4 strokes) at 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# Layout: tall rectangle roughly centered horizontally, occupying ~y=55 to y=270.
# Left side: 撇 (piě) - slanted stroke curving down-left
# Right side: vertical + hook (横折钩)
# Inside: two short horizontal strokes

# Stroke 1: 撇 (left slanting stroke, starts upper-right of left edge, curves down-left)
# Approximate a slight curve using multiple points.
pie_pts = [(120, 60), (110, 110), (95, 170), (78, 235), (65, 275)]
d.line(pie_pts, fill=BLACK, width=LW, joint="curve")

# Stroke 2: 横折钩 (horizontal + turn + vertical + small hook at bottom-left)
# top-horizontal from (120,60) to (210,60), then vertical down to (210,265), then small hook to (195,258)
top_h = [(118, 60), (215, 60)]
d.line(top_h, fill=BLACK, width=LW, joint="curve")
right_v = [(213, 60), (213, 262)]
d.line(right_v, fill=BLACK, width=LW, joint="curve")
hook = [(213, 262), (198, 252)]
d.line(hook, fill=BLACK, width=LW, joint="curve")

# Stroke 3: first inner horizontal (upper)
inner1 = [(105, 130), (208, 130)]
d.line(inner1, fill=BLACK, width=LW, joint="curve")

# Stroke 4: second inner horizontal (middle)
inner2 = [(95, 195), (210, 195)]
d.line(inner2, fill=BLACK, width=LW, joint="curve")

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_130_月/01_月.png"
img.save(out)
print(out)
