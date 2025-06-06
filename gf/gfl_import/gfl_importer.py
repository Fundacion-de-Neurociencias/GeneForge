from gf.lexer import tokenize
from gf.parser import parse_tokens
from gf.semantic import validate_ast

def load_gfl_string(code: str):
    tokens = tokenize(code)
    ast = parse_tokens(tokens)
    validate_ast(ast)
    return ast
