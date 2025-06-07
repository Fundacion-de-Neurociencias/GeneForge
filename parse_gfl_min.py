import re
import json

def parse_gfl_min(filename):
    with open(filename, encoding="ascii") as f:
        text = f.read()
    # Busca bloques thought { ... }
    pattern = r'thought\s*{([^}]*)}'
    matches = re.findall(pattern, text, re.DOTALL)
    nodes = []
    for block in matches:
        node = {"type": "thought", "attrs": {}}
        type_match = re.search(r'type:\s*"([^"]+)"', block)
        if type_match:
            node["attrs"]["type"] = type_match.group(1)
        val_match = re.search(r'val:\s*"([^"]+)"', block)
        if val_match:
            node["attrs"]["val"] = val_match.group(1)
        # Otros atributos: puedes añadir aquí más extracciones según el formato
        nodes.append(node)
    return nodes

if __name__ == "__main__":
    nodes = parse_gfl_min("test_structured_noBOM.gfl")
    print(json.dumps(nodes, indent=2, ensure_ascii=False))
