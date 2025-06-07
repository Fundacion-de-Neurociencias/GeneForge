from gf.gfl_import.gfl_importer import load_gfl_string

print("🧪 Testing node: feedback_loop with nested chain_of_thought...\n")

code = """
feedback_loop {
    condition: "dopamine levels < 50%"
    max_iterations: 3
    strategy: chain_of_thought {
        goal: "Restore dopamine levels"
        steps: [
            { thought: "Administer L-DOPA", id: "step1" },
            { thought: "Evaluate motor response", eval: "rotarod test" },
            { condition: "if eval fails", retry: "step1", modification: "increase dose" },
            { conclusion: "Improved motor performance suggests dopamine restoration" }
        ]
        evaluation: ["Dopamine concentration", "Behavioral score"]
    }
}
"""

try:
    result = load_gfl_string(code)
    for node in result:
        print("✅", node)
except Exception as e:
    print(f"❌ Error: {e}")
