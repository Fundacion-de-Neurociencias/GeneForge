from gf.parser import parse_tokens
from gf.lexer import tokenize
from gf.semantic import validate_ast

def load_gfl_string(code):
    if isinstance(code, list):
        lines = code
    else:
        lines = code.splitlines()

    tokens = tokenize(lines)
    ast = parse_tokens(tokens)
    validate_ast(ast)
    return ast
