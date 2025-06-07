import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_chain_of_thought(goal):
    prompt = f"""
You are an expert in genetic strategies and synthetic biology. Using GFL (Genetic Function Language), generate a valid chain_of_thought block to reason toward the following biological goal:

Goal: {goal}

Use this format:
chain_of_thought {{
    goal: "..."
    steps: [ ... ]
    evaluation: [ ... ]
}}

Only return valid GFL code, no explanation.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a GFL reasoning engine."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    gfl_code = response["choices"][0]["message"]["content"]
    return gfl_code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python generate_chain.py \"goal text here\"")
        sys.exit(1)

    goal_input = sys.argv[1]
    output = generate_chain_of_thought(goal_input)
    print("\n🧠 Generated GFL Chain-of-Thought:\n")
    print(output)

    with open("output_chain.gfl", "w", encoding="utf-8") as f:
        f.write(output)
        print("\n💾 Saved to output_chain.gfl")
