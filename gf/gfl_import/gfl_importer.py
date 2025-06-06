from gf.parser import parse_tokens
from gf.semantic import validate_ast

def load_gfl_string(code):
    if isinstance(code, list):
        code = '\n'.join(code)
    tokens = parse_tokens(code)
    ast = validate_ast(tokens)
    return ast
