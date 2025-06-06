from gf.lexer import tokenize
from gf.parser import parse_tokens
from gf.semantic import validate_ast
from gf.core import Node

def load_gfl_string(code: str):
    tokens = tokenize(code)
    parsed = parse_tokens(tokens)
    validated = validate_ast(parsed)
    return [Node(type=token['type'], attrs=token['attrs']) for token in validated]
