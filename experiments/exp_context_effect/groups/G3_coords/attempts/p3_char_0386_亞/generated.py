# BANK_DEVIATION
# skipped: (no matching bank entry — 亞 is fresh)
# reason: 亞 is a symmetric two-side character with mirrored inward ticks
#         and a wide baseline; no bank entry captures this envelope. Inline.
# fresh_component: ya2_char (亞 8-stroke envelope: top-hor, L/R box-verticals
#                   with paired inward ticks, middle horizontal, wide baseline)
from PIL import Image, ImageDraw


def draw_ya2(img_path):
    W = H = 300
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    w = 5  # ink width, uniform-ish for MMH GT (P12)

    # 1) Top horizontal — sits in upper third, medium span
    d.line([(95, 78), (210, 74)], fill="black", width=w)

    # 2) Left outer vertical (slight outward flare toward bottom)
    d.line([(102, 78), (94, 218)], fill="black", width=w)

    # 3) Right outer vertical (mirror)
    d.line([(203, 78), (211, 218)], fill="black", width=w)

    # 4) Left UPPER inward tick
    d.line([(96, 120), (150, 118)], fill="black", width=w)

    # 5) Right UPPER inward tick
    d.line([(155, 118), (209, 120)], fill="black", width=w)

    # 6) Middle full horizontal — connects the two side pieces at the waist
    d.line([(96, 168), (209, 170)], fill="black", width=w)

    # 7) Left LOWER inward tick (short, closes the lower cell)
    d.line([(95, 216), (148, 214)], fill="black", width=w)

    # 8) Right LOWER inward tick (mirror)
    d.line([(157, 214), (210, 216)], fill="black", width=w)

    # 9) Wide bottom horizontal — the widest stroke, sits low, continuous
    d.line([(38, 258), (262, 254)], fill="black", width=w)

    img.save(img_path)


if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    draw_ya2(os.path.join(here, "01_亞.png"))
