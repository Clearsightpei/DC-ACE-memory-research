# G4 drawer_memory (v8, position 350)

*Free-form persistent memory added at v8 unlock. Same shape as G2's
memory. Curator writes here; drawer reads it via `memory_index.md`.
Read this BEFORE the structured bank — for many items it will already
name the primitive to call.*

*The grid bank (`success_bank/code/`) + principles + form_catalog +
joint_atlas remain available as REFERENCE. Nothing in them is mandatory
under v8. When this file and the structured bank disagree, follow this
file.*

---

## Fast lookup — call these primitives directly

The single highest-value action per B6 evidence: **when a character
contains one of these components as a sub-part, IMPORT and CALL the
primitive**. Do not reinvent. B6 had ~15 items where reuse would have
saved the attempt; ~8 of them FAILed by drawing fresh instead.

### Chronic canonical primitives (mandatory imports)

If the target contains 丿, 刀, 冂, 弓, 马 as a component: **import the
chronic module**. B6 showed drawers cite these in comments but never
import them; that is treated as a mechanism failure. From B7 onward,
comment-only mention is not sufficient.

```python
from chronic.pie_radical import draw_pie_radical    # 丿
from chronic.dao_char     import draw_dao_char       # 刀 (and 刅, 刀-containing chars)
from chronic.jiong_frame  import draw_jiong_frame    # 冂 (and 用, 内, 円, 内, 门-containing chars)
from chronic.gong_bow     import draw_gong_bow       # 弓 (and 引, 弗, 弘)
from chronic.ma_horse     import draw_ma_horse       # 马 (and 乌, 鸟)
```

If the character contains the component but at a different position/
scale, still call the chronic primitive first and shift its output via
the `offset_x`/`offset_y`/`scale` parameters where available, rather
than redrawing.

### High-value component primitives

For left-radical or bottom-radical compositions, these bank files are
worth importing:

```python
from ren_side  import draw_ren_side    # 亻 (仔/付/打/化/他/仝/仕 all reused this in B6)
from shou_side import draw_shou_side   # 扌
from xin_side  import draw_xin_side    # 忄
from si_silk   import draw_si_silk     # 纟
from chi_step  import draw_chi_step    # 彳
from you_again import draw_you_again   # 又 (needed for 反 又 对 权 etc)
from bi        import draw_bi          # 匕 (mirror for 比; call TWICE for 比)
from li        import draw_li          # 力 (needed for 办 加 男)
from bao_char  import draw_bao_char    # 勹 (needed for 勻 匀 匆)
from er_legs   import draw_er_legs     # 儿 (needed for 元 兄 光)
from xin       import draw_xin         # 心 (needed for 必)
from tu        import draw_tu          # 土 (needed for 去 圭 坐)
from si_private import draw_si_private # 厶 (needed for 去 台 参)
from shan      import draw_shan        # 山 (call TWICE stacked for 出)
```

### Never-tune-anchors rule for reused primitives

When you import a primitive, call it with its DEFAULT signature. If
the primitive doesn't fit exactly, prefer inlining fresh (per shared
rules "supplementary aid") — do NOT try to override 3+ anchors of a
mastered primitive. That path caused the p2_082_子 chronic saturation
in B4.

---

## Compositional playbook — how to think about 3+-part characters

B6 diagnosis: all 24 main FAILs are multi-part characters where the
sub-parts don't visually cohere. All 26 main PASSes are either
simple 3-4 stroke chars or 亻/扌/宀-prefixed reuses. **The failure
mode is composition, not stroke rendering.**

**Step 1**: split the target into named sub-radicals BEFORE looking at
anchors. Write the split as a comment: `# 反 = 厂 + 又`.

**Step 2**: for each sub-radical, look for a mastered bank primitive
in the shortlist above OR in `success_bank/INDEX.md`. If one exists,
IMPORT it.

**Step 3**: place the sub-radicals in a grid layout:
- **Left-right** (亻+X, 扌+X): left in x∈[0.05, 0.40], right in x∈[0.45,
  0.95]. Both fill y∈[0.10, 0.90].
- **Top-bottom** (宀+X, 一+X, 亠+X): top in y∈[0.05, 0.35], bottom in
  y∈[0.35, 0.95].
- **Enclosing** (囗+X, 门+X, 冂+X): frame fills [0.10, 0.90] both axes;
  inner sub-radical fills middle 60% both axes.
- **Stacked repeated** (出=山+山, 比=匕+匕): use SAME primitive twice
  with mirrored or offset anchors.

**Step 4**: enforce compositional coherence — every sub-radical must
share at least one anchor pixel with an adjacent sub-radical, or leave
a visible ~15-25 px gap. Never touch AND never disconnected.

---

## B6 systematic failure notes

**Enclosing frames (冂/门/囗-containing chars)**: 用, 们, 内 all failed
by not calling `chronic/jiong_frame.py`. If the target contains an
enclosing frame, the FIRST line of code should be
`from chronic.jiong_frame import draw_jiong_frame`.

**Left 阝 radical is missing from the bank.** 队 FAILed because there
is no primitive for 阝-left. Right 阝 exists (`fu_right.py`) but is
NOT a mirror. Until a `fu_left.py` promotion arrives, decompose 阝-left
as: short 撇 top + 竖 left + 横折 bend + tail — 3 strokes in x∈[0.05,
0.35] column.

**Stroke-count omissions**: 水 keeps rendering as 3 strokes (missing
right 捺); 礻 keeps rendering as 3 strokes (missing top dot). Add an
explicit `assert len(strokes) == expected` before rendering, and add a
retry pass if the count is off.

**Symmetry pairs (比, 丱, 从, 双)**: these characters are TWO copies
of the same sub-radical. Compute anchors ONCE, then mirror x_frac via
`(cell, 1 - x_frac, y_frac)` for the mirrored copy. Do NOT hand-derive
two independent copies — they will not match.

**顶部单点 items (礻 主 亠-family)**: the top dot is often the first
thing dropped by the drawer. Render the dot LAST as a defensive step
so it can't be overwritten by later strokes.

**Chronic-mechanism import discipline**: when the target maps to a
chronic primitive, the drawer's `generated.py` MUST include the
`from chronic.<x> import draw_<x>` line and MUST call it. A comment
citing the primitive is NOT sufficient (B6 evidence: 18 comment
mentions, 0 imports across all history since position 300).

---

## What NOT to do (drawer traps from B1–B5)

- Do not chain multiple beziers to fake a compound stroke. Use
  `stroke_variable_width` with a single polyline. (see 飞 chronic fails)
- Do not draw two separate strokes for what MMH lists as one compound.
  (e.g. 及, 廷, 建 need `heng_zhe_zhe_zhe.py` NOT 3 pieces.)
- Do not tune the anchors of a chronic primitive. Call it as-is. If
  it looks wrong to you, that means your visual read of the GT differs
  from the panel's — the panel wins.
- Do not skip `errata.md` on repeat items. Every retry is against a
  drawer's own prior failure, and the errata fix is the panel's summary
  of what needs to change.
- Do not soft-interpret an errata fix. "Widen to anti-diagonal ('TR',
  0.85, 0.15) → ('BL', 0.15, 0.85)" means those exact tuples, not
  "something more diagonal than before."

---

## Interpretation window (from v8 rules)

Everything in the bank + principles + form_catalog + joint_atlas is
REFERENCE ONLY. If your visual read of the GT disagrees with them,
follow your read. But: when an item has failed 2+ times and the errata
gives a literal fix, the interpretation window closes — follow the
errata verbatim. The 4-batch chronic-cluster saga (see `evolution.md`
position 300) is the negative evidence.

---

## v9 addendum — VISUAL DIFF STEP 0 (from B7r evidence)

Under the v9 retry prompt, drawers open the prior failed PNG side-by-
side with the GT before touching code and write a `VISUAL DIFF` block
at the top of `generated.py` naming concrete gaps ("prior right half
collapsed to 乙 curl because s3 and s4 heads coincide at MR(0.55,0.10)").
Both B7r PASSes (比, 文) did this. The 10 B7r FAILs also did it, so
visual-diff is necessary-not-sufficient — but it is CHEAP and it
converts "chronic invisible topology bugs" into named diagnoses the
next retry can literally fix. **On any retry, do Step 0 in prose
before writing anchor tuples.**

Concrete lessons from the 2 v9 PASSes:
- **比 (retry_1 v9)**: prior halves were centered at x≈55 and x≈250 —
  too far apart, off-center. GT halves live at x∈[55,145] and
  x∈[145,265]. Fix was to trust MMH anchors verbatim (they are more
  centered than any hand-tuned attempt). When a symmetry-pair is
  failing, MMH-verbatim is stronger than clever mirror math.
- **文 (retry_2 v9)**: prior X-cross had both pie head and na head at
  the same point on the heng — reads as 人 (inverted V), not X. Fix
  was `CROSS_ANCHOR = ('BC', 0.385, 0.225)` welded at pie-MID and
  na-MID (not at their heads). The X-cross weld point is BELOW the
  heng, not on it.

---

## B7 failure pattern (post-batch — 25 FAILs, 4 clusters)

**Cluster 1 — frame-plus-interior (5 items)**: 冊, 册, 冋, 冎, 冯.
All contain 冂 or 马 as a dominant part. `chronic/jiong_frame.py` /
`chronic/ma_horse.py` were NEVER imported (0/6 candidates checked; 4
mentioned in comments then reinvented). The chronic-mechanism import
failure from B6 REPEATS in B7. `drawer_memory.md` already contains
the mandatory-import snippets and it is still not being followed.
Next batch: consider stronger enforcement (e.g., dispatcher pre-check
that greps generated.py for `from chronic.` when the target contains
a chronic component, and stalls if missing).

**Cluster 2 — 一 + horizontal-fold-stack (4 items)**: 亘, 亙, 会,
that-family. All have a top-and-bottom heng bracketing a compressed
middle. FAIL mode: the two brackets don't align vertically and the
middle collapses. Fix pattern: enforce `s1.head.y == s_last.head.y`
alignment; middle content in y∈[0.25, 0.75] band only.

**Cluster 3 — 亻/讠-prefix + non-bank right (4 items)**: 仡, 仫, 记.
亻 side is fine (imports ren_side); right sub-component is not in the
bank and comes out fragmented. No fix beyond promoting the missing
sub-components (乞, 么, 己-full).

**Cluster 4 — X-cross topology (5+ items)**: 癶, 处, 処, 乩, 那.
Same topology bug that v9 rerun caught for 文: apex pixel not shared,
so 撇+捺 reads as 人 not X. **Standard fix**: define a `CROSS_ANCHOR
= (cell, x_frac, y_frac)` tuple and pass it as MID (not head) to
both pie and na. This is now a pattern worth spelling out here.

### Ready-to-copy X-cross snippet

```python
# X-cross weld pattern (from B7r 文 success)
CROSS = ('BC', 0.5, 0.25)  # adjust per item
# Route both pie and na through CROSS as their MID control:
draw_pie(d, head=('TC', 0.45, 0.10), tail=('BL', 0.20, 0.90),
         mid=CROSS)  # or use quad_bezier with CROSS as ctrl
draw_na(d, head=('C', 0.35, 0.15), tail=('BR', 0.30, 0.85),
        mid=CROSS)
# Verify shared pixel: anchor_to_xy(CROSS) same for both calls.
```

---

## Bank-utilization guidance (post-B7 prune)

Post-B7 prune round 2 removed ~10 additional never-imported thin
wrappers (see `evolution.md`). Files that survive represent primitives
with either (a) proven reuse, or (b) high-value slots the v8 mechanism
is trying to activate. Do NOT re-derive functionality that a surviving
bank file provides. When in doubt, prefer IMPORT over INLINE, even
if MMH anchors seem to disagree — the panel accepts bank-canonical
shapes with wide anchor tolerance.


---

## B8 addendum (position 450) — bank-import discipline + 亻+X pattern

**B8 outcome**: 20/50 mains (40%); 0/7 retries. Bank import rate
cratered: 40/50 mains inlined everything via `_anchor + fat_line`.
The 30 FAILs are almost all 亻+X or radical-radical compositions
where inlining the right-half loses coherence.

### If your target contains 亻 (as left radical) — this is 25/50 of B8

- **DO**: `from ren_side import draw_ren_side` and use its default
  anchors. Do not hand-place the 亻 strokes; the primitive already
  handles the pie+shu joint. B8 evidence: 亻 chars with imported
  ren_side PASS more than those with hand-derived 亻.
- **DO**: for the right sub-radical, LOOK UP whether it exists in
  `success_bank/INDEX.md` under any of its forms. B8 lost items
  where kou/nv/zi/mian/ren/bi/li could have handled the right half
  but drawer inlined instead.
- **DO NOT** override ren_side default anchors because they "sit in
  TC/C/BC" and you want TL/ML/BL — that was p3_char_0252_伊's
  documented FAIL note. If you need a different column, inline the
  2 strokes yourself; do not partially-override the primitive.

### If your target contains 冂 or 用/内/门/円 shape

**MANDATORY**: `from chronic.jiong_frame import draw_jiong_frame`.
Failure to import is a mechanism failure regardless of visual result.
B8 evidence: 3 chronic-component targets (再, 同, 西), all 3 mentioned
chronic in comments, 0 imported. Comment-only mention has been
insufficient for 3 batches (B6/B7/B8) — the import statement
is what enforces adoption.

### The 7 canonical primitives that DO NOT exist

Position 400 queued canonical primitives for 长, 夂, 夊, 水, 礻, 无,
气 but **the files were never written**. If your target contains any
of these radicals as a sub-part, DO NOT try to `from chronic.chang_long
import draw_chang_long` — the file is not there. Fall back to MMH-
verbatim anchors + inline base primitives (pie, shu, na, heng). These
7 items are marked TERMINAL_FROZEN in the retry log.

### Compositional-coherence check — new mandatory step for 6-stroke
### 2-radical chars

Before rendering, verify:
1. Left radical occupies x∈[0.05, 0.42] (2-3 strokes).
2. Right radical occupies x∈[0.48, 0.95] (3-4 strokes).
3. Combined stroke count matches MMH `expected_strokes`.
4. Every stroke is drawn by a NAMED primitive (either imported or
   inline). If more than 4 draw calls are inline `fat_line`, that
   is a signal to look for a bank primitive.

B8 FAIL pattern: 14 of 30 mains had ZERO bank draw calls. The
render-from-scratch approach hits panel-visible coherence failures
on ~60% of 2-radical chars.

---

## B9 A-recipe (position 500) — how to produce reference-quality (A) renders

B9 landmark: 11 A verdicts (10 mains + 1 retry) in a single batch.
G4 is the only group producing A verdicts at scale. Common pattern
extracted from all 11 A-verdict `generated.py` files:

### The 5-point A-recipe

1. **Explicit decomposition comment at the top** naming every
   sub-radical + total stroke count:
   ```python
   """佉 (qū) — 7 strokes.
   Decomposition: 佉 = 亻 (left) + 去 (right); 去 = 土 (top) + 厶 (bottom).
   """
   ```

2. **MMH-verbatim anchors** — pass every dispatcher-injected anchor
   tuple UNCHANGED into your stroke calls. Do not "tune" them, do
   not "clean them up", do not use clever mirror-math on symmetric
   halves. When your visual read of the GT disagrees with MMH, trust
   MMH. B9 evidence: every A used MMH literally.

3. **SELF_CHECK block** declaring stroke count and joint class:
   ```python
   SELF_CHECK = {
       'visual_ok': True,
       'stroke_count_ok': True,
       'endpoint_mismatches': [],
       'joint_class_mismatches': [],
       'overall_pass': True,
       'notes': '7 strokes MMH-verbatim; all N-joints preserved as gaps.',
   }
   ```

4. **Base primitives (`_anchor + fat_line` + `pie/shu/heng/na/dian/pie_zhe`)
   over compound bank primitives**. When MMH placement disagrees with
   a compound primitive's defaults (ren_side, mian, etc.), inline the
   sub-radical with MMH anchors + base primitives rather than partially
   override the compound primitive. B8 evidence (p3_char_0252_伊):
   partial override of a compound primitive is the #1 way to lose a
   near-A. B9 evidence: 4 of 10 A items explicitly rejected ren_side
   because MMH placed 亻 far-left of ren_side's TC/C defaults, and
   inlined with pie+shu MMH anchors.

5. **N-joint discipline**: declare every joint's class in the header
   comment or SELF_CHECK. **Leave the natural gap** (~15-25 px) for
   N-joints. Novices try to weld everything; A-drawers respect the gap.

### Compare to PASS vs FAIL patterns (B9)

- **PASS items (10 mains)**: follow points 1-3 but sometimes skip
  point 4 (use a compound primitive that happens to fit MMH well
  enough).
- **FAIL items (30 mains)**: most miss BOTH point 1 (no decomposition
  comment) AND point 4 (over-invest in compound primitives whose
  defaults don't match MMH placement, causing coherence loss).

### The counterintuitive finding

The A-recipe is NOT "import more bank primitives". It is "trust MMH
literally + structure the code around the decomposition". The bank
mostly serves as a low-level (single-stroke) toolbox; compound
primitives help when MMH placement matches their defaults, hurt when
it doesn't. This inverts the v6/v7 mandate-more-imports philosophy.

---

## v13 BANK_DEVIATION channel — no usage in B9

The v13 prompt added a `BANK_DEVIATION` block for drawers to signal
"I deviated from bank on purpose; here is what I changed and why".
B9 usage: **0/66 attempts**. Either drawers didn't read the v13
addendum, or every deviation was implicit under point 2 above
("trust MMH over memory"). No worked example exists yet.

If you deviate from a bank primitive (e.g., override its default
anchors, or inline fresh instead of importing when a mastered
primitive exists), add a BANK_DEVIATION block at the top of your
`generated.py`:

```python
# BANK_DEVIATION:
#   ren_side.py default anchors sit at (TC, 0.5) + (C, 0.5); MMH places
#   亻 at (TL, 0.8) + (ML, 0.6). Inlining pie+shu with MMH anchors
#   instead of importing ren_side. Reason: partial override of compound
#   primitive caused p3_char_0252_伊 FAIL in B8.
```

Curator promotes successful deviations as `<name>_A.py`, `<name>_B.py`,
or `chronic/<name>_v2.py` variants. Without your signal, the curator
cannot see the deviation from anchor-diff alone.

---

## B9 chronic-mandatory mechanism — falsified (3 batches)

Chronic-import rate: B7 = 0/6, B8 = 0/3, B9 = 0/5. Three negative
batches on the same mechanism. The "MANDATORY `from chronic.<x>
import draw_<x>`" text in the top of this file has been ignored
by every drawer since position 300 (except for comment-only
mentions).

**Effective decision for B10+**: treat the chronic-mandatory section
as REFERENCE (not mandatory). If your target contains 丿/刀/冂/弓/马
and you can import the chronic primitive with anchors that match MMH,
do so — it will save you code. If MMH placement clashes with the
chronic default, inline via base primitives per the A-recipe point 4.

---

## B10 addendum (position 550) — BANK_DEVIATION channel evidence + refined A-recipe

**B10 outcome**: 19/50 mains (38%; 10 A + 9 PASS), 6/16 retries (38%;
3 A + 3 PASS). 13 A verdicts total (10 mains + 3 retries) — the
strongest calligraphic-quality signal to date. Cumulative through B10:
50% success, 20 A's before B10 (24 with B10 adjustments).

### BANK_DEVIATION channel — first live batch, first evidence

The v13 channel produced its first data. 13 attempts included a
`BANK_DEVIATION` block; 8 of those 13 were on PASS/A attempts (4 A + 4
PASS). **The channel is producing A-quality when drawer judgment about
primitive mismatch is correct.** All 8 successful deviations shared
one meta-pattern:

> Bank primitives (ren_side, ri, cao_grass_radical, wei_enclose,
> shou_side, bao_char, zhi_stop, er_legs) render their component at
> STANDALONE scale — filling the canvas. When that component is
> embedded in a compound character, MMH shifts it to a specific slot
> (far-left column, top-band, BC-compression, right-half compression,
> inset-frame). Partial anchor override of the compound primitive is
> the p3_char_0252_伊 FAIL pattern (B8, documented). Inlining via base
> primitives with MMH-verbatim anchors preserves the compositional
> proportion.

Concrete B10 A/PASS deviations:

| item | verdict | skipped primitive | slot pattern |
|------|---------|-------------------|--------------|
| 佟 (A) | A | ren_side | 亻 at TL/ML/BL far-left column |
| 者 (A) | A | ri | 日 compressed to BC cell (bottom-center) |
| 花 (A) | A | cao_grass_radical | 艹 in top band (y ~110), leave room for 化 |
| 佔 (A) | A | ren_side + bu + kou | multi-slot compression |
| 皃 (A) | A | er_legs | 儿 under narrow 白, compressed |
| 步 (PASS) | PASS | zhi_stop | 止 around C/TR, abuts bottom 少 |
| 别 (PASS) | PASS | kou + li + dao_side | left-block + right 刂 slot |
| 的 (PASS) | PASS | bao/bao_char | 勺 right-half compressed |
| 国 (PASS) | PASS | wei_enclose + wang | inset frame with 玉 interior |
| 把 (PASS retry) | PASS | shou_side | 扌 far-left ML column |

**No new variant primitives promoted this batch.** The curator's
rationale: creating `cao_grass_top.py` / `ri_compressed.py` /
`wei_enclose_compact.py` etc. would REINTRODUCE the very compound-
primitive-standalone-scale problem the deviations are avoiding. The
A-recipe point 4 already codifies "inline base primitives with MMH
anchors" — no variant is needed. Defer promotion until a specific
fresh_component fires on 2+ PASSing attempts across future batches.

### When to use BANK_DEVIATION (drawer decision tree)

1. Compound primitive default anchors match MMH within ±0.15 in
   x_frac AND y_frac for every stroke? → **USE the bank primitive**.
2. Compound primitive would need 3+ anchor overrides? → **SKIP,
   inline via base primitives, write BANK_DEVIATION block**.
3. Bank primitive is chronic (`chronic/*.py`) AND MMH matches within
   the tolerance? → **USE the chronic primitive**.
4. Component is being embedded in a compound with slot compression?
   → **SKIP the compound primitive, inline** (per point 2 above).
5. Component appears standalone or at full-canvas scale? → **USE the
   bank primitive as-is** (that is what it was written for).

### BANK_DEVIATION on FAIL items — what to avoid

Four B10 deviations landed on FAIL/C outcomes with sound reasoning
but insufficient execution:

- **张 (C)**: skipped `chronic/gong_bow.py` because 弓 is left-column
  compressed. The reasoning was CORRECT (chronic gong_bow is
  hardcoded full-canvas 300×300; can't share space with 长 on the
  right). But the fresh inline 弓 had joint misalignment. If future
  attempts skip chronic/gong_bow with the same left-column reasoning
  AND pass, promote `chronic/gong_bow_v2.py` (left-column variant).
- **改 (FAIL)**: skipped `yi_already.py` because target's left is 己
  (not 已) and left-third compressed. Sound reasoning, but the 己
  inline confused 己 vs 已 topology. Errata note added.
- **乩 (retry_3 FAIL)**: skipped bu + kou + yi_hook. Composition
  scaling remained off — X-cross bug persists.
- **那 (retry_3 FAIL)**: skipped fu_right + heng_pie_wan_gou for a
  single-bezier. Cleaner-looking but 阝-right's ear shape lost.

### Refined B10 A-recipe (extends B9 A-recipe)

The 5-point B9 recipe (explicit decomposition + MMH-verbatim anchors +
SELF_CHECK + base primitives + N-joint discipline) continues to hold.
B10 adds:

**6. BANK_DEVIATION signal for compound-slot embedding**. When you
   inline a component that has a compound bank primitive because MMH
   places it in a non-standalone slot, add the `BANK_DEVIATION`
   comment block. This gives the curator evidence to eventually
   promote variants when a pattern proves out. Format below.

**7. Chronic-full-canvas awareness**. `chronic/*.py` primitives
   (pie_radical, dao_char, jiong_frame, gong_bow, ma_horse) all bake
   full-canvas 300×300 anchors. If your target puts 丿/刀/冂/弓/马 in
   less than the full canvas (e.g. left column of a compound char),
   the chronic primitive won't fit — skip and inline with a
   BANK_DEVIATION block. B10 evidence: 张 (C, sound skip but
   execution bug).

**8. X-cross topology remains a chronic weakness**. B10 X-cross
   FAILs: 癶 (retry_3), 処 (retry_3), 乩 (retry_3), 那 (retry_3),
   亥 (retry_2), 亦 (retry_2). The B7r 文 fix (CROSS_ANCHOR shared
   between pie-mid and na-mid) generalizes only when the X-cross is
   isolated. When X-cross sits inside a compound char (那 = 冄 + 阝-r
   with 冄 having internal cross), CROSS_ANCHOR alone doesn't save
   it. No mechanism proposed yet. Consider these items
   TERMINAL_FROZEN candidates after retry_3.

### BANK_DEVIATION block format (recap)

```python
# BANK_DEVIATION
# skipped: <bank_file.py>  (or: "replaced: <bank_file.py> with local render")
# reason: <one-sentence visual/compositional reason — name the slot pattern>
# fresh_component: <name the fresh sub-element, e.g. "cao_grass_top_for_花">
```

Multiple skips OK: list them all under `skipped:`. Keep `reason` to
one-two sentences naming the SLOT (top-band, far-left column,
BC-compression, right-half, inset-frame, etc.). The
`fresh_component` name is what the curator uses to decide variant
promotion — pick a name that describes the SLOT + CONTEXT, not the
specific char.

---

## Retry queue for B11 (curator picks post-B10)

Selection criteria: (a) failed once with a diagnosable fix, (b) not
already at retry_3 saturation, (c) X-cross cluster gets ONE more
chance under a new tactic. B11 queue (13 items):

- **X-cross retry_3+ candidates (SATURATION check)**: 癶, 処, 乩, 那
  — all at retry_3 FAIL. If B11 fails, mark TERMINAL_FROZEN and
  promote `chronic/x_cross_composite.py`.
- **New retries at retry_1**: 佚, 社, 佛, 即, 改, 到, 事, 所, 学.
- **Escalating**: 亥 (→retry_3), 亦 (→retry_3), 更 (→retry_2),
  龹 (→retry_2).
