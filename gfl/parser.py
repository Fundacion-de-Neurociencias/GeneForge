import ply.yacc as yacc
from .lexer import tokens

def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_statements_multiple(p):
    '''statements : statements statement'''
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    '''statements : statement'''
    p[0] = [p[1]]

def p_statement(p):
    '''statement : IDENTIFIER LBRACE attributes RBRACE'''
    p[0] = (p[1], p[3])

def p_attributes_multiple(p):
    '''attributes : attributes attribute'''
    p[0] = {**p[1], **p[2]}

def p_attributes_single(p):
    '''attributes : attribute'''
    p[0] = p[1]

def p_attribute(p):
    '''attribute : IDENTIFIER EQUALS STRING'''
    p[0] = {p[1]: p[3].strip('"')}

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def parse_code(code: str):
    return parser.parse(code)
