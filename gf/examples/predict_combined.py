import sys
import os

# Ensure 'gf' is importable from any subdirectory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from gf.ai_tools.evaluator import evaluate_sequence

sequence = "GCTAGCTAGCTAGCTAGCTA"
result = evaluate_sequence(sequence)

# Qualitative interpretations
def interpret_efficiency(score):
    if score >= 0.75:
        return "High editing efficiency"
    elif score >= 0.5:
        return "Moderate efficiency"
    else:
        return "Low editing efficiency"

def interpret_crista(score):
    if score >= 0.65:
        return "High specificity"
    elif score >= 0.5:
        return "Acceptable specificity"
    else:
        return "Risk of off-target effects"

def interpret_fidelity(flag):
    return "High-fidelity guide" if flag else "Potential editing errors"

# Output
print(f"🧬 Guide sequence: {sequence}")
print(f"🔬 Efficiency (DeepCRISPR): {result['efficiency']:.3f} → {interpret_efficiency(result['efficiency'])}")
print(f"⚙️  CRISTA score: {result['crista_score']} → {interpret_crista(result['crista_score'])}")
print(f"✅ High fidelity (DeepHF): {'Yes' if result['high_fidelity'] else 'No'} → {interpret_fidelity(result['high_fidelity'])}")
