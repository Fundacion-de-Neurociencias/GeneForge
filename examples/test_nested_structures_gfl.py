from gf.gfl_import.gfl_importer import load_gfl_string

nested_code = '''
complex_technique {
    name = "Prime Editing"
    components = [
        { name = "pegRNA", length = 100 },
        { name = "Cas9-nickase", target = "PAM site" }
    ]
    meta = {
        origin = "Zhang Lab",
        approved = true,
        versions = [1, 2, 3]
    }
}
'''

print("🔍 Parsing nested GFL structure...\n")
try:
    result = load_gfl_string(nested_code)
    for node in result:
        print(f"✅ Node: {node.type}")
        for k, v in node.attrs.items():
            print(f"   🔹 {k}: {v}")
except Exception as e:
    print(f"❌ Error: {e}")
