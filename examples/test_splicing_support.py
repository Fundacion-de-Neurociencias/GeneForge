from gf.gfl_import.gfl_importer import load_gfl_string

code = '''
transcript_variant {
    gene = "TP53"
    exons = [1, 2, 4, 5, 9]
    splicing_pattern = "exon skipping"
    functional_impact = "dominant negative"
}

protein {
    name = "p53-alpha"
    domains = ["DNA-binding", "tetramerization"]
    post_translational_modifications = ["phosphorylation"]
    localization = "nucleus"
}

regulatory_element {
    name = "TATA-box"
    element_type = "promoter"
    binding_sites = ["TBP", "TFIID"]
    strength = "strong"
}
'''

print("🧪 Testing advanced node structures (splicing, protein, regulation)...\n")

try:
    result = load_gfl_string(code)
    print(f"🔍 Type of result: {type(result)}")
    for node in result:
        print(f"🔸 Raw node: {node}")
        print(f"✅ {getattr(node, 'type', '<no type>')} parsed: {getattr(node, 'attrs', node)}")
except Exception as e:
    print(f"❌ Error: {e}")
