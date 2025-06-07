from gfl.utils.gfl_fix import fix_gfl_file
from gfl.parser import parse_tokens
from gfl.prob_rules import ProbReasoner, default_rules

lines = fix_gfl_file("ejemplo_test.gfl")
ast_nodes = parse_tokens(lines)
res = ProbReasoner(default_rules(), prior=0.5).posterior({"nodes": ast_nodes})
print(res["confidence"])
