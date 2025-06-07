from gf.gfl_import.gfl_importer import load_gfl_string

print("🧪 Testing strategic node: strategic_plan...\n")

code = """
strategic_plan {
    goal: "Restore GABAergic tone"
    preconditions: ["Confirmed interneuron loss"]
    steps: [
        { name: "Induce Nkx2.1 expression", method: "AAV-mediated" },
        { name: "Support migration", method: "CXCL12 infusion" }
    ]
    fallbacks: ["Use GABA agonist if cell therapy fails"]
    evaluation_criteria: ["EEG theta normalization", "reduced seizure frequency"]
}
"""

try:
    result = load_gfl_string(code)
    for node in result:
        print("✅", node)
except Exception as e:
    print(f"❌ Error: {e}")
