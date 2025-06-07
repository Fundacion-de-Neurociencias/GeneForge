from gf.gfl_import.gfl_importer import load_gfl_string

print("🧪 Testing strategic node: chain_of_thought...\n")

code = """
chain_of_thought {
    goal: "Inhibit mTOR in glioblastoma stem cells"
    steps: [
        { thought: "mTOR is overactivated in these cells" },
        { thought: "Rapamycin is a known mTOR inhibitor" },
        { thought: "We can encapsulate it in nanoparticles for delivery" },
        { thought: "Targeting CD133+ cells will improve specificity" },
        { conclusion: "Use CD133-targeted nanorapamycin to inhibit mTOR" }
    ]
    evaluation: ["mTOR phosphorylation via Western", "stemness marker reduction"]
}
"""

try:
    result = load_gfl_string(code)
    for node in result:
        print("✅", node)
except Exception as e:
    print(f"❌ Error: {e}")
