import re
import json

# Atributos relevantes por tipo
ATTRS = [
    ("val",    r'val:\s*"([^"]+)"'),
    ("label",  r'label:\s*"([^"]+)"'),
    ("frame",  r'frame:\s*"([^"]+)"'),
    ("?G",     r'\?G:\s*"([^"]+)"'),
    ("pct",    r'pct:\s*"([^"]+)"'),
    ("rbp",    r'rbp:\s*"([^"]+)"'),
    # Añade aquí más si necesitas
]

def parse_gfl_struct(filename):
    with open(filename, encoding="ascii") as f:
        text = f.read()
    pattern = r'thought\s*{([^}]*)}'
    matches = re.findall(pattern, text, re.DOTALL)
    nodes = []
    for block in matches:
        node = {"type": "thought", "attrs": {}}
        for key, rgx in ATTRS:
            m = re.search(rgx, block)
            if m:
                node["attrs"][key] = m.group(1)
        type_match = re.search(r'type:\s*"([^"]+)"', block)
        if type_match:
            node["attrs"]["type"] = type_match.group(1)
        nodes.append(node)
    return nodes

if __name__ == "__main__":
    nodes = parse_gfl_struct("test_structured_noBOM.gfl")
    with open("ast_struct.json", "w", encoding="utf8") as f:
        json.dump(nodes, f, indent=2, ensure_ascii=False)
    print("AST estructurado generado en ast_struct.json")
