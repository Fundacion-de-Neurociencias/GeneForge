# model/transformer_multimodal.py
"""
Minimal stub so the QuickScore demo can import GeneForgeModel
without syntax errors. Replace later with real transformer code.
"""

class GeneForgeModel:
    def __init__(self):
        # placeholder init
        pass

    # ---- helpers expected by the rest of the demo ------------------
    def from_gfl_ast(self, ast):
        """Return dummy token list from AST."""
        return []

    def predict(self, features):
        """Return a dummy prediction dict with confidence key."""
        return {"label": "unknown", "confidence": 0.5}

    def infer_causal_variant(self, phenotype_description):
        return {"variant": "rs000000", "confidence": 0.4}

    def assess_off_targets(self, gfl_ast):
        return []
