"""judge_blind.py — batch human judgment UI for exp_context_effect.

Reads a batch manifest, presents each attempt one at a time. Human presses:
  a = A (perfect)   p = PASS   c = C (close)   f = FAIL
  s = SKIP   b = BACK   q = QUIT (auto-save)

Four-level verdict rubric (v10 added A, v12 added C):
  A    — "absolutely perfect" — calligraphic reference quality;
         structure, proportion, and brush feel all correct.
  PASS — correct + recognizable; a fluent reader identifies it and
         nothing structurally wrong; may still be mechanical.
  C    — CLOSE but not exact / minor error. Counts as FAIL for
         success rate. Preserved separately so curators can
         distinguish "close miss" (one stroke off / one component
         mis-positioned) from "total wreck". Drawers get graduated
         feedback via retry-trajectory annotations.
  FAIL — not recognizable or structurally wrong.

Downstream analytics:
  - Success rate = (A + PASS) / total. A counts as success.
  - Failure rate = (C + FAIL) / total. C counts as failure.
  - A count is reported separately (calligraphic-quality signal).
  - C count is reported separately (near-miss signal for
    curator retry prioritization).

Blinding: attempts within each item are shuffled before display so the
human cannot infer which group produced which attempt. The true group is
recorded in the label file (for post-hoc analysis) but never shown in the UI.

Display rules:
  - Phase "stroke": show target LABEL + text DESCRIPTION only.
    No target PNG (strokes have no GT). AI's attempt PNG below.
  - Phase "radical" and "character": show target PNG (GT) alongside
    attempt PNG. Radicals gained MMH GTs in v6 (135/137 available).

Labels persist to <batch_dir>/labels.json after every keypress.
Resumable — reopens on the first unjudged attempt.

Usage:
    python3 judge_blind.py --batch judgments/manifest_batch_1.json
"""
import argparse
import json
import os
import random
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk


def load_labels(labels_path):
    if os.path.exists(labels_path):
        return json.load(open(labels_path, "r", encoding="utf-8"))
    return {}


def save_labels(labels, labels_path):
    with open(labels_path, "w", encoding="utf-8") as f:
        json.dump(labels, f, ensure_ascii=False, indent=2)


def flatten_manifest(manifest, seed=42):
    """Flatten the batch to a list of (item, attempt) records with attempts
    shuffled within each item for blinding."""
    rng = random.Random(seed)
    flat = []
    for item in manifest["items"]:
        attempts = list(item["attempts"])
        rng.shuffle(attempts)
        for shown_idx, att in enumerate(attempts):
            flat.append({
                "item_id": item["id"],
                "shown_position": shown_idx,
                "actual_group": att["group"],
                "attempt_path": att["path"],
                "target_label": item["target_label"],
                "target_description": item.get("target_description") or "",
                "target_png": item.get("target_png"),
                "phase": item["phase"],
            })
    return flat


class JudgeApp:
    def __init__(self, flat, labels_path, batch_dir):
        self.flat = flat
        self.labels_path = labels_path
        self.batch_dir = batch_dir
        self.labels = load_labels(labels_path)
        self.idx = self._first_unjudged()

        self.root = tk.Tk()
        self.root.title("Judge — exp_context_effect (blind)")
        self.root.geometry("780x680")
        self.root.bind("<Key>", self.on_key)
        self._build_ui()
        self.show_current()

    def _key(self, item):
        return f"{item['item_id']}__att{item['shown_position']}"

    def _first_unjudged(self):
        for i, item in enumerate(self.flat):
            if self._key(item) not in self.labels:
                return i
        return len(self.flat)

    def _build_ui(self):
        # header: target label
        self.header = ttk.Label(self.root, text="", font=("Helvetica", 26, "bold"))
        self.header.pack(pady=(12, 4))

        # description (for strokes/radicals)
        self.desc = ttk.Label(self.root, text="", font=("Helvetica", 14),
                              wraplength=720, justify="center")
        self.desc.pack(pady=(0, 8))

        # body: target + attempt PNGs side by side
        self.body = ttk.Frame(self.root)
        self.body.pack(pady=8)

        self.target_frame = ttk.LabelFrame(self.body, text="Target (GT)")
        self.target_frame.grid(row=0, column=0, padx=12, sticky="n")
        self.target_lbl = ttk.Label(self.target_frame,
                                    text="(no target image)",
                                    width=42, anchor="center", padding=10)
        self.target_lbl.pack()

        self.attempt_frame = ttk.LabelFrame(self.body, text="Attempt (AI)")
        self.attempt_frame.grid(row=0, column=1, padx=12, sticky="n")
        self.attempt_lbl = ttk.Label(self.attempt_frame,
                                     text="(no attempt image)",
                                     width=42, anchor="center", padding=10)
        self.attempt_lbl.pack()

        # status
        self.status = ttk.Label(self.root, text="", font=("Helvetica", 12))
        self.status.pack(pady=8)

        # help
        self.help = ttk.Label(self.root,
                              text="a = A (perfect)    p = PASS    c = C (close)    f = FAIL    s = SKIP    b = BACK    q = QUIT (auto-save)",
                              font=("Helvetica", 11))
        self.help.pack(pady=(0, 12))

    def _show_png(self, label_widget, path):
        try:
            img = Image.open(path)
            photo = ImageTk.PhotoImage(img)
            label_widget.image = photo  # anchor to prevent GC
            label_widget.config(image=photo, text="")
        except Exception as e:
            label_widget.config(image="", text=f"(cannot load {path}: {e})")

    def show_current(self):
        if self.idx >= len(self.flat):
            self.header.config(text="✓ All judged in this batch")
            self.desc.config(text="Press b to review/change previous labels, or q to quit.")
            self.target_lbl.config(image="", text="")
            self.attempt_lbl.config(image="", text="")
            self._refresh_status()
            return

        item = self.flat[self.idx]
        self.header.config(text=f"Target: {item['target_label']}")
        self.desc.config(text=item.get("target_description") or "")

        # target: for radicals and characters (Phase 2+ has GT); strokes have none
        if item["phase"] in ("radical", "character") and item.get("target_png") and os.path.exists(item["target_png"]):
            self._show_png(self.target_lbl, item["target_png"])
            self.target_frame.grid()
        else:
            # strokes (Phase 1) or missing GT: hide target frame, only label shown
            self.target_lbl.config(image="", text="(judge by label + description)")

        # attempt
        if item["attempt_path"] and os.path.exists(item["attempt_path"]):
            self._show_png(self.attempt_lbl, item["attempt_path"])
        else:
            self.attempt_lbl.config(image="", text=f"(missing: {item['attempt_path']})")

        self._refresh_status()

    def _refresh_status(self):
        judged = len(self.labels)
        total = len(self.flat)
        a_n = sum(1 for v in self.labels.values() if v.get("verdict") == "A")
        p_n = sum(1 for v in self.labels.values() if v.get("verdict") == "PASS")
        c_n = sum(1 for v in self.labels.values() if v.get("verdict") == "C")
        f_n = sum(1 for v in self.labels.values() if v.get("verdict") == "FAIL")
        s_n = sum(1 for v in self.labels.values() if v.get("verdict") == "SKIP")
        pos_txt = f"{self.idx + 1}/{total}" if self.idx < total else f"{total}/{total}"
        self.status.config(text=f"[Attempt {pos_txt}   ·   Judged {judged}   ·   A {a_n} · PASS {p_n} · C {c_n} · FAIL {f_n} · SKIP {s_n}]")

    def _record(self, verdict):
        item = self.flat[self.idx]
        self.labels[self._key(item)] = {
            "verdict": verdict,
            "actual_group": item["actual_group"],
            "shown_position": item["shown_position"],
            "phase": item["phase"],
            "item_id": item["item_id"],
            "target_label": item["target_label"],
            "judged_at": datetime.now().isoformat(timespec="seconds"),
        }
        save_labels(self.labels, self.labels_path)

    def on_key(self, event):
        k = event.keysym.lower()
        if k == "q":
            self.root.destroy()
            return
        # `b` (back) always works, even after finishing — lets you review
        # or change a prior verdict.
        if k == "b":
            self.idx = max(0, self.idx - 1)
            self.show_current()
            return
        # Once we're past the end, only q and b are meaningful.
        if self.idx >= len(self.flat):
            return
        if k == "a":
            self._record("A"); self.idx += 1; self.show_current()
        elif k == "p":
            self._record("PASS"); self.idx += 1; self.show_current()
        elif k == "c":
            self._record("C"); self.idx += 1; self.show_current()
        elif k == "f":
            self._record("FAIL"); self.idx += 1; self.show_current()
        elif k == "s":
            self._record("SKIP"); self.idx += 1; self.show_current()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--batch", required=True, help="Path to manifest_batch_<N>.json")
    args = p.parse_args()

    manifest = json.load(open(args.batch, "r", encoding="utf-8"))
    batch_dir = os.path.dirname(os.path.abspath(args.batch))
    labels_path = os.path.join(batch_dir, "labels.json")

    flat = flatten_manifest(manifest, seed=manifest.get("shuffle_seed", 42))
    print(f"Batch: {len(manifest['items'])} items, {len(flat)} attempts total.")
    print(f"Labels will save to: {labels_path}")

    app = JudgeApp(flat, labels_path, batch_dir)
    app.root.mainloop()

    labels = load_labels(labels_path)
    a_n = sum(1 for v in labels.values() if v.get("verdict") == "A")
    p_n = sum(1 for v in labels.values() if v.get("verdict") == "PASS")
    c_n = sum(1 for v in labels.values() if v.get("verdict") == "C")
    f_n = sum(1 for v in labels.values() if v.get("verdict") == "FAIL")
    s_n = sum(1 for v in labels.values() if v.get("verdict") == "SKIP")
    print(f"Done. A {a_n} / PASS {p_n} / C {c_n} / FAIL {f_n} / SKIP {s_n}, total judged {a_n+p_n+c_n+f_n+s_n}/{len(flat)}")


if __name__ == "__main__":
    main()
