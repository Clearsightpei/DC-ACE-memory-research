# 亘 (xuan) — top 一 + small 日 + bottom wider 一
# G3 v8: inline PIL, thin uniform strokes matching MMH GT (P12).
from PIL import Image, ImageDraw

def draw_heng(d, x1, y1, x2, y2, w=4):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

def draw_shu(d, x1, y1, x2, y2, w=4):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

def draw_xuan(img_path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # Top short 一
    draw_heng(d, 95, 70, 205, 68, w=5)

    # Middle 日 (small rectangle with middle bar)
    # Left vertical
    draw_shu(d, 110, 105, 112, 205, w=5)
    # Top horizontal (of 日) — meets left vertical, extends right with slight downturn hook
    draw_heng(d, 110, 105, 195, 108, w=5)
    # Right vertical — a bit shorter, slight taper
    draw_shu(d, 195, 108, 195, 205, w=5)
    # Middle horizontal
    draw_heng(d, 118, 155, 190, 155, w=4)
    # Bottom horizontal of 日
    draw_heng(d, 115, 205, 195, 203, w=5)

    # Bottom wider 一
    draw_heng(d, 60, 245, 240, 243, w=5)

    img.save(img_path)

if __name__ == "__main__":
    draw_xuan("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0230_亘/01_亘.png")
