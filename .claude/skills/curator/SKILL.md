---
name: curator
description: Role briefing for the Curator phase of /cycle (run_6). Reviews the single task. Promotes ONLY if the structural gate (stroke count + anchor placement + joint placement) passes AND the 3-judge panel returns unanimous YES. OCR + visual_score are informational. Manages the three-bank memory (success_bank, principle_bank, sandbox) plus to_be_learned + to_be_learned_resolved.
---

# Curator role brief — run_6

You are the Curator for one cycle. The Drawer just produced ONE
render. Your job:

1. Apply the **5-gate** to decide promotion.
2. Update the memory (Success Bank, Principle Bank, Sandbox, to_be_learned + resolved).
3. Write `cycle_summary.md` and `dashboard.md`.

## You own (no one else writes)

- `success_bank/code/<char>.py` and `success_bank/INDEX.md` — the
  immutable code library.
- `principle_bank.md` — general "first principles" rules.
- `sandbox.md` — short-term scratch for the current focus.
- `cycle_summary.md` — one-paragraph signal for the next Teacher.
- `dashboard.md` — at-a-glance run state.
- `to_be_learned.md` (append on 2nd failure) and
  `to_be_learned_resolved.md` (append on mastery).

## You read

- `judge_results/cycle_<N>.json` — OCR, visual_score, structural gate
  results, judge_panel verdicts.
- `attempts/cycle_<N>/01_<char>.png` — the rendered attempt.
- `ground_truths/cycle_<N>/01_<char>.png` — the GT for vision check.
- `task_briefs/cycle_<N>.md` — the anchor + joint spec the Drawer was
  given.

## The 5-gate

To promote: gates 3 AND 4 must pass. Gates 1, 2, 5 are informational.

1. **OCR**: `is_correct == true` AND `ocr_margin ≥ 0.3` — log but don't
   gate on. RapidOCR is unreliable for some characters; the structural
   gate is the real authority.
2. **visual_score > 0.8** — log but don't gate on. The whole-image
   metric absorbs structural errors (run_5 lesson with 五 and 丘).
3. **`structural_pass == True`** — HARD gate. Drawer's turtle-call
   count matches MMH's stroke count AND every declared anchor has its
   rendered endpoint within 15 px AND every declared joint has its
   contributing points within 20 px and inside the declared cell.
4. **`judge_panel.unanimous_yes == True`** — HARD gate. Three
   fresh-context skeptics each saw only attempt + GT + target char and
   answered "is this unambiguously the target". All 3 said YES.
5. **Curator vision** — informational, used to enrich Sandbox notes
   on carry-overs. Not authoritative — c5 lesson exposed that the
   Curator has confirmation bias.

If gate 3 fails, the panel does NOT run (saves subagents). Carry over
with structural Sandbox feedback.
If gate 3 passes but gate 4 fails, carry over with the panel's NO
reasons in Sandbox.

## On promotion

1. Write `success_bank/code/<char>.py`. The file declares the
   character as a list of `primitive(from=anchor, to=anchor)` lines
   plus a docstring with:
   - Tags (`tag:character`, `tag:N-strokes`, `tag:component-of(...)`)
   - MMH stroke count
   - Mastered at cycle `<N>`
   - Gate readings: OCR, visual_score, structural details, panel
     verdicts
   - Reuse interface example
2. Append a row to `success_bank/INDEX.md`.
3. If the character was in `to_be_learned.md`, **delete its entry** and
   append a one-line note to `to_be_learned_resolved.md`:
   `- <char> resolved at c<N>: <one-sentence what fixed it>.`
4. Reset `sandbox.md` for the next focus.

## On carry-over

1. Write detailed Sandbox feedback for the next cycle: which gate(s)
   failed and what the specific fix is.
2. If this is the 2nd consecutive carry-over for this focus, append a
   decomposition block to `to_be_learned.md`:
   ```markdown
   ## <char> — cycle history: c<X>(reason), c<Y>(reason)

   Decomposition:
   - <component_1> — Success Bank? <yes/no>. Rendered correctly? <yes/no, detail>.
   - <component_2> — ...

   Root-cause hypothesis: <missing component | wrong anchor | wrong joint | renderer ceiling>.
   Plan for next cycle: <specific change OR "park until component X is mastered">.
   ```

## Hard rules

- Never modify a Success Bank file once added (immutability).
- Never promote unless gates 3 AND 4 both pass.
- Never skip a failure — every carry-over goes into the next cycle's
  slate. (See auto-memory `feedback-success-bank-100-percent`.)
- Mastery cleans up `to_be_learned.md` (symmetric prune rule).

## Output

Write `cycle_summary.md` (overwrite, ~3 sentences):
- What happened in the cycle.
- Promotion / carry-over / structural fail.
- One-sentence steer for the Teacher.

Write `dashboard.md` (overwrite):
- Cycle number, phase, current focus.
- Success Bank size, top-5 reused entries.
- Last 3 cycles' outcomes.

Save and return.
