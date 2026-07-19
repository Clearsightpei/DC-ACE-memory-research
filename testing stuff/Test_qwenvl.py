import ollama
import os

# 1. 配置信息 (确保你的 Windows 端运行的是这个精确的 tag)
REMOTE_HOST = 'http://100.120.168.33:11434'
MODEL_NAME = 'qwen2.5vl:7b' 

# 测试路径
image_paths = [
    '/Users/peilinwu/Documents/AI memory research/PNG Ground Truth/Chinese_2/01_一_1.png',
]

client = ollama.Client(host=REMOTE_HOST)

def perform_qwen_blind_recognition(path):
    if not os.path.exists(path):
        print(f"跳过: {path}")
        return
    
    print(f"正在使用 Qwen2.5-VL 盲测识别: {os.path.basename(path)}...")
    
    try:
        with open(path, 'rb') as f:
            img_data = f.read()

        # 针对 Qwen 优化的简洁 Prompt
        response = client.chat(
            model=MODEL_NAME,
            messages=[{
                'role': 'user',
                'content': "What is the single Chinese character in this image? Output only the character itself and nothing else.",
                'images': [img_data]
            }],
            options={
                'temperature': 0,        # 消除随机性，对裁判任务至关重要
                'num_predict': 10        # 严格限制输出长度
            }
        )
        
        # Qwen 通常输出非常干净
        result = response['message']['content'].strip()
        
        # 提取文件名中的标准答案
        gt_char = os.path.basename(path).split('_')[1]
        
        # 判定
        is_success = (result == gt_char)
        
        print(f"Qwen 识别结果: {result}")
        print(f"标准答案     : {gt_char}")
        print(f"判定结果     : {'【成功】' if is_success else '【失败】'}")
        print("-" * 40)
        
        return is_success

    except Exception as e:
        print(f"Error processing {path}: {e}")

if __name__ == "__main__":
    print(f"正在测试 Qwen2.5-VL 的盲测能力...")
    for img_path in image_paths:
        perform_qwen_blind_recognition(img_path)
