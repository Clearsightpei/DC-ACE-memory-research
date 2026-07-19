# Principle Bank (G4 grid-bank)

**Reset with Phase-2 restart.** Phase-2-specific diagnostics, batch
statistics, and radical-family anti-rules have been stripped so the
bank contains only Phase-1-derived general rules and the transformation
rules that apply to any 米字格 composition. This is the memory the
Drawer inherits going forward.

General rules and techniques discovered while drawing. Not
item-mastery — those live in the Success Bank after human PASS.

## CRITICAL — TRANSFORMATION RULES (read FIRST every cycle)

**The reason bank primitives keep failing on new radicals is not that
the primitives are wrong — it's that Drawers are calling them with
DEFAULT anchors and expecting them to fit a new composition. Every
primitive in the bank is designed for STANDALONE use with anchors
spanning the full 米字格. To use it as a component you MUST OVERRIDE
the default anchors with new anchor tuples appropriate to the
composition.**

### TR1. Every primitive call must supply NEW anchor tuples, not defaults

Wrong:
```python
from shu import draw_shu
draw_shu(draw)  # default anchors — will span full canvas height
```

Right:
```python
from shu import draw_shu
# For 亻 (right side): 竖 lives in right half, from mid-height to bottom
draw_shu(draw, top=('TR', 0.3, 0.6), bot=('BR', 0.4, 0.9), width=10)
```

Before calling ANY primitive from the bank, decide three things:
1. **Which cells** should its head/tail land in (moves it in 米字格)?
2. **What x_frac/y_frac** within those cells (fine placement)?
3. **What width** — component strokes are usually thinner than
   standalone (default width * 0.7-0.85)?

If you can't answer all three, don't call the primitive — inline the
recipe (per the sandbox observation from batch 3-4).

### TR2. Radical-position anchor conventions

Component role → typical cell span (relative to standalone which fills TL-BR):
- **Left radical** (亻, 氵, 女): head anchors in TL/ML column, tail
  anchors in BL/ML column. x_frac range ≈ 0.1–0.6 (occupies left third).
- **Right radical** (刂, 阝-right, 攵): TR/MR column head, BR/MR tail.
  x_frac range ≈ 0.5–0.9 (occupies right third).
- **Top radical** (艹, 宀, 冖): TL/TC/TR row, y_frac range ≈ 0.0–0.4.
- **Bottom radical** (大, 皿, 心): BL/BC/BR row, y_frac range ≈ 0.6–1.0.
- **Enclosing** (门, 匚, 囗): all four cells, x_frac 0.05–0.95,
  y_frac 0.05–0.95 (leave ~5% edge margin).
- **Standalone**: fills the full 米字格 with anchors at cell edges
  (x_frac 0 or 1, y_frac 0 or 1) as needed.

### TR3. Cell selection IS transformation

Moving a primitive = choosing DIFFERENT cells for its endpoint anchors.
Do not think of `ox/oy` offsets — G4's format is (cell, x_frac,
y_frac). If you want a stroke shifted right, put its head in the TR
column instead of TC or TL. If you want it lower, use the B row.

This means when copying a standalone bank primitive into a composed
radical:
- Read the primitive's default anchor tuple defaults.
- Compute the target anchors for THIS composition (different cells or
  different fractions).
- Call the primitive with the new anchors as explicit overrides.

### TR4. Joint enforcement via shared anchor tuples

When two strokes should weld (P-class joint) or share a tip (T-class):
- Compute the shared anchor tuple explicitly.
- Pass it verbatim to both primitives (as the tail of stroke A and
  the head of stroke B, for example).
- Do NOT independently pick anchors and hope they land near each other.

For 十 (crossing at center C):
```python
CROSS = ('C', 0.5, 0.5)
draw_heng(draw, left=('ML', 0.15, 0.5), right=('MR', 0.85, 0.5))
draw_shu(draw, top=('TC', 0.5, 0.15), bot=('BC', 0.5, 0.85))
# Both strokes pass through CROSS by construction — P-weld verified.
```

For 亻 (T-joint, 竖 head touches 撇 body):
```python
# Compute where pie's body sits at y_frac = ~0.5 in the ML cell
TOUCH = ('ML', 0.55, 0.5)  # will be pie's mid-body
draw_pie(draw, head=('TL', 0.75, 0.2), tail=('BL', 0.2, 0.85))
draw_shu(draw, top=TOUCH, bot=('BR', 0.25, 0.85), width=8)
```

### TR5. Scale via anchor SPAN, not via a scale parameter

米字格 primitives don't take a `scale` parameter — smaller = shorter
anchor span. To shrink a stroke:
- Move its head anchor's x_frac/y_frac closer to its tail anchor's.
- Or move both anchors into a subset of cells (2 cells instead of 3).

Example: standalone 横 spans ('ML', 0.1, 0.5) → ('MR', 0.9, 0.5).
Component-width 横 (for 士's shorter bottom bar) spans
('C', 0.15, 0.5) → ('C', 0.85, 0.5) — same y, tighter x, one cell wide.

### TR6. If a primitive doesn't have the right anchor flexibility,
INLINE the recipe

Signs to inline instead of override:
- The composition requires a joint class not in the primitive's spec
  (e.g. primitive was defined with T-joint, composition needs P).
- The primitive's internal curve/bezier control points are baked to
  its default anchor span and don't rescale cleanly.
- Anchors would fall outside the primitive's expected cells (e.g.
  needing 竖 with head in the C cell instead of T row).

When inlining: copy the primitive's rendering code into your
`generated.py`, adjust the anchor tuples and any hardcoded pixel
constants, and add an inline joint spec comment. This preserves the
shape idiom while allowing per-item tuning.

### TR7. Every composition documents its anchor plan BEFORE render

```python
# 亻 anchor plan:
#   stroke 1 (撇): head @ ('TL',0.75,0.2), tail @ ('BL',0.2,0.85), width 10
#   stroke 2 (竖): head @ ('ML',0.55,0.5) [T-joint on pie body],
#                  tail @ ('BR',0.25,0.85), width 8
# Joints: s1.mid(0.5) ⇆ s2.head @ ML  — class T (tip touches body)
```

Comments force the transformation logic to be explicit. Bare
`draw_pie(draw); draw_shu(draw)` = guaranteed failure on any non-十
composition.

### TR8. Sanity check anchors before render

Before `python3 generated.py`:
1. For each stroke, is its head anchor pixel above/left of its tail
   anchor (or wherever the stroke direction demands)?
2. For each expected joint, are the two anchor tuples IDENTICAL (weld)
   or within 0.15 x_frac/y_frac of each other (N-class small gap)?
3. Do all anchors sit inside the 米字格 (x_frac and y_frac in [0,1])?
4. If your primitive has internal geometry constraints (e.g. shu_gou
   requires belly.x == head.x for a straight body), verify the anchors
   satisfy them. If they don't, OVERRIDE the anchor that violates or
   INLINE the recipe (TR6). Do NOT render a primitive with known-broken
   input — the drawer's own docstring flagging "this won't work" then
   rendering anyway was the root cause of 刂 failure.

If any check fails, adjust anchors before rendering. Rendering →
inspecting → adjusting wastes cycles.

### TR9. MMH anchors are a floor, not a ceiling for standalone radicals

MMH stroke-median data is derived from character glyphs where a
radical is one component of a larger character. When the current
task is a STANDALONE radical (Phase 2), verbatim MMH anchors will
often produce a stroke that occupies only a sub-region of the 米字格.

**Rule**: For single-stroke radicals, expand MMH anchors to a full
米字格 span before drawing:
- 丿-family: head ('TR', 0.85, 0.15), tail ('BL', 0.15, 0.85).
- 一-family: head ('ML', 0.1, 0.5), tail ('MR', 0.9, 0.5).
- 丨-family: head ('TC', 0.5, 0.1), tail ('BC', 0.5, 0.95).
- 乚-family: head TC or upper, tail reaches BR corner or nearly.

Verbatim MMH is fine when the radical appears as a component of a
larger character (Phase 3); as a standalone Phase-2 item, MMH
under-spans the grid. Empirical: bootstrap-batch 丿 FAILed due to
verbatim MMH.

### TR10. N-class joints must LOOK connected — enforce pixel proximity

N-class ("natural gap ~15-20 px") does NOT mean "strokes are visually
independent." When implementing N-class, verify pixel distance
between the two joint endpoints is ≤ 25 px. If MMH gives anchors in
different cells producing a large gap (>30 px), OVERRIDE to
near-weld: share the anchor tuple exactly (upgrade to T-class) or
place both in the SAME cell with fracs within 0.15.

Failure modes if you don't: the character breaks into fragments.
Bootstrap-batch 厂 and 刀 both FAILed by treating N-class as literal
separation.

### TR11. SELF_CHECK.visual_ok is a real check, not a checkbox

Before setting `SELF_CHECK.visual_ok = True`, name TWO SPECIFIC
visual features that agree between your rendered PNG and GT.
Examples:
- "Both have a curved 撇 sweep from upper-right to lower-left."
- "Both have the horizontal stroke terminating right of the vertical."

If you cannot name two agreements, `visual_ok=False` and revise once.

Empirical: bootstrap batch — ALL 6 G4 FAILs had
`SELF_CHECK.overall_pass=True`. The rubber-stamp habit is a
documented failure mode.

---

## Bank is supplementary, not mandatory

The Success Bank and this Principle Bank are *supplementary* memory,
not a required call-graph. When a bank primitive fits the composition
cleanly (correct joint class, anchor flexibility, taper profile), use
it via TR1-TR8 with explicit anchor overrides. When it doesn't, inline
the recipe (TR6). The Drawer's per-item cognitive budget is finite —
do not spend it wrestling a primitive into a shape it wasn't built for.

## 米字格 conventions

- Grid partitions the 300×300 character region into 9 cells
  (100×100 each). Cell names TL/TC/TR/ML/C/MR/BL/BC/BR.
- Anchor tuple `(cell, x_frac, y_frac)`: x_frac from cell LEFT edge,
  y_frac from cell TOP edge (reading-order convention: y=0 at top).
- PIL pixel mapping: `px = mx + 150`, `py = 150 - my` (flip y) —
  math-coord convention only. New work uses the PIL-native helper
  (see Standardized anchor convention below).

## Rendering primitives

- **Tapered stroke**: sample a quadratic Bézier from head→tail and lay
  down filled discs whose diameter linearly interpolates from
  `head_width` to `tail_width`. Also connect adjacent samples with a
  fat line to avoid gaps when the taper is steep. This yields
  calligraphic tapering for 撇 (thick TR head → thin BL tip), 提
  (thick BL head → thin TR tip), 捺, 点, 竖 (with hook).

- **fat_line**: filled polygon between two endpoints at a given width,
  used for straight segments (horizontal/vertical fills of 折-family
  compound strokes).

- **quad_bezier**: sample a quadratic Bezier at N points; the caller
  decides whether to render as a variable-width polyline (filled discs
  per vertex) or as fat_line segments.

- **stroke_variable_width**: given a polyline and per-vertex widths,
  fill discs at every vertex and fat_line between adjacent vertices.
  Used for hooks, 弯钩 bodies, and any stroke with a taper.

- **Curved sweep direction**: `curve>0` bows the arc toward the
  perpendicular of the chord. For 提, the bow points toward the
  upper-left (concave-down), matching the subtle upward-arcing feel
  of a rising stroke.

## Diagonal-stroke pairs

- 撇 (piě) and 提 (tí) are mirror partners along the anti-diagonal:
  撇 goes TR→BL, thick head at TR; 提 goes BL→TR, thick head at BL.
  Both taper to a needle tip. Same rasterizer, different endpoints.

- 捺 (nà) is a mirror of 撇 across the vertical: TL→BR, but 捺 has a
  broadened foot (顿笔) at the tail instead of a needle tip.

## 弯钩 (curved-vertical + hook)

- The bend ("弯") is **concentrated near the bottom third**, not spread
  along the full descent. If x_frac drifts left through the top half
  the stroke reads as 撇, not 弯钩.
- Head → belly x_frac should stay ~constant; the leftward swing happens
  in the last ~30% of the body.
- The hook ("钩") flick must be **short and sharp**: length ≈ 25–35% of
  body length, direction up-and-left, tapering to a fine tip.
- Width profile: taper up head→belly (顿笔 press mid-lower), then taper
  down through the hook to a near-zero tip.
- Rendered with a single quad-Bezier body + a short quad-Bezier hook,
  each stroked as a variable-width polyline (per-segment width from
  the width profile, filled discs at every vertex for smooth joins).

## Success-Bank protection

- During drawing, NEVER write to `success_bank/code/`. Attempts and
  general observations only. Success Bank is populated by the Curator
  after human PASS.

## Standardized anchor convention (locked-in as of batch 1 promotion)

The Curator has resolved the "PIL vs math-coord" ambiguity. **All
Success Bank entries and future drawer attempts use the PIL-native
convention**:

- Canvas 300x300, cell size 100x100, 3x3 米字格.
- Cell origin at top-left; x_frac grows RIGHT, y_frac grows DOWN.
- Helper: `success_bank/code/_anchor.py` exports `anchor_to_xy(anchor)`.
- Every promoted primitive imports the helper — no per-file copies.
- The math-coord note (`px = mx + 150`, `py = 150 - my`) refers to the
  legacy convention and is obsolete for new work.

## Compound-stroke joint convention (P/T/N/S classification)

- Every entry with more than one segment declares its internal joints:
  - **P (piercing / welded)**: shared anchor tuple, drawn with a small
    顿笔 disc at the joint vertex so it stays visible even when segment
    widths differ.
  - **T (tangent / tip-touches-body)**: one stroke's endpoint sits on
    another stroke's body but does not cross it.
  - **N (near / small gap)**: two endpoints intentionally sit within
    ~0.15 x_frac/y_frac of each other without touching.
  - **S (separate / no interaction)**: strokes that share the character
    but do not participate in any joint.
- For strokes with a hook (钩), the hook is treated as an internal
  segment of the same primitive, NOT a separate joint. Only pivots
  between different stroke types (横→竖, 竖→提, 撇→点, 撇→横) count
  as declared joints.

## Bezier control derivation for "curve passes through a target"

- When you want the body Bezier to visibly pass THROUGH a declared
  belly point (rather than merely bend toward it), use
  `ctrl = 2*belly - (p_start + p_end) / 2`. Verified in `xie_gou.py`
  (斜钩).
- CAUTION: this derivation places `ctrl` on the far side of `belly`
  from the chord midpoint. If `belly` is far from the chord midpoint
  the control point can end up outside the canvas, producing wild
  curves. When in doubt: place `belly` NEAR the chord midpoint (within
  ~15% of chord length) or use `belly` as the raw control point
  instead (`quad_bezier(start, belly, end)`).
- Phase-1 cross-cycle observation: attempts that use `belly` as raw
  Bezier control (弯钩, 竖弯, 横撇, 横钩) were crisp; attempts that
  derive control via `2*belly - midpoint` (斜钩, 横斜钩) are riskier.
  Prefer raw control unless the belly placement really demands a "pass
  through" guarantee.

## Sanity assertions before rendering

- After computing pixel coords from anchors, assert the direction
  invariants you expect from the stroke's description. Examples:
  - 竖钩 body: `p_hook.x == p_head.x` (straight vertical).
  - 横斜钩 descent: `p_hook.x > p_corner.x` (rightward slant).
  - Any 钩 flick: `p_tip.y < p_flick_start.y` (upward flick).
- This turns silent geometric bugs into loud assertion failures, at
  ~1 line of code per invariant.

## Phase-1-general rules for stroke families

### 1-画 primitives as radical wrappers

When a radical's canonical shape matches an existing stroke primitive,
promote it as a wrapper with fixed default anchors centered on the
米字格 (typically spanning ~70% of a full row/column so the radical
reads as prominent, not as a stroke fragment). Do NOT re-derive the
geometry.

Examples validated in Phase 1:
  丨 → `draw_shu`      (gun.py)
  亅 → `draw_shu_gou`  (jue.py)
  乛 → `draw_heng_gou` (heng_gou_cover.py)
  一 → `draw_heng`     (yi_one.py)
  丶 → `draw_dian`     (zhu.py)

### Extending N-piece 折-family strokes

To add a 90°-turn segment to an existing 折-family primitive, append
one anchor (`corner_{N+1}`), one `fat_line` segment (direction
alternates: horizontal → vertical → horizontal …), and one 顿笔 disc.
To add a hook, replace the terminal anchor with (hook_pt, tip) and
append the standard tapered quad-Bezier hook flick (borrowed from
`shu_gou.py`). Direction invariants for the new segment must be
asserted before rendering.

Verified extensions from Phase 1:
  横折  + hook          → 横折钩       (`heng_zhe_gou.py`)
  竖折折 + hook          → 竖折折钩    (`shu_zhe_zhe_gou.py`)
  横折折折 + hook        → 横折折折钩  (`heng_zhe_zhe_zhe_gou.py`)
  竖折   + zhe          → 竖折折      (`shu_zhe_zhe.py`)
  横折折 + zhe          → 横折折折    (`heng_zhe_zhe_zhe.py`)

### 折-family final-phase disambiguation

The final phase of a 折-family stroke must match the MMH decomposition:
does it end in **弯** (rounded Bezier sweep), **撇** (tapered
down-and-left diagonal), or **竖** (straight fat_line vertical)?
Do not extrapolate a staircase pattern by name alone — check the
canonical shape. Direction and shape of the final phase is what human
judges use to identify the stroke.

- 弯 finish: quad-Bezier with the arc concentrated in the last ~30%.
- 撇 tail: tapered variable-width, leftward-and-down direction.
- 竖 finish: fat_line vertical, no taper unless a hook follows.

## SELF_CHECK.visual_ok must be earned, not asserted (bootstrap batch)

Observed on 6/6 G4 FAILs in the bootstrap batch: every failing attempt
had `SELF_CHECK = {'visual_ok': True, 'overall_pass': True, ...}`.
Direction asserts and stroke-count checks numerically held, but the
rendered PNG did not read as the target radical. The self-check had
degenerated into a checkbox.

**Rule for future Drawer turns**: `visual_ok=True` requires a **text
observation** in the `notes` field naming AT LEAST two specific
features that agree between your PNG and the GT (e.g. "top 横 is
shorter than bottom 横", "hook flick points up-and-left, not
down-right"). If you can't name two, set `visual_ok=False` and use
your one revision. Direction asserts and stroke-count parity are
NECESSARY but NOT SUFFICIENT for `overall_pass`.
