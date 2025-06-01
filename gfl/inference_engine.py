import torch
from gfl.translate_lstm import TranslateLSTM

class InferenceEngine:
    def __init__(self):
        # Cargar modelo TE si existe
        try:
            self.te_model = TranslateLSTM()
            self.te_model.load_state_dict(torch.load("models/translate_lstm_ft.pth"))
            self.te_model.eval()
        except:
            self.te_model = None

    def predict_translation_efficiency(self, utr_seq, cds_seq, features):
        if not self.te_model:
            return {"te": None, "explanation": "No TE model available"}
        # TODO: convertir utr_seq, cds_seq a one-hot tensors (stub)
        utr_onehot = torch.zeros((1, len(utr_seq), 4))
        cds_onehot = torch.zeros((1, len(cds_seq), 4))
        extra = torch.tensor([features], dtype=torch.float32)
        te_pred = self.te_model(utr_onehot, cds_onehot, extra).item()
        return {"te": round(te_pred, 3), "explanation": "Predicted via TranslateLSTM"}

    def post_annotate(self, ast_dict):
        # Reglas probabilísticas existentes
        from gfl.prob_rules import ProbReasoner, default_rules
        post = ProbReasoner(default_rules(), prior=0.5).posterior(ast_dict)
        result = {"confidence": post["confidence"], "fired_rules": post["fired_rules"]}

        # Extraer features de AST si existen (ejemplo simple)
        utr_seq   = ast_dict.get("attrs",{}).get("utr_sequence","")
        cds_seq   = ast_dict.get("attrs",{}).get("cds_sequence","")
        # Ejemplo de features: [GC%, ΔG, #uAUG, #RBP_sites, #miR_sites]
        features = [
            float(ast_dict.get("attrs",{}).get("gc_pct",   0)),
            float(ast_dict.get("attrs",{}).get("dg",       0)),
            int(ast_dict.get("attrs",{}).get("uaug_count",0)),
            int(ast_dict.get("attrs",{}).get("rbp_count", 0)),
            int(ast_dict.get("attrs",{}).get("mir_count", 0))
        ]
        te_res = self.predict_translation_efficiency(utr_seq, cds_seq, features)
        result["te_prediction"] = te_res
        return result
# ─── Handling new edit types in inference ───────────────────────
if node.name == "prime_edit":
    context["has_prime_edit"] = True
    context["pegRNA"] = node.args.get("pegRNA")

if node.name == "base_edit":
    context["has_base_edit"] = True
    context["base_editor"] = node.args.get("base_editor")
