import json
from gfl.utils.gfl_fix import fix_gfl_file
from gfl.parser import parse_tokens
from gfl.prob_rules import ProbReasoner, default_rules

INPUT_FILE = "ejemplo_test.gfl"

# 1. Arreglar sintaxis
lines = fix_gfl_file(INPUT_FILE)

# 2. Tokenizar
ast_nodes = parse_tokens(lines)

# 3. Crear reasoner y evaluar
reasoner = ProbReasoner(default_rules(), prior=0.5)
resultado = reasoner.posterior({"nodes": ast_nodes})

# 4. Imprimir resultado global
print("🎯 Resultado Probabilístico:")
print(json.dumps(resultado, indent=2))

# 5. 🔍 Debug: ver qué reglas se activan nodo a nodo
print("\n🔎 Evaluación detallada por nodo:")
for i, node in enumerate(ast_nodes):
    print(f"\n🧠 Nodo #{i+1}: {json.dumps(node, indent=2)}")
    for rule in default_rules():
        try:
            if rule.func(node):
                print(f"  ✅ Disparada: {rule.name}")
        except Exception as e:
            print(f"  ⚠️  Error en regla {rule.name}: {e}")
