#!/usr/bin/env python3
"""Render a single Chinese stroke as a ground-truth PNG.

Usage:
    python tools/make_stroke_gt.py <stroke_name> <output_path> [--size N] [--seed N]

Examples:
    python tools/make_stroke_gt.py heng ground_truths/heng.png
    python tools/make_stroke_gt.py heng_zhe_gou ground_truths/heng_zhe_gou.png --size 60

List available strokes:
    python tools/make_stroke_gt.py --list
"""

import argparse
import io
import os
import random
import sys
import turtle

from PIL import Image

from strokes import STROKES

WIDTH = 800
HEIGHT = 600


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    b = io.BytesIO(ps.encode("utf-8"))
    img = Image.open(b)
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def render(stroke_name, out_path, size=None, seed=None):
    if stroke_name not in STROKES:
        print(f"Unknown stroke: {stroke_name}. Use --list to see available.", file=sys.stderr)
        sys.exit(1)

    if seed is not None:
        random.seed(seed)

    spec = STROKES[stroke_name]
    if size is None:
        lo, hi = spec["size_range"]
        size = (lo + hi) / 2  # deterministic midpoint

    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    turtle.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)

    spec["fn"](t, size)

    turtle.update()
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    save_canvas_to_png(screen, out_path)
    try:
        screen.bye()
    except Exception:
        pass

    print(f"Wrote {out_path}  (stroke={spec['char']} '{stroke_name}', size={size:.1f})")


def main():
    parser = argparse.ArgumentParser(description="Render a single Chinese stroke as ground truth PNG.")
    parser.add_argument("stroke_name", nargs="?", help="Stroke key (e.g. 'heng', 'shu_gou'). See --list.")
    parser.add_argument("output_path", nargs="?", help="Output PNG path.")
    parser.add_argument("--size", type=float, default=None, help="Stroke size (default: midpoint of stroke's range)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed (rarely needed; deterministic by default)")
    parser.add_argument("--list", action="store_true", help="List all available strokes and exit")
    args = parser.parse_args()

    if args.list:
        print(f"{'key':<22} {'char':<6} {'meaning':<28} size_range")
        print("-" * 70)
        for k, v in STROKES.items():
            print(f"{k:<22} {v['char']:<6} {v['meaning']:<28} {v['size_range']}")
        return

    if not args.stroke_name or not args.output_path:
        parser.error("stroke_name and output_path are required (or use --list)")

    render(args.stroke_name, args.output_path, size=args.size, seed=args.seed)


if __name__ == "__main__":
    main()
