import sys
import os
from pathlib import Path

# Setup import path for gf and gfl modules
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from gfl.parser import parse_file
from gf.ai_tools.evaluator import evaluate_sequence

# 📂 Input file
gfl_file = os.path.join(BASE_DIR, "examples", "test_extended_semantics.gfl")
print(f"📥 Loading: {gfl_file}")

# 🧠 Parse .gfl file
ast = parse_file(gfl_file)
print("✅ AST parsed.")

# 🔍 Look for genetic_technique with sequence info
for node in ast:
    if node[0] == "genetic_technique":
        details = node[1]
        sequence = details.get("components")  # assuming this holds the gRNA or similar

        if sequence and isinstance(sequence, str) and len(sequence) >= 15:
            print(f"\n🧬 Found guide-like sequence: {sequence}")
            result = evaluate_sequence(sequence)

            def interp_eff(s): return "High" if s >= 0.75 else "Moderate" if s >= 0.5 else "Low"
            def interp_crista(s): return "High specificity" if s >= 0.65 else "Acceptable" if s >= 0.5 else "Risk of off-targets"
            def interp_fid(b): return "High-fidelity guide" if b else "Risk of errors"

            print(f"🔬 Efficiency (DeepCRISPR): {result['efficiency']:.3f} → {interp_eff(result['efficiency'])}")
            print(f"⚙️  CRISTA score: {result['crista_score']} → {interp_crista(result['crista_score'])}")
            print(f"✅ Fidelity (DeepHF): {'Yes' if result['high_fidelity'] else 'No'} → {interp_fid(result['high_fidelity'])}")
        else:
            print("⚠️ No valid sequence found in 'components'.")
