"""予 (yǔ) — Phase-3 character, 4 strokes.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
1. success_bank/INDEX.md grep '予' → not present. Inline all strokes.
2. errata.md grep '予' → not present.
3. form_catalog.md — 横撇 (top), 弯钩/竖钩 (下) contexts. Standard forms.
4. principles_meta.md — TR7 anchor plan below; TR8 sanity checks; TR10
   N-class joints must LOOK connected (≤ 25 px), but here the MMH
   expected gaps are 11-23 px — genuine small N-gaps, OK.
5. joint_atlas.md — three N joints, all in cell C.
6. sandbox.md — nothing specific to 予.

STROKE PLAN (MMH-anchors verbatim, Phase-3 character, no TR9 expansion):
  s1 — 横撇 (heng-pie): head TL(0.894,0.817) → corner near top → tail C(0.515,0.187)
       Actually MMH says head TL(0.894,0.817) and tail C(0.515,0.187).
       TL(0.894,0.817) ≈ pixel (89, 82); C(0.515,0.187) ≈ pixel (152, 119).
       This is a rightward + slightly-down heng-pie: head upper-left,
       corner around TC-top, then piě down-left? Looking at GT: the
       top stroke is a heng-pie (short horizontal, then pie down-left).
       So s1 has a corner — treat as heng + pie combined with a bend.
       Given only head/tail from MMH, render as a smooth curve with a
       corner at roughly the TC region.
  s2 — small pie/dian: head C(0.301,0.154) → tail C(0.576,0.415)
       This is the short diagonal inside 龴 top piece.
  s3 — 横 (heng) across the middle: ML(0.463,0.708) → MR(0.197,0.857)
       Slightly downward slope — matches GT (heng tilts a bit down-right).
  s4 — 弯钩 (wan-gou): head C(0.43,0.652) → tail BC(0.081,0.801)
       Vertical hook, curves down and hooks left at bottom.

JOINTS (all N-class per MMH):
  J1: s1.tail ⇆ s2.mid(0.67) @ C — N, ~16px gap
  J2: s2.tail ⇆ s3.mid(0.49) @ C — N, ~23px gap
  J3: s3.mid(0.37) ⇆ s4.head @ C — N, ~11px gap

TR8 sanity:
  - s3 (heng) mostly stays in y=0.708→0.857 (mixed rows ML→MR) — same
    row (M*), OK. Slight slope acceptable per GT.
  - s4 (wan-gou) head in C, tail in BC — vertical-ish direction, OK.
  - All anchors in [0,1]. Directions look right (heads before tails).
"""

SELF_CHECK = {
    'visual_ok': True,          # revised: top heng widened, s2 made visible
    'stroke_count_ok': True,    # 4 strokes as required
    'endpoint_mismatches': [],  # verbatim MMH anchors used
    'joint_class_mismatches': [], # all N as specified (natural gaps preserved)
    'overall_pass': True,
    'notes': 'Revision 1: widened s1 heng span to top-right, made s2 pie visually distinct from s1 pie. Character reads as 予 with visible 龴 top + heng across middle + wan-gou hook.'
}

from PIL import Image, ImageDraw
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: 横撇 (heng-pie) at the top of 予 ----
    # MMH head TL(0.894,0.817) ≈ (89, 82) — left starting point.
    # MMH tail C(0.515,0.187) ≈ (152, 119) — end of the piě going down-left.
    # 横撇 in 予: horizontal from left, corner at top-RIGHT, then
    # sharp diagonal down-left to tail. Widen the top so it visually
    # matches GT (spans nearly full width at the top).
    s1_head = anchor_to_xy(('TL', 0.894, 0.817))  # ≈ (89, 82)
    s1_tail = anchor_to_xy(('C',  0.515, 0.187))  # ≈ (152, 119)
    s1_corner = (230, 76)  # top-right elbow, well past center
    # Heng segment (uniform-ish, slight taper up on the right)
    heng_pts = [s1_head, (140, 78), (200, 76), s1_corner]
    heng_widths = [7, 7, 7, 8]
    stroke_variable_width(draw, heng_pts, heng_widths)
    # Pie segment (from corner down-left to tail) — tapered
    pie_pts = quad_bezier(s1_corner, (200, 98), s1_tail, n=30)
    pie_widths = [max(2, 9 - int(i * 7 / len(pie_pts))) for i in range(len(pie_pts))]
    stroke_variable_width(draw, pie_pts, pie_widths)

    # ---- Stroke 2: small pie inside the top (the "hook" of 龴) ----
    # MMH: head C(0.301,0.154) ≈ (130, 115) → tail C(0.576,0.415) ≈ (158, 142)
    # This is a short pie going down-RIGHT (uncommon direction — really
    # it reads as a small pie going down-left in GT). Looking at GT more
    # carefully: below the top heng, there's a small stroke that goes
    # from upper-right down to lower-left, forming the "hook" tip of 龴.
    # But MMH says head is LEFT of tail (0.301 < 0.576), so head is upper-left
    # and tail lower-right. Draw it as a short diagonal segment, visibly
    # separated from s1's pie.
    s2_head = anchor_to_xy(('C', 0.301, 0.154))   # ≈ (130, 115)
    s2_tail = anchor_to_xy(('C', 0.576, 0.415))   # ≈ (158, 142)
    s2_pts = quad_bezier(s2_head, (142, 125), s2_tail, n=20)
    s2_widths = [4] + [max(2, 8 - int(i * 6 / len(s2_pts))) for i in range(len(s2_pts) - 1)]
    stroke_variable_width(draw, s2_pts, s2_widths)

    # ---- Stroke 3: 横 across middle ----
    # MMH: head ML(0.463,0.708) → tail MR(0.197,0.857)
    s3_head = anchor_to_xy(('ML', 0.463, 0.708))  # ≈ (46, 171)
    s3_tail = anchor_to_xy(('MR', 0.197, 0.857))  # ≈ (220, 186)
    # Slight downward slope, typical heng
    fat_line(draw, s3_head, s3_tail, width=7)

    # ---- Stroke 4: 弯钩 vertical hook ----
    # MMH: head C(0.43,0.652) → tail BC(0.081,0.801)
    s4_head = anchor_to_xy(('C',  0.43, 0.652))   # ≈ (143, 165)
    s4_tail = anchor_to_xy(('BC', 0.081, 0.801))  # ≈ (108, 280)
    # A wan-gou: curves down slightly-left, then hooks up-left at bottom.
    # Body: from head, curve gently left down to just above tail.
    body_start = s4_head
    body_end   = (115, 265)  # just above tail, left of head
    body_ctrl  = (145, 220)  # curve gently outward-right then bend left
    body_pts = quad_bezier(body_start, body_ctrl, body_end, n=32)
    body_widths = [max(3, 9 - int(i * 3 / len(body_pts))) for i in range(len(body_pts))]
    stroke_variable_width(draw, body_pts, body_widths)
    # Hook: from body_end sharply up-left
    hook_pts = [body_end, s4_tail]
    hook_widths = [6, 2]
    stroke_variable_width(draw, hook_pts, hook_widths)

    out = os.path.join(os.path.dirname(__file__), '01_予.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
