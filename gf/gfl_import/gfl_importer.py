from gfl.parser import parse_code
from gfl.semantic_validator import validate_ast

def parse_gfl_to_ast(gfl_code: str):
    ast = parse_code(gfl_code)
    validate_ast(ast)
    return ast

def load_gfl_file(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    return parse_gfl_to_ast(code)
