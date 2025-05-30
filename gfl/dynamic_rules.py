"""Loads rule_table.yaml and appends dynamic ProbRules."""
import yaml, re
from gfl.prob_rules import ProbRule

def load_dynamic_rules(path='gfl/rule_table.yaml'):
    try:
        spec=yaml.safe_load(open(path))
    except FileNotFoundError:
        return []
    rules=[]
    for key,lr in spec.items():
        k,pat=key.split(':',1)
        rules.append(ProbRule(f'dyn_{key}', float(lr), lambda n,pa=pat,kk=k: pa in n['attrs'].get(kk,'') ))
    return rules
