# Principle Bank (Part B of memory)

Curator-owned. Natural-language **positive rules** for using the
Success Bank's primitives. Never error logs. Never "don't do X".
Always "to achieve Y, do Z".

A principle is graduated INTO this bank from the Sandbox (Part C)
once it has worked on a real success — the Curator pulls the
generalizable rule out and writes it here.

---

## §1 — Brushwork primitives

(Initially empty — populated as run_4 develops mastered atomic
strokes. Likely first entries: how to render 横/竖/撇/捺/提/点
with per-sample pensize on a smooth cubic Bézier, with the width
floor mandate from run_3's c17→c18 lesson.)

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
