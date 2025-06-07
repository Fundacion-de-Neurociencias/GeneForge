from gf.gfl_import.gfl_importer import load_gfl_string

print("🧪 Testing strategic node: gene_strategy...\n")

code = """
gene_strategy {
    objective: "Knockout of TP53 in cancer cells"
    steps: ["Design gRNA", "Assemble CRISPR-Cas9", "Transfect cells", "Screen for knockout"]
    validation: "PCR + Western Blot"
    conditions: "Only in cells with KRAS mutation"
    priority: "High"
}
"""

try:
    result = load_gfl_string(code)
    for node in result:
        print("✅", node)
except Exception as e:
    print(f"❌ Error: {e}")
