from gf.core import Node
from gf.export.gfl_exporter import export_to_gfl
from gf.gfl_import.gfl_importer import load_gfl_string

# Custom node definition
class MyCustomNode(Node):
    def __init__(self, label, params):
        super().__init__('my_custom_node', label=label, params=params)

# Create instance
original = MyCustomNode(label="test_node", params={"x": 1, "y": 2})

# Export to GFL
gfl_string = export_to_gfl(original)
print("🔁 Exported GFL:\n")
print(gfl_string)

# Re-import
print("\n🔁 Re-importing...\n")
reimported = load_gfl_string(gfl_string)

# Display result
print("✅ Parsed node:\n")
for node in reimported:
    print(f"🔹 {node.type} - {node.attrs}")
