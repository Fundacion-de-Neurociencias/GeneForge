from gf.ai_tools.deepcrispr import predict_on_target_efficiency
from gf.ai_tools.crista import predict_crista_score
from gf.ai_tools.deephf import predict_high_fidelity

sequence = "GCTAGCTAGCTAGCTAGCTA"

print(f"🧬 Secuencia guía: {sequence}")
print(f"🔬 Eficiencia (DeepCRISPR): {predict_on_target_efficiency(sequence):.3f}")
print(f"⚙️  Score CRISTA: {predict_crista_score(sequence)}")
print(f"✅ Alta fidelidad (DeepHF): {'Sí' if predict_high_fidelity(sequence) else 'No'}")
