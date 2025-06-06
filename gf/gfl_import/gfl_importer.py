from gf.parser import parse_gfl
from gf.semantic import validate_ast

def load_gfl_string(code):
    if isinstance(code, list):
        code = '\n'.join(code)
    tokens = parse_gfl(code)
    ast = validate_ast(tokens)
    return ast
