from gf.lexer import tokenize
from gf.parser import parse_tokens
from gf.semantic import validate_ast
from gf.core import Node

def load_gfl_string(code: str):
    tokens = tokenize(code)
    parsed = parse_tokens(tokens)

    # Asegura que parsed sea una lista de dicts planos
    if not isinstance(parsed, list) or not all(isinstance(el, dict) for el in parsed):
        raise ValueError("Parser output is not a list of dicts")

    validated = validate_ast(parsed)

    # Asegura que validated también es una lista de dicts con claves 'type' y 'attrs'
    if not isinstance(validated, list) or not all(isinstance(n, dict) and 'type' in n and 'attrs' in n for n in validated):
        raise ValueError("AST validation did not return list of dicts with 'type' and 'attrs'")

    return [Node(type=token["type"], attrs=token["attrs"]) for token in validated]
