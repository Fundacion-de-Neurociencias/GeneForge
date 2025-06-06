from gf.parser import parse_tokens
from gf.lexer import tokenize
from gf.semantic import validate_ast

def load_gfl_string(code):
    # Normaliza: asegura que siempre trabaje con lista de líneas
    if isinstance(code, str):
        lines = code.splitlines()
    elif isinstance(code, list):
        lines = code
    else:
        raise TypeError(f"Expected string or list of lines, got {type(code).__name__}")

    tokens = tokenize(lines)
    ast = parse_tokens(tokens)
    validate_ast(ast)
    return ast
