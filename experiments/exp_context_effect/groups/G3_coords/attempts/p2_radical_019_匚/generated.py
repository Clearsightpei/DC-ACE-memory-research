# p2_radical_019_匚 (fang) — G3 attempt
#
# 匚 is a 2-stroke radical (MMH decomposition):
#   1. 横 (top horizontal), extending across upper portion
#   2. 竖折 (left vertical + bottom horizontal, joined at bottom-left corner)
#
# Bank consideration (per TR1-TR7 + Bank-is-supplementary):
#   - `heng` primitive fits stroke 1 with deliberate transform (TR1, TR2:
#     enclosing role → scale ~0.75, spanning most of upper canvas).
#   - `shu_zhe` primitive's default proportions (100 wide horizontal,
#     160 tall vertical) don't match 匚's near-square envelope
#     (~150 wide × ~150 tall). Per TR5, INLINE the 竖折 recipe rather
#     than force-stretch the primitive with non-uniform axis scaling.
#   - Also, 匚's vertical starts UP at the same y-level as the top 横
#     ends (weld at the top-left corner) — the standalone shu_zhe
#     assumes a lower head.
#
# Corner welds (TR4):
#   - Top 横's LEFT end and 竖折's vertical TOP share the pixel (-80, +50).
#   - Layout uses math coords (center origin, +y up), matches P5.
#
# Envelope (eyeball TR7): all four extreme points ≈ 20 px inside canvas
# margins → fits 300×300 with breathing room.

from PIL import Image, ImageDraw
import sys, os

# Import bank primitives (from success_bank/code/)
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from heng import draw_heng  # standalone heng: 200px wide, 12px thick, centered at (ox,oy)

CANVAS = 300


def _to_pixel(ox, oy):
    """math coords (center origin, +y up) -> PIL pixel."""
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def draw_fang_radical(t):
    # --- Stroke 1: top 横 ---
    # Target span in math coords: x from -80 to +70, y ≈ +50.
    # Standalone heng half_len = 100. We want half_len = 75 → scale = 0.75.
    # Center of the horizontal at x = (-80 + 70)/2 = -5; y = +50.
    # (TR6: primitive center (0,0) → target center (-5, +50); ox=-5, oy=+50, scale=0.75)
    draw_heng(t, ox=-5, oy=+50, scale=0.75)

    # --- Stroke 2: 竖折 (left vertical + bottom horizontal), inlined ---
    # Vertical top: (-80, +50) — welded to left end of top 横
    # Vertical bottom / horizontal left: (-80, -95) — bottom-left corner
    # Horizontal right: (+75, -95)
    ink_v = 12
    ink_h = 12

    v_top = (-80, +50)
    v_bot = (-80, -95)
    h_right = (+75, -95)

    t.line([_to_pixel(*v_top), _to_pixel(*v_bot)],
           fill=(0, 0, 0), width=ink_v)
    t.line([_to_pixel(*v_bot), _to_pixel(*h_right)],
           fill=(0, 0, 0), width=ink_h)

    # 顿笔 (small corner blob) at the bottom-left elbow so the two
    # segments read as one continuous 竖折 rather than two lines
    # (P6). Diameter ≈ ink so it merges with the stroke.
    cx, cy = _to_pixel(*v_bot)
    r = 6
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_fang_radical(draw)
    out = os.path.join(HERE, "01_匚.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
