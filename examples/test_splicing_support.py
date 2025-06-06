from gf.gfl_import.gfl_importer import load_gfl_string

code = """
splicing_event {
    gene = "TP53"
    type = "exon_skipping"
    exon_number = 4
    consequence = "loss_of_function"
}

protein {
    name = "p53"
    domains = ["DNA_binding", "oligomerization"]
    isoelectric_point = 6.8
}

regulation {
    target = "BAX"
    regulator = "p53"
    mechanism = "transactivation"
}
"""

print("🧪 Testing advanced node structures (splicing, protein, regulation)...\n")

try:
    result = load_gfl_string(code)
    for node in result:
        print(f"✅ {node.type} parsed: {node.attrs}")
except Exception as e:
    print(f"❌ Error: {e}")
