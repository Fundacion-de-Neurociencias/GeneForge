import json
from gfl.utils.gfl_fix import fix_gfl_file
from gfl.parser import parse_tokens
from gfl.prob_rules import ProbReasoner, default_rules

INPUT_FILE = "ejemplo_test.gfl"
OUTPUT_AST = "parsed_ast.json"

lines = fix_gfl_file(INPUT_FILE)
ast_nodes = parse_tokens(lines)
ast = {"nodes": ast_nodes}

with open(OUTPUT_AST, "w", encoding="utf-8") as f:
    json.dump(ast_nodes, f, indent=2, ensure_ascii=False)

print("📦 Nodos AST parseados:")
print(json.dumps(ast_nodes, indent=2, ensure_ascii=False))

reasoner = ProbReasoner(default_rules(), prior=0.5)
resultado = reasoner.posterior(ast)

print("\\n🎯 Resultado Probabilístico:")
print(json.dumps(resultado, indent=2, ensure_ascii=False))
