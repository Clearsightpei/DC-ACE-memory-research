# Vendored MMH joint-detection modules

These three modules are vendored verbatim from `runs/run_6/tools/` so that
`tools/mmh_joints.py` is self-contained on this branch. The `runs/` tree
holding the exploratory phase lives on the `legacy` branch; without these
copies the structural-supervision tooling cited in the paper cannot run
from a clean checkout of `main`.

Source: `git show legacy:runs/run_6/tools/<file>.py`

They read MakeMeAHanzi's `graphics.txt`, which is NOT redistributed here
(Arphic Public License lineage). Obtain it upstream at commit 618dbab8 and
place it at `draw_character/graphics.txt`.
