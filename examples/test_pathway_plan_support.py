from gf.gfl_import.gfl_importer import load_gfl_string

print("🧪 Testing strategic node: pathway_plan...\n")

code = """
pathway_plan {
    goal: "Increase dopamine synthesis"
    subgoals: [
        { name: "Upregulate TH", method: "CRISPRa" },
        { name: "Enhance BH4 availability", method: "cofactor supplementation" }
    ]
    conditions: "Only in substantia nigra"
    checkpoints: ["qPCR for TH", "dopamine levels via HPLC"]
}
"""

try:
    result = load_gfl_string(code)
    for node in result:
        print("✅", node)
except Exception as e:
    print(f"❌ Error: {e}")
