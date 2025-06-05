def parse_code(code):
    from gf.lexer import tokenize
    from gf.parser_utils import parse_tokens
    tokens = tokenize(code)
    return parse_tokens(tokens)
