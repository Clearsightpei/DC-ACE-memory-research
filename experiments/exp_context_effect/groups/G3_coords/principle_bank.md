# Principle Bank — G3 (coord-bank) — SPLIT AND MOVED

*This file was split on 2026-07-18 (v7 self-evolution) into three
focused files. Drawers should read those instead of this stub.*

## Where to find what

- **Meta-rules** (how to use the bank; TR1-TR7; retired TR8-TR9):
  → `principles_meta.md`
- **Stroke-family observations** (P1-P11; width profiles; math
  convention; hook directions):
  → `principles_stroke_family.md`
- **Stroke × context form lookup** (concrete angle/taper/bow numbers
  per stroke per position — NEW file):
  → `form_catalog.md`

## Why the split

`principle_bank.md` grew to 287 lines during B1 with an accumulation
of meta-cognitive TR-rules ("call primitives deliberately", "budget
your reach", "INLINE-FRESH TEST"). B2's pass rate (34%) fell BELOW
G1's no-memory control (38%) despite drawer compliance with those
rules. Root cause: rules told the drawer *when* to reach for the
bank, but the underlying issue was that the bank could not express
the *variation in stroke form* that different compositions require.

The split makes it obvious that the missing knowledge is
context-form (form_catalog.md, the new file) — not more meta-rules.
See `evolution.md` @ position 150 for the full rationale.

## Change log

- **2026-07-31** (position 500, B10 curator) — added principle
  P-DEV1 (below) codifying the v13 BANK_DEVIATION channel; no split.
- **2026-07-18** (position 150) — split into three files; retired
  TR8 and TR9 (documented in `principles_meta.md`); created
  `form_catalog.md` for stroke × context lookup.
- **2026-07-16** (Phase-2 restart) — reset to TR1-TR7 + P1-P10.
- **Various B1 additions** — TR8, TR9, P11 (reverted / migrated).

## Cross-cutting principles (added post-split)

### P-DEV1 (B10, 2026-07-31) — when to deviate from a bank primitive

*Evidence*: 16 BANK_DEVIATIONs in B10 across 50 items. 3 became PASS
(皃, 畀, 的). 13 became FAIL or C. The 3 that PASSed shared a common
pattern; the FAILs shared a different one. Rule:

**Deviate when** (all three):
1. The bank primitive's absolute coords can't shrink into your slot
   without visible overlap of a sibling component (typical case:
   full-canvas primitive being asked to occupy a 40% left-side slot).
2. You can name the fresh_component as a KNOWN SHAPE VARIANT
   (compressed 白, wide-spread 儿, top-half compact 白) — meaning
   there is an existing shape family the fresh render belongs to.
3. Your fresh render uses thin (5-9px) uniform ink, not calligraphic
   embellishment. Deviations for stylistic weight lose the panel.

**Do NOT deviate when**:
- The bank primitive fits with a modest (ox, oy, scale) shift → use it.
- Your fresh_component is a NOVEL SHAPE with no bank sibling
  (聿, 巛-curly-scoop, 乞, 戈, 己-open-top). Fresh renders of
  novel shapes fail 4-of-5 times in B10.
- You want to "improve" the bank primitive aesthetically. That's
  variant proliferation without cause — v13 forbids.

**When you deviate, write the BANK_DEVIATION comment block** naming
the skipped file, the reason, and the fresh_component's one-line name.
If your attempt PASSes, the curator will promote the fresh_component
as `<orig>_<qualifier>.py` (v13 variant naming).

### P-DEV2 (B10) — retrieval-leak fix works for stack/side-by-side,
### fails for 3-part proportion compositions

*Evidence*: 5 B9 "all-parts-bank-mastered-but-drawer-inlined" leak
candidates got explicit-bank-call retries in B10. 2 PASSed (时 = 日+寸
side-by-side; 串 = 口+口 stack). 3 FAILed (疖 = 疒+卩 narrow-column;
亨 = 亠+口+了 3-stack; 声 = 士+尸 envelope). Rule:

**When the current char is a 2-part side-by-side OR a 2-part stack of
bank-mastered pieces**, cite both pieces explicitly and copy the L-R
scale table from drawer_memory.md.

**When the current char is a 3+-part stack OR a narrow-column
envelope** — bank-call alone isn't sufficient. Also cite the y-band
per piece (e.g. "亠 in y=40-90, 口 in y=100-170, 了 in y=180-280") or
the column width per piece. If you can't derive those from GT, expect
proportion drift.


### P-DEV3 (B11, 2026-08-03) — variant-promotion signal (which fresh_components deserve bank promotion)

*Evidence*: B10+B11 combined = 34 BANK_DEVIATIONs across 100 items;
7 became PASS-and-promoted variants (20.6%); 6 became PASS-but-NOT-
promoted (17.6%); the rest were FAIL or C. The promoted vs
not-promoted split obeys a clear signal:

**Promote (variant deserves a bank entry) when ALL three hold**:
1. The fresh_component belongs to an OBVIOUS shape family — you can
   name 3+ near-cousin compounds that would plausibly reuse it in
   the next 200 items (e.g. `zhu_master_for_LR_right` → 住/注/柱/驻/蛀;
   `you_frame_up` → 由/曲/甲-cousin; `tu_cun_stacked_for_LR_right` →
   待/恃/詩/峙).
2. The recipe is PARAMETERIZABLE — you can add `mx_off`, `scale`, or
   `ox` args that let callers slot into varied positions without
   editing internals. (Bare hardcoded pixel recipes are one-offs, not
   variants.)
3. The recipe is DISTINCT from the original bank primitive — either
   different placement rules (canvas-centered → shifted), different
   shape topology (甲 shu-below → 由 shu-above), or different
   composition mode (turtle → PIL inline for compatibility).

**Do NOT promote** when the fresh_component is:
- A one-off inline of a specific character's whole-body composition
  (e.g. `guo_mu_under_tian` for 果, `ju_char` for 具, `kong_char` for
  空, `biao_char` for 表, `hua_speak` for 话). These lack a family;
  future compounds needing the same character will re-derive.
- A TERMINAL-errata sub-radical inline (讠 in 话/说). Cannot promote
  a permanently-frozen shape as a bank primitive.
- A bank primitive lightly modified for one-off scale — that's already
  covered by (ox, oy, scale) call-site adjustment.

**Why this matters**: uncontrolled variant proliferation bloats the
bank and defeats the "identity-alias is highest-yield lever" pattern
that drives G3's B3-onward pass rate. P-DEV3 keeps the bank sharp
by preserving the "each entry has 3+ reuse cases" invariant. Combined
with v13 immutability (originals never edited) and P-DEV1 (deviate
only for real mismatch), the bank grows monotonically but not
combinatorially.

### P-DEV4 (B12, 2026-08-04) — X-crossing compression pathway (A-verdict exception)

*Evidence*: One data point — but the ONLY A verdict across 600 items
/ 12 batches / 4 format unlocks. `p3_char_0434_畎` (田 + 犬) achieved
A while the same X-crossing family (人/入/大/矢/失) is
TERMINAL_FROZEN at C after 4 retries each under progressive unlocks.

**The pattern**:
- 犬 in 畎 occupies right ~55% of canvas (x ≈ 150–275). Cross-apex
  at (215, 143). Thin ink (~4-5px).
- Standalone 大 in `p3_char_0197_矢` / `p3_char_0216_失` occupied
  full canvas (~x 40–260). Cross-apex near canvas center. Thicker ink.

**Hypothesis**: the calligraphic-joint-modulation gap that fails full-
canvas X-crossing at the panel does NOT bind when the crossing is
compressed into a sub-slot. Small-pixel-area X-crossings apparently
sit under the panel's discrimination threshold, so thin-ink line
segments read as A rather than as "recognizable-but-uncalligraphic".

**When this pathway MAY unlock A** (all four must hold):
1. Target character is L-R or U-D composition; X-crossing radical
   occupies ≤ ~55% of one axis.
2. Cross-apex explicitly computed as a shared pixel — pie and na
   share exactly one coord (do NOT let them cross approximately).
3. Ink weight ≤ 5px uniform; two-cubic pie (head + body) for the
   continuous curve; thin tapered na.
4. The composition sibling (left/top) is a stable envelope/frame
   (田, 口, 目, 日, 山, 木) — anchors the X-crossing visually.

**When this pathway does NOT apply**:
- Standalone characters (大, 人, 入, 天, 夫, 太, 犬-alone). Full-canvas
  X-crossing stays TERMINAL_FROZEN. P-DEV4 does not unfreeze them.
- Multi-X-crossing compositions (乔, 会, 从 stack) — untested; treat
  as format-ceiling until evidence.

**Actionable implications for B13+**:
- `quan_dog_for_LR_right.py` is available; try for 猷 (酉 + 犬).
- For L-R compounds whose right radical is 大/太/夫/矢/失, attempt
  a P-DEV4-style compressed inline (thin ink + explicit shared cross)
  before defaulting to bank primitives. But do NOT promote as variant
  until a second A verdict of the same class arrives — one data point
  is not a family.

**What this DOES NOT change**:
- The paper's central finding (G3 line-primitive can't cross the
  calligraphic-joint threshold at full-canvas scale) still holds —
  P-DEV4 is a NARROW exception, not a refutation. Zero-A across
  standalone X-crossing family remains the ceiling. G4's 米字格
  A-rate advantage on non-P-DEV4-class items is unaffected.
- Do NOT retroactively un-freeze 矢/失/大.
- Update the "zero A" language in curator communications to "one A
  in 600 items, structurally-contained pathway; format ceiling
  otherwise unchanged".

### P-DEV5 (B13, 2026-08-05) — variant reuse targets are SPECULATIVE until verified

*Evidence*: B12 curator promoted `quan_tian_for_LR_left` from the 畎 A
verdict and named 畈, 畋 as "reuse targets" (both had B11 fails).
Both were queued for B13 R1 with the new variant. **Both FAILED.**
Diagnosis: the variant primitive covered the LEFT slot correctly (the
田 rendered cleanly in both attempts, and independently PASSed as the
田 slot inside 畛's C attempt). The failure was entirely in the RIGHT
radical — 反 (畈) collapsed to a ㄋ-curl and 攵 (畋) became a floating
dash + tiny 人. Neither 反 nor 攵 has a bank primitive, and both
demand X-crossing-like weld geometry with no matched recipe.

**Rule**: when promoting a variant that covers ONE SLOT of an L-R (or
U-D) composition, the "reuse targets" listed in the INDEX row are
SPECULATIVE unless BOTH conditions hold:

1. **The sibling slot has a bank primitive or a documented recipe.**
   Listing 畈 as a reuse target for `quan_tian_for_LR_left` was valid
   for the 田 side but ignored that 反 is a novel unmastered right
   radical. Similarly for 畋 / 攵.
2. **The sibling recipe has been verified in a prior PASS with the
   same composition mode.** Speculation is not evidence. If no prior
   PASS used the sibling recipe in this slot-position, mark the target
   as "candidate — sibling unverified" in the INDEX, not "reusable for
   X, Y, Z" as if it were confirmed.

**Actionable implication**: when queueing a retry that relies on a
newly-promoted variant, list the SIBLING radical's status ("sibling 反
UNMASTERED — R1 may still fail on that side") in the retry_log reason,
and don't count the retry as a validation of the variant if the sibling
side is what fails.

**What P-DEV5 does NOT overturn**: `quan_tian_for_LR_left` itself is
still valid (B13 evidence: it worked cleanly in the 畎 A original AND
in 畛's C attempt where the box side was fine). The lesson is about
CURATOR PROJECTION (over-broad reuse claims), not about the variant
primitive.

**Precedent for language**: replace INDEX-row phrasings like
"template for 略/畔/畝/畦/畯/畈/畋" with "L-R-left box slot; sibling
radical unverified — reuse contingent on sibling recipe". Do NOT list
sibling-dependent chars as if the variant alone unlocks them.
