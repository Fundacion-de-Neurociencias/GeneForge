# Define ProbRule and ProbReasoner
class ProbRule:
    def __init__(self, name, likelihood_ratio, condition):
        self.name = name
        self.lr = likelihood_ratio
        self.condition = condition

def default_rules():
    return [
        ProbRule("high_offtarget", 0.4,
                 lambda n: n["type"] == "risk" and float(n["attrs"]["val"].split(':')[1]) > 0.6),
        ProbRule("repeat_interruption", 4.0,
                 lambda n: n["type"] == "repeat_edit"),
        ProbRule('ncAA_LNP_match', 2.0,
                 lambda n, ast=None: n['type'] == 'residue' and ('LNP' in str(ast))),
        ProbRule('uAUG_penalty', 0.4,
                 lambda n, ast=None: n['type'] == 'uaug' and n['attrs'].get('frame', '') != '0'),
        ProbRule('structure_penalty', 0.6,
                 lambda n, ast=None: n['type'] == 'structure' and float(n['attrs'].get('?G', 0)) < -8),
        ProbRule('gc_content_penalty', 0.8,
                 lambda n, ast=None: n['type'] == 'gc_content' and float(n['attrs'].get('pct', 0)) > 0.60),
        ProbRule('rbp_Pumilio_penalty', 0.7,
                 lambda n, ast=None: n['type'] == 'rbp_site' and n['attrs'].get('rbp') == 'Pumilio'),
    ]

class ProbReasoner:
    def __init__(self, rules, prior=0.5):
        self.rules = rules
        self.prior = prior

    def posterior(self, ast):
        log_odds = self._logit(self.prior)
        fired = []
        for n in ast.get("nodes", []):
            for rule in self.rules:
                try:
                    if rule.condition(n, ast):
                        log_odds += self._logit(rule.lr)
                        fired.append(rule.name)
                except:
                    continue
        posterior = self._sigmoid(log_odds)
        return {"confidence": round(posterior, 3), "fired_rules": fired}

    def _logit(self, p):
        import math
        return math.log(p / (1 - p))

    def _sigmoid(self, x):
        import math
        return 1 / (1 + math.exp(-x))
