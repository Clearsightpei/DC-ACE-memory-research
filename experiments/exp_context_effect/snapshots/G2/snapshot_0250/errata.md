# G2 错题集 (Wrong-Answer Notebook)

Failed items awaiting retry. Format: item_id · target · batch of first failure ·
diagnosis (curator, from vision — no human text feedback exists).

**Batch B1 update** (positions 51-100, radicals 019-068): 1 GRADUATED
(厂 — retry PASSed, removed from notebook). 2 retry FAILs incremented
(匕 retry_n→2, 刀 retry_n→2). 15 NEW fails added from main B1 curriculum
(阝 力 人 入 厶 巛 飞 干 弓 己 彑 巾 马 门 士). Errata net change:
-1 (厂 graduated) + 15 (new fails) = +14. New distilled principle:
"draw the flick — a stroke's identity often rides on its terminal
hook/flick direction, and omitting or misdirecting a 2-3 px terminal
is enough to fail an otherwise-correct silhouette" (see drawer_memory).

**Batch-3 update**: 5 items GRADUATED (撇点, 横折弯, 竖弯钩, 横折折, 丿) — all
PASSed on retry and removed from this notebook. 2 items FAILED retry again
(横折折折钩, 乛) — diagnosis updated below with retry note. 8 NEW items added
from the batch-3 main curriculum (all 2画 radicals).

**Batch-4 update**: 2 more GRADUATED (八, 冂 — both retry PASSed) and REMOVED.
6 retry FAILs incremented (乛 retry_n→2, 厂 retry_n→1, 横折折折钩 retry_n→2, 匕
retry_n→1, 冖 retry_n→1, 人 retry_n→1, 丷 retry_n→1). 13 NEW items added from
batch-4 main curriculum. Errata net change: -2 (八, 冂 graduated) + 13 (new
fails) = +11. Total open errata items now = 20 (was 11).

**Batch-5 update**: 1 GRADUATED (亻 — retry PASSed) and REMOVED. 4 retry FAILs
incremented (屮 retry_n→1, 干 retry_n→1, 廴 retry_n→1, 讠 retry_n→1). 11 NEW
items added from batch-5 main curriculum (弓, 广, 己, 彑, 马, 门, 宀, 女, 犭,
尸, 士). All new items tagged `initial_batch: 5`. Errata net change: -1 (亻) +
11 (new) = +10. Total open errata items now = 30 (was 20).

**IMPORTANT — BATCH 6 ONE-TIME ERRATA REFRESH**: per shared_rules "One-time
errata refresh", the Drawer will attempt EVERY item currently in this errata
in batch 6, using the new "bank is supplementary, never mandatory" framing.
Items tagged `initial_batch: 5` are the newest under the current-rules regime
and should show early signal about whether new principles help.

**BATCH B2 UPDATE (positions 101–150, curated at pos 168 after v7 unlock)**:
- 2 GRADUATED (力, 人 — both retry PASSed and removed below).
- 8 retry FAILs incremented (匕 retry_n→3, 刀 retry_n→3, 入 retry_n→1,
  飞 retry_n→1, 干 retry_n→2, 己 retry_n→1, 马 retry_n→1, 士 retry_n→1).
- 30 NEW fails added from B2 main curriculum (夕 忄 幺 尢 夂 丬 夊 贝 比 长
  车 厄 方 风 父 戈 户 火 旡 见 斤 耂 肀 牛 爿 片 攴 攵 氏 礻). All new items
  tagged `initial_batch: B2`.
- v7 self-evolution: created `form_catalog.md` + `radical_position_rules.md`.
  Fixes below cross-reference these where relevant.

**BATCH B4 UPDATE (positions 214–263, curated at pos 277 under v7.1)**:
- 3 GRADUATED (干, 止, 入 — all retry PASSed and removed below).
  入's retry directly validates the v7.1 HARD RULE "sibling-bit override" —
  drawer respected the 捺-overhangs-撇 signature without waffling.
- 11 retry FAILs incremented (匕 retry_n→4, 飞 retry_n→3, 己 retry_n→3,
  门 retry_n→2, 夊 retry_n→2, 了 retry_n→2, 人 retry_n→2, 乃 retry_n→2,
  几 retry_n→2, 九 retry_n→2, 刀 retry_n→2). Diagnoses updated inline.
- 21 NEW main-B4 fails added (丬 个 丸 久 也 子 亾 么 卂 与 及 纟 干 夊 飞
  孑 孓 习 已 女 尢). All tagged `initial_batch: B4`.
- Retry pass rate 3/14 = 21% (DOWN from B3's 31%). Main pass rate
  29/50 = 58% (roughly flat vs B3's 60%). Retry regression traced
  to the retry cohort now dominated by recurring hook-flick and
  sibling-bit failures that the HOT LOOKUP does not directly address.
- Citation-rate audit (grepping generated.py): HOT LOOKUP 0/64,
  HARD RULE 4/64, form_catalog 21/64 (33%), radical_position_rules
  0/64, drawer_memory 2/64. Retry-PASSes cited form_catalog 3/3
  (100%); retry-FAILs cited form_catalog 5/11 (45%).

**BATCH B3 UPDATE (positions 151–213, curated at pos 213 under v7)**:
- 4 GRADUATED (夕, 忄, 父, 火 — all retry PASSed and removed below).
  All four cited form_catalog entries in their retry generated.py —
  first direct evidence the restructure helps.
- 9 retry FAILs incremented (尢, 夂, 丬, 车, 方, 风, 旡, 牛, 攴 all
  retry_n→2). Diagnoses updated inline.
- 20 NEW main-B3 fails added (水 瓦 尣 韦 毋 牙 支 止 爪 乚 了 丩 人 乃 乜
  几 九 入 刀). All tagged `initial_batch: B3`.
  - Note: 人 fail is a SIGNATURE-BIT failure — the drawer read
    form_catalog + sibling-pair table but over-reasoned to a
    variant reading; codified as a "no-override" note in errata.
  - Note: 入, 刀 are recurring — they persist through the sibling-
    bit reasoning barrier. Same failure mode as 人.
- Retry pass rate 4/13 = 31% (up from B2's 20%). Main pass rate
  30/50 = 60% (recovering from B2's 40%).

Retry counter is tracked per item as `retry_n`.

---

## p1_stroke_24_横撇弯钩   (batch 2, retry_n=0)

**Attempt file**: `attempts/p1_stroke_24_横撇弯钩/01_横撇弯钩.png`

**Diagnosis (curator, vision-based)**:

Overall shape reads as a numeral **"3"**, not a right-ear-radical hook.
Two specific errors:

1. The 弯 arc sweeps DOWN-and-RIGHT then curls RIGHT-and-DOWN — belly
   on the lower side, opening to the upper-right. Correct 横撇弯钩
   (as in 阝-right / 及) has belly on the RIGHT with the arc opening
   to the left, so the tail can hook back UP-and-LEFT into the interior
   of the character.
2. The terminal 钩 flick reads as DOWN-and-RIGHT, not the intended
   up-and-left; likely a collision-with-arc issue.

**Root cause**: arc-parameterization confusion — belly on wrong side.

**Fix for retry** (still not proven, do NOT retry until belly-on-right
primitive is validated on another PASS):
- Belly-on-right arc: `x = cx - R*sin(t*pi/2), y = cy + R*(1 - cos(t*pi/2))`
  starting from the 撇 tip.
- Terminal 钩 flicks UP-and-LEFT (~-135° in image coords) from arc's
  bottom endpoint.

**Retry eligibility**: SKIPPED in batch 3 (log reason: primitive not
yet proven). Reconsider after any batch that proves belly-on-right
arcs on a different item.

---

## p1_stroke_32_横折折折钩   (batch 2, retry_n=2, retry FAILED batch 3 AND batch 4)

**Batch-4 retry FAIL update**: attempted again at scan #2. Applied the
"1.5-2× further" rule — pushed terminal 竖 further left (~30 px lean)
and made hook 40 px. But the render (see `retry_attempts/.../01_横折折折钩.png`)
STILL fails: the terminal 竖 now leans correctly but the retrograde
middle 横 became too short (~25 px), making the whole zigzag look
cramped in the upper half of the canvas. The 乃-swoop needs BOTH long
verticals AND a wide overall footprint — moving one knob at a time is
not enough. Also the hook still reads as a right-angle nub rather than
a swept flick.

**Fix for next retry (retry_n=2)**: rebuild from scratch with the whole
shape scaled to fill 250 px vertical extent. Middle 横 length must be
~50 px (not 25); terminal 竖 length ~120 px with 25 px lean; hook 50 px
at -145°. Do not tweak — restart.

**Original diagnosis retained (still applicable):**

**Attempt file (retry)**: `retry_attempts/p1_stroke_32_横折折折钩/01_横折折折钩.png`

**Diagnosis of retry FAIL (curator, vision-based)**:

Retry applied the segment-length hierarchy rule (retrograde middle 横
shortened to ~35 px, terminal 竖 extended to ~90 px). Beat count is
right. But visually the glyph STILL reads as a squarish zigzag, not
the tall/swept 乃-shape. Two remaining defects:

1. **Terminal 竖 lean is too weak.** The final 竖 drops nearly vertically;
   canonical 乃/及 has the terminal 竖 clearly LEANING LEFT (starts at
   roughly the middle 横's left endpoint, descends and drifts further
   left), so the whole bottom-hook profile swings to the lower-left.
2. **Hook flick is too small and near-horizontal.** Reads as a small
   right-angle nub. Needs to be ~30-40 px long, angled -140° to -150°
   (a diagonal up-and-left sweep), tapered to a sharp tip.

**Fix for next retry**:
- Move terminal 竖's END point ~20-30 px LEFT of its start (strong lean).
- Increase hook length to ~35 px, angle -145°, taper r=6→1.
- Consider also making the top 横 slightly longer than currently used
  (the 横 dominance sets up the "tall swept" balance).

**Retry eligibility**: after batch-4 boundary (item #80) at earliest.

---

## p2_radical_011_匕   (bootstrap batch, retry_n=4, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p2_radical_011_匕__retry_3/`.
撇 now crosses through the 竖 correctly — that half is fixed. But the
TERMINAL HOOK of the 竖弯钩 flicks DOWN-and-right instead of UP-and-left.
Same "draw the flick" failure that keeps dogging this item across 4
retries. Fix next: hard-code the hook as a mandatory final step —
30 px flick at angle -105° to -115° (upward-and-slightly-left in image
coords). Cross-ref drawer_memory §"Draw the flick" AND form_catalog
"匕 vs 七" sibling row (upward-hook is 匕's identity, downward-nub is
what turns it into 七 mis-drawn).

**B2 retry FAIL note**: retry at `attempts/p2_radical_011_匕__retry_2/`.
The 撇 direction is correct and the hook is now present, but the 撇's
tip doesn't cross THROUGH the 竖 — it lands to the LEFT of the vertical
without visibly cutting through it. Result reads as 匕 with a floating
top-flick. Cross-ref: form_catalog.md "撇 as body-crossing diagonal" —
the 撇's END should sit CLEARLY LEFT of the 竖 (past it), and its
BODY must overlap the 竖. Fix: extend 撇 endpoint to x≈70 with body
crossing at ~y=110.


**B1 retry FAIL note**: Second retry (see `attempts/p2_radical_011_匕__retry_1/`).
The 撇 now throws upper-right → lower-left correctly (principle 1 in
memory applied — no more docstring waffling about stroke class). But
the 竖弯钩's terminal hook is still absent: the L-shape at the bottom
ends flat, no visible up-and-slightly-left flick. Root cause this
attempt: the drawer drew the 竖弯 body but forgot to append the 钩
flick at all. The crossing of 撇 through the vertical is present but
happens too high — 撇 tip lands close to the top of 竖 rather than
crossing through it in the upper-third. Fix for next retry: (1) draw
the hook as a mandatory final step ~30-35 px @ -105° from the bottom
of the L; (2) start the 撇 higher (upper-right ~y=55) so its tip
crosses the 竖 at around 30% depth, not 5%.



**Attempt file**: `attempts/p2_radical_011_匕/01_匕.png`

**Diagnosis (curator, vision-based)**:

The top stroke was rendered as a near-horizontal top-bar sliding LEFT→RIGHT
with slight down-tilt (drawer set `p1_start=(55,95)`, `p1_end=(215,128)`).
That direction is a 提/横, not a 撇. Canonical 匕's stroke 1 is a 撇 that
throws from upper-right down toward lower-left. Because the drawer rendered
it as a nearly-horizontal bar sitting on top of the 竖弯钩, the result
reads as **七** (with a top 横 crossing a 乚), not 匕.

Compounding defect: the terminal hook was set at angle -95° (nearly
straight up), when 匕's 竖弯钩 hook flicks up-and-slightly-left (more like
-100° to -115°) — visible as a rigid vertical nub in the attempt.

**Root cause**: drawer talked themselves out of the correct direction in
the docstring — the reasoning trail explicitly waffled between 撇 and
提/横, and settled on the wrong reading. When the label unambiguously
names a stroke class, RENDER THAT CLASS. Never let GT-tracing over-rule
the canonical direction the label prescribes.

**Fix for retry**:
- Stroke 1 = 撇: start upper-right around (170, 75), throw down-and-left
  to about (85, 155), thick→thin taper, gentle rightward bow (Bezier
  control pulled toward the interior).
- Stroke 2 = 竖弯钩: 竖 descends from around (85, 100), arcs
  tangent-continuously into a rightward 横 near the baseline, terminal
  hook flicks up-and-slightly-left at ~-105° (NOT nearly-vertical).
- The 撇 must cross the 竖弯钩's vertical, with its tip landing to the
  LEFT of the 竖.

---

## p2_radical_014_厂   (bootstrap batch — GRADUATED B1)

**GRADUATED B1** — retry PASSed and item removed from active errata.
Fix applied: shared top-left corner between 横 and 撇 (no inset). The
"Compound radicals: adjacent strokes SHARE joints" principle in
drawer_memory (added in bootstrap batch) transferred cleanly. Retained
below only for chain-of-evidence, not action.

---

## p2_radical_015_刀   (bootstrap batch, retry_n=3, retry FAILED B2)

**B2 retry FAIL note**: retry at `attempts/p2_radical_015_刀__retry_2/`.
Stray-nub artifact resolved (joining-dab discipline applied), but the
撇 now doesn't cross the top 横 — it starts INSIDE the 横折钩 body and
sweeps down-left without any part poking ABOVE the 横 line. Same
crossing-visibility failure that 匕 has. Fix: 撇 start ABOVE the 横
(y≈55 with 横 at y≈85), cross through at x≈140. Cross-ref:
form_catalog.md "撇 as body-crossing diagonal".


**B1 retry FAIL note**: Second retry (see `attempts/p2_radical_015_刀__retry_1/`).
The 撇 now crosses through the top 横 (principle applied — good). But a
stray ink artifact remains BELOW the main body (visible as a small dot
around y=260, x=155), which is the same "hook-tail overshoot" defect
flagged in the original diagnosis. Root cause this attempt: the drawer
kept the hook flick at a steep angle with a joining dab larger than
segment radius, and the joining dab bled below the intended endpoint.
Fix for next retry: (a) set joining-dab radius EQUAL to segment radius
(not r+1, not r+2) at the hook base; (b) shorten hook flick to ~25 px
so it doesn't overshoot; (c) verify by pixel-scan that no ink exists
below the intended terminal-竖 endpoint y-value.



**Attempt file**: `attempts/p2_radical_015_刀/01_刀.png`

**Diagnosis (curator, vision-based)**:

Two defects visible:

1. The 横折钩's terminal hook geometry produced an extra downward-going
   ink artifact — the hook flick angle (-150°) combined with the joining
   dab at `v_end=(175,260)` leaves a small stray protrusion below the
   main body. Reads as a spurious dot/stroke inside the radical.
2. The 撇 (stroke 2) ends at `(40, 275)` — near the extreme lower-left
   corner — but starts at `(160, 95)` INSIDE the 横折钩. In canonical 刀
   the 撇 crosses THROUGH the top 横 (starting ABOVE it and passing
   down through it), so the top of the 撇 is visible ABOVE the 横 line.
   In the attempt the 撇 is entirely inside/below the 横, so the
   crossing signature is missing.

**Root cause**: stroke-order confusion + hook-tail overshoot. The
drawer treated the 撇 as "under the 横" instead of "crossing the 横".

**Fix for retry**:
- Stroke 1 (横折钩): keep the top 横 short (~120 px), shoulder, then
  the curving 竖 with belly on the RIGHT (concave-left). Hook flick
  angle around -135° to -145° with joining dab RADIUS equal to segment
  radius (not r+1) to avoid the stray-nub artifact.
- Stroke 2 (撇): start ABOVE the 横 (e.g. y=70, above the 横's y=90),
  cross THROUGH the 横 at about x=140, continue down-and-left to
  around (55, 260). Thick→thin taper with 顿 press at start.
- Verify by eye: the top of the 撇 must poke UP above the 横 line.

---

## p2_radical_020_阝   (batch B1, retry_n=0)

**Attempt file**: `attempts/p2_radical_020_阝/01_阝.png`

**Diagnosis (curator, vision-based)**: reads as a numeral "3" sitting
on top of a straight 竖. Canonical 阝 (right ear) is a single 横撇弯钩
(the ear-lobe compound) attached to a 竖 that starts AT the hook's
end — one continuous ear-and-drop. The attempt renders the ear as
two disconnected humps (like a script 3), and the 竖 begins BELOW the
ear instead of continuing from the hook base.

**Fix**: draw the ear as ONE 横撇弯钩 primitive with belly-on-right
(SAME primitive we still need to prove for stroke_24). Until that
primitive is proven, this item cannot be reliably fixed. Skip retry
until belly-on-right arc is demonstrated elsewhere.

---

## p2_radical_025_力   (batch B1, GRADUATED B2)

**GRADUATED B2** — retry PASSed and removed from active errata. Fix
applied: 撇 as a full body-crossing diagonal (~150 px, starting above
the 横折钩's top 横 and throwing down-left past the hook body).
Recorded as `form_catalog.md` entry "撇 as body-crossing diagonal".

---

## p2_radical_028_人   (batch B1, GRADUATED B2)

**GRADUATED B2** — retry PASSed and removed from active errata. Fix
applied: right stroke rendered as a proper 捺 with thin→thick taper
and broad terminal foot; 撇 got a subtle rightward bow; apex meeting
correct. Recorded as `form_catalog.md` entry "捺 as right-leg of
two-stroke apex".

---

## p2_radical_030_入   (batch B1, retry_n=1, retry FAILED B2)

**B2 retry FAIL note**: retry attempt at `attempts/p2_radical_030_入__retry_1/`.
The 捺 does now start higher than the 撇's top and there IS a visible
overhang, but the two strokes were placed so they still meet visually
at a shared point and the overhang is too small (~10 px). The signature
"捺 covers 撇" needs a bigger vertical offset (~30 px) AND the 捺 must
be the visually-dominant thick-footed stroke. Fix for next retry: 捺
starts at y≈50, 撇 starts at y≈80; the 撇's top must sit CLEARLY below
the 捺's top by eyeball. Cross-ref: form_catalog "捺 as right-leg of
two-stroke apex" + sibling-pair table row 人-vs-入.


**Attempt file**: `attempts/p2_radical_030_入/01_入.png`

**Diagnosis**: reads identical to 人 — two straight legs meeting at
the very top. Canonical 入 differs from 人 in topology: the 撇 starts
LOWER than the 捺's top; the 捺 covers the 撇's top with an overhang.
Instead the attempt drew both legs meeting at a single apex, which is
the 人 topology.

**Fix**: draw 捺 first from an upper-left start (e.g. y=60), then draw
撇 starting at ~(150, 90) — 30 px BELOW the 捺's top — so the 捺
overhangs the 撇 at the top. This overhang is 入's distinguishing
signature.

---

## p2_radical_032_厶   (batch B1, retry_n=0)

**Attempt file**: `attempts/p2_radical_032_厶/01_厶.png`

**Diagnosis**: shape reads as an incomplete triangle with a stray tail.
厶 = 撇折 + 点 stacked. The attempt shows the 撇折 corner but the closing
点 is misplaced/oversized as an extension of the 折 tail rather than
a separate teardrop dot below/right.

**Fix**: (1) draw 撇折 as a proper compound (撇 tip → shoulder-dab → short
横 rightward) — DO NOT extend it into the 点; (2) draw 点 as a SEPARATE
teardrop-shape short dot (~40 px, thin→thick, ending in press) placed
UNDER the right end of the 撇折's 横.

---

## p2_radical_042_巛   (batch B1, retry_n=0)

**Attempt file**: `attempts/p2_radical_042_巛/01_巛.png`

**Diagnosis**: reads as three parallel curved 撇 strokes. Canonical 巛
is three ㄑ-shapes (each a small 撇 + 竖 rightward-curving into a hook
or point) — wave/river signature. The attempt drew simple curved
verticals with no zig-zag or wave.

**Fix**: each of the three strokes should be a small compound —
short 撇 at top-left, then a short curving 竖 (or 竖弯) that swings
down-and-right. Reserve room to fit three of these side by side in
300 px width.

---

## p2_radical_047_飞   (batch B1, retry_n=3, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p2_radical_047_飞__retry_2/`.
Retry now reads as 力 — the top 横折 body is present but the terminal
UP-LEFT hook is completely missing, and the inside 撇-dot is missing.
Regression from B3 retry (which at least attempted the hook). Fix:
this item now needs to be REBUILT from scratch — decompose per drawer_memory
"横折弯钩" KEY PRIMITIVE and enforce a terminal hook check. Cross-ref
form_catalog "点" entries for the inside dot placement.

**B2 retry FAIL note**: retry at `attempts/p2_radical_047_飞__retry_1/`.
Applied the tangent-continuous arc primitive from drawer_memory
("横折弯钩" recipe). The primary compound came out cleaner but the
inside 点 is missing / rendered as a stray mark, and the terminal hook
still doesn't flick decisively up-and-left. Fix next: (a) draw the
inside 撇-dot first at ~(180, 105) as a short down-left teardrop,
BEFORE the primary compound; (b) hook flick 40 px @ angle -115° to
-120° with taper r=5→1. Cross-ref: form_catalog "点" entries, no
existing entry for 飞's specific inside dot — a candidate future entry.


**Attempt file**: `attempts/p2_radical_047_飞/01_飞.png`

**Diagnosis**: attempt shows top 横折 + a downward hook at the right,
plus a stray small stroke. Two defects: (1) hook flicks DOWNWARD when
canonical 飞's terminal 斜钩 hooks UP-and-LEFT; (2) missing the middle
点 that sits inside the 横折 corner.

**Fix**: (1) render the primary as 横折弯钩 (proven KEY PRIMITIVE — see
drawer_memory) — 横 then shoulder + short 竖 + tangent arc into
rightward 横 + hook up-and-LEFT (~-115°); (2) add a small 撇-style dot
inside the upper-right of the 横 corner.

---

## p2_radical_048_干   (batch B1 — GRADUATED B4)

**GRADUATED B4** — retry_2 PASSed and removed from active errata. Fix
applied: form_catalog "竖 as through-going axis" cited — top 横 pushed
down to y≈85 and shortened, bottom 横 lengthened, through-竖 extends
~15 px below bottom 横. Length ratio (top ~65% of bottom) now visually
decisive, glyph no longer collapses to 千/士.

---

## p2_radical_050_弓   (batch B1, retry_n=0)

**Attempt file**: `attempts/p2_radical_050_弓/01_弓.png`

**Diagnosis**: rendered as three disconnected horizontals + a bottom
hook. Canonical 弓 is a 3-fold connected shape: 横折 + 横 + 横折钩 (with
the strokes sharing 折 shoulders). The horizontals appear as separate
bars with no visible 折 corners.

**Fix**: use the beat-count rule (memory): 弓 has 2 pieces — top 横折
+ bottom 横折钩, plus the middle 横 that sits between. All connect at
折 shoulders on the RIGHT edge, forming a stacked "E" open-to-the-left,
with bottom hook flicking up-and-left.

---

## p2_radical_053_己   (batch B1, retry_n=3, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p2_radical_053_己__retry_2/`.
The middle 横 now floats away from the LEFT wall (good — the B2 fix
transferred). But the middle 横 EXTENDS to touch the RIGHT wall,
making the interior read like a closed box. Also the bottom 竖弯钩's
outward sweep past top-right edge is only marginal. Silhouette reads
as 巴 or 已 rather than 己. Fix: middle 横 must FLOAT on BOTH sides
(start at x≈95, end at x≈200 with clear gap from right wall too);
bottom 竖弯钩 must sweep RIGHT past the top-right's x-coord by 20+ px.

**B2 retry FAIL note**: retry at `attempts/p2_radical_053_己__retry_1/`.
The bottom 竖弯钩 now sweeps rightward past the top-right endpoint —
good. But the middle 横 in the retry TOUCHES the left wall, which
converts the glyph into 已 not 己. See the new sibling-pair table
entry (己 / 已 / 巳) in `form_catalog.md`. Fix next: the middle 横
must FLOAT — start at ~x=95 (not x=75) so there's a visible 15+ px
gap between the left wall and the middle 横's left endpoint.


**Attempt file**: `attempts/p2_radical_053_己/01_己.png`

**Diagnosis**: reads as a boxy 巳-like shape — the bottom terminal
lacks the sweeping 竖弯钩 tail that opens the base of 己 to the RIGHT.
己 vs 已 vs 巳 distinguishes by how the middle 横 attaches to the left
vertical (己: doesn't touch; 已: touches midway; 巳: touches at top).
The attempt closes the top-right corner as a box and doesn't swing
the base outward.

**Fix**: 3 strokes: (1) 横折 top; (2) short 横 middle floating away
from the left wall; (3) 竖弯钩 bottom — descend on the left, arc
smoothly rightward past the right edge, hook up-and-left at the end.
The bottom stroke's tail must extend RIGHT past where the top ends.

---

## p2_radical_055_彑   (batch B1, retry_n=0)

**Attempt file**: `attempts/p2_radical_055_彑/01_彑.png`

**Diagnosis**: attempt renders 工-like shape on a base 横 — but canonical
彑 is 彐 with a small ㄑ hat (like a downward-pointing chevron above the
E-shape). The attempt lost the chevron entirely and drew straight
segments.

**Fix**: (1) top: small downward chevron (撇 + 点) meeting at an apex;
(2) middle+bottom: 彐 shape (three horizontals stacked with vertical
right closure) BELOW the chevron. The chevron must be small (~40 px
wide) and sit centered above the 彐 body.

---

## p2_radical_056_巾   (batch B1, retry_n=0)

**Attempt file**: `attempts/p2_radical_056_巾/01_巾.png`

**Diagnosis**: reads as sparse — top 冂 with center 竖 but the 冂's
right side lacks a terminal hook flick, and the center 竖 doesn't
extend far enough below the 冂 base. Silhouette is too thin.

**Fix**: (1) 冂 right stroke should end in a 竖 (no hook needed) with
noticeable weight; (2) center 竖 must extend AT LEAST 100 px below the
冂 base to give the character its "hanging cloth" proportion; (3)
横 top should have small terminal presses at both ends.

---

## p2_radical_058_马   (batch B1, retry_n=1, retry FAILED B2)

**B2 retry FAIL note**: retry at `attempts/p2_radical_058_马__retry_1/`.
Applied principle 8 (bottom 横 originates at left edge). Bottom 横
now connects but the zig-zag body is still cramped — the middle 折
segments are too small (~20 px each), so the character reads as a
narrow rectangle with a tail rather than the tall 马 profile. Fix
next: increase middle-body height to ~130 px (currently ~80); each
折 segment should be ~40 px minimum. Cross-ref: form_catalog.md
"折 shoulder placement" family + drawer_memory beat-count rule
(马's 竖折折钩 is 3 body beats + hook).


**Attempt file**: `attempts/p2_radical_058_马/01_马.png`

**Diagnosis**: attempt has upper box with slanted internal stroke +
a DISCONNECTED bottom 横. 马 is a 3-stroke compound: 横折 + 竖折折钩 +
横, but all three visually connect — the bottom 横 must run THROUGH
the terminal hook of stroke 2, not float below it.

**Fix**: bottom 横 must originate at the LEFT edge (roughly aligned
with stroke-2's left vertical) and run rightward through/past the
hook. Also: internal structure needs to read as a clear zig-zag 折
body, not a diagonal slash.

---

## p2_radical_059_门   (batch B1, retry_n=1, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p2_radical_059_门__retry_1/`.
Bracket topology now correct — top-left dot present, left 竖 present,
top 一 spans to left 竖. But the terminal HOOK on the right 横折钩
flicks DOWN-RIGHT instead of UP-LEFT. Same "draw the flick" mode as
匕. Fix: cross-ref new form_catalog "门 as bracket enclose" entry —
hook MUST flick UP-and-LEFT (~ -105°) with taper r=5→1.

**Attempt file**: `attempts/p2_radical_059_门/01_门.png`

**Diagnosis**: three of four components present (点 + 竖 + 横折钩) but
the right 横折钩's top 横 doesn't reach the left 竖 (visible gap at
the top). Canonical 门 has the top 横 spanning between the two verticals
as a single visual bar.

**Fix**: extend the top 横 leftward so it touches (or nearly touches)
the top of the left 竖. Do NOT expect the strokes to physically join
in MMH — but the visual gap should be < ~10 px, not the current ~40 px.

---

## p2_radical_067_士   (batch B1, retry_n=1, retry FAILED B2)

**B2 retry FAIL note**: retry at `attempts/p2_radical_067_士__retry_1/`.
Length ratio was swapped (top LONGER than bottom — good direction),
but the difference is subtle (~140 vs ~120). Human eye still reads
it as ambiguous or 土. Use the "move the knob further" rule from
drawer_memory: push the ratio to 160 vs 100 (top ~1.6× bottom). The
new sibling-pair table in `form_catalog.md` codifies this — top 横
LONGER is 士's ONLY signature bit, so exaggerate rather than tweak.


**Attempt file**: `attempts/p2_radical_067_士/01_士.png`

**Diagnosis**: 士 vs 土 distinguishes by top 横 length: 士 has TOP 横
LONGER than bottom, 土 has bottom LONGER. Attempt renders the top
shorter than the bottom, reading as 土.

**Fix**: swap the length ratio — top 横 ~150 px, bottom 横 ~110 px.
Vertical passes through both. This is the mirror-image of the 干 fix.

---

## p2_radical_075_夕   (batch B2 — GRADUATED B3)

**GRADUATED B3** — retry PASSed and item removed from active errata.
Fix applied: square silhouette per `radical_position_rules.md` +
form_catalog "撇 as top-of-radical single flick" + "折 shoulder
placement". Direct citation of the new files in the retry
generated.py — first evidence the v7 restructure transfers.

---

## p2_radical_077_忄   (batch B2 — GRADUATED B3)

**GRADUATED B3** — retry PASSed and item removed from active errata.
Fix applied: form_catalog "点 as 忄 heart-radical side dot" entry
was cited verbatim in the retry — the drawer used the entry's dot
lengths and positions directly. Left/right side dots came out
correctly as short flicks not full 撇.

---

## p2_radical_078_幺   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_078_幺/01_幺.png`

**Diagnosis**: Rendered as two horizontal flicks + a small bottom
dot, but the two 折 loops that make 幺 are missing — 幺 is two
stacked 撇折 loops + a bottom 点 (or 撇折 · 撇折 · 点). The attempt
looks more like 乡 with missing hooks.

**Fix**: draw two small compound loops: each = short 撇 + shoulder +
short 折 tail going down-right. Stack them at ~(140,80) and (140,150).
Bottom 点 at ~(155, 220). Cross-ref drawer_memory "撇折 family".

---

## p2_radical_080_尢   (batch B2, retry_n=2, retry FAILED B3)

**B3 retry FAIL note**: 竖弯钩 leg present but bend angle too weak;
still reads ambiguous with 尤/大. Next retry: apply the KEY PRIMITIVE
tangent-arc from drawer_memory with a LARGER R (~45 not ~30) so the
bend is visually decisive. Cross-ref form_catalog new "撇 + 竖弯钩 as
leg-pair" entry.



**Attempt file**: `attempts/p2_radical_080_尢/01_尢.png`

**Diagnosis (curator, vision-based)**: Likely rendered without the
bent 竖弯钩 leg — 尢 = 一 + 撇 + 竖弯钩 (leg bent to the right at
bottom). If the leg came out as a plain vertical or hooked wrong,
reads as 大 or 尤 sibling.

**Fix**: right leg must be a proper 竖弯钩 with smooth arc into
rightward run + up-left hook. See drawer_memory "tangent-continuous
vertical→horizontal arc" primitive.

---

## p2_radical_081_夂   (batch B2, retry_n=2, retry FAILED B3)

**B3 retry FAIL note**: 捺 present but too short/flat; compact "each"
silhouette not achieved. Fix: shorten top 撇 (~50 px) and lengthen
捺 (~150 px) with r_end ~10 for broad terminal foot. Let the 捺
dominate.



**Attempt file**: `attempts/p2_radical_081_夂/01_夂.png`

**Diagnosis**: 夂 = 撇 + 横撇 + 捺. Silhouette should be a small
compact "each" shape. Attempt likely lost the 捺's thick foot or
made the top 撇 too dominant.

**Fix**: three tight strokes: top 撇 short (~60 px), middle 横撇
short crossing the 撇 mid-height, terminal 捺 long down-right with
broad terminal foot. Cross-ref form_catalog "捺 as right-leg" and
"撇 as top-of-radical single flick".

---

## p2_radical_083_丬   (batch B2, retry_n=2, retry FAILED B3)

**B3 retry FAIL note**: 提 rising into 竖 but not physically touching;
brackets don't asymmetrize enough. Fix: the 提's TIP must terminate
AT the 竖's x-coord (joint pixel). Non-touching brackets read as
separate marks.



**Attempt file**: `attempts/p2_radical_083_丬/01_丬.png`

**Diagnosis**: Rendered as two dots + a straight 竖 (looks like 冫
+ 丨). Canonical 丬 = 点 top + 提 middle + 竖 right, forming an
asymmetric structure where the top and middle strokes bracket the
竖 from the LEFT. Attempt has the small strokes too far LEFT / not
touching the 竖.

**Fix**: 点 top at (100, 90) with down-right taper; 提 middle at
(90, 155) rising up-right and TOUCHING the 竖 at right; 竖 straight
vertical at x≈175 spanning y=70-260. Cross-ref form_catalog "点"
entries + "竖 as through-going axis".

---

## p2_radical_084_夊   (batch B2, retry_n=2, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p2_radical_084_夊__retry_1/`.
Still reads as 夂 — the extra top-left short 撇 that distinguishes 夊
from 夂 is missing entirely. The drawer produced a valid 夂 body but
forgot the leading tick. Fix: enforce 4-stroke count check — 夊 has
FOUR strokes (short 撇 top-left + 横撇 crossing + long 撇 body + 捺
foot), whereas 夂 has three.

**Attempt file**: `attempts/p2_radical_084_夊/01_夊.png`

**Diagnosis**: 夊 is similar to 夂 but the top has an extra
short 撇. Attempt likely conflated with 夂 or produced ambiguous
crossed-strokes.

**Fix**: 4 strokes — small 撇 top-left, small 横撇 crossing, then
larger 撇 body + 捺 body. Same right-foot rule as 夂.

---

## p2_radical_085_贝   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_085_贝/01_贝.png`

**Diagnosis (vision-verified)**: rendered as 冂 with only bottom
"人-legs" — the two internal 横 bars are missing. Reads as 几. 贝 =
top box (口/日-like) with TWO internal cross-bars + splayed legs
(撇 + 点) hanging below.

**Fix**: (1) top box: 竖 + 横折 forming a rectangle at y=60-160;
(2) two internal 横 bars at y≈100 and y≈145; (3) legs — 撇 from
box-bottom-left sweeping down-left, 点 from box-bottom-right
flicking down-right. Cross-ref form_catalog sibling-pair table
row 贝-vs-见.

---

## p2_radical_086_比   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_086_比/01_比.png`

**Diagnosis (vision-verified)**: rendered as 忙-like — a 竖 with a
top 横 on the left half and a hooked shape on the right half. But
比 = 匕 + 匕 (two 匕 side by side). Attempt has neither 匕 clearly
readable; the left half looks like a plus (十) and right half looks
like a 乚.

**Fix**: draw two 匕s side by side. Left 匕: 横 (55,110)→(130,105)
plus 竖弯钩 x=120. Right 匕: 撇 (200,60)→(155,135) plus 竖弯钩 x=200
with hook up-left. Each 匕 follows the sibling-pair table entry
(匕 top = 撇 not 横 for the RIGHT one; the LEFT one is a 提 in 比's
convention, unusual — verify against GT).

---

## p2_radical_088_长   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_088_长/01_长.png`

**Diagnosis**: 长 has a distinctive top short 撇 + top 横 + long
竖提 + long slanted 捺 sweeping down-right. Attempt likely got the
silhouette wrong (missing the wide 捺 splay or getting the 竖提
angle wrong).

**Fix**: Use radical_position_rules "square" family. 4 strokes: top
撇 (short 45 px), top 横 (medium 100 px), 竖提 (long 竖 turning
into rising 提 mid-body), 捺 (long thin→thick sweeping down-right
past the right wall). The 捺 is the dominating stroke visually.

---

## p2_radical_089_车   (batch B2, retry_n=2, retry FAILED B3)

**B3 retry FAIL note**: Retry rendered as 王-like symmetric stack.
Fix: top-lid shoulder-竖 drop MUST be visible (~30 px short 竖 on
the right of the top 横). Also the middle 横 must be DIFFERENTIAL
length from the bottom (~65%) or the glyph collapses to 王.



**Attempt file**: `attempts/p2_radical_089_车/01_车.png`

**Diagnosis (vision-verified)**: rendered as a symmetric 王-like
stack (three horizontals + long central 竖). But 车 has a
distinctive top 横折 lid + middle 十-cross + long bottom 横 + long
竖 through everything. The top-右 shoulder is missing and the
middle bar is unbalanced.

**Fix**: 4 strokes: (1) top-lid = short 横 + shoulder + short 竖-drop
on the right (forming a ⊤-like top); (2) middle 横 medium length;
(3) bottom 横 the LONGEST; (4) central 竖 passing through everything
with slight 提 at bottom (or straight). Cross-ref form_catalog "竖
as through-going axis" and "横" as top-vs-bottom differentiator.

---

## p2_radical_092_厄   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_092_厄/01_厄.png`

**Diagnosis**: 厄 = 厂 (top-left corner) + 卩 (inside body). Attempt
likely lost the inside 卩 shape or got the 厂 corner disconnected.

**Fix**: Use radical_position_rules "off-center L" family for the 厂
outer. Inside 卩 (right-ear compound with 横折钩 + 竖) sits inside
the 厂's opening. The 厂's 撇 tail must sweep out to lower-left,
the inside 卩 must be small and contained.

---

## p2_radical_093_方   (batch B2, retry_n=2, retry FAILED B3)

**B3 retry FAIL note**: 亠 top present but body 横折钩 + crossing 撇
imbalanced, reads too narrow. Fix: increase body x-extent to fill
~70% width; the crossing 撇 must sweep clearly outside the 横折钩's
right wall on its way to lower-left.



**Attempt file**: `attempts/p2_radical_093_方/01_方.png`

**Diagnosis**: 方 = 亠 top (dot + 横) + 万-like body (横折钩 + 撇).
Attempt likely rendered too tall / too narrow, or lost the 亠 lid.

**Fix**: top 点 above middle 横; then body 横折钩 with 撇 crossing
through from upper-right to lower-left. Cross-ref form_catalog "撇
as top-lid" for the top dot form.

---

## p2_radical_094_风   (batch B2, retry_n=2, retry FAILED B3)

**B3 retry FAIL note**: Outer 撇 attempted with curvature but still
reads too boxy — 撇 not curved enough. Fix: Bezier P1 must be pulled
significantly right of chord midpoint (~40 px offset) to make the
left wall a proper curved sweep, not a diagonal straightaway.



**Attempt file**: `attempts/p2_radical_094_风/01_风.png`

**Diagnosis (vision-verified)**: rendered as a top rectangle with
inside 人-legs. But the outer shape should have a curved-diagonal
LEFT stroke (撇) rather than a straight-vertical left wall, and the
top-right should be a shouldered 横折钩 not a boxy right-angle.
Silhouette reads as 冈 not 风.

**Fix**: outer = 撇 (curved down-left from top-right to bottom-left)
+ 横折弯钩 (top-right corner sweeping down and hooking right). Inside
= small 乂 (short 撇 + 点). Cross-ref drawer_memory "横折弯钩" KEY
PRIMITIVE.

---

## p2_radical_095_父   (batch B2 — GRADUATED B3)

**GRADUATED B3** — retry PASSed and item removed from active errata.
Fix applied: top-splay 八-style dots + 乂 body-crossing (form_catalog
"乂 as body-cross" now codifies this template). Cross-ref with the
passing 爻 at pos 161 (two 乂 stacked) validated the pattern.

---

## p2_radical_096_戈   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_096_戈/01_戈.png`

**Diagnosis**: 戈 = 横 + 斜钩 (long diagonal with belly-on-lower-left,
hook up) + 撇 + 点. Attempt likely rendered the 斜钩 as a plain
diagonal (no hook) or straightened its bow.

**Fix**: Use drawer_memory "斜钩 (戈钩)" entry — P0=(95,55), P2=(245,245),
P1=(125,195), hook flick at -110° to -120°. Add 撇 short from top
horizontal + 点 upper-right corner.

---

## p2_radical_097_户   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_097_户/01_户.png`

**Diagnosis**: 户 = 丶 top dot + 一 + 尸-like body (厂 + inside).
Attempt likely conflated with 尸 by omitting the top dot, or got
the top dot positioned wrong.

**Fix**: TOP DOT is the signature — small teardrop at ~(140, 55)
ABOVE the 一 line. Then 一 at y≈85. Then body 尸-like (厂 corner
with inside 横 + tail 撇). Cross-ref form_catalog sibling-pair table
row 户-vs-尸.

---

## p2_radical_098_火   (batch B2 — GRADUATED B3)

**GRADUATED B3** — retry PASSed and item removed from active errata.
Fix applied: 4-stroke layout with flanking side dots at (90,100) and
(200,100) + 人-body per form_catalog "点" and "捺 as right-leg". The
distinction between "flanking dots" and "middle-body dots" was the
signature-bit fix.

---

## p2_radical_099_旡   (batch B2, retry_n=2, retry FAILED B3)

**B3 retry FAIL note**: Closer to 无 but still ambiguous — leg-count
or 竖弯钩 subtlety off. Fix: cross-ref the PASSING 无 (position 167,
B3) which has identical structure; copy 无's 二 top + 撇+竖弯钩 splay
layout verbatim, then verify against 旡's GT for the differentiating
bit. Cross-ref new form_catalog entries "二 as top-of-radical stacked
pair" and "撇 + 竖弯钩 as leg-pair under a lid".



**Attempt file**: `attempts/p2_radical_099_旡/01_旡.png`

**Diagnosis**: 旡 is a rare radical similar to 无. Silhouette should
match 无's — a horizontal top + 一 + 儿-legs. Attempt likely produced
an ambiguous shape.

**Fix**: 5-stroke: 横 top + 横 middle + 竖 crossing both + 竖弯钩 as
right leg + 撇 as left leg. Cross-ref 无 if it exists in mastery ledger.

---

## p2_radical_100_见   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_100_见/01_见.png`

**Diagnosis**: 见 = 冂-box + 一 inside + ㄦ legs (撇 + 竖弯钩).
Attempt likely lost the inside 一 or the terminal 竖弯钩's outward
sweep. Sibling risk: 贝 (which has TWO inside bars).

**Fix**: outer box 冂 at y=60-140; inside single 横 at y≈115; legs
= 撇 sweeping down-left + 竖弯钩 sweeping down and hooking up-left.
Cross-ref form_catalog sibling-pair table row 贝-vs-见.

---

## p2_radical_101_斤   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_101_斤/01_斤.png`

**Diagnosis**: 斤 = 撇 + 撇 + 横 + 竖. Two 撇 stacked on top plus a
横 crossing then a 竖 dropping. Silhouette should be axe-like with
narrow top and wider bottom. Attempt likely got the two-撇 stack
wrong.

**Fix**: 4 strokes in order. Top 撇 short at (140,60)→(90,110). Middle
撇 medium at (200,90)→(90,180). 横 crossing at y≈150. 竖 dropping from
横's right end straight down to y≈250.

---

## p2_radical_102_耂   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_102_耂/01_耂.png`

**Diagnosis**: 耂 (old-radical variant) = 土 top + long 撇 sweeping
across. Attempt likely lost the crossing 撇 or made the 土 wrong.

**Fix**: 土 top (short 横 + long 横 + 竖 through) then a long 撇
sweeping from upper-right down through the middle-bottom of the 土
out to lower-left. The 撇 must dominate visually.

---

## p2_radical_105_肀   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_105_肀/01_肀.png`

**Diagnosis**: 肀 is uncommon; similar to 聿 top. Attempt likely
produced an ambiguous stack.

**Fix**: 4 strokes — top 横折 lid + one internal 横 + one 竖 through
all + terminal 横. Compact square silhouette.

---

## p2_radical_106_牛   (batch B2, retry_n=2, retry FAILED B3)

**B3 retry FAIL note**: Top 撇 present but length ratio between the
two 横 too subtle to differentiate from 午. Apply the "move the knob
further" rule: exaggerate ratio to 65 vs 165 (top ~40% of bottom),
not tweak.



**Attempt file**: `attempts/p2_radical_106_牛/01_牛.png`

**Diagnosis**: 牛 = short 撇 top + 横 + 横 (longer) + 竖 through all.
Very similar to 午 (has 撇 lid + 干 body). Attempt likely rendered
with wrong length ratios or missing the top 撇.

**Fix**: top short 撇 at (130,55)→(105,90). Two 横s: upper shorter
(105 px), lower LONGER (150 px). 竖 through all extending below.
Cross-ref form_catalog "横 as top-vs-bottom length-differentiator"
and "竖 as through-going axis".

---

## p2_radical_107_爿   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_107_爿/01_爿.png`

**Diagnosis**: 爿 is the mirror of 丬 — appears as 4 strokes forming
a bracket-like left-facing shape. Sibling of 丬.

**Fix**: 4 strokes — top 横 + shoulder + 竖 dropping (like 冂 left
half) + inside 横 midway + bottom 一. Silhouette is a left-open
rectangle.

---

## p2_radical_108_片   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_108_片/01_片.png`

**Diagnosis**: 片 = 4 strokes forming an asymmetric bracket. Similar
structural risk to 爿 / 丬.

**Fix**: 撇 down-left top + 竖 (right side) + 横折 (right corner
folded down) + inside 一 crossing. Silhouette compact, upper-left
opening.

---

## p2_radical_109_攴   (batch B2, retry_n=2, retry FAILED B3)

**B3 retry FAIL note**: 卜 top + 又 bottom present but the two halves
overlap oddly; stacking gap unclear. Fix: enforce a clear ~20 px
whitespace band between the two halves. Cross-ref with the failing
支 (modern sibling in B3, same failure mode).



**Attempt file**: `attempts/p2_radical_109_攴/01_攴.png`

**Diagnosis**: 攴 = 卜 top + 又-like bottom (横撇 + 捺). Attempt
likely conflated the two halves.

**Fix**: top 卜 = short 竖 with a small 点 to the right at mid-height.
Bottom 又 = 横撇 + 捺 crossing. Two halves stacked vertically.

---

## p2_radical_110_攵   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_110_攵/01_攵.png`

**Diagnosis**: 攵 = 撇 + 横 + 撇 + 捺 in a compact 夂-like shape
(basically 攴's cursive form). Attempt may have produced too spread-
out a silhouette.

**Fix**: compact square silhouette (radical_position_rules "square").
Top strokes small; bottom 撇 + 捺 dominate as a splay from center
apex. Right-foot 捺 with broad terminal press. Cross-ref form_catalog
"捺 as right-leg of two-stroke apex".

---

## p2_radical_115_氏   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_115_氏/01_氏.png`

**Diagnosis**: 氏 = 撇 + 横 + 竖提 + 斜钩. Distinctive terminal
斜钩 sweeping down-right with hook up. Attempt likely rendered the
斜钩 as a plain diagonal.

**Fix**: 4 strokes. Top 撇 short. 横 medium. 竖提 in middle rising
right at bottom. Terminal 斜钩 (drawer_memory "斜钩" entry) sweeping
from top-middle down to lower-right with hook up-and-left.

---

## p2_radical_116_礻   (batch B2, retry_n=0, initial_batch: B2)

**Attempt file**: `attempts/p2_radical_116_礻/01_礻.png`

**Diagnosis**: 礻 (spirit radical) = 丶 + 横撇 + 竖 + 点. Similar to
衤 but with ONE bottom dot (衤 has TWO). Attempt likely conflated
with 衤 or lost the top dot.

**Fix**: 4 strokes. Top 丶 dot at ~(150,50) small teardrop. 横撇
lid (short 横 + shoulder + medium 撇 to lower-left). Central 竖
straight down. Bottom 点 to the right of the 竖. Cross-ref
form_catalog "点 as 宀 roof-cap dot" pattern for the top 丶.

---


## p2_radical_119_水   (batch B3, retry_n=0, initial_batch: B3)

**Attempt file**: `attempts/p2_radical_119_水/01_水.png`

**Diagnosis**: 4-stroke water — 竖钩 central + 横撇 upper-left + 撇 left-leg + 捺 right-leg. Wing 撇/捺 aren't sweeping outward with enough length; central 竖钩 dominates but outer legs read as short humps not water-drops.

**Fix**: increase left/right wing sweep to ~150 px each with clear splay outward from mid-height of 竖钩. Cross-ref form_catalog "捺 as terminal splay under a body".

---

## p2_radical_120_瓦   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 瓦 = 一 top + 竖提 + 横折弯钩 + 点. Compact tile-radical. Attempt likely conflated strokes or dropped the inside 点.

**Fix**: 4 strokes. Top 一 short (~90 px). 竖提 left-side descending then rising to right. 横折弯钩 right-side (KEY PRIMITIVE tangent-arc). Inside 点 in the belly.

---

## p2_radical_121_尣   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: Sibling of 尢/无. One 横 + 撇 + bent 竖弯钩 right-leg. Silhouette under-splayed.

**Fix**: cross-ref new form_catalog "撇 + 竖弯钩 as leg-pair under a lid" — legs must SPLAY, not run parallel.

---

## p2_radical_123_韦   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 韦 = 二 top + 口 body + 亅 tail. Attempt likely lost the box or the tail crossing through the body.

**Fix**: 4 strokes. Top 二 wide (~130 px). Middle 口 box centered. Bottom 亅 = 竖 through the box down + hook at bottom.

---

## p2_radical_125_毋   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 毋 = 母-like box with cross-body 撇, no interior dots. Sibling risk with 母 (has TWO dots) and 毌 (has crossing 一).

**Fix**: outer box 3-fold (竖 + 横折钩 + inside 横). Cross-body 撇 from upper-right to lower-left. NO interior dots. Signature bit: dot-count.

---

## p2_radical_127_牙   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 牙 = 一 + 竖 + 横折钩 + 撇. Distinctive tooth shape — the tail 撇 is a signature bit.

**Fix**: 4 strokes. Top 一 short. 竖 dropping mid-canvas. 横折钩 forming the right-side tooth loop. Terminal 撇 sweeping down-left from the middle. Silhouette square-ish.

---

## p2_radical_131_爫   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 爫 (claw-top) = 4 short down-flicks arranged in a splay. Attempt likely rendered as 灬-style dots or uniformly parallel.

**Fix**: 4 strokes at top-of-canvas, ~y=70-140. Leftmost is a short 撇 flicking down-left; middle-left, middle-right, right are short 竖 or 点 forms with slight left-splay. Aspect: wide-flat.

---

## p2_radical_132_支   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 支 = 十 top + 又 bottom (modern form of 攴). Attempt likely fused halves or lost the 又's 横撇+捺 signature.

**Fix**: two halves with clear ~20 px whitespace band. Top 十 = 横 + 竖 cross. Bottom 又 = 横撇 + 捺 fork per form_catalog "又 as two-stroke fork". Cross-ref with the failing 攴 (classical sibling).

---

## p2_radical_133_止   (batch B3 — GRADUATED B4)

**GRADUATED B4** — retry_1 PASSed and removed from active errata. Fix
applied: clean 4-stroke square silhouette — 卜 top (short 竖 + right
tick) + central through-竖 + wide bottom 一. Sibling-bit vs 上 preserved
(the 卜 tick is visible).

---

## p2_radical_134_爪   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 爪 = 撇 top + 3 sub-strokes forming a hand. Distinct from 瓜 (adds a 厶 inside). Attempt likely too symmetric.

**Fix**: top 撇 medium-length. Under it, three splayed sub-strokes: left 竖, middle 竖, right 捺 slanting outward. Asymmetric — right leg dominates.

---

## p3_char_0006_乚   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 乚 needs smooth tangent-continuous arc + terminal press. Attempt likely lacks smooth arc or ended with wrong flick.

**Fix**: apply drawer_memory "KEY PRIMITIVE tangent-continuous vertical→horizontal arc" (proven for 乚). 竖 (130,70)→(130,170) + arc R=40 centered (170,170) parameterized `x=cx-R*cos(t*pi/2), y=cy+R*sin(t*pi/2)` + 横 to (240,210) + terminal press.

---

## p3_char_0009_了   (batch B3, retry_n=1, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p3_char_0009_了__retry_1/`.
Top 横撇 present but the 撇 tail became a detached short flick, and
the body 竖钩 shifted RIGHT of the horizontal midpoint. Result reads
as 刁 sibling (top-flick outside enclose) rather than 了. Different
failure mode from B3 (was silhouette-cramping); now it's a stroke-
detachment + midpoint-drift failure. Fix: enforce that 撇 tail
CONTINUES from the shoulder (no gap), and 竖钩 starts AT the top
一's midpoint (x-alignment check).

**Diagnosis (original B3)**: 了 = 横撇 top + 竖钩 body. Sibling risk with 子 (adds a 一) and 孑 (adds a 一 with hook detail).

**Fix**: 2 strokes only. Top 横撇 = short 横 (~90 px) + shoulder + medium down-left 撇. Body 竖钩 = straight 竖 from the horizontal's midpoint down, terminal hook up-left. No extras.

---

## p3_char_0010_丩   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 丩 (rare) — two intersecting curves. Silhouette ambiguous.

**Fix**: 2 strokes crossing at ~center. Left curve = shallow ㄑ from upper-left down to lower-middle. Right curve = shallow ㄒ crossing through it. Sits centered on canvas.

---

## p3_char_0011_人   (batch B3, retry_n=1, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p3_char_0011_人__retry_1/`.
CURATOR-BLIND-VERDICT: this retry looks correct to the curator's eye
— apex is shared, 捺 has thick foot, 撇 tapers. The human labeled it
FAIL (possibly because apex is too pointy/geometric compared to
handwritten GT). Signature bit (shared apex + thick 捺 foot) IS
present. Retaining in errata per the human label, but flagging as a
CANDIDATE DISAGREEMENT — the memory did its job here. Fix (if pressed):
soften the apex meeting-point (small joining dab), give the 撇 a
slight rightward bow.

**Diagnosis (original B3, vision-verified)**: Drawer explicitly cited form_catalog AND sibling-pair table but then OVER-REASONED to "small gap between strokes based on handwritten GT" and broke the apex-shared signature. Result reads as 入 (捺 overhangs) or ambiguous.

**Fix**: SIGNATURE-BIT OVERRIDE — when form_catalog + sibling-table say "shared apex", the drawer must not veer to "well the GT shows a small gap". The apex-shared bit IS 人's identity. Retry: 撇 tip and 捺 top at same y=~90; both throw outward to y=~270.

**LESSON (added to memory)**: sibling-pair table signatures OVERRIDE any perceived GT nuance. If a drawer overrides via GT-tracing, the signature bit fails.

---

## p3_char_0016_乃   (batch B3, retry_n=1, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p3_char_0016_乃__retry_1/`.
Zigzag body is taller than the B3 attempt (good) but the terminal
撇 didn't cross back through the body — it hangs to the left as a
separate detached diagonal. Reads as 万/刀 rather than 乃. Fix:
the terminal 撇 must ORIGINATE from the middle-横's terminal (right
end) and sweep down-and-left ACROSS the zigzag body, not from
outside it. Cross-ref drawer_memory batch-2 mastery entry for
横折折撇 with exact endpoint sequence.

**Diagnosis (original B3)**: 乃 = 横折折撇 + 撇. Zigzag body must be tall enough and terminal 撇 dominant — likely too compressed (same failure as p1_stroke_32_横折折折钩).

**Fix**: cross-ref drawer_memory batch-2 mastery entry 横折折撇: 横 (70,78)→(170,70) + shoulder + short down-left slant to (135,120) + shoulder + rightward 横 to (200,118) + LONG bowed 撇 Bezier to (70,250). Then add a SECOND terminal 撇 body-crossing.

---

## p3_char_0018_乜   (batch B3, retry_n=0, initial_batch: B3)

**Diagnosis**: 乜 = 横 + 竖弯钩. Sibling risk with 也 (adds a 竖 middle) and 巴. Attempt likely renders as 也 or ambiguous.

**Fix**: 2 strokes only. Top 横 medium. 竖弯钩 body = 竖 dropping through horizontal midpoint + arc rightward + hook up-left. NO middle 竖 (that would be 也).

---

## p3_char_0021_几   (batch B3, retry_n=1, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p3_char_0021_几__retry_1/`.
CURATOR-BLIND-VERDICT: this retry looks correct — left 撇 curves
down-left, right 横折弯钩 present with sweeping arc and terminal
hook. Human labeled FAIL — possibly because the hook is a subtle
nub rather than a decisive flick. CANDIDATE DISAGREEMENT: signature
form_catalog "撇 + 竖弯钩 as leg-pair under a lid" seems satisfied.
Fix (if pressed): make the terminal hook longer (~30 px) and more
angled (-115°).

**Diagnosis (original B3)**: 几 = 撇 + 横折弯钩. Bracket-family. Right side rendered without the sweeping hook.

**Fix**: 2 strokes. Left 撇 short curved from top-middle to lower-left. Right 横折弯钩 (KEY PRIMITIVE) — short 横 top + shoulder + 竖 dropping + tangent arc + rightward run + hook up-left. Silhouette open at bottom.

---

## p3_char_0023_九   (batch B3, retry_n=1, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p3_char_0023_九__retry_1/`.
Retry reads as 勺/勹 (wrap-bracket). The 撇 is too short and didn't
cross THROUGH the 横折弯钩's top 横 — 九's signature is the 撇
crossing above the top of the enclose. Fix: cross-ref form_catalog
"撇 as body-crossing diagonal" AND new "勹 vs 九" distinction (九
has the 撇 crossing through, 勹 has the 撇 as top-flick outside).
撇 must start ABOVE the 横 line by 20+ px.

**Diagnosis (original B3)**: 九 = 撇 + 横折弯钩. Same failure as 几 — the terminal sweeping-hook underscaled.

**Fix**: Similar to 几 fix; the 撇 is shorter and higher; the 横折弯钩 dominates and sweeps wider (~200 px x-extent).

---

## p3_char_0029_入   (batch B3 — GRADUATED B4)

**GRADUATED B4** — retry_1 PASSed and removed from active errata. Fix
applied: v7.1 HARD RULE "sibling-bit override" cited; drawer respected
the 捺-overhangs-撇 signature (top of 捺 well above and left of 撇's
top) with a thick terminal 捺 foot. First direct empirical validation
that the HARD RULE breaks the recurring 入→人 collapse.

---

## p3_char_0033_刀   (batch B3, retry_n=1, retry FAILED B4)

**B4 retry FAIL note**: retry at `attempts/p3_char_0033_刀__retry_1/`.
CURATOR-BLIND-VERDICT: this retry looks correct — 横折钩 body present
with visible top hook flick, 撇 crosses ABOVE the top 横 line by
20+ px. Human labeled FAIL — possibly reads too much like 力 due to
the crossing-撇 mimicking a 力-inside. CANDIDATE DISAGREEMENT: the
form_catalog "body-crossing diagonal" fix was applied and works.
Fix (if pressed): shorten the 撇 crossing so it doesn't dominate the
enclose (~120 px, not full-canvas).

**Diagnosis (original B3, recurring)**: 刀 = 横折钩 + body-crossing 撇 (same as 力 but no 力-hook body). Recurring crossing-visibility failure across bootstrap/B1/B2/B3.

**Fix**: cross-ref form_catalog "撇 as body-crossing diagonal" — 撇 start ABOVE the 横 (y≈55, 横 at y≈85), cross through at x≈140. Then the top of the 撇 must poke ABOVE the 横 line by 20+ px.

---

## p3_char_0042_丬   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0042_丬/01_丬.png`

**Diagnosis**: rendered as two floating diagonal ticks plus a straight
right-side 竖 — same bracket-non-touching failure as the p2 version.
点 and 提 sit LEFT of the 竖 without physically touching it. Reads
as 冫 with a 丨.

**Fix**: 点 top at (100,90) with tip touching 竖's LEFT edge; 提 middle
at (90,155) rising up-right with TIP AT 竖's x-coord. Cross-ref
form_catalog "点" entries + "竖 as through-going axis".

---

## p3_char_0043_个   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0043_个/01_个.png`

**Diagnosis**: 人-lid rendered but both legs came out as thin taper
撇 (no thick 捺 foot). Reads as 亇 or two-撇 + 竖 hybrid. Signature
bit for 个: RIGHT leg must be a proper 捺 with thin→thick taper and
broad terminal foot, matching 人.

**Fix**: cross-ref form_catalog "捺 as right-leg of two-stroke apex"
+ new sibling-pair "个 vs 亇" row. Right leg thin at top, thick
foot at bottom-right. Central 竖 hangs from apex.

---

## p3_char_0044_丸   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0044_丸/01_丸.png`

**Diagnosis**: rendered as 内-like (crossing 撇 forming an X inside
a bracket). But 丸 = 九 + 丶. Missing the interior 丶 and the 九's
横折弯钩 is not the outer enclose.

**Fix**: build up 九 first (cross-ref new sibling-pair 丸 vs 九):
撇 + 横折弯钩 with terminal up-left hook. Then add a single 丶 dot
INSIDE the enclose at ~(180, 140).

---

## p3_char_0046_久   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0046_久/01_久.png`

**Diagnosis**: reads as 夂 — only 撇 + 捺 with no middle 横撇 tick.
久's signature is the middle horizontal-tick separating the top-撇
from the body-捺.

**Fix**: 4 strokes — top 撇 short + middle 横撇 (horizontal tick with
shoulder) crossing the 撇's tip + long 撇 body + terminal 捺 with
thick foot. Compact "each" silhouette per form_catalog "夂" adjacent
template.

---

## p3_char_0047_也   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0047_也/01_也.png`

**Diagnosis**: cluttered silhouette. Bracket topology is scrambled
and the terminal 竖弯钩 hook flicks DOWN as an arrow-head instead
of UP-and-left.

**Fix**: 3 strokes — top 横折钩 (short 横 + shoulder + straight 竖
+ hook up-left) + central 竖 dropping through the horizontal +
bottom 竖弯钩 sweeping right and hooking UP-and-left. Cross-ref
drawer_memory "draw the flick".

---

## p3_char_0049_子   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0049_子/01_子.png`

**Diagnosis**: top 横撇 rendered as small right-angle tick rather than
a sweeping 横 + shoulder + down-left 撇. Middle 一 present, body 竖钩
present. Reads borderline — arguably 孑 due to short top-撇.

**Fix**: top 横撇 must have the 撇 arm sweep down-left decisively
(~60 px, angle ~55°). Middle 一 must cross the 竖钩 through the middle,
not float above.

---

## p3_char_0056_亾   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0056_亾/01_亾.png`

**Diagnosis**: silhouette off — appears as 亠 lid + separate 人 body,
but 亾 = 亡 + 人 inside. Drawer split the composition wrong.

**Fix**: build 亡 outer (cross-ref new form_catalog "亡 as 亠 + L
body") and place a small 人 INSIDE the L's opening (upper-right).

---

## p3_char_0059_么   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0059_么/01_么.png`

**Diagnosis**: reads as 久 (only 3 diagonal strokes visible). Missing
the 撇折 loop that defines 么.

**Fix**: 3 strokes — top 撇 short + 撇折 middle (short 撇 + shoulder
+ short 横 rightward, forming a small loop) + bottom 点 teardrop.
Cross-ref drawer_memory "撇折 family".

---

## p3_char_0060_卂   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0060_卂/01_卂.png`

**Diagnosis**: reads as 刁 or 司 sibling. Missing the central
cross-stroke that distinguishes 卂 from 刁.

**Fix**: 3 strokes — top 横折钩 (wide enclose) + internal 一 (crossing
horizontally through the middle) + central 竖 dropping through.
Compact enclosed silhouette.

---

## p3_char_0061_与   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0061_与/01_与.png`

**Diagnosis**: silhouette off — extraneous top dot, bottom-right hook
missing. Reads as scrambled 与-fragment.

**Fix**: 3 strokes — top 一 (~140 px) + central 横折钩 shape (short
一 + shoulder + 竖 down + terminal hook up-left) + bottom 一 base
that runs THROUGH the hook's base. NO top dot.

---

## p3_char_0065_及   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0065_及/01_及.png`

**Diagnosis**: reads as R with tail. The 乃-style zigzag body is
overcompressed and the terminal 捺 attaches as arrowhead rather
than sweeping foot.

**Fix**: 及 = 乃-body + 捺. Build 乃 per drawer_memory 横折折撇
mastery entry (tall zigzag with LONG bowed 撇), then add a 捺
sweeping down-and-right from the middle-shoulder to a broad
lower-right foot. Cross-ref form_catalog "捺 as terminal splay".

---

## p3_char_0068_纟   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0068_纟/01_纟.png`

**Diagnosis**: two 撇折 loops rendered as open chevrons (no fold-back),
bottom 提 present but detached. Reads ambiguous.

**Fix**: each 撇折 must be a SHORT 撇 + shoulder + SHORT 横 rightward
(a closed corner, not a chevron). Stack two at ~(140,80) and (140,145).
Bottom 提 rising up-right from ~(120,215) to (170,200).

---

## p3_char_0069_干   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0069_干/01_干.png`

**Diagnosis**: CURATOR-BLIND-VERDICT this is close to PASS —
top 横 shorter, bottom 横 longer, through-竖 with protrusion below.
Human labeled FAIL, possibly because the strokes are too geometric/
clean (reads as machine-drawn "十" hybrid). CANDIDATE DISAGREEMENT.

**Fix**: add slight 顿 dabs at 横 endpoints; slight up-tilt on both
横; give 竖 a small terminal press. Signature bit (top-shorter) IS
present.

---

## p3_char_0072_夊   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0072_夊/01_夊.png`

**Diagnosis**: identical failure to the p2 version — reads as 夂,
missing the extra top-left short 撇 that gives 夊 its 4-stroke
signature.

**Fix**: enforce 4-stroke count. Cross-ref p2_radical_084_夊 B4 note.

---

## p3_char_0073_飞   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0073_飞/01_飞.png`

**Diagnosis**: hook flicks DOWNWARD (arrowhead style), inside dot
present but tiny. Same recurring failure mode as p2 version.

**Fix**: cross-ref p2_radical_047_飞 B4 note and drawer_memory
"横折弯钩" KEY PRIMITIVE — terminal hook flicks UP-and-LEFT (~ -115°).

---

## p3_char_0074_孑   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0074_孑/01_孑.png`

**Diagnosis**: horizontal tick pointing to LEFT (wrong direction).
孑's signature is a LEFTWARD short tick, but attempt drew it as a
detached diagonal + extra spurious mark.

**Fix**: cross-ref new sibling-pair "孑 vs 孓 vs 子" — 孑 has a
SHORT 横 tick pointing LEFT of the 竖钩 (not a diagonal, not
detached).

---

## p3_char_0076_孓   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0076_孓/01_孓.png`

**Diagnosis**: reads as 子 — full-width 一 crossing the 竖钩. 孓's
signature is a short RIGHTWARD tick, not a full 一.

**Fix**: cross-ref new sibling-pair "孑 vs 孓 vs 子". Middle horizontal
must be a SHORT tick to the RIGHT of the 竖钩 (~40 px), not a
wall-to-wall 一.

---

## p3_char_0077_习   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0077_习/01_习.png`

**Diagnosis**: bracket topology present but 横折钩 lacks terminal
up-left hook flick, and interior has two 撇 instead of a single
compact 冫-style element.

**Fix**: 3 strokes — top 横折钩 (enclose) with UP-LEFT terminal
hook + interior 冫-style short 撇 + 提 pair. Wide-flat aspect.

---

## p3_char_0079_已   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0079_已/01_已.png`

**Diagnosis**: box structure closed too neatly — the bottom 竖弯钩
tail doesn't sweep outward past the top-right corner. Middle 横
touches left wall (correct for 已 per sibling table), but the base
doesn't open.

**Fix**: bottom 竖弯钩 must arc rightward AND its tip must extend
PAST the x-coord of the top-right corner by 20+ px. Cross-ref
form_catalog sibling-pair 己/已/巳 row.

---

## p3_char_0081_女   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0081_女/01_女.png`

**Diagnosis**: three crossing diagonals only — missing the 撇点 loop
that defines 女's top-left. Reads as scrambled X-shape.

**Fix**: 3 strokes — 撇点 (a 撇 that folds back into a 点 at the tip,
forming a small loop) upper-body + long 撇 body-cross + long 一
horizontal base crossing the 撇. Cross-ref form_catalog "撇" and
future "撇点 as loop" entry (candidate).

---

## p3_char_0082_尢   (batch B4, retry_n=0, initial_batch: B4)

**Attempt file**: `attempts/p3_char_0082_尢/01_尢.png`

**Diagnosis**: reads as 九 — missing the top 一 lid that distinguishes
尢 from 九. Only 撇 + 竖弯钩 visible.

**Fix**: cross-ref new sibling-pair "尢 vs 九" — 尢 has a top 一
lid (3 strokes total), 九 has no lid (2 strokes). Add wide 一 at
y≈70 crossing both legs.
