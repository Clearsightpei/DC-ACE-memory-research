# p2_radical_007_乚 — the 乚 radical (1画 in the MMH catalog, orthographically a
# vertical-curve-hook 竖弯钩 shape positioned lower-left of the canvas).
#
# TR1/TR6 transform derivation:
#   Bank primitive: draw_shu_wan_gou.
#   Standalone default centers the shaft at x=150 (canvas center) and its shaft
#   top at y_math=+70 (pixel y=80). Tail runs right to x_math=+80 (pixel x=230),
#   hook tip at x_math=+75 (pixel x=225).
#
#   GT PNG inspection (乚 at 300x300):
#     - shaft top near pixel (95, 80)   -> shift x by ~-55
#     - tail runs to about pixel (215, 235) -> shaft bottom sits lower too
#     - hook tip near pixel (220, 210)
#   Net: primitive fits with ox=-55, oy=-20, scale=1.0 (shifts everything left
#   and down; the shape and proportions of the primitive are correct for 乚).
#
# TR7 sanity:
#   shaft top pixel = (150-55, 150-(-20+70)) = (95, 100)
#   shaft bot pixel = (95, 150-(-20-30)) = (95, 200)
#   arc bottom pixel = (95+40, 150-(-20-70)) = (135, 240)
#   tail end pixel  = (95+80, 200)? No — tail_end math = (ox+80, oy-70)
#                                = (-55+80, -20-70) = (25, -90) -> pixel (175, 240)
#   hook tip pixel  = (ox+75, oy-48) = (20, -68) -> pixel (170, 218)
#   All inside canvas with margin > 30 px. Good.

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
from shu_wan_gou import draw_shu_wan_gou

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
draw = ImageDraw.Draw(img)

# REVISION 1 — first pass was too small (shape occupied only 100x100 in center).
# GT fills roughly 130 (H) x 130 (W) with shaft top at pixel (95, 78) and tail
# end at pixel (215, 245). Scale up to 1.4 and reposition:
#   scale=1.4: shaft_span math=140, tail_span math=112
#   Target shaft top pixel y=78 -> oy + 70*1.4 = 72 -> oy = -26
#   Target tail end pixel x=215 -> ox + 80*1.4 = 65 -> ox = -47
# TR7 sanity re-check:
#   shaft top pixel = (150-47, 150-(-26+98)) = (103, 78)   OK
#   shaft bot pixel = (103, 150-(-26-42)) = (103, 218)     OK
#   tail end pixel  = (150+(-47+112), 218) = (215, 218)    OK
#   hook tip pixel  = (150+(-47+105), 150-(-26-67.2)) = (208, 243)? recompute:
#     hook_tip math = (ox+75*s, oy-48*s) = (-47+105, -26-67.2) = (58, -93.2)
#                   -> pixel (208, 243) — up-and-slightly-left of tail_end (215,218)
#     Wait: hook must flick UP (P1). tail_end pixel = (215, 218). hook tip pixel
#     y=243 is BELOW tail — that's wrong direction. Let me recompute.
#     tail_end math = (ox+80*s, oy-70*s) = (-47+112, -26-98) = (65, -124) -> pixel (215, 274). shaft bot recompute: (ox, oy-30*s)=(−47, −68) -> pixel (103, 218). So arc goes from (103,218) down to (215,274) — but that puts tail off-canvas (274 > 300 is ok, but too low).
# Recompute with oy=-26 targets: shaft bot math = -26 - 30*1.4 = -68 -> pixel y=218. Tail end math y = -26-70*1.4 = -124 -> pixel y=274. That's too low.
# Reset: the shu_wan_gou primitive's shaft is 100 units (70 top to -30 bot), tail-end is 40 units below shaft-bot (from -30 to -70). Total vertical extent = 70 to -70 = 140 units at scale 1.0. At scale 1.4 = 196 units. To fit in 300 canvas: shaft top pixel = 150 - (oy+98), tail bottom pixel = 150 - (oy-98). For symmetry around center: oy=0 -> top pixel=52, bot pixel=248.
# GT vertical extent is roughly from 78 (top of shaft) to 245 (bottom of tail) = 167 pixels. So at scale=1.2, vertical = 168 -> matches.
# Recompute at scale=1.2, oy=0: shaft_top pixel y = 150-(0+84) = 66. GT shaft top y=78. Adjust oy=-12 -> shaft_top pixel = 150-(-12+84)=78. Tail_end pixel y = 150-(-12-84)=246. GT=245. Good.
# Horizontal at scale=1.2: tail_end math x = ox+96. Target pixel x=215 -> 150+ox+96=215 -> ox=-31. Shaft pixel x = 150-31=119. GT shaft x=95. Small mismatch (~24px). Shift ox=-55: then shaft pixel=95 (matches GT), tail_end pixel=150-55+96=191. GT tail x=215. Trade-off. Compromise ox=-42: shaft=108, tail=204. Or accept slightly narrower shape.
# Final choice: scale=1.2, ox=-45, oy=-12.
#   shaft top pixel = (150-45, 150-(-12+84)) = (105, 78)
#   shaft bot pixel = (105, 150-(-12-36)) = (105, 198)
#   tail end pixel  = (150+(-45+96), 150-(-12-84)) = (201, 246)
#   hook tip pixel  = (150+(-45+90), 150-(-12-57.6)) = (195, 219.6)  -- flicks UP ✓
draw_shu_wan_gou(draw, ox=-45, oy=-12, scale=1.2)

out = os.path.join(os.path.dirname(__file__), "01_乚.png")
img.save(out)
print(f"Wrote {out}")
