"""G1 render for 都 (dū) — Phase 3 character. Revised."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 3


def line(p0, p1, w=LW):
    d.line([p0, p1], fill=BLACK, width=w)


def poly(pts, w=LW):
    d.line(pts, fill=BLACK, width=w, joint="curve")


# === LEFT: 者 ===
# 耂 top:
# 1. Short vertical/tick (top-left stub)
line((70, 40), (70, 62), LW)
# 2. Top horizontal
line((30, 62), (155, 62), LW)
# 3. Second horizontal (middle of 耂), slightly shorter, higher-left descending-right
line((45, 100), (135, 95), LW)
# 4. Long 撇 sweeping from upper-right down-left, passing to the LEFT of 日
poly([(150, 45), (120, 110), (80, 170), (40, 230), (20, 260)], LW)

# 日 box (sun) — positioned to the RIGHT of the 撇's descent, lower half
box_l, box_t, box_r, box_b = 70, 175, 155, 260
line((box_l, box_t), (box_r, box_t), LW)  # top
line((box_l, box_t), (box_l, box_b), LW)  # left
line((box_r, box_t), (box_r, box_b), LW)  # right
line((box_l, box_b), (box_r, box_b), LW)  # bottom
# middle horizontal inside 日
line((box_l + 3, 218), (box_r - 3, 218), LW)

# === RIGHT: 阝 (right ear/city radical) ===
# Upper loop — like a "3" shape
# Top stroke: 横折折折钩 - starts high, goes right, curves down, back left, down, back right
poly([
    (200, 60),   # start top
    (240, 65),   # go right
    (245, 100),  # curve down
    (210, 115),  # back to spine
    (245, 125),  # out again
    (250, 160),  # down
    (215, 175),  # back to spine
], LW)
# Long vertical descender (the 竖)
line((215, 90), (215, 285), LW)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0503_都/01_都.png"
)
print("saved")
