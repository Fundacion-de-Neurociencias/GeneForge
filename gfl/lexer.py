import ply.lex as lex

tokens = [
    'IDENTIFIER',
    'STRING',
    'EQUALS',
    'LBRACE',
    'RBRACE'
]

t_EQUALS = r'='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ignore = ' \t\r'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'"[^"\n]*"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
