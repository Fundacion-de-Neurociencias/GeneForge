from gf.lexer import tokenize
from gf.parser import parse_tokens
from gf.semantic import validate_ast
from gf.core import Node

def load_gfl_string(code: str):
    tokens = tokenize(code)
    parsed = parse_tokens(tokens)

    # parsed debe ser lista de dicts
    if not isinstance(parsed, list) or not all(isinstance(el, dict) for el in parsed):
        raise ValueError("Parser output must be a list of dictionaries")

    validated = validate_ast(parsed)

    # validated también debe ser lista de dicts con 'type' y 'attrs'
    if not isinstance(validated, list) or not all(
        isinstance(n, dict) and 'type' in n and 'attrs' in n for n in validated):
        raise ValueError("Validation must return list of dicts with 'type' and 'attrs'")

    # Construimos nodos correctamente
    return [Node(type=el["type"], attrs=el["attrs"]) for el in validated]
