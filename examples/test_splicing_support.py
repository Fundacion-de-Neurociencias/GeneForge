from gf.gfl_import.gfl_importer import load_gfl_string

code = \"\"\" 
splicing_event {
    type = "alternative"
    exons = ["exon1", "exon2", "exon3"]
    regulators = ["SRSF1", "hnRNP"]
}

protein {
    name = "TP53"
    domains = ["DNA-binding", "Tetramerization"]
    modifications = ["phosphorylation", "ubiquitination"]
}

regulation {
    source = "TP53"
    target = "MDM2"
    effect = "repression"
}
\"\"\"

print("🧪 Testing advanced node structures (splicing, protein, regulation)...\n")

try:
    result = load_gfl_string(code)
    for node in result:
        print(f"✅ {node.type} parsed: {node.attrs}")
except Exception as e:
    print(f"❌ Error: {e}")
