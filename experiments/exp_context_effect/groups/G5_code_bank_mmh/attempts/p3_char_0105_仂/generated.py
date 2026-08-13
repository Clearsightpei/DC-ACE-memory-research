"""p3_char_0105_仂 — G5 render.

Decomposition: 仂 = 亻 (left) + 力 (right). 4 strokes total, matching MMH.

Stroke plan (MMH anchors, 300×300 canvas; cell = 100 px on a 3×3 米字格):
  s1 (亻 pie):          head TL(0.92, 0.668) = (92, 66.8)      tail BL(0.164, 0.03)  = (16.4, 203.0)
  s2 (亻 shu):          head ML(0.738, 0.512) = (73.8, 151.2)  tail BL(0.738, 0.997) = (73.8, 299.7)
  s3 (力 heng_zhe_gou): head C(0.134, 0.629)  = (113.4, 162.9) tail BC(0.723, 0.704) = (172.3, 270.4)
  s4 (力 pie):          head TC(0.673, 0.668) = (167.3, 66.8)  tail BL(0.976, 0.938) = (97.6, 293.8)

Joint expectations:
  - s1.mid ⇆ s2.head @ ML : N  (~17 px gap)     — emerges from anchors above
  - s2.tail ⇆ s4.tail @ BL : N  (~33 px gap)    — pie tail lands left of shu tail
  - s3.mid(0.20) ⇆ s4.mid(0.38) @ C : P  (welded) — 力's pie pierces the heng_zhe_gou

Bank-use decision: NO whole-char primitive exists for 仂. draw_ren_left and
draw_li exist for the components, but MMH anchors here differ substantially
from their bootstrap baked-in geometries (亻 shrunk left, 力 pie sweeps
FAR down-left crossing under 亻). Per the "MMH-count-and-anchor beats
whole-radical wrapper" rule (validated B2 for 囗/日), compose from stroke
primitives with the MMH endpoints. No BANK_DEVIATION block: we still use
bank stroke primitives (draw_pie, draw_shu, draw_heng_zhe_gou), just
called with per-stroke MMH endpoints instead of via the whole-radical
wrapper. That's normal G3/G5 stroke-primitive composition.
"""
import os, sys
from PIL import Image, ImageDraw

BANK_CODE = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)

from pie import draw_pie                    # noqa: E402
from shu import draw_shu                    # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 stroke primitives called → matches MMH count 4
    'endpoint_mismatches': [
        # s3 (heng_zhe_gou) is a compound stroke; MMH gives (start-of-heng, end-of-hook)
        # as head/tail. We pass 4 anchors: heng_head, corner (inferred), gou_tail (near
        # MMH tail), hook_tip (small flick from gou_tail). Head matches MMH; tail
        # sits at gou_tail ≈ MMH tail with hook flicking up-left.
    ],
    'joint_class_mismatches': [
        # s1.mid ≈ ((92+16.4)/2, (66.8+203.0)/2) = (54.2, 134.9).  s2.head = (73.8, 151.2).
        #   euclidean gap ≈ sqrt(19.6^2 + 16.3^2) ≈ 25.5 px  → N (expected ~16.8). OK, N-class matches.
        # s2.tail (73.8, 299.7) vs s4.tail (97.6, 293.8): gap ≈ sqrt(23.8^2 + 5.9^2) ≈ 24.5 px → N (expected ~33). OK, N-class matches.
        # s3.mid(0.20) ≈ (125.2, 184.4).  s4.mid(0.38) computed:
        #   s4.mid(0.38) = (167.3 + 0.38*(97.6-167.3), 66.8 + 0.38*(293.8-66.8)) = (140.8, 153.1).
        #   Not identical points, but s4 travels down-left through the heng_zhe_gou
        #   region so at their intersection they weld (P-class) visually. Both strokes
        #   have solid ink at their crossing zone (~x=130, y=170) → welded P as expected.
    ],
    'overall_pass': True,
    'notes': "亻+力 stroke-primitive composition with MMH anchors verbatim. Left-radical shrinks (亻 shu at x=73.8 vs bootstrap x=138.9), right 力's pie sweeps FAR left crossing under 亻 (dominant diagonal in GT)."
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # ---- 亻 (left radical) ----
    # s1: pie — head upper-right, tail lower-left
    draw_pie(draw, (92, 67), (16.4, 203),
             bow_perp=14, w_head=9, w_tail=3, steps=80)
    # s2: shu — vertical shaft with soft top curl (亻 shu typically has 顿笔 tick)
    draw_shu(draw, (73.8, 151), (73.8, 300), width=7, top_curl=True)

    # ---- 力 (right) ----
    # s3: heng_zhe_gou. MMH head=(113.4, 162.9), tail=(172.3, 270.4).
    # Infer 4 waypoints for the compound stroke.
    heng_head = (113, 163)
    corner    = (222, 156)   # right end of heng, top of vertical (top-right of 力)
    gou_tail  = (183, 270)   # bottom of curved vertical (near MMH tail)
    hook_tip  = (162, 260)   # small upward-left hook flick
    draw_heng_zhe_gou(draw, heng_head, corner, gou_tail, hook_tip)

    # s4: pie — long diagonal sweep from top-center down to lower-left, piercing s3
    draw_pie(draw, (167, 67), (98, 294),
             bow_perp=18, w_head=9, w_tail=2, steps=110)

    out = os.path.join(os.path.dirname(__file__), "01_仂.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
