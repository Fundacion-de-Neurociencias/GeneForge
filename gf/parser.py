from gf.lexer import tokenize

def parse_tokens(code: str):
    tokens = tokenize(code)
    return tokens
