from gf.parser import parse_tokens
from gf.lexer import tokenize
from gf.semantic import validate_ast

def load_gfl_string(code):
    # Asegura que el input sea una sola cadena de texto, no una lista
    if isinstance(code, list):
        code = "\n".join(code)

    lines = code.splitlines()
    tokens = tokenize(lines)
    ast = parse_tokens(tokens)
    validate_ast(ast)
    return ast
