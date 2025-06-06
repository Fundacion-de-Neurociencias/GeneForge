from gf.gfl_import.gfl_importer import load_gfl_string

code = \"\"\"
splicing_event {
    type = "exon_skipping"
    exon = "exon_3"
    context = "brain"
}

protein {
    name = "p53"
    domains = ["transactivation", "DNA_binding", "oligomerization"]
}

regulation {
    target = "p53"
    mechanism = "ubiquitination"
    effector = "MDM2"
}
\"\"\"

print("🧪 Testing advanced node structures (splicing, protein, regulation)...\n")

try:
    result = load_gfl_string(code)
    for node in result:
        print(f"✅ {node.type} parsed: {node.attrs}")
except Exception as e:
    print(f"❌ Error: {e}")
