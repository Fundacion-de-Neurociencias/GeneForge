from gf.parser import parse_code
from gf.semantic import validate_ast

def load_gfl_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    return _parse_and_validate(code)

def load_gfl_string(code):
    return _parse_and_validate(code)

def _parse_and_validate(code):
    ast = parse_code(code)
    validated = validate_ast(ast)
    return validated
