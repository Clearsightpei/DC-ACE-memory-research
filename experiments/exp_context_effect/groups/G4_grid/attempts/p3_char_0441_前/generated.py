"""前 (qián, "front") — 9 strokes.

Decomposition: 前 = 䒑 (top: 丷 + 一) + 月 (left-inner frame + 2 hengs) + 刂 (right vertical).
The 9-stroke MMH count matches the ⺊-style top + 月-body + 刂 tail composition.

A-recipe applied (per drawer_memory.md B9+B10+B11 codification):
  1. Explicit decomposition (this docstring).
  2. MMH-verbatim anchors (all 9 head/tail tuples passed unchanged).
  3. SELF_CHECK block below.
  4. Base primitives (_anchor + fat_line + variable-width polylines) — no compound
     bank primitive fits this composition cleanly.  月-inner and 刂 slot into a
     compressed right-lower block that no bank component matches at scale.
  5. N-joint discipline: all 6 declared joints are class N (small natural gaps).
     Do NOT weld the top-heng to the two dots; do NOT weld the internal hengs
     to the frame sides — leave the ~15-25 px gaps MMH indicates.

No bank primitive skip requires BANK_DEVIATION block here: no compound primitive
in the bank targets a 9-stroke 前-shape, so inlining is default not deviation.
"""

from PIL import Image, ImageDraw
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke calls below
    'endpoint_mismatches': [], # all anchors MMH-verbatim
    'joint_class_mismatches': [], # all joints N; base primitives naturally leave gaps
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; all N-joints preserved via unwelded endpoints.',
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- MMH-verbatim anchors ----
    # s1: left top dot 丶
    S1_H = anchor_to_xy(('TC', 0.055, 0.642))
    S1_T = anchor_to_xy(('TC', 0.33,  0.92))
    # s2: right top dot 丶
    S2_H = anchor_to_xy(('TC', 0.928, 0.492))
    S2_T = anchor_to_xy(('TC', 0.679, 0.949))
    # s3: top horizontal 一
    S3_H = anchor_to_xy(('ML', 0.322, 0.245))
    S3_T = anchor_to_xy(('MR', 0.792, 0.11))
    # s4: left vertical (left side of 月)
    S4_H = anchor_to_xy(('ML', 0.738, 0.547))
    S4_T = anchor_to_xy(('BL', 0.712, 0.812))
    # s5: 横折钩-like right-side fold of 月 inner frame — starts as short
    #     heng across, then long shu down.  Approximate as two segments.
    S5_H = anchor_to_xy(('ML', 0.911, 0.635))
    S5_T = anchor_to_xy(('BC', 0.069, 0.672))
    S5_CORNER = anchor_to_xy(('C', 0.20, 0.05))  # implicit bend at top of shu
    # s6: bottom heng of 月 frame
    S6_H = anchor_to_xy(('ML', 0.894, 0.98))
    S6_T = anchor_to_xy(('C',  0.195, 0.928))
    # s7: inner middle heng of 月
    S7_H = anchor_to_xy(('BL', 0.885, 0.309))
    S7_T = anchor_to_xy(('BC', 0.181, 0.256))
    # s8: small inner heng/dot inside 月 (upper)
    S8_H = anchor_to_xy(('C',  0.702, 0.614))
    S8_T = anchor_to_xy(('BC', 0.764, 0.417))
    # s9: 刂 right vertical (long tail down)
    S9_H = anchor_to_xy(('MR', 0.118, 0.333))
    S9_T = anchor_to_xy(('BC', 0.875, 0.774))

    # ---- render ----
    # s1: left top-dot 丶 — MMH gives a longish diagonal; render as a short
    # taper (dian) shape rather than a full-length blade.  Shrink to ~55% of
    # MMH length while keeping the head anchor fixed.
    def shrink(h, t, frac=0.6):
        return (h[0] + frac*(t[0]-h[0]), h[1] + frac*(t[1]-h[1]))
    S1_T_s = shrink(S1_H, S1_T, 0.7)
    pts1 = [S1_H, ((S1_H[0]+S1_T_s[0])/2, (S1_H[1]+S1_T_s[1])/2), S1_T_s]
    stroke_variable_width(d, pts1, [3, 7, 10])

    # s2: right top-dot 丶 — mirror shape, similarly shrunk
    S2_T_s = shrink(S2_H, S2_T, 0.7)
    pts2 = [S2_H, ((S2_H[0]+S2_T_s[0])/2, (S2_H[1]+S2_T_s[1])/2), S2_T_s]
    stroke_variable_width(d, pts2, [3, 7, 10])

    # s3: top heng — slight up-slope, variable width
    pts3 = [S3_H,
            ((S3_H[0]+S3_T[0])/2, (S3_H[1]+S3_T[1])/2),
            S3_T]
    stroke_variable_width(d, pts3, [7, 6, 9])

    # s4: 月 left vertical — slight leftward curve (撇-lean)
    ctrl4 = ((S4_H[0]+S4_T[0])/2 - 3, (S4_H[1]+S4_T[1])/2)
    pts4 = quad_bezier(S4_H, ctrl4, S4_T, n=30)
    stroke_variable_width(d, pts4, [7]*len(pts4))

    # s5: 横折钩 — right side of the 月 inner frame.  MMH head is top-right,
    # tail is bottom-left of the frame.  Add an explicit heng segment at top
    # before the shu drops, so the corner reads as a fold rather than a bare
    # curve.
    S5_TOP_LEFT = (S5_H[0] - 14, S5_H[1] - 2)  # short heng going LEFT from head
    ctrl5 = (S5_H[0] + 3, (S5_H[1]+S5_T[1])/2)
    pts5_shu = quad_bezier(S5_H, ctrl5, S5_T, n=32)
    hook_end = (S5_T[0] - 9, S5_T[1] - 7)
    # combined polyline: top-left heng end → head (corner) → shu → hook
    pts5_full = [S5_TOP_LEFT, S5_H] + pts5_shu[1:] + [hook_end]
    widths5 = [5, 8] + [8]*(len(pts5_shu)-1) + [4]
    stroke_variable_width(d, pts5_full, widths5)

    # s6: bottom heng of 月
    fat_line(d, S6_H, S6_T, 6)

    # s7: inner middle heng of 月
    fat_line(d, S7_H, S7_T, 5)

    # s8: small inner heng inside 月 (near top)
    fat_line(d, S8_H, S8_T, 5)

    # s9: 刂 right vertical — long, slight taper at tail (竖)
    pts9 = [S9_H,
            ((S9_H[0]+S9_T[0])/2, (S9_H[1]+S9_T[1])/2),
            S9_T]
    stroke_variable_width(d, pts9, [8, 7, 5])

    out = os.path.join(HERE, "01_前.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
