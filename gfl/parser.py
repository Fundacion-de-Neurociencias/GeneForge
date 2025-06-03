import ply.yacc as yacc
from gfl.lexer import tokens

def p_statement_expr(p):
    '''statement : prime_edit
                 | base_edit
                 | prime_del'''
    p[0] = p[1]

def p_prime_edit(p):
    'prime_edit : PRIME_EDIT LPAREN arguments RPAREN'
    p[0] = ('prime_edit', p[3])

def p_base_edit(p):
    'base_edit : BASE_EDIT LPAREN arguments RPAREN'
    p[0] = ('base_edit', p[3])

def p_prime_del(p):
    'prime_del : PRIME_DEL LPAREN arguments RPAREN'
    p[0] = ('prime_del', p[3])

def p_arguments(p):
    '''arguments : argument
                 | argument COMMA arguments'''
    if len(p) == 2:
        p[0] = dict([p[1]])
    else:
        p[0] = dict([p[1]] + list(p[3].items()))

def p_argument(p):
    'argument : ID EQUALS ID'
    p[0] = (p[1], p[3])

def p_error(p):
    print(f"Syntax error at {p.value!r}")

parser = yacc.yacc()
