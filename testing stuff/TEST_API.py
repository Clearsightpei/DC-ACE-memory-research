import openai
import sys

# Orchestrator configuration
client = openai.OpenAI(
    base_url="http://100.120.168.33:11434/v1",
    api_key="ollama"
)

def query_ckg_engine(prompt):
    try:
        response = client.chat.completions.create(
            model="gemma4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Connection Error: {e}"

# Verification execution
if __name__ == "__main__":
    print("Sending request to Windows 'Machine Room'...")
    result = query_ckg_engine("Briefly explain what a Conceptual Knowledge Graph is.")
    print("-" * 30)
    print(f"Response from Gemma 4:\n{result}")
    print("-" * 30)