from gfl.utils.gfl_fix import fix_gfl_file
from gfl.parser import parse_tokens
from gfl.prob_rules import ProbReasoner, default_rules

INPUT_FILE = "ejemplo_test.gfl"

lines = fix_gfl_file(INPUT_FILE)
ast_nodes = parse_tokens(lines)

resultado = ProbReasoner(default_rules(), prior=0.5).posterior({"nodes": ast_nodes})

for rule in resultado["fired_rules"]:
    print(rule)
