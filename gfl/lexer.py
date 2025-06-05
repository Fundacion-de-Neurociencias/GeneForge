import ply.lex as lex

tokens = (
    'ID',
    'STRING',
    'EQUALS',
    'LBRACE',
    'RBRACE',
)

reserved = {
    'pirna': 'PIRNA',
    'transposon': 'TRANSPOSON',
    'endogenous_retrovirus': 'RETROVIRUS',
    'mitochondrial_gene': 'MITOGENE',
    'mendel_law': 'MENDEL',
    'genetic_technique': 'TECHNIQUE',
    'application': 'APPLICATION',
    'ai_tool': 'AITOOL',
    'ethics_guideline': 'ETHICS'
}

tokens += tuple(reserved.values())

t_EQUALS = r'='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_STRING = r'\"[^\\"]*\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
