from ply import yacc
from .lexer import tokens, lexer

def p_code(p):
    '''code : block_list'''
    p[0] = p[1]

def p_block_list(p):
    '''block_list : block block_list
                  | block'''
    p[0] = [p[1]] + (p[2] if len(p) == 3 else [])

def p_block(p):
    '''block : PIRNA LBRACE kvs RBRACE
             | TRANSPOSON LBRACE kvs RBRACE
             | RETROVIRUS LBRACE kvs RBRACE
             | MITOGENE LBRACE kvs RBRACE
             | MENDEL LBRACE kvs RBRACE
             | TECHNIQUE LBRACE kvs RBRACE
             | APPLICATION LBRACE kvs RBRACE
             | AITOOL LBRACE kvs RBRACE
             | ETHICS LBRACE kvs RBRACE'''
    p[0] = (p[1], p[3])

def p_kvs(p):
    '''kvs : kv kvs
           | kv'''
    p[0] = {**p[1], **(p[2] if len(p) == 3 else {})}

def p_kv(p):
    '''kv : ID EQUALS STRING'''
    p[0] = {p[1]: p[3].strip('"')}

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def parse_code(code: str):
    return parser.parse(code, lexer=lexer)
