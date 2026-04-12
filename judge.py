"""DC-ACE Visual Judge

Evaluates AI-generated Chinese character PNGs against ground truth using:
  - OpenCV phase correlation → visual_score
  - RapidOCR (local ONNX, rec-only) → recognized_char + ocr_confidence
  - Python == comparison → is_correct
  - DeepSeek-OCR (both images) → coordinates of GT and AI strokes

Outputs per character:
    1. visual_score       — OpenCV phase correlation (0.0 to 1.0)
    2. recognized_char    — What RapidOCR reads from the AI image
    3. ocr_confidence     — RapidOCR recognition confidence (0.0 to 1.0)
    4. is_correct         — Boolean: Python comparison (recognized == target)
    5. gt_coordinates     — Stroke coordinates extracted from GT image
    6. ai_coordinates     — Stroke coordinates extracted from AI image

Usage:
    python judge.py \
        --mode 1 \
        --ai-png-dir AI_Generated_PNG_1/ \
        --gt-png-dir "PNG Ground Truth/Chinese_2/" \
        --dataset "PNG Ground Truth/Chinese_2/characters.json" \
        --generated-code generated_characters_1.py

Requirements:
    pip install opencv-python numpy ollama rapidocr
"""

import os
import re
import json
import argparse
import logging
from typing import Dict, List, Optional, Tuple

import cv2
import numpy as np
import ollama
from PIL import Image as PILImage
from rapidocr import RapidOCR

# Suppress noisy RapidOCR/onnxruntime logs
logging.getLogger("RapidOCR").setLevel(logging.WARNING)
logging.getLogger("rapidocr").setLevel(logging.WARNING)


# ─────────────────────────── File Matching ────────────────────────────────

def find_png_by_index(directory: str, index: int) -> Optional[str]:
    """Find a PNG in *directory* whose filename starts with the index prefix (e.g. '01_')."""
    prefix = f"{index:02d}_"
    for fname in sorted(os.listdir(directory)):
        if fname.startswith(prefix) and fname.lower().endswith(".png"):
            return os.path.join(directory, fname)
    return None


# ─────────────────────────── Code Extraction ──────────────────────────────

def extract_functions_from_file(filepath: str) -> Dict[int, str]:
    """Parse a generated_characters_N.py file and return {index: function_code}.

    Splits on '# ── Task NN' markers to isolate per-character code.
    """
    if not filepath or not os.path.exists(filepath):
        return {}

    with open(filepath, "r", encoding="utf-8") as fh:
        content = fh.read()

    functions: Dict[int, str] = {}
    # Split on task markers like: # ── Task 01 | 一 (yī) | ...
    parts = re.split(r"(# ── Task \d+.*)", content)

    for i, part in enumerate(parts):
        m = re.match(r"# ── Task (\d+)", part)
        if m and i + 1 < len(parts):
            idx = int(m.group(1))
            code_block = parts[i + 1].strip()
            if code_block:
                functions[idx] = code_block

    return functions


# ─────────────────────────── OpenCV Visual Score ──────────────────────────

def compute_visual_score(ai_path: str, gt_path: str) -> float:
    """Phase-correlation similarity between two images.

    Both images are loaded as grayscale.  The AI image is resized to match
    the GT dimensions.  cv2.phaseCorrelate returns a response value in
    roughly [0, 1] indicating how well the frequency domains align.
    """
    gt_img = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE)
    ai_img = cv2.imread(ai_path, cv2.IMREAD_GRAYSCALE)

    if gt_img is None or ai_img is None:
        return 0.0

    # Resize AI to match GT
    gt_h, gt_w = gt_img.shape[:2]
    ai_img = cv2.resize(ai_img, (gt_w, gt_h))

    # float32 required by phaseCorrelate
    gt_f = np.float32(gt_img)
    ai_f = np.float32(ai_img)

    _shift, response = cv2.phaseCorrelate(gt_f, ai_f)
    return max(0.0, min(1.0, response))


# ─────────────────────────── RapidOCR Recognition ────────────────────────

def _preprocess_for_ocr(image_path: str) -> np.ndarray:
    """Preprocess a character PNG for OCR recognition.

    Steps: load → crop to ink bounding box → thicken strokes via
    morphological dilation → pad to square → resize to 320×320.
    """
    img = PILImage.open(image_path).convert("RGB")
    arr = np.array(img)
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)

    # Threshold to find ink pixels
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    coords = np.argwhere(binary > 0)
    if len(coords) == 0:
        # No ink found — return a blank white image
        return np.ones((320, 320, 3), dtype=np.uint8) * 255

    # Crop to bounding box of ink with padding
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0)
    pad = 40
    y0, x0 = max(0, y0 - pad), max(0, x0 - pad)
    y1, x1 = min(arr.shape[0], y1 + pad), min(arr.shape[1], x1 + pad)
    cropped = arr[y0:y1, x0:x1]

    # Thicken strokes (turtle graphics produce thin lines)
    gray_crop = cv2.cvtColor(cropped, cv2.COLOR_RGB2GRAY)
    _, bin_crop = cv2.threshold(gray_crop, 200, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(bin_crop, kernel, iterations=2)
    result_img = np.ones_like(cropped) * 255
    result_img[dilated > 0] = [0, 0, 0]

    # Pad to square
    h, w = result_img.shape[:2]
    size = max(h, w)
    square = np.ones((size, size, 3), dtype=np.uint8) * 255
    dy, dx = (size - h) // 2, (size - w) // 2
    square[dy:dy + h, dx:dx + w] = result_img

    # Resize to 320×320
    sq_img = PILImage.fromarray(square).resize((320, 320), PILImage.LANCZOS)
    return np.array(sq_img)


def _read_image_bytes(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def recognize_character(
    ocr_engine: RapidOCR,
    image_path: str,
) -> Tuple[str, float]:
    """Recognize a single Chinese character from a PNG using RapidOCR.

    Preprocesses the image (crop, thicken, square, resize) then runs
    recognition-only mode (no text detection, no classification).

    Returns (recognized_char, confidence) where recognized_char is a
    single Chinese character or "", and confidence is 0.0–1.0.
    """
    try:
        preprocessed = _preprocess_for_ocr(image_path)
        result = ocr_engine(preprocessed, use_det=False, use_cls=False)

        if result is None or not hasattr(result, "txts") or not result.txts:
            return "", 0.0

        # Find the best result containing a Chinese character
        best_char, best_score = "", 0.0
        for txt, score in zip(result.txts, result.scores):
            chinese = re.findall(r'[\u4e00-\u9fff]', txt)
            if chinese and score > best_score:
                best_char = chinese[0]
                best_score = score

        return best_char, best_score

    except Exception as e:
        print(f"    [OCR] Error: {e}")
        return "", 0.0


# ─────────────────────────── DeepSeek Coordinate Extraction ──────────────

_COORD_OPTS = {
    "temperature": 0,
    "num_predict": 300,
}


def extract_coordinates(
    client: ollama.Client,
    image_path: str,
    label: str,
    model: str = "deepseek-ocr",
) -> Dict:
    """Extract stroke bounding-box coordinates from a single character image.

    Returns {"strokes": [{"x": .., "y": .., "w": .., "h": ..}, ...]}
    or an empty dict on failure.
    """
    try:
        img_data = _read_image_bytes(image_path)
        resp = client.chat(
            model=model,
            messages=[{
                "role": "user",
                "content": (
                    'Return the bounding box of each stroke as JSON. '
                    'Format: {"strokes":[{"x":0,"y":0,"w":0,"h":0}]}'
                ),
                "images": [img_data],
            }],
            options=_COORD_OPTS,
        )
        raw = resp["message"]["content"].strip()
        raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
        cleaned = re.sub(r"```(?:json)?\n?", "", raw)
        cleaned = re.sub(r"```$", "", cleaned).strip()
        return json.loads(cleaned)
    except (json.JSONDecodeError, Exception) as e:
        print(f"    [COORD-{label}] Error: {e}")
        return {}


# ─────────────────────────── Per-Character Judge ──────────────────────────

def judge_character(
    index: int,
    character: str,
    pinyin: str,
    ai_png_dir: str,
    gt_png_dir: str,
    ocr_engine: Optional[RapidOCR] = None,
    vision_client: Optional[ollama.Client] = None,
    vision_model: str = "deepseek-ocr",
    generated_code: str = "",
) -> Dict:
    """Evaluate one character:
      1. OpenCV phase correlation → visual_score
      2. RapidOCR (local, rec-only) → recognized_char + ocr_confidence
      3. Python == comparison → is_correct
      4. DeepSeek-OCR → coordinates for GT and AI images
    """

    ai_path = find_png_by_index(ai_png_dir, index)
    gt_path = find_png_by_index(gt_png_dir, index)

    result: Dict = {
        "index": index,
        "character": character,
        "pinyin": pinyin,
        "visual_score": 0.0,
        "recognized_char": "",
        "ocr_confidence": 0.0,
        "is_correct": False,
        "gt_coordinates": {},
        "ai_coordinates": {},
        "generated_code": generated_code,
        "final_score": 0.0,
    }

    if ai_path is None:
        result["error"] = f"AI PNG not found for index {index:02d}"
        print(f"  [{index:02d}] {character} ({pinyin}) — AI PNG not found")
        return result

    if gt_path is None:
        result["error"] = f"GT PNG not found for index {index:02d}"
        print(f"  [{index:02d}] {character} ({pinyin}) — GT PNG not found")
        return result

    result["ai_file"] = os.path.basename(ai_path)
    result["gt_file"] = os.path.basename(gt_path)

    # ── Phase 1: OpenCV phase correlation ─────────────────────────────
    visual_score = compute_visual_score(ai_path, gt_path)
    result["visual_score"] = round(visual_score, 4)

    # ── Phase 2: RapidOCR character recognition (local) ───────────────
    recognized = ""
    ocr_conf = 0.0
    if ocr_engine is not None:
        recognized, ocr_conf = recognize_character(ocr_engine, ai_path)
    result["recognized_char"] = recognized
    result["ocr_confidence"] = round(ocr_conf, 4)
    result["is_correct"] = (recognized == character)

    correct_val = 1.0 if result["is_correct"] else 0.0
    result["final_score"] = round(0.5 * visual_score + 0.5 * correct_val, 4)

    # ── Phase 3: Coordinate extraction for GT and AI ──────────────────
    if vision_client is not None:
        result["gt_coordinates"] = extract_coordinates(
            vision_client, gt_path, "GT", model=vision_model
        )
        result["ai_coordinates"] = extract_coordinates(
            vision_client, ai_path, "AI", model=vision_model
        )

    # ── Console output ────────────────────────────────────────────────
    print(
        f"  [{index:02d}] {character} ({pinyin})  "
        f"visual={result['visual_score']:.4f}  "
        f"ocr={recognized!r} ({ocr_conf:.2f})  "
        f"correct={result['is_correct']}  "
        f"final={result['final_score']:.4f}"
    )

    return result


# ─────────────────────────── Main ─────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="DC-ACE Visual Judge: evaluate AI character PNGs against ground truth",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
  python judge.py \\
      --mode 1 \\
      --ai-png-dir AI_Generated_PNG_1/ \\
      --gt-png-dir "PNG Ground Truth/Chinese_2/" \\
      --dataset "PNG Ground Truth/Chinese_2/characters.json" \\
      --generated-code generated_characters_1.py
""",
    )
    parser.add_argument("--mode", type=int, choices=[1, 2, 3], default=1,
                        help="Experiment mode (1=baseline, 2=failure, 3=success). Controls output filename.")
    parser.add_argument("--ai-png-dir", required=True,
                        help="Directory of AI-generated PNGs")
    parser.add_argument("--gt-png-dir", required=True,
                        help="Directory of ground truth PNGs")
    parser.add_argument("--dataset", required=True,
                        help="Path to characters.json (for char/pinyin/index metadata)")
    parser.add_argument("--generated-code", default=None,
                        help="Path to generated_characters_N.py (embeds code into results)")
    parser.add_argument("--output", default=None,
                        help="Output JSON path (default: judge_results_N.json based on --mode)")
    parser.add_argument("--ollama-host", default="http://100.120.168.33:11434",
                        help="Ollama server URL (default: http://100.120.168.33:11434)")
    parser.add_argument("--vision-model", default="deepseek-ocr",
                        help="Ollama vision model for OCR (default: deepseek-ocr)")
    parser.add_argument("--skip-ocr", action="store_true", default=False,
                        help="Skip character recognition (RapidOCR), use visual score only")
    parser.add_argument("--skip-coords", action="store_true", default=False,
                        help="Skip DeepSeek-OCR coordinate extraction")
    args = parser.parse_args()

    # Default output filename based on mode
    if args.output is None:
        args.output = f"judge_results_{args.mode}.json"

    # ── Initialize RapidOCR (local, fast) ─────────────────────────────
    ocr_engine: Optional[RapidOCR] = None
    if not args.skip_ocr:
        ocr_engine = RapidOCR()

    # ── Initialize Ollama client (for coordinate extraction only) ─────
    vision_client: Optional[ollama.Client] = None
    if not args.skip_coords:
        vision_client = ollama.Client(host=args.ollama_host)

    # ── Load generated code (for embedding into results) ─────────────
    code_map: Dict[int, str] = {}
    if args.generated_code:
        code_map = extract_functions_from_file(args.generated_code)

    # ── Load dataset ──────────────────────────────────────────────────
    with open(args.dataset, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    # Support both JSON formats:
    #   characters.json  → {"characters": [{index, character, pinyin, ...}]}
    #   chinese_strokes.json → [{id, prompt, params: {stroke, pinyin, meaning}}]
    if isinstance(data, list):
        characters: List[Dict] = []
        for i, entry in enumerate(data):
            p = entry.get("params", {})
            characters.append({
                "index":     i + 1,
                "character": p.get("stroke", ""),
                "pinyin":    p.get("pinyin", ""),
            })
    else:
        characters = data["characters"]

    # ── Banner ────────────────────────────────────────────────────────
    mode_names = {1: "No Memory (Baseline)", 2: "Failure Learning", 3: "Success Learning"}
    print("=" * 70)
    print(f"DC-ACE Visual Judge  [RapidOCR+DeepSeek]  Mode {args.mode}: {mode_names[args.mode]}")
    print("=" * 70)
    print(f"AI PNGs    : {args.ai_png_dir}")
    print(f"GT PNGs    : {args.gt_png_dir}")
    print(f"Dataset    : {args.dataset}  ({len(characters)} characters)")
    print(f"RapidOCR   : {'enabled (local)' if ocr_engine else 'skipped'}")
    print(f"DeepSeek   : {args.ollama_host}  model={args.vision_model}  "
          f"coords={'enabled' if vision_client else 'skipped'}")
    print(f"Code file  : {args.generated_code or '(none)'}")
    print(f"Output     : {args.output}")
    print()

    # ── Evaluate each character ───────────────────────────────────────
    results: List[Dict] = []
    for entry in characters:
        idx  = entry.get("index", 0)
        char = entry.get("character", "")
        pin  = entry.get("pinyin", "")
        code = code_map.get(idx, "")
        result = judge_character(
            idx, char, pin, args.ai_png_dir, args.gt_png_dir,
            ocr_engine=ocr_engine,
            vision_client=vision_client, vision_model=args.vision_model,
            generated_code=code,
        )
        results.append(result)

    # ── Save JSON report ──────────────────────────────────────────────
    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=2)

    # ── Summary table ─────────────────────────────────────────────────
    total = len(results)
    avg_visual = sum(r["visual_score"] for r in results) / total if total else 0.0
    avg_final  = sum(r["final_score"]  for r in results) / total if total else 0.0
    correct_count = sum(1 for r in results if r.get("is_correct"))

    print()
    print("=" * 80)
    print(f"SUMMARY  [Mode {args.mode}: {mode_names[args.mode]}]")
    print("=" * 80)
    print(f"{'Idx':<5} {'GT':<5} {'Pinyin':<10} "
          f"{'Visual':>7} {'OCR':<10} {'Correct':>8} {'Final':>7}")
    print("-" * 80)

    for r in results:
        print(f"{r['index']:<5} {r['character']:<5} {r['pinyin']:<10} "
              f"{r['visual_score']:>7.4f} {r.get('recognized_char', '') or '(none)':<10} "
              f"{str(r.get('is_correct', '')):>8} {r['final_score']:>7.4f}")

    print("-" * 80)
    print(f"Characters evaluated : {total}")
    print(f"Correct              : {correct_count}/{total}")
    print(f"Avg visual score     : {avg_visual:.4f}")
    print(f"Avg final score      : {avg_final:.4f}")
    print(f"\nReport saved: {args.output}")


if __name__ == "__main__":
    main()
