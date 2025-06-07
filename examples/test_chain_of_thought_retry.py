from gf.gfl_import.gfl_importer import load_gfl_string

print("🧪 Testing node: chain_of_thought with conditional retry...\n")

code = """
chain_of_thought {
    goal: "Reduce Tau aggregation in neurons"
    steps: [
        { thought: "Tau aggregates are stabilized by phosphorylation" },
        { thought: "GSK3β is a key kinase involved in this phosphorylation" },
        { thought: "Inhibit GSK3β with lithium", id: "step1" },
        { thought: "Test phosphorylation levels after treatment", eval: "pTau ELISA" },
        { condition: "if eval fails", retry: "step1", modification: "increase lithium dose" },
        { conclusion: "If pTau is reduced, aggregation should decrease" }
    ]
    evaluation: ["Neuron viability", "Tau aggregation via immunostaining"]
}
"""

try:
    result = load_gfl_string(code)
    for node in result:
        print("✅", node)
except Exception as e:
    print(f"❌ Error: {e}")
