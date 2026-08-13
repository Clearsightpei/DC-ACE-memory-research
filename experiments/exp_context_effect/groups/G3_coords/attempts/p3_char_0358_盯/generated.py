# BANK_DEVIATION
# skipped: ri.py (目) — ri.py uses fixed absolute pixel coords centered at
#   150 with x_left=90..x_right=205 (~115px wide). Cannot compress to fit
#   left-half slot for 盯 without rewriting; scale only affects stroke width.
# reason: 盯 needs 目 rendered narrow on the LEFT side (~30% width), and
#   ri.py's baked-in width doesn't shrink; also ding_char.py's heng is
#   centered on canvas which is wrong for right-half placement.
# fresh_component: mu_left_narrow (compressed tall 目 for L-R composition)
# fresh_component: ding_right (丁 with heng+shu_gou anchored to right half)

# 盯 = 目 (left, narrow-tall) + 丁 (right, top heng spans right half, shu_gou drops)
# GT: 目 occupies left ~25%, 丁 heng bridges from top of 目 across right,
#     shu_gou descends from ~2/3 x, tiny left hook at bottom.

from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), (255, 255, 255))
t = ImageDraw.Draw(img)

# ---- 目 on the LEFT ----
# Narrow tall rectangle with two inner horizontals
mu_L = 55
mu_R = 118
mu_T = 88
mu_B = 245
w_edge = 8
w_mid = 6

# Stroke 1: left 竖
t.line([(mu_L, mu_T), (mu_L, mu_B)], fill=(0, 0, 0), width=w_edge)
# Stroke 2: top 横 + right 竖 (横折)
t.line([(mu_L, mu_T), (mu_R, mu_T)], fill=(0, 0, 0), width=w_edge)
t.line([(mu_R, mu_T), (mu_R, mu_B)], fill=(0, 0, 0), width=w_edge)
# Stroke 3: upper inner 横 (with small gap on right per GT convention)
y_mid_upper = mu_T + (mu_B - mu_T) // 3
t.line([(mu_L + 3, y_mid_upper), (mu_R - 5, y_mid_upper)],
       fill=(0, 0, 0), width=w_mid)
# Stroke 4: lower inner 横
y_mid_lower = mu_T + 2 * (mu_B - mu_T) // 3
t.line([(mu_L + 3, y_mid_lower), (mu_R - 5, y_mid_lower)],
       fill=(0, 0, 0), width=w_mid)
# Stroke 5: bottom 横
t.line([(mu_L, mu_B), (mu_R, mu_B)], fill=(0, 0, 0), width=w_edge)

# ---- 丁 on the RIGHT ----
# Top heng spans from just right of 目 across to near canvas edge.
# GT shows the heng crossing over the top of 目 as well.
ding_heng_L = mu_L + 5           # heng starts slightly right of 目 left edge
ding_heng_R = 285
ding_heng_y = mu_T - 5           # slightly above 目 top per GT
t.line([(ding_heng_L, ding_heng_y), (ding_heng_R, ding_heng_y)],
       fill=(0, 0, 0), width=w_edge)

# Shu_gou: vertical from just below heng down to ~mu_B, with small left hook
sg_x = 215
sg_top = ding_heng_y + 2
sg_bot = mu_B
t.line([(sg_x, sg_top), (sg_x, sg_bot)], fill=(0, 0, 0), width=w_edge)
# hook: short segment to the upper-left
hook_end_x = sg_x - 18
hook_end_y = sg_bot - 12
t.line([(sg_x, sg_bot), (hook_end_x, hook_end_y)],
       fill=(0, 0, 0), width=w_edge)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_盯.png"))
