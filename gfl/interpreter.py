import os
import sys

# Asegura que GFL y GF están en el path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from gfl.parser import parse_code
from gfl.semantic_validator import validate_ast
from gf.ai_tools.evaluator import evaluate_sequence

def run_interpreter(gfl_path):
    print(f"📂 Processing file: {gfl_path}")

    # 1. Parse
    with open(gfl_path, "r", encoding="utf-8") as f:
        code = f.read()
    ast = parse_code(code)
    print("✅ AST parsed.")

    # 2. Validate
    if not validate_ast(ast):
        print("❌ Semantic validation failed.")
        return
    print("✅ Semantic validation passed.")

    # 3. Search for CRISPR-like entries
    for node_type, attrs in ast:
        if node_type == "genetic_technique" and attrs.get("mechanism", "").lower() == "crispr":
            guide_seq = attrs.get("components", "").upper()
            if guide_seq:
                print(f"🧬 Guide sequence found: {guide_seq}")
                result = evaluate_sequence(guide_seq)
                print("🔬 Evaluation Results:")
                print(f"   - Efficiency (DeepCRISPR): {result['efficiency']:.3f}")
                print(f"   - CRISTA Score: {result['crista_score']}")
                print(f"   - High Fidelity (DeepHF): {'Yes' if result['high_fidelity'] else 'No'}")
                return
    print("ℹ️ No CRISPR-compatible technique found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m gfl.interpreter <path_to_gfl_file>")
    else:
        run_interpreter(sys.argv[1])
