## 🧪 GFL Parser Edge Case Test

This script checks how the GFL parser handles edge cases such as missing attributes, booleans, null values, and syntax errors.

### Example usage:

```bash
python examples/test_edge_cases_gfl.py
Sample output:
pgsql
Copiar
Editar
🔍 Case 1:
empty_node { }
----------------------------------------

🔍 Case 2:
incomplete_node { key = }
----------------------------------------

🔍 Case 3:
logic_node { flag = true, debug = false, fallback = null }
----------------------------------------

🔍 Case 4:
list_node { items = [] }
----------------------------------------

🔍 Case 5:
bad_syntax_node { key == "value" }
----------------------------------------
