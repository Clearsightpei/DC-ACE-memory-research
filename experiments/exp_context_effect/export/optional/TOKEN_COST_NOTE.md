# Token and cost logs — status

Per-attempt token accounting was **not archived** during the experiment. The Anthropic Workflow tool reports `subagent_tokens` totals at workflow completion (visible in each workflow's completion notification), but per-attempt breakdowns were not persisted to durable storage.

**Aggregate token estimate** (from workflow completion notifications collected across the experiment):

- **G1-G4 main experiment (bootstrap through B13)**: ~60M drawer subagent tokens across ~2800 drawer dispatches + ~7M curator subagent tokens across ~50 curator dispatches. Rough total: **~70M subagent tokens** (main experiment).
- **G5 catch-up (14 batches)**: ~40M drawer subagent tokens across ~800 drawer dispatches + ~2M curator subagent tokens across ~13 curator dispatches. Rough total: **~42M subagent tokens** (G5 catch-up).
- **Grand total**: **~112M subagent tokens** across the entire experiment.

Cost estimate at Claude Opus 4.7 pricing (as of experiment window): approximately **USD $2,000-$3,000** at listed API prices, though the actual budget consumed depends on subscription/API-tier billing (which is not the API listed price for Claude Code SDK use).

**Retention gap acknowledged as a limitation**: per-attempt cost accounting would enable claims about "memory format X converges N% faster per dollar" that we cannot make from current data. Future replications should log per-attempt token usage.
