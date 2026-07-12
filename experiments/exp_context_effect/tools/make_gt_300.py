"""Render Chinese characters/strokes/radicals as 300×300 GT PNGs.

Differences from runs/run_6/tools/make_char_gt.py:
- Canvas is 300×300 (not 800×600).
- Coordinate scale defaults so the character fills ~250×250 (leaves margin).
- Supports rendering a single stroke from a character's medians (for
  the stroke primer, Phase 1) via --stroke-index.

Usage:
    python3 make_gt_300.py --char 一 --out out.png
    python3 make_gt_300.py --char 一 --stroke-index 0 --out heng.png
    python3 make_gt_300.py --char 口 --out kou.png
"""
import argparse
import io
import json
import os
import sys
import turtle
from PIL import Image

WIDTH = 300
HEIGHT = 300
DEFAULT_SCALE = 0.25  # 0.25 × 1024 = 256 px char range in 300×300 canvas

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_default_graphics():
    """Walk up looking for draw_character/graphics.txt."""
    for depth in range(6):
        candidate = os.path.join(HERE, *([".."] * depth), "draw_character", "graphics.txt")
        if os.path.exists(candidate):
            return os.path.abspath(candidate)
    return None


DEFAULT_GRAPHICS = _find_default_graphics()


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


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    b = io.BytesIO(ps.encode("utf-8"))
    img = Image.open(b)
    img.load(scale=1)
    # Crop to 300x300 in case postscript adds padding
    img = img.convert("RGBA")
    if img.size != (WIDTH, HEIGHT):
        # Center-crop
        w, h = img.size
        left = (w - WIDTH) // 2
        top = (h - HEIGHT) // 2
        img = img.crop((left, top, left + WIDTH, top + HEIGHT))
    img.save(path, "PNG")


def render(char, out_path, stroke_index=None, scale=DEFAULT_SCALE, graphics_path=None):
    graphics_path = graphics_path or os.environ.get("GRAPHICS_TXT", DEFAULT_GRAPHICS)
    if not graphics_path or not os.path.exists(graphics_path):
        print(f"graphics.txt not found; set $GRAPHICS_TXT or pass --graphics", file=sys.stderr)
        sys.exit(2)

    item = load_character(graphics_path, char)
    if item is None:
        print(f"Character {char!r} not in graphics.txt", file=sys.stderr)
        sys.exit(1)

    medians = item["medians"]
    if stroke_index is not None:
        if stroke_index >= len(medians):
            print(f"stroke_index {stroke_index} >= {len(medians)} strokes in {char!r}",
                  file=sys.stderr)
            sys.exit(1)
        medians = [medians[stroke_index]]

    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    turtle.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(4)

    def to_xy(p):
        # Math-convention (y-up) coords centered at 0,0
        x, y = p
        tx = (x - 512) * scale
        ty = (y - 512) * scale
        return tx, ty

    for stroke in medians:
        if not stroke:
            continue
        x0, y0 = to_xy(stroke[0])
        t.penup(); t.goto(x0, y0); t.pendown()
        for p in stroke[1:]:
            t.goto(*to_xy(p))
        t.penup()

    turtle.update()
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    save_canvas_to_png(screen, out_path)
    try:
        screen.bye()
    except Exception:
        pass
    n = len(medians) if stroke_index is None else 1
    print(f"Wrote {out_path}  (char={char}, {n} strokes, scale={scale}, canvas={WIDTH}x{HEIGHT})")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--char", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--stroke-index", type=int, default=None,
                   help="Render only this stroke of the character (0-indexed).")
    p.add_argument("--scale", type=float, default=DEFAULT_SCALE)
    p.add_argument("--graphics", default=None)
    args = p.parse_args()
    render(args.char, args.out, args.stroke_index, args.scale, args.graphics)


if __name__ == "__main__":
    main()
