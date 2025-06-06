from gf.lexer import tokenize
from gf.parser import parse_tokens
from gf.parser_utils import build_ast
from gf.semantic import validate_ast

def load_gfl_string(code: str):
    tokens = parse_tokens(code)
    ast = build_ast(tokens)
    validate_ast(ast)
    return ast
