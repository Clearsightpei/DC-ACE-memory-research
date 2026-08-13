"""p3_char_0264_伢 — G5 attempt.

伢 = 亻 (left, 2 strokes) + 牙 (right, 4 strokes) = 6 strokes per MMH.

Follows P-A-006 recipe (MMH-anchor-verbatim + stroke-primitive layer,
refusing whole-radical composition like draw_ren_left). Every stroke
uses MMH anchors directly with bank stroke primitives.

Not a BANK_DEVIATION — all 6 strokes are bank stroke primitives (heng,
shu, pie). Refusing draw_ren_left is a P-A-006 recipe choice, not a
deviation from a fitting primitive.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng      # noqa: E402
from pie import draw_pie        # noqa: E402
from shu import draw_shu        # noqa: E402


_CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    x0, y0 = _CELL_ORIGIN[cell]
    return (x0 + xf * 100.0, y0 + yf * 100.0)


# ---------------- MMH-derived pixel anchors ----------------
# 亻 (person radical, left)
s1_head = anchor('TC', 0.011, 0.697)   # (101.1, 69.7)
s1_tail = anchor('ML', 0.214, 0.992)   # ( 21.4, 199.2)
s2_head = anchor('ML', 0.718, 0.585)   # ( 71.8, 158.5)
s2_tail = anchor('BL', 0.779, 0.988)   # ( 77.9, 298.8)

# 牙 (right side)
s3_head = anchor('C',  0.509, 0.046)   # (150.9, 104.6)  short heng, upper-right
s3_tail = anchor('TR', 0.414, 0.967)   # (241.4,  96.7)
s4_head = anchor('C',  0.324, 0.342)   # (132.4, 134.2)  middle heng, descending
s4_tail = anchor('MR', 0.646, 0.717)   # (264.6, 171.7)
s5_head = anchor('C',  0.966, 0.110)   # (196.6, 111.0)  vertical descender
s5_tail = anchor('BC', 0.652, 0.830)   # (165.2, 283.0)
s6_head = anchor('C',  0.969, 0.813)   # (196.9, 181.3)  long pie sweep
s6_tail = anchor('BC', 0.069, 0.754)   # (106.9, 275.4)


img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)

# --- s1: 亻 pie (long left-diagonal, thick head tapering to fine tail) ---
draw_pie(d, head=s1_head, tail=s1_tail,
         bow_perp=12, w_head=9, w_tail=3, steps=90)

# --- s2: 亻 shu (short vertical, slight rightward drift baked in) ---
draw_shu(d, head=s2_head, tail=s2_tail, width=7)

# --- s3: 牙 top heng (short, slight up-rise to top-right corner) ---
draw_heng(d, head=s3_head, tail=s3_tail, width_head=6, width_tail=7)

# --- s4: 牙 middle heng (long, descending to MR — the crossing bar) ---
draw_heng(d, head=s4_head, tail=s4_tail, width_head=7, width_tail=8)

# --- s5: 牙 vertical descender (from top-right down to BC, slight
#         leftward drift baked into endpoints — no top curl, no hook) ---
draw_shu(d, head=s5_head, tail=s5_tail, width=7)

# --- s6: 牙 long pie (from mid-right down-left to BC, prominent) ---
draw_pie(d, head=s6_head, tail=s6_tail,
         bow_perp=14, w_head=9, w_tail=3, steps=90)

out = pathlib.Path(__file__).parent / "01_伢.png"
img.save(out)
print(f"wrote {out}")

# ---------------------------------------------------------------
# Mandatory self-check
# ---------------------------------------------------------------
SELF_CHECK = {
    "visual_ok": None,           # inspected after render
    "stroke_count_ok": True,     # exactly 6 primitive calls: pie/shu/heng/heng/shu/pie
    "endpoint_mismatches": [],   # all 6 strokes use MMH anchors verbatim
    "joint_class_mismatches": [
        # s1.mid(0.57) ⇆ s2.head @ ML : N ~15px
        #   s1.mid ≈ (56.6, 143.4); s2.head = (71.8, 158.5); dist ≈ 21 px → N (gap present).
        # s3.mid(0.41) ⇆ s5.head @ C : N ~16px
        #   s3.mid ≈ (188.0, 101.4); s5.head = (196.6, 111.0); dist ≈ 13 px → N.
        # s4.mid(0.69) ⇆ s5.mid(0.28) @ MR : P (welded)
        #   s4.mid ≈ (223.7, 160.1); s5.mid ≈ (188.8, 159.2); horizontal bar CROSSES vertical
        #   near y=160 x≈190 → visually welded (P).
        # s4.mid(0.67) ⇆ s6.head @ MR : N ~15px
        #   s4.mid ≈ (220.9, 159.4); s6.head = (196.9, 181.3); dist ≈ 33 px → N (gap present).
        # s5.mid(0.26) ⇆ s6.head @ MR : N ~23px
        #   s5.mid ≈ (188.4, 155.7); s6.head = (196.9, 181.3); dist ≈ 27 px → N.
    ],
    "overall_pass": None,
    "notes": (
        "P-A-006 recipe: all 6 strokes inlined from bank stroke primitives "
        "(pie/shu/heng) with MMH anchors verbatim. Refused draw_ren_left "
        "whole-radical composition to avoid double-transform at Phase-3 aspect. "
        "s4 is a descending heng (Δy=+37 over Δx=132) — straight heng renders as "
        "the correct diagonal middle bar of 牙."
    ),
}
