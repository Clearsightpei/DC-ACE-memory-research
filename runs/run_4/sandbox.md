# Sandbox (Part C of memory)

Curator-owned, **short-term per-task**. Reset after the current
task's character is mastered (and findings are promoted to Principle
Bank or Success Bank).

This file is where the Curator's diagnoses live during active
iteration on a SINGLE focus character. It is the place to be
specific: "the 人 inside 天 is too small by ~30 px; try
`scale=1.2`". When that fix works, the Curator pulls a *general*
form into the Principle Bank ("§2.X — re-scaling a nested component
inside a parent: scale 1.2 keeps proportions for top-stacked
compositions").

## Layout

```
## Current focus
- Character: <char>
- Cycle started: c<N>
- Prerequisites mastered: <list from Success Bank>
- Why this character: <Teacher's pedagogy note>

## Iteration log
### c<N> — skeleton phase
- Drawer's skeleton (link to attempts/cycle_<N>/generated_skel.py).
- GT-vs-skeleton diff (Curator, with GT access):
  - what's right
  - what's wrong, with pixel-level targets
- Decision: skeleton APPROVED / not approved; if not, the specific
  fix to try next.

### c<N> — brushwork phase
- (only present if skeleton approved this cycle)
- Drawer's brushed render result.
- Judge result: visual_score, OCR, rubric.
- Decision: mastered → promote to Success Bank; or fix and retry.

## Generalizable findings (drafts)
- Hunches the Curator wants to promote to Principle Bank once
  proven. These move OUT of sandbox once tested.
```

## Rules

- **One focus character at a time** (Teacher decides).
- **Reset on success**: when the focus character is mastered, the
  Curator:
  1. Adds the code to Success Bank with component tags.
  2. Regenerates `success_bank/visual/visual_index.png` with the
     new entry included.
  3. Promotes generalizable findings to Principle Bank.
  4. Overwrites this file with the next focus character's header.
- **Reset on abandonment**: if the Teacher decides the focus is too
  far from prerequisites, document the abandon reason, archive the
  sandbox content to `sandbox_archive/c<N>_<char>.md`, and start
  fresh.

---

## Current focus

(Not yet set — Teacher will write the first focus in c1.)
