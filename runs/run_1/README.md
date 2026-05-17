# DC-ACE Cycle Repo

Self-contained git repository that captures one full run of the DC-ACE
emergent-memory experiment. Every cycle commits separate Teacher,
Drawer, Judge, and Curator changes so the git log is the experimental
record.

## Roles

| Role     | Owns (writes)                              | Reads                                                          |
|----------|--------------------------------------------|----------------------------------------------------------------|
| Teacher  | `teaching_plan.md`, `teaching_log.md`, `task_briefs/`, `ground_truths/` | `cycle_summary.md`, `drawer_memory.md`, `cycle_state.json` |
| Drawer   | `attempts/cycle_<N>/`                      | `drawer_memory.md`, `task_briefs/cycle_<N>.md`, `ground_truths/cycle_<N>/` |
| Judge    | `judge_results/cycle_<N>.json`             | `attempts/`, `ground_truths/`, `task_briefs/`                  |
| Curator  | `drawer_memory.md`, `cycle_summary.md`, `dashboard.md` | `judge_results/cycle_<N>.json`, `attempts/cycle_<N>/`, `task_briefs/cycle_<N>.md` |

Single-writer rule prevents merge conflicts and keeps `git log -p
<file>` a clean record per role.

## Running

Open Claude Code in the project root (one level up). Then:

```
/loop 10m /cycle
```

That fires `/cycle` every 10 minutes. Each fire is one cycle (Teacher →
Drawer → Judge → Curator → 4 commits). To stop:

- **Pause** (cycles become no-ops, loop keeps firing): `./stop_loop.sh`
- **Resume**: `./start_loop.sh`
- **Fully halt the loop**: press Esc in the Claude Code session

## Running one cycle manually

Just type `/cycle` in Claude Code. Useful for debugging.

## What lives where

```
dc_ace_run/
├── tools/
│   ├── strokes.py            # vendored stroke functions (Teacher only)
│   ├── make_stroke_gt.py     # CLI: render one stroke as PNG
│   ├── make_char_gt.py       # CLI: render one character as PNG (uses ../draw_character/graphics.txt)
│   └── judge.py              # OpenCV + RapidOCR judge
├── ground_truths/cycle_<N>/  # PNGs the Teacher generated
├── task_briefs/cycle_<N>.md  # what the Teacher asked for
├── attempts/cycle_<N>/       # Drawer's code + rendered PNGs
├── judge_results/cycle_<N>.json
├── drawer_memory.md          # Curator-owned, free-form
├── teaching_plan.md          # Teacher-owned, evolves
├── teaching_log.md           # Teacher-owned, append-only
├── cycle_summary.md          # Curator → Teacher, overwritten each cycle
├── dashboard.md              # human-readable snapshot
└── cycle_state.json          # cycle counter + last batch
```

## Reading the experimental record

- **What memory has emerged?** `git log -p drawer_memory.md`
- **How has the Teacher's pedagogy evolved?** `git log -p teaching_plan.md`
- **Per-cycle summary:** `git log --oneline`
- **One specific cycle:** `git log --grep "cycle 12"`

## Pushing to GitHub

```
git remote add origin git@github.com:<you>/<repo>.git
git push -u origin main
```

Once `origin` is configured, `/cycle` will push automatically at the
end of each cycle.
