# Principle Bank (Part B of memory) — run_5

Curator-owned. Natural-language **positive rules** for producing a
render that looks unambiguously like the target character. Never
error logs. Never "don't do X". Always "to achieve Y, do Z".

A principle is graduated INTO this bank from the Sandbox once it has
worked on a real success.

---

## §0 — How the Drawer works in run_5

The Drawer is dispatched as a fresh subagent and **is given the GT
PNG to look at**. Its job is to *mimic the GT visually*: open the GT
with Read, sketch a turtle program, render its own PNG, open that
PNG too, and iterate until the two images read as the same
character. Vision is the primary signal; numeric coordinates are a
means, not the goal.

The Success Bank (when populated) provides reusable mastered code
the Drawer may compose via translate/scale. The Principle Bank
(this file) provides universal brushwork rules. The Sandbox holds
Curator notes on whatever character is currently in progress.

`tools/` remains quarantined during the Drawer's turn — the
parameter-leak concern from run_2 is unchanged. Only `ground_truths/`
is now visible.

---

## §1 — Brushwork primitives

### §1.0 — Universal brushwork rules (carried from run_4)

**To render any brushed stroke**: use a smooth cubic Bézier
centerline with per-sample pensize. The canonical helper
`brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220)` walks
`s ∈ [0, 1]` and calls `t.pensize(max(3, w_profile(s)))` then
`t.goto(x, y)` at each sample. The `max(3, ...)` floor is
non-negotiable — pensize < 3 anywhere except a deliberately tapered
tip reads as a hairline (run_3 c17 lesson, verified across run_4).

**Min sample count**: 200 for atomic strokes, 160 for short
hooks/segments. Below ~120 the Bézier looks polygonal.

(Per-stroke recipes — §1.1 onward — populate as the Drawer masters
atomic strokes in run_5.)

---

## §2 — Composition (reuse interface)

### §2.1 — Translate/scale interface (carried from run_4)

Every Success Bank `draw()` function takes
`(t, ox=0, oy=0, scale=1.0)`. Translation adds `(ox, oy)` to every
coordinate; scale multiplies coordinates but does NOT scale the
pensize (width is in pixel-units of the stroke, not the character).

To use a primitive inside a character, call e.g. `draw_heng(t,
ox=<center_x>, oy=<center_y>, scale=<s>)`.

---

## §3 — Graphics-coordinate translation

`tools/list_chars.py` and `graphics.txt` provide canonical stroke
skeletons in MakeMeAHanzi's coordinate system (1024×1024 canvas,
math-convention y-up). The Drawer doesn't read graphics.txt
directly (it's quarantined inside `tools/`); the GT PNG is the
visible surface.

The Teacher generates the GT via `tools/make_char_gt.py` which
encodes `tx = (x - 512) * scale; ty = (y - 512) * scale` with
`scale = 0.4`. **No mirror, no flip.** The GT PNG is rendered on
the same 800×600 canvas the Drawer uses.

---

## §4 — Slot reserved for run_5-emergent rules

(Empty. The Curator graduates a sandbox finding into a numbered §4.N
entry when it has worked on a real Success Bank promotion.)
