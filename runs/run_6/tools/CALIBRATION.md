# Calibration (32 PASS, 37 FAIL incl NEAR-as-FAIL)

## Best deterministic config
`brush_radius=14, recall_threshold=0.15, precision_threshold=0.3, trace_min=0.3`

- Agreement: 59/69 (85.5%)
- Confusion: TP=26 FP=4 TN=33 FN=6
- F1: 0.839

## LLM panel comparison
- Panel verdicts available: 20/69
- Panel agreement: 15/20 (75.0%)
- Deterministic on same subset: 18/20 (90.0%)

## Runtime
- Deterministic: ~91ms/cycle
- LLM panel: ~10s wall + ~66k tokens/cycle
