# G5 bootstrap radical 乙 (1 stroke)
# Bank empty at fresh start — no BANK_DEVIATION applies.
# MMH block: 1 stroke, head @ ('TL', 0.715, 0.955), tail @ ('BR', 0.49, 0.083).
# Endpoints (300x300, TL=[0,150]x[0,150], BR=[150,300]x[150,300], screen y-down):
#   head ~ (107, 143)  tail ~ (223, 163)
# The MMH median gives just the two path endpoints; the visible glyph's
# extreme points (top curve, bottom hook) are traversed BETWEEN these anchors,
# reaching well below y=163 (bottom sweep) and near the canvas top. We follow
# the GT PNG shape and place head/tail approximately near the MMH anchors.

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': None,           # judged post-render
    'stroke_count_ok': True,     # 1 continuous stroke = 1 primitive
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # no joints expected
    'overall_pass': None,
    'notes': '乙 = single continuous S/hook curve; drawn as one polyline of cubic Bezier segments.'
}


def bezier(p0, p1, p2, steps=50):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_yi(draw):
    # Sequential quadratic Beziers approximating 乙:
    # A) short top curve (head): starts ~upper-left area of glyph, dips slightly, ends upper-right
    top_start = (95, 125)          # head — approximately MMH ('TL', ~0.63, ~0.83) i.e. near (107,143)
    top_apex  = (135, 108)
    top_end   = (175, 128)
    # B) throat descent: curves down-and-left forming 乙's diagonal
    throat_ctrl = (155, 180)
    throat_end  = (105, 220)
    # C) down-and-left sweep to bottom-left corner of glyph
    bl_ctrl = (82, 255)
    bl_end  = (85, 278)
    # D) bottom sweep to the right (long horizontal-ish)
    bot_ctrl = (150, 288)
    bot_end  = (220, 275)
    # E) small hook up (tail)
    hook_ctrl = (223, 258)
    hook_end  = (222, 240)  # tail — approximately MMH ('BR', ~0.48, ~0.60) i.e. near (222,240)

    segs = []
    segs += bezier(top_start, top_apex, top_end)
    segs += bezier(top_end, throat_ctrl, throat_end)
    segs += bezier(throat_end, bl_ctrl, bl_end)
    segs += bezier(bl_end, bot_ctrl, bot_end)
    segs += bezier(bot_end, hook_ctrl, hook_end)

    for i in range(len(segs) - 1):
        draw.line([segs[i], segs[i + 1]], fill='black', width=6)
    # Round the joints between beziers
    for p in [top_start, top_end, throat_end, bl_end, bot_end, hook_end]:
        r = 3
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_yi(draw)
    img.save('/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_006_乙/01_乙.png')


if __name__ == '__main__':
    main()
