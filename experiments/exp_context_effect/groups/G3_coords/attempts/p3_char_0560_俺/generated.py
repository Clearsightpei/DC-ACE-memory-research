# BANK_DEVIATION
# skipped: (none for 亻 — using ren_pang_pil_for_LR_left as-is)
# reason: right side 奄 (大 stacked over 电/甩-form) has no bank entry;
#         fresh inline PIL render
# fresh_component: yan_right_for_俺 (奄: 大 over 电-like)
#
# 俺 = 亻 (LR-left) + 奄 (LR-right). 奄 = 大 (top ~85-170) stacked over
# 电/甩-form (bottom ~170-265): 日-frame + shu-hook.
# Thin MMH-style widths ~3-4 px.
import os, sys, math
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 "..", "..", "success_bank", "code"))
from ren_pang_pil_for_LR_left import draw_ren_pang_pil_for_LR_left


def bezier(d, p0, p1, p2, w_head, w_tail, n=45, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (bx, by)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0]-r, cur[1]-r, cur[0]+r, cur[1]+r], fill=black)
        prev = cur


def tline(d, p0, p1, w_head, w_tail, n=30, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (x, y)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0]-r, cur[1]-r, cur[0]+r, cur[1]+r], fill=black)
        prev = cur


def draw_yan_right(d, black=(0, 0, 0)):
    """奄 in right slot. Top 大 spans y=55-160; bottom 电/日+hook y=155-265."""
    # -------- Top: 大 (clearer, bigger) --------
    # S1: horizontal 一 (top of 大), long span
    tline(d, (110, 95), (275, 92), 4, 4, n=40)
    # S2: 撇 (pie): from top-center-right sweeps down to lower-left
    bezier(d, (200, 62), (168, 105), (115, 165),
           w_head=6, w_tail=3, n=55)
    # S3: 捺 (na): from crossing sweeps down-right, tapered thick
    bezier(d, (192, 95), (225, 130), (275, 170),
           w_head=3, w_tail=7, n=55)

    # -------- Bottom: 电-like (日-frame + central shu-弯钩) --------
    box_l, box_r = 145, 250
    box_t, box_b = 175, 250
    # S4: top horizontal of 日
    tline(d, (box_l, box_t), (box_r, box_t), 4, 4, n=30)
    # S5: left vertical
    tline(d, (box_l + 2, box_t), (box_l + 2, box_b - 5), 4, 4, n=30)
    # S6: right vertical
    tline(d, (box_r - 2, box_t), (box_r - 2, box_b - 5), 4, 4, n=30)
    # S7: middle horizontal (日 divider)
    tline(d, (box_l + 4, (box_t + box_b) // 2),
          (box_r - 4, (box_t + box_b) // 2), 3, 3, n=30)
    # S8: bottom horizontal (closes 日 base)
    tline(d, (box_l, box_b - 5), (box_r, box_b - 5), 4, 4, n=30)
    # S9: 竖弯钩 — central vertical piercing from just above top,
    # through the frame, then bending right at bottom into a hook
    cx = (box_l + box_r) // 2
    tline(d, (cx, box_t - 10), (cx, box_b + 5), 4, 4, n=35)
    # Hook curves down-right then flicks right-up
    bezier(d, (cx, box_b + 5),
           (cx + 25, box_b + 18),
           (box_r + 12, box_b - 2),
           w_head=4, w_tail=2, n=40)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Left: 亻
    draw_ren_pang_pil_for_LR_left(d, cx=68, y_top=85, y_bot=240,
                                   w_pie_head=6, w_pie_tail=2, w_shu=5)
    # Right: 奄
    draw_yan_right(d)

    out = os.path.join(os.path.dirname(__file__), "01_俺.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
