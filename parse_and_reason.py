import re
import json
from gfl.prob_rules import ProbReasoner, default_rules

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
        nodes.append(node)
    return nodes

if __name__ == "__main__":
    ast_nodes = parse_gfl_min("test_structured_noBOM.gfl")
    print("NODOS AST PARSEADOS:")
    print(json.dumps(ast_nodes, indent=2, ensure_ascii=False))
    reasoner = ProbReasoner(default_rules(), prior=0.5)
    resultado = reasoner.posterior({"nodes": ast_nodes})
    print("\nRESULTADO PROBABILISTICO:")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
