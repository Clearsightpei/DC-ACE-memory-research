# BANK_DEVIATION
# skipped: shi_male.py, shi_radical.py
# reason: stacked shi_male + shi_radical composition drifted proportions
#   in main + retry_1 (both FAIL); GT shows 士 sitting inside the top
#   arm of 尸 with the long 撇 sweeping fully to bottom-left corner.
#   Fresh inline render lets me control the shared envelope directly.
# fresh_component: sheng_char_inline (士 sub + 尸 envelope with long 撇)
#
# RETRY MEMORY CHECKLIST (B4-B5 v7 evolution)
# Q1 (errata): errata.md p3_char_0315_声 says "Bank shi_male + shi_radical
#   stacked composition SHOULD have worked; drawer's proportions cramped
#   the 尸 hook. Retry candidate." Fix: keep 士 compact and centered,
#   give 尸 full width and a long 撇 that reaches bottom-left.
# Q2 (form_catalog): 撇 in long-sweep contexts wants gentle bow, tapered
#   tail; horizontals in envelope contexts want thin uniform width.
# Q3 (helpers): none — this is a stacked/envelope composition, not
#   X-cross / mirror-dot / apex-kiss. Inline fresh.
#
# TRAJECTORY DIFF
# GT: 声 = 士 (top: long 横, 竖, short 横) + 尸 wrapping bottom
#   - top 横 spans ~55%-75% of canvas width (broad)
#   - 竖 through center of top 横, short
#   - middle 横 shorter than top, sits close under 竖
#   - 尸 top 横 is wide (canvas ~25%-80%)
#   - long 撇 starts at left end of 尸 top 横, sweeps down-left to bottom
#   - small enclosure on right side of 尸 = 竖 down + 横 back
# Main FAIL: rendered only a compact 白-looking box on right; missed
#   the top 横 of 士; 撇 too short; missing middle 横.
# Retry_1 FAIL: similar — got a shorter, right-shifted 士; the 尸
#   envelope collapsed; 撇 present but 士 sat too far right of center.
# Fixes this attempt:
#   1. Draw ALL 7 strokes explicitly, one per line.
#   2. 士 sits centered over 尸's top 横; both horizontals of 士 above
#      尸's top 横.
#   3. 撇 starts at (~x=95, y=115) and sweeps to (~x=45, y=270) with
#      a moderate bow — long sweep.
#   4. Thin uniform 4px width for envelope strokes; 5-6px for 撇.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
THIN = 4
MED = 5


def hline(x1, x2, y, w=THIN):
    d.line([(x1, y), (x2, y)], fill=INK, width=w)


def vline(x, y1, y2, w=THIN):
    d.line([(x, y1), (x, y2)], fill=INK, width=w)


def curve_pie(pts, w=MED):
    # simple polyline through control points
    d.line(pts, fill=INK, width=w, joint="curve")


def draw_sheng(t=None):
    # ------- 士 (top) -------
    # Stroke 1: long top 横
    hline(75, 215, 62)
    # Stroke 2: short 竖 through center of top 横
    vline(145, 60, 108)
    # Stroke 3: shorter middle 横 (under 竖, above 尸)
    hline(100, 190, 108)

    # ------- 尸 envelope + inner box -------
    # Stroke 4: long top 横 of 尸 (widest)
    hline(70, 235, 148)
    # Stroke 5: right-side inner box 竖 (short, goes down from ~x=225)
    vline(225, 148, 195)
    # Stroke 6: inner box bottom 横 (from ~x=115 back to right vline)
    hline(115, 225, 195)

    # Stroke 7: long 撇 — starts at left end of 尸 top 横,
    # sweeps down-left with gentle bow to bottom-left corner
    # Use bezier-like polyline
    pie_pts = [
        (95, 115),
        (90, 145),
        (85, 175),
        (78, 205),
        (68, 235),
        (55, 265),
        (45, 285),
    ]
    curve_pie(pie_pts, w=MED)


draw_sheng()

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0315_声__retry_2/01_声.png"
img.save(out)
print(f"saved {out}")
