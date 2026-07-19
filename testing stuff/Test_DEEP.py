import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env
load_dotenv()

# Retrieve the key from environment variables
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("❌ Error: DEEPSEEK_API_KEY not found in .env file.")
else:
    client = OpenAI(
        api_key=api_key, 
        base_url="https://api.deepseek.com"
    )

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "tell me who the best basketball player is"},
                {"role": "user", "content": "API test. Confirm connection status."}
            ],
            stream=False
        )
        print("--- DeepSeek Response ---")
        print(response.choices[0].message.content)
        print("-------------------------")
        
    except Exception as e:
        print(f"❌ Connection Failed: {e}")