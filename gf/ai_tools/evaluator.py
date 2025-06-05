from .deepcrispr import predict_on_target_efficiency
from .crista import predict_crista_score
from .deephf import predict_high_fidelity

def evaluate_sequence(sequence: str) -> dict:
    return {
        "efficiency": predict_on_target_efficiency(sequence),
        "crista_score": predict_crista_score(sequence),
        "high_fidelity": predict_high_fidelity(sequence),
    }
