import ollama
import os
import re

# 1. Configuration
# Ensure this matches your Windows machine's Tailscale/Local IP
REMOTE_HOST = 'http://100.120.168.33:11434'
MODEL_NAME = 'deepseek-ocr'

# Test paths from your environment
image_paths = [
    '/Users/peilinwu/Documents/AI memory research/PNG Ground Truth/Chinese_2/01_一_1.png',
    '/Users/peilinwu/Documents/AI memory research/PNG Ground Truth/Chinese_2/02_人_1.png'
]

client = ollama.Client(host=REMOTE_HOST)

def clean_ocr_output(text):
    """
    Extracts only Chinese characters to handle cases where 
    DeepSeek-OCR adds tags or English descriptions.
    """
    # Filter for Unicode range of Chinese characters
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    return "".join(chinese_chars)

def perform_ocr_test(path):
    if not os.path.exists(path):
        print(f"File missing: {path}")
        return

    print(f"Testing: {os.path.basename(path)}")
    
    try:
        with open(path, 'rb') as f:
            img_data = f.read()

        # STRATEGY: Minimalist Prompt + Stop Sequence
        # Using "Transcription:" often triggers the OCR-only weights in DeepSeek
        response = client.chat(
            model=MODEL_NAME,
            messages=[{
                'role': 'user',
                'content': 'Transcription:', 
                'images': [img_data]
            }],
            options={
                'temperature': 0,           # Zero randomness
                'num_predict': 5,           # Force a short answer
                'stop': ['Transcription:', '\n'] # Kill the loop if it tries to repeat
            }
        )
        
        raw_output = response['message']['content'].strip()
        final_result = clean_ocr_output(raw_output)
        
        # Extract GT from filename (e.g., "01_一_1.png" -> "一")
        gt_char = os.path.basename(path).split('_')[1]
        
        success = (final_result == gt_char)
        
        print(f"  > Raw Output: {raw_output}")
        print(f"  > Extracted : {final_result}")
        print(f"  > Expected  : {gt_char}")
        print(f"  > Status    : {'PASSED' if success else 'FAILED'}")
        print("-" * 40)
        
    except Exception as e:
        print(f"  > Execution Error: {e}")

if __name__ == "__main__":
    print(f"Connecting to DeepSeek-OCR at {REMOTE_HOST}...")
    for img_path in image_paths:
        perform_ocr_test(img_path)