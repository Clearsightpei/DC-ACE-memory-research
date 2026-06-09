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

### §1.1 — 横 (heng) width profile (verified c2)

**To draw a 楷书 横**: width profile is `entry-press 16 → shaft 11 →
closing-press 22`, with the RIGHT END being the heaviest point of
the stroke. The right closing-press (收笔) is what makes the stroke
read as 楷书 rather than block-printing or thin cursive.

**Wrong** (verified c1 failure): bell-curve `light → heavy → light`
with the right end tapered thin. This reads as a calligraphic
stroke but fails the `dunbi` (顿笔) criterion because the 收笔 is
the opposite of a press — it's a release.

**Right** (verified c2 success): right end is the visibly thickest
point. A small angled foot at each end is OK but it must be at
the same heavy width as the closing-press (not tapered down).

See `success_bank/code/heng.py`'s `draw_heng(draw, ox, oy, length,
scale=1.0)` for the canonical implementation. Reuse it whenever
you need a 横 — do not re-derive the width profile.

### §1.2+ — populate as more strokes master.

---

## §2 — Composition (reuse interface)

### §2.1 — Translate/scale interface (PIL-based in run_5)

Every Success Bank `draw()` function takes
`(pil_draw, ox=0, oy=0, scale=1.0)`. `pil_draw` is a
`PIL.ImageDraw.Draw` object — run_5 standardized on PIL rendering
in c2 because the turtle.PostScript → PIL pipeline was fragile on
macOS. The math is unchanged from §1.0: cubic Bezier centerline +
per-sample `max(3, w(s))` width floor.

Translation adds `(ox, oy)` to every coordinate; scale multiplies
coordinates but does NOT scale the pensize (width is in pixel-units
of the stroke, not the character).

The 横 primitive (`heng.py`) additionally takes a `length` parameter
because the same stroke is reused at different horizontal extents
across a character (e.g. 三's bottom 横 is longer than its top).

To use a primitive inside a character, call e.g. `draw_heng(pil_draw,
ox=<center_x>, oy=<center_y>, length=<px>, scale=<s>)`.

To use a whole-character entry (e.g. 一/二/三), call its `draw(pil_draw,
ox=0, oy=0, scale=1.0)`.

### §2.2 — 竖 vs 横 structural relationships (verified c3/c4)

When composing a character with a 横 and a 竖, the **vertical position of
the 竖's top entry-press relative to the 横's centerline** determines what
the silhouette reads as. Three distinct patterns:

| pattern | `oy_top` rule | examples (verified) |
|---|---|---|
| **piercing** (竖 crosses through heng) | `oy_top` is 50–100px ABOVE the heng's centerline | 十 (c3), 干 (c4) |
| **hanging** (竖 hangs from heng) | `oy_top` is AT or just below the heng's centerline (no pierce) | 下 (c4) |
| **spanning** (竖 stretches between two hengs) | `oy_top` at the upper heng's y, `length` = vertical gap | 工 (c4) |

The c3 attempt of 下 failed because the Drawer applied the piercing pattern
(treating 下 like 十) — the 竖 poked above the heng and the silhouette read
as 十-with-dot. The c4 attempt applied the hanging pattern correctly.

When the brief asks for a character with both 横 and 竖, the Drawer must
choose the pattern from the character's structure, not from defaults.

### §2.3 — 撇+捺 structural relationships (verified c5)

The three Chinese characters 八, 人, 入 are all composed of a 撇 and a
捺, but the relative position of the two stroke heads determines which
character the silhouette reads as. **This is the exact class that
produced the run_4 false positives** (c20 入 promoted at visual 0.58).
In run_5 the Drawer sees the GT and applies the right pattern:

| pattern | head relationship | examples (verified) |
|---|---|---|
| **separated** (visible gap between 撇 head and 捺 head) | 撇 head is below and to the left; 捺 head is above and to the right; roughly 80–100px horizontal slot between them | 八 (c5) |
| **shared apex** (撇 and 捺 emanate from the same point) | both stroke heads at exactly the same (x, y) | 人 (c5) |
| **捺 dominant, 撇 attached** (撇 head is BELOW the 捺's apex) | 捺's head is the topmost point; 撇's head sits below the 捺's head and the 撇 attaches as a shorter secondary stroke | 入 (c5) |

If the Drawer treats all three identically (or applies the shared-apex
pattern to 入), the silhouettes collapse to ambiguous wedges that OCR
maps to whichever character is closest in its small vocabulary — the
exact run_4 false-positive mechanism.

When the brief asks for a 撇+捺 character, the Drawer must look at the
GT and identify which of the three patterns applies before placing any
coordinates.

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
