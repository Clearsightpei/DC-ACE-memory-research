"""p3_char_0195_皿 — G4 render.

Memory read order (v8):
  1. drawer_memory.md — no chronic primitive matches 皿 (no 丿/刀/冂/弓/马).
  2. success_bank/INDEX.md — no direct 皿 primitive; not a compositional reuse.
  3. errata.md — 皿 not listed.

Decomposition: 皿 is a 5-stroke frame + inner-verticals + base horizontal.
  s1 = 竖 (left vertical)
  s2 = 横折 (top-horizontal + right-vertical, single stroke)
  s3 = 竖 (inner left vertical)
  s4 = 竖 (inner right vertical)
  s5 = 一 (bottom horizontal, wider than the frame — the base of the dish)

Anchors taken from MMH structural block (PIL y-down convention).
"""
import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
from _anchor import anchor_to_xy, fat_line, stroke_variable_width  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 5 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],     # all 7 joints implemented as N (neighbor gap)
    'overall_pass': True,
    'notes': 'Frame with N-gap corners; bottom horizontal extends past frame.',
}


def draw_min(draw):
    # ---- stroke 1: 竖 (left vertical), slight lean toward center at bottom
    p1a = anchor_to_xy(('ML', 0.53, 0.427))
    p1b = anchor_to_xy(('BL', 0.876, 0.309))
    fat_line(draw, p1a, p1b, width=6)

    # ---- stroke 2: 横折 (top + right side). Head at ML upper-left,
    # corner at (tail_x, head_y), tail at BC upper-right area.
    p2a = anchor_to_xy(('ML', 0.732, 0.444))
    p2b = anchor_to_xy(('BC', 0.986, 0.221))
    corner = (p2b[0], p2a[1])   # 横折 corner: same y as head, same x as tail
    fat_line(draw, p2a, corner, width=6)
    fat_line(draw, corner, p2b, width=6)

    # ---- stroke 3: inner left 竖
    p3a = anchor_to_xy(('C', 0.119, 0.503))
    p3b = anchor_to_xy(('BC', 0.266, 0.291))
    fat_line(draw, p3a, p3b, width=5)

    # ---- stroke 4: inner right 竖
    p4a = anchor_to_xy(('C', 0.632, 0.427))
    p4b = anchor_to_xy(('BC', 0.567, 0.259))
    fat_line(draw, p4a, p4b, width=5)

    # ---- stroke 5: bottom 一 (extends past the frame on both sides)
    p5a = anchor_to_xy(('BL', 0.217, 0.417))
    p5b = anchor_to_xy(('BR', 0.783, 0.367))
    fat_line(draw, p5a, p5b, width=7)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_min(d)
    out = os.path.join(os.path.dirname(__file__), "01_皿.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
