# Research Observations Log

Notable, human-flagged, cross-batch phenomena worth citing in the paper.
Format: newest at top. Each entry names the observation, evidence, and its
significance for the memory-effect / AI-for-science framing.

---

## Obs-01 — The G1 "print-quality solo-win" phenomenon (2026-08-04, updated 2026-08-05)

### Claim

The control group **G1 (no memory, no MMH, no bank, no retries, no
curator)** intermittently produces the **single cleanest A-quality
attempt in the batch**, on items where every memory-equipped group
fails or scores C. The G1 rendering is visually described as
"printed-looking" — clean, symmetric, structurally correct — and
notably *different* from the MakeMeAHanzi GT PNG, i.e. it is not a
copy of the reference but an independent well-formed rendering.

### Evidence — all G1 A verdicts through B13

| Batch | Item | G1 | G2 | G3 | G4 | G5 |
|---|---|---|---|---|---|---|
| B10 | 佧 | A | A | PASS | A | — |
| B11 | 侉 | A | FAIL | FAIL | FAIL | — |
| B12 | 俎 | A | C | C | PASS | A |
| B13 | 俜 | A | FAIL | FAIL | FAIL | FAIL |
| B13 | 畟 | A | FAIL | C | FAIL | FAIL |
| B13 | 热 | A | FAIL | FAIL | C | FAIL |

- **4/6 are solo wins** (all memory-equipped groups scored FAIL or C on
  the same item).
- **1/6 co-win with G4 only** (佧 — but G3 got only PASS, not A).
- **1/6 co-win with G4 + G5** (俎).
- **All 6 items are late-curriculum** (positions 354, 416, 482, 496,
  510, 529 — none earlier than pos 354). Suggests the phenomenon
  emerges once items get compositionally complex enough that
  memory-directed drawers commit to a specific decomposition and lose
  the ability to produce a clean naive rendering.

### Why this matters for the paper

Three angles:

1. **Memory as *constraint*, not just aid.** The G4/G5 drawers arrive
   with rich reasoning scaffolding (bank primitives, memory files,
   MMH endpoint injection). That scaffolding successfully raises PASS
   rate on the whole, but it also steers the drawer down a specific
   compositional path. On items where the "obvious" naive path is
   actually the correct one, memory pulls the drawer away from it.
   G1, with no such steering, occasionally lands the naive-correct
   rendering cleanly.

2. **A-quality has two roads.** The A rate story so far has been
   framed as "G4's format enables calligraphic modulation → A." That
   story is intact for the modal A verdict, but the G1 solo-wins
   demonstrate a **second, independent road to A**: cold-attempt
   compositional serendipity. The paper should distinguish these two
   as separate mechanisms rather than treating A as a single quality
   bit.

3. **Warning against uncritical "more memory = better".** In some
   framings of AI-for-science, richer memory is assumed monotone-
   beneficial. G1's solo-wins are a small but recurring
   counter-example: on the subset of items where naive rendering is
   optimal, adding memory strictly *hurts*. In an ablation table this
   shows up as G1 outperforming every memory-equipped group on those
   items.

### Not to be over-interpreted

- G1's cumulative pass rate (~33%) remains meaningfully below G4's
  (~48%). The solo-win phenomenon is real but rare (~1% of items).
- The verdict is human blind-judgment, so we can't rule out that
  G1's cleanness partly reflects the panel's tolerance for
  simpler renderings on hard items. Would need a controlled panel
  study to fully separate.
- The GT PNG itself is a thin-line MMH-median render (not calligraphic).
  G1 outputs described as "printed-looking" may be scoring high in
  part because they visually resemble what the panel expects when
  the GT is skeletal.

### Concrete items to inspect (for figure-panel candidates)

Recommended for a paper figure showing side-by-side attempts of the
same item across the 4-5 groups:

- **B13 俜 (idx 496)** — 5-way comparison, only G1 A. Compositionally
  simple 亻+甹 that memory-equipped groups over-engineered.
- **B13 畟 (idx 510)** — user-flagged as "print-quality"; G1 A, G3 C,
  everyone else FAIL.
- **B13 热 (idx 529)** — user-flagged as "print-quality"; G1 A, G4 C
  (best of the memory groups), others FAIL. The 灬 bottom is likely
  the failure zone for the memory groups.
- **B11 侉 (idx 416)** — pure solo win, all memory groups FAIL.

### Recording context

Flagged by user during B13 review after noticing "每一轮都有一个或两个
[G1 A that] 非常完美，像打印出来的一样... 最好的最标准的一定是 G1
这个". Prior batches (B10 佧, B11 侉, B12 俎, then B13's three)
form a consistent cross-batch pattern, not a one-off.

---
