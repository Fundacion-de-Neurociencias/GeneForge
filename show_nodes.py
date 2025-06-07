from gfl.utils.gfl_fix import fix_gfl_file
from gfl.parser import parse_tokens
import json

INPUT_FILE = "ejemplo_test.gfl"

lines = fix_gfl_file(INPUT_FILE)
nodes = parse_tokens(lines)

print("📦 Nodos AST detectados:")
for i, node in enumerate(nodes, 1):
    print(f"\\n🔹 Nodo {i}:")
    print(json.dumps(node, indent=2))
