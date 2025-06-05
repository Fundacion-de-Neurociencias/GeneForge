## 🧪 GFL Custom Node Test

This script demonstrates how to define and roundtrip a custom node class using the GFL format.

### Example usage:

python examples/test_custom_nodes_gfl.py

### Sample output:

🔁 Exported GFL:

my_custom_node {
    label = "test_node"
    params = {"x": 1, "y": 2}
}

🔁 Re-importing...

✅ Parsed node:

🔹 my_custom_node - {'label': 'test_node', 'params': {'x': 1, 'y': 2}}
