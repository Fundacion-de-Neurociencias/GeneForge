import ply.lex as lex

reserved = {
    'prime_edit': 'PRIME_EDIT',
    'base_edit': 'BASE_EDIT',
    'prime_del': 'PRIME_DEL',
    'peg': 'PEG'
}

tokens = list(reserved.values()) + [
    'ID', 'EQUALS', 'COMMA', 'LPAREN', 'RPAREN',
    'NUMBER', 'STRING', 'PLUS', 'MINUS'
]

t_EQUALS = r'='
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value)
    return t

t_ignore = ' \t\n\r'

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

lexer = lex.lex()
