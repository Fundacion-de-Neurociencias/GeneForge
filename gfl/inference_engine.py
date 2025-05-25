# gfl/inference_engine.py

from typing import Any, Dict

class InferenceEngine:
    def __init__(self, model):
        """
        model: objeto con métodos predict(), infer_causal_variant() y assess_off_targets()
        """
        self.model = model

    def predict_effect(self, gfl_ast: Dict[str, Any]) -> Dict[str, Any]:
        """
        Predice efectos funcionales a partir de una edición genética representada en GFL.
        """
        features = self._extract_features(gfl_ast)
        prediction = self.model.predict(features)
        return {
            "prediction": prediction,
            "input_features": features
        }

    def retroinfer_cause(self, phenotype_description: str) -> Dict[str, Any]:
        """
        Retroinfiere posibles mutaciones causales a partir de un fenotipo descrito.
        """
        return self.model.infer_causal_variant(phenotype_description)

    def evaluate_off_target(self, gfl_ast: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evalúa efectos no deseados (off-targets) potenciales de una edición propuesta.
        """
        off_targets = self.model.assess_off_targets(gfl_ast)
        return {
            "off_target_hits": off_targets
        }

    def _extract_features(self, gfl_ast: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transforma el AST en un vector de características para el modelo.
        Aquí puedes aplicar lógica más compleja si deseas trabajar con embeddings simbólicos.
        """
        return {
            "edit": gfl_ast.get("edit"),
            "target": gfl_ast.get("target"),
            "effect": gfl_ast.get("effect"),
            "pathway": gfl_ast.get("pathway")
        }
