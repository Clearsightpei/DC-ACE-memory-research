# run_3 — Postmortem

**Run:** run_3 — first run on the Teacher-as-tool-orchestrator design
with the Claude-vision calligraphy rubric as the primary stroke
signal, fresh-subagent Drawer with hard filesystem isolation, and the
multi-signal judge (Dice+Chamfer+proportion `visual_score` + RapidOCR
+ vision rubric). 25 cycles, Phase 1 → Phase 2, then frozen.

## Headline results

- **6/6 atomic strokes mastered** (cycle 1 cold start, rubric 9.5/10
  avg — directly validated the run_2 thesis that vision-rubric
  judging produces better brushwork than weak GT-matching).
- **37 Phase-2 characters mastered**: 一二三十人八又个不木工王中口子日习已月大入力火天了见小太巴几车夫公为女.
- **3 characters stuck after 8–16 attempts each**: 也 (16x), 寸 (9x),
  万 (9x). Each has a stable rubric (4–8/10, decent brushwork) but
  the silhouette persistently lands in adjacent OCR classes
  (也→卫/已/吧, 寸→十/于/小, 万→力/九/方).

## The core problems this run surfaced

**The text-only-brief Drawer hits a "composition precision wall."**
For structurally simple characters (37 of 40 attempted) the
brushed-primitive library + Curator-written compositional rules
generalize cleanly. For characters whose silhouette differs from an
OCR-neighbor by a few-pixel margin (also/寸/万), text prescriptions
of the form "撇 head at y > heng + 80" can't reliably push the render
across the boundary, even after a dozen iterations. The Curator can
see the GT and write specific prescriptions, but the channel between
"what the Curator sees" and "what the Drawer produces" loses the
sub-pixel fidelity needed for these cases.

**Memory accumulated as an error log, not as transferable skill.**
The `drawer_memory.md` grew across cycles to ~250 lines of
diagnostic prose describing what went wrong on past attempts and
what to try next. The Drawer reads this every cycle and tries to
parse the latest prescription out of a wall of historical
diagnoses. As the file grew, transfer became noisier, not clearer.
The "long file of errors" memory is a fundamentally wrong frame:
the space of possible errors is infinite, the space of correct
techniques is finite.

**Two failure modes can swap places under a single prompt change.**
c17 introduced "smooth Bézier" guidance and brushwork regressed to
hairline-thin strokes (OCR passed, rubric failed taper=0). c18
introduced width floors and the brushwork came back but silhouettes
shifted enough to fail OCR. The "composition" and "brushwork"
skills are intertwined in a single render pass; pushing one fixes
some characters and breaks others. There is no separation of
concerns in the current Drawer pipeline.

**OCR-pass without rubric-quality is not mastery.** c17 marked 3
"successes" (也/太/几) that the strict rubric correctly rejected
(taper=0 from hairline strokes). The "hard no-skip" rule was added
mid-run (between c11 and c12) and proved its worth — 大/入/火 had
been "retired as OCR-wall" through c11 and were mastered at 10/10
in c12–c14 once forced back into rotation. The rule held for c12+
but exposed that earlier mastery accounting was generous.

## Memory-mechanism findings

- Faithful transfer of techniques worked at the primitive level
  (atomic strokes c1→c2; composition primitives c3→c8). The
  brushed-Bézier-with-per-sample-pensize approach emerged in c1 and
  survived through c16 across many subagents.
- Reflection-validation arcs landed for ~30 cases: a Curator
  diagnosis in cycle N → carry-over in cycle N+1 → mastery. This is
  the memory loop working as designed.
- Five OCR-boundary failures (也/巴/寸/万/公/为) needed 4–16
  carry-over cycles each; 巴/公/为 eventually crossed; 也/寸/万 did
  not. The boundary cases are where the text-brief channel runs out
  of expressive power.

## Why it motivates the next run

These findings motivate **run_4** with a redesigned memory
architecture and four orthogonal mechanism upgrades:

1. **Three-bank memory** replacing the single `drawer_memory.md`:
   - **Success Bank** (Part A): exact code + NL description of past
     wins, indexed by character/component, with the exact parameters
     preserved (changing them is what causes disconnect).
   - **Principle Bank** (Part B): natural-language *positive*
     rules ("to shrink a 部首 to 1/x, …"), including a contrastive
     section ("X vs Y: distinguishing features"). Never error logs.
   - **Sandbox** (Part C): short-term per-task corrections, GT-vs-
     attempt diffs. On task success, the Curator promotes
     generalizable findings from sandbox into Principle Bank (or
     code into Success Bank); sandbox then resets.

2. **Visual anchor cards**: the Drawer is allowed to see its own
   past successful renders (not GT — past self-outputs) as a visual
   index, to ground the code+text Success Bank in what those
   blueprints actually produce.

3. **Skeleton → brushwork as two phases**: the Drawer first writes
   skeleton-only code (centerlines, uniform thin width). The Curator
   compares skeleton vs GT (GT *is* skeleton — graphics.txt has no
   brushwork) and gives composition feedback. Only after the
   skeleton is approved does the Drawer add brushwork. This
   decouples the two skills that c17/c18 showed are intertwined.

4. **Component-tagged Success Bank with query interface**: each
   entry tagged with the 偏旁/部首/笔画 it provides; the Teacher
   composes complex characters from existing components instead of
   from scratch (essential for Phase 3).

5. **Drawer self-preview** within a single cycle: max 2 internal
   iterations where the Drawer renders, views its own attempt via
   vision, self-critiques against the brief, refines, then commits.
   Catches brushwork regressions before the Curator has to.

6. **One-character-at-a-time focus**: the Teacher abandons 6-per-
   batch and focuses each cycle on ONE character (or stroke or
   部首). The Teacher must verify all prerequisites are mastered
   before introducing a character (e.g., 天 requires 二 + 人, each
   itself requiring atomic strokes).

run_3 is preserved unchanged. Its 25-cycle history is the
text-brief-only ceiling; run_4 measures whether the new
architecture pushes through the boundary cases that run_3 stuck on.
