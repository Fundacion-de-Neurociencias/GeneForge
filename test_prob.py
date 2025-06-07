from gfl.prob_rules import ProbReasoner, default_rules
import json

ast = {
    "nodes": [
        {"type": "risk", "attrs": {"val": "offtarget:0.85"}},
        {"type": "repeat_edit"},
        {"type": "residue", "attrs": {"label": "ncAA"}},
        {"type": "uaug", "attrs": {"frame": "1"}},
        {"type": "structure", "attrs": {"?G": "-12.5"}},
        {"type": "gc_content", "attrs": {"pct": "0.72"}},
        {"type": "rbp_site", "attrs": {"rbp": "Pumilio"}}
    ]
}

result = ProbReasoner(default_rules(), prior=0.5).posterior(ast)
print("🎯 Resultado Probabilístico:")
print(json.dumps(result, indent=2))
