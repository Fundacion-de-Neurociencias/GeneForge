from gf.gfl_import.gfl_importer import load_gfl_string

code = '''
splicing_event {
    type = "exon skipping"
    exon = "exon 3"
    effect = "loss of function"
}

protein {
    name = "p53"
    domains = ["DBD", "TAD"]
    post_translational_modifications = ["phosphorylation", "acetylation"]
}

regulation {
    regulator = "miR-21"
    target = "PTEN"
    type = "inhibition"
}
'''

print("🧪 Testing advanced node structures (splicing, protein, regulation)...\n")

try:
    nodes = load_gfl_string(code)
    for node in nodes:
        print(f"✅ {node.type} parsed: {node.attrs}")
except Exception as e:
    print(f"❌ Error: {e}")
