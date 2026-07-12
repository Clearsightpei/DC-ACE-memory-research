# Orchestrator Guide — How to Run the Experiment

This document is the *runbook* for the main thread (Claude Code) that
drives the experiment. The infrastructure is in `tools/`. The
orchestration logic — dispatching 4 sub-agents in parallel per item,
waiting for human judgment, promoting/erratafying, snapshotting — is
performed by Claude Code turn-by-turn.

## Ingredients

- **State**: `state/teacher_state.json` (position, phase, batch count)
- **Curriculum**: `curriculum/{strokes_32.md, radicals.md, chars_1000.json}`
- **Group briefs**: `protocol/{shared_rules.md, G1..G4/rules.md}`
- **Group memory dirs**: `groups/G{1..4}_*/`
- **Batches**: `judgments/batch_<N>/manifest.json` + labels.json
- **Snapshots**: `snapshots/G{1..4}/snapshot_<pos>/`

## One turn = one "run N items" command

User says "run N items". Claude Code does:

### Phase A — dispatch

```python
from tools.teacher import Teacher, GROUPS
from tools.dispatcher import build_drawer_prompt
from tools.snapshot import take_snapshot

t = Teacher()
items_and_attempts = []

for _ in range(N):
    item = t.next_item()
    if item is None:
        break                          # curriculum done
    attempts = {}                      # {group: attempt_path}
    for g in GROUPS:
        prompt = build_drawer_prompt(g, item)
        # SPAWN AGENT with `prompt` — main thread does this in parallel
        # for all 4 groups (single tool_use with 4 concurrent Agent calls).
        # Each subagent's task: read its brief + memory, render, save PNG.
        attempts[g] = f"groups/{g}_.../attempts/{item['id']}/01_{item['character_or_shape']}.png"
    items_and_attempts.append((item, attempts))
    t.advance()

    if t.snapshot_due():
        take_snapshot(t.position)

    if t.should_scan_errata():
        # For each group: spawn Curator sub-agent to scan errata + pick retries.
        # Retry attempts join the batch below.
        pass

batch_dir = f"judgments/batch_{t.state.batches_created + 1:03d}"
manifest_path = t.build_batch_manifest(items_and_attempts, batch_dir)
t.save()
```

Emit to user:

> Dispatched N items. Batch manifest at `<batch_dir>/manifest.json`.
> Run `python3 tools/judge_blind.py --batch <path>` to judge.

### Phase B — after human judgment

User runs the judge tool, then reports "labels done". Claude Code does:

```python
import json
labels = json.load(open(f"{batch_dir}/labels.json"))
# For each attempt (keyed by item_id__attN):
#   - Look up actual_group and verdict
#   - Group PASS → spawn G<X>'s Curator to encode into memory
#   - Group FAIL → spawn G<X>'s Curator to add to errata + self-diagnose
```

### Phase C — snapshot check

Already handled in Phase A (`take_snapshot(pos)` after each `advance()`).

## Errata scan behavior (every 20 items)

When `t.should_scan_errata()` returns True after Phase A's dispatch loop:

- For each group with a non-empty errata:
  - Spawn Curator sub-agent with prompt: *"Read your current memory
    and your errata. Self-judge which items (if any) you can now
    solve. Return the list. Remember the penalty for over-retrying."*
  - Curator returns list of item_ids.
  - For each returned item_id, spawn Drawer to re-attempt. Save the
    attempt PNG. **These retry attempts join the current batch's
    manifest.** They are still judged blind.
- Every retry gets logged in `groups/G<X>/retry_log.jsonl`.

## Data files (auto-created)

- `state/teacher_state.json` — position, phase, batch_count
- `groups/G<X>/attempts/<item_id>/01_<char>.png`
- `groups/G<X>/attempts/<item_id>/generated.py`
- `groups/G<X>/errata.md` (per-group 错题集)
- `groups/G<X>/retry_log.jsonl`
- `groups/G<X>/success_bank/…` (G3/G4 only)
- `groups/G<X>/drawer_memory.md` (G2 only)
- `judgments/batch_<N>/manifest.json`
- `judgments/batch_<N>/labels.json` (human output)

## Debugging + inspection helpers

```bash
# Where are we in the curriculum?
python3 tools/teacher.py

# What snapshots exist?
python3 -c "from tools.snapshot import list_snapshots
for g in ['G1','G2','G3','G4']:
    print(g, list_snapshots(g))"

# Rebuild the curriculum after a seed update
python3 tools/build_curriculum.py

# Preview what prompt a Drawer would see
python3 tools/dispatcher.py
```

## Reset / start over

```bash
rm -rf state/ groups/*/attempts/ judgments/ snapshots/
for g in G1_no_memory G2_free_form G3_coords G4_grid; do
    mkdir -p groups/$g/attempts
done
```

## Ready to start? (infrastructure checklist)

- [x] `teacher.py` loads 1169 items
- [x] `dispatcher.py` builds valid Drawer prompts for all 4 groups
- [x] `snapshot.py` runs
- [x] `judge_blind.py` smoke-tested with test batch
- [x] `curriculum/chars_1000.json` generated with 47/53 common/rare mix
- [x] `protocol/` files present for all 4 groups + shared_rules.md
- [ ] GT PNGs for Phase 3 characters pre-rendered in bulk (`gt/phase3/`)
- [ ] Bulk GT renderer for Phase 3 (`tools/render_all_gt.py`) — trivial
      loop over `chars_1000.json` calling `make_gt_300.py`. TBD.
