import json
from gfl.utils.gfl_fix import fix_gfl_file
from gfl.parser import parse_tokens
from gfl.prob_rules import ProbReasoner, default_rules

INPUT_FILE = "ejemplo_test.gfl"

lines = fix_gfl_file(INPUT_FILE)
ast_nodes = parse_tokens(lines)

reasoner = ProbReasoner(default_rules(), prior=0.5)
resultado = reasoner.posterior({"nodes": ast_nodes})

print("🧪 Test automático de reglas:")
for rule in resultado['fired_rules']:
    print(f"✅ Se activó la regla: {rule}")
print(f"\n🔢 Confianza final: {resultado['confidence']:.3f}")
