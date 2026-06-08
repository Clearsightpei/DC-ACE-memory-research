# Principle Bank (Part B of memory)

Curator-owned. Natural-language **positive rules** for using the
Success Bank's primitives. Never error logs. Never "don't do X".
Always "to achieve Y, do Z".

A principle is graduated INTO this bank from the Sandbox (Part C)
once it has worked on a real success — the Curator pulls the
generalizable rule out and writes it here.

---

## §1 — Brushwork primitives

### §1.0 — Universal brushwork rules

**To render any brushed stroke**: use a smooth cubic Bézier
centerline with per-sample pensize. The canonical helper, kept as
`brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220)`, walks
`s ∈ [0, 1]` and calls `t.pensize(max(3, w_profile(s)))` then
`t.goto(x, y)` at each sample. The `max(3, ...)` floor is
non-negotiable — pensize < 3 anywhere except a deliberately tapered
tip will read as a hairline and fail the rubric's `taper` criterion
(run_3 c17 lesson).

**Min sample count**: 200 for atomic strokes, 160 OK for short
hooks/segments. Below ~120 the Bézier looks polygonal.

### §1.1 — 横 (heng, horizontal stroke)

**To draw 横**: use `success_bank/code/heng.py`'s `draw(t, ox=0,
oy=0, scale=1.0)`. The canonical endpoints are (-200, -3) →
(+200, +3) — note the gentle ~6 px upward rise that gives the
楷书 tilt. Width profile: entry press 16 → shaft 11 →
closing press 19 (right end is heaviest, this is the 收笔).

Established by c1 (rubric 10/10).

### §1.2 — 竖 (shu, vertical stroke, 垂露 variant)

**To draw 竖**: use `success_bank/code/shu.py`'s `draw(t, ox=0,
oy=0, scale=1.0)`. Canonical endpoints (0, +200) → (0, -200),
perfectly vertical. Width profile: symmetric barbell — top
press 16 → shaft 11 → bottom 垂露 press 18.

The 垂露 (rounded-bottom) variant is preferred over 悬针
(needle-tip) for general reuse inside compound characters. If a
needle-tip is needed later (e.g. lone 竖 in 中, 十), add a separate
`shu_needle.py` entry rather than modifying this one.

Established by c2 (rubric 10/10). Also verified the §2.1 reuse
interface: shu.py imports `brushed_bezier` from heng.py rather than
duplicating the helper. This is the canonical pattern for future
entries.

### §1.3 — 撇 (pie, diagonal sweep, 斜撇 variant)

**To draw 撇**: use `success_bank/code/pie.py`'s `draw(...)`.
Canonical endpoints head (+150, +200) → tail (-180, -180). Control
points place the centerline above the straight head-to-tail line for
a gentle concave-down arc. Width profile: head 18 → shaft 14 → 11
→ tail 3.

**General pattern for tapered-tip strokes (撇 / 提 / etc.):**
1. Heavy weighted head (16–18 peak) over the first ~10–12% of `s`.
2. Solid shaft (~11) over the middle ~76% — DON'T let it thin out
   early, or the stroke reads as flimsy.
3. Final 10–15% taper from shaft width down to pensize 3 (the floor
   enforced by `brushed_bezier`'s `max(3, ...)`). A 12% taper window
   reads smoother than a 5% window (c3 self-preview refinement
   verified this).

Established by c3 (rubric 10/10).

### §1.4 — 捺 (na, right-diagonal with flat kick, 斜捺 variant)

**To draw 捺**: use `success_bank/code/na.py`'s `draw(...)`. The
critical difference from 撇: 捺's width profile is REVERSED
(thin head → heavy tail) and it has a **flat-kick** tail (顿笔 +
出锋), not a tapered point.

Canonical segments:
- **Main sweep**: head (-150, +200) → kick base (+170, -180).
  Controls bow the centerline below the straight line → gentle
  concave-UP arc (opposite of 撇's concave-down).
- **Flat kick**: (+170, -180) → (+240, -172). Short ~70 px,
  near-horizontal release.

Width profile:
- Main sweep: 5 → 8 → 14 → 18.
- Flat kick: 18 → 16 (press hold, 25%) → 3 (release, 75%).

### §1.5 — Two-segment stitched strokes (general pattern)

(Established by c4 with 捺's main + kick segments.)

When a stroke has a distinct **terminal feature** (kick, hook,
turn) that has different width and direction than the main sweep,
implement it as **TWO Bézier segments stitched at a junction**:

1. **Segment A** = the main sweep. End its centerline pointing
   tangentially toward the next segment's direction by placing A's
   final control point (A2) near the junction in the direction of
   B's first control point (B1).
2. **Segment B** = the terminal feature. Start at A's endpoint
   (A3 == B0).
3. Use independent `w_profile` functions for each segment so the
   width can change discontinuously across the junction if needed
   (e.g. 捺's kick starts at the same width A ended at, then has
   its own press-and-release sub-curve).

This pattern is what makes 横折, 竖钩, 横折钩, 竖弯钩, 横撇,
横折弯钩, 撇点 all expressible as small variations on a shared
structure. The c4 self-preview verified that **tangential junction
control** (pulling A2 toward the next segment's direction)
eliminates the angular-notch artifact at the junction.


---

## §2 — Composition (positioning, scaling, layering components)

(Initially empty — populated when the Curator promotes findings from
the Sandbox after a successful character is built from existing
parts. Examples of entry shape:

> **§2.1 — Translating a Success Bank entry**: to move a mastered
> 部首 left by `Δx` pixels, call its `draw(t, ox=Δx_neg, oy=0)`. The
> entry's internal coords are expressed relative to (0, 0); the
> `ox`/`oy` parameters translate the entire stroke set without
> distortion.
>
> **§2.2 — Scaling a Success Bank entry**: to shrink a 部首 to 1/N,
> ...

are placeholders — actual rules emerge from real successes.)

**§2.1 (verified c1)**: every Success Bank `draw()` function takes
`(t, ox=0, oy=0, scale=1.0)`. Translation is by adding `(ox, oy)`
to every coordinate; scale multiplies the coordinates (but does
NOT scale the pensize — width is in pixel-units of the stroke, not
the character). To use 横 inside a character, call `draw_heng(t,
ox=<center_x>, oy=<center_y>)`.

---

## §3 — Contrastive principles (distinguishing X from Y)

These are entries that prevent OCR-boundary near-misses. The Curator
writes one HERE when the same OCR-mis-classification recurs ≥ 2
cycles on the same character pair. Each contrastive principle has
the form:

> **§3.N — `X` vs `Y`**: to make a render read as `X` (and not as
> `Y`), the **distinguishing feature** is: …. If your render lacks
> this feature, OCR will collapse `X` into `Y`. This was learned
> from cycles `[a, b]` where the silhouette was geometrically
> reasonable for `X` but kept reading as `Y`.

(Initially empty. Examples that would have helped run_3 — DO NOT
import these as facts, they are illustrations; rebuild from
run_4's own evidence:

- 力 vs 万: 万 has a separate 横 *above* the 力 portion;
- 卫 vs 也: 也's 竖弯钩 must hook up at the right end;
- 已 vs 巴: 巴's upper portion has a closed-bottom internal divider.)

---

## §4 — Graphics-coordinate translation

The `tools/list_chars.py` and `graphics.txt` provide canonical
stroke skeletons in MakeMeAHanzi's coordinate system (1024×1024
canvas, math-convention y-up). Our canvas is 800×600 turtle (origin
center, y-up). The `tools/make_char_gt.py` already encodes the
transform: `tx = (x - 512) * scale; ty = (y - 512) * scale` with
`scale = 0.4` by default. **No mirror, no flip** — math-convention
to math-convention.

(More translation rules added as the Teacher's brief-generation
tools mature.)

---

## §5 — Skeleton vs brushwork phases

run_4 splits each character into two phases:

> **§5.1 — Skeleton phase**: the Drawer outputs `generated_skel.py`
> using thin uniform pensize (3). Goal: get all stroke endpoints
> and centerlines RIGHT — composition only.
>
> **§5.2 — Brushwork phase**: only after the Curator approves the
> skeleton, the Drawer outputs `generated.py` adding per-sample
> pensize per the width-floor table in §1. The brushwork phase
> must NOT change endpoint coordinates from the approved skeleton.

(Width-floor table and Bézier helper to be added once the first
atomic-stroke recipes are mastered in run_4 cycle 1–2.)

### §5.3 — Atomic strokes are SINGLE-PHASE

(Established by c1 design.)

For Phase 1 (atomic strokes) and Phase 2 (compound strokes), there
is no GT (eval = `vision` only). The skeleton-vs-GT comparison is
not applicable — the stroke IS its own composition. So these
phases run a single brushwork pass and are scored by the vision
rubric directly. The skeleton/brushwork split kicks in at Phase 3
(characters).
