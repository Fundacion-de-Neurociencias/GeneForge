from gf.gfl_import.gfl_importer import load_gfl_string

code = '''
enhanced_construct {
    name = "Super GFP"
    elements = ["promoter", "GFP"]
    marker = "Kanamycin"
}
'''

print("🔍 Testing schema inheritance (enhanced_construct extends construct)...\n")

try:
    result = load_gfl_string(code)
    for node in result:
        print(f"✅ {node.type} parsed: {node.attrs}")
except Exception as e:
    print(f"❌ Semantic error: {e}")
