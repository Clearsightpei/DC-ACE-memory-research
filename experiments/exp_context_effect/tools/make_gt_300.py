"""Render Chinese characters/strokes/radicals as 300x300 GT PNGs.

Deterministic pure-PIL renderer. No turtle, no postscript, no subprocess
isolation needed. Same input -> byte-identical output.

Uses upsample-then-Lanczos-downsample for anti-aliasing (draw at 900x900,
resize to 300x300).

Usage (CLI, kept for back-compat with existing callers):
    python3 make_gt_300.py --char 一 --out out.png
    python3 make_gt_300.py --char 一 --stroke-index 0 --out heng.png

In-process:
    from make_gt_300 import render
    render("人", "out.png")

Replaces the earlier turtle-based renderer (2026-07-19). The turtle
version leaked postscript state across chars when the bulk generator
was interrupted / re-invoked without full subprocess isolation, producing
overlaid glyphs (e.g. Jul-12 phase3 GTs had 以 painted on top of 人).
Pure PIL eliminates the class of bug entirely.
"""
import argparse
import json
import os
import sys
from PIL import Image, ImageDraw

CANVAS = 300           # final PNG size (WxW)
UPSAMPLE = 3           # draw at CANVAS*UPSAMPLE for AA via Lanczos
LINE_W = 4 * UPSAMPLE  # 4-px effective stroke at final resolution
MARGIN = 0.075         # 7.5% margin each side => char fills central 85%

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_default_graphics():
    for depth in range(6):
        p = os.path.join(HERE, *([".."] * depth), "draw_character", "graphics.txt")
        if os.path.exists(p):
            return os.path.abspath(p)
    return None


DEFAULT_GRAPHICS = _find_default_graphics()


class CharNotFound(Exception):
    """Raised when a character is missing from graphics.txt."""


def load_character(graphics_path, char):
    with open(graphics_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if item.get("character") == char:
                return item
    return None


def render(char, out_path, stroke_index=None, graphics_path=None):
    """Render one character's medians to a 300x300 PNG.

    Raises CharNotFound if char isn't in graphics.txt.
    Raises FileNotFoundError if graphics.txt itself is missing.
    """
    graphics_path = graphics_path or os.environ.get("GRAPHICS_TXT", DEFAULT_GRAPHICS)
    if not graphics_path or not os.path.exists(graphics_path):
        raise FileNotFoundError(
            "graphics.txt not found; set $GRAPHICS_TXT or pass graphics_path"
        )

    item = load_character(graphics_path, char)
    if item is None:
        raise CharNotFound(f"Character {char!r} not in graphics.txt")

    medians = item["medians"]
    if stroke_index is not None:
        if stroke_index >= len(medians):
            raise IndexError(
                f"stroke_index {stroke_index} >= {len(medians)} strokes in {char!r}"
            )
        medians = [medians[stroke_index]]

    W = CANVAS * UPSAMPLE
    img = Image.new("RGB", (W, W), "white")
    draw = ImageDraw.Draw(img)

    def to_xy(p):
        # MMH medians: (x, y) in [0, 1024], y grows UP (math convention).
        # PIL: y grows DOWN. Flip y, then map to canvas with margin.
        mx, my = p
        nx = mx / 1024.0
        ny = 1.0 - my / 1024.0
        px = int(round((MARGIN + nx * (1.0 - 2.0 * MARGIN)) * W))
        py = int(round((MARGIN + ny * (1.0 - 2.0 * MARGIN)) * W))
        return (px, py)

    for stroke in medians:
        if not stroke:
            continue
        pts = [to_xy(p) for p in stroke]
        for i in range(len(pts) - 1):
            draw.line([pts[i], pts[i + 1]], fill="black", width=LINE_W)
        r = LINE_W // 2
        for (px, py) in pts:
            draw.ellipse((px - r, py - r, px + r, py + r), fill="black")

    img = img.resize((CANVAS, CANVAS), Image.LANCZOS)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    img.save(out_path, "PNG")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--char", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--stroke-index", type=int, default=None,
                   help="Render only this stroke of the character (0-indexed).")
    p.add_argument("--scale", type=float, default=None,
                   help="Ignored (kept for CLI back-compat). Fit is margin-based.")
    p.add_argument("--graphics", default=None)
    args = p.parse_args()
    try:
        render(args.char, args.out, args.stroke_index, args.graphics)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr); sys.exit(2)
    except CharNotFound as e:
        print(str(e), file=sys.stderr); sys.exit(1)
    except IndexError as e:
        print(str(e), file=sys.stderr); sys.exit(1)
    print(f"Wrote {args.out}  (char={args.char}, canvas={CANVAS}x{CANVAS})")


if __name__ == "__main__":
    main()
