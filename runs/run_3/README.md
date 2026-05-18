# DC-ACE run — pristine scaffold

This is one run of the DC-ACE emergent-memory experiment. Created by
`new_run.sh` from the project root.

## Roles

| Role     | Played by         | Owns (writes)                              | Reads                                                          |
|----------|-------------------|--------------------------------------------|----------------------------------------------------------------|
| Teacher  | main thread       | `teaching_plan.md`, `teaching_log.md`, `task_briefs/`, `ground_truths/` | `cycle_summary.md`, `drawer_memory.md`, `cycle_state.json` |
| Drawer   | **fresh subagent**| `attempts/cycle_<N>/`                      | `drawer_memory.md`, `task_briefs/cycle_<N>.md` ONLY            |
| Judge    | `tools/judge.py`  | `judge_results/cycle_<N>.json`             | `attempts/`, `ground_truths/`, `task_briefs/`                  |
| Curator  | main thread       | `drawer_memory.md`, `cycle_summary.md`, `dashboard.md` | `judge_results/cycle_<N>.json`, `attempts/cycle_<N>/`, `task_briefs/cycle_<N>.md`, `ground_truths/cycle_<N>/` |

The Drawer is **dispatched to a fresh Agent** each cycle so it cannot
inherit context (and thus answer-key parameters) from the orchestrator.

## Activating this run

Edit `active_run.txt` at the project root to point here:

```
echo "runs/<this_run_name>" > ../active_run.txt
```

Then `/loop 10m /cycle` in Claude Code, or `/cycle` for a single cycle.

## Pause / resume

- Pause: `./stop_loop.sh` (creates `.stop`)
- Resume: `./start_loop.sh` (removes `.stop`)
- Fully halt: press Esc on the `/loop` in Claude Code.

## Pushing to GitHub

This run is its own git repo. Push it separately:

```
git remote add origin git@github.com:<you>/<repo-name>.git
git push -u origin main
```

Once `origin` is configured, `/cycle` auto-pushes after each cycle.
