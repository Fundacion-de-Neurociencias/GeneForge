def validate_ast(ast):
    if not ast:
        print("❌ Error: AST nulo.")
        return False

    if isinstance(ast, list):
        for node in ast:
            if not validate_node(node):
                return False
    else:
        if not validate_node(ast):
            return False

    return True


def validate_node(node):
    if not isinstance(node, tuple):
        print("❌ Error: Nodo inválido:", node)
        return False

    node_type, args = node
    if node_type == 'prime_edit':
        if 'target' not in args:
            print("❌ Error: Falta 'target' en prime_edit.")
            return False
    elif node_type == 'base_edit':
        if 'target' not in args or 'deaminase' not in args:
            print("❌ Error: Falta 'target' o 'deaminase' en base_edit.")
            return False
    elif node_type == 'prime_del':
        if 'target' not in args or 'pegRNA_left' not in args or 'pegRNA_right' not in args:
            print("❌ Error: Falta información en prime_del.")
            return False
    elif node_type == 'peg':
        if 'sequence' not in args:
            print("❌ Error: Falta 'sequence' en peg.")
            return False
    elif node_type == 'nick_site':
        if 'position' not in args:
            print("❌ Error: Falta 'position' en nick_site.")
            return False
    elif node_type == 'reverse_transcriptase':
        if 'enzyme' not in args:
            print("❌ Error: Falta 'enzyme' en reverse_transcriptase.")
            return False
    else:
        print(f"❌ Error: Tipo de nodo desconocido '{node_type}'")
        return False

    print(f"✅ {node_type}: validación semántica superada.")
    return True
# Validaciones semánticas ampliadas para entidades genómicas específicas

def validate_piRNA(node):
    if not isinstance(node, dict):
        return False
    return 'target' in node or 'cluster' in node

def validate_transposon(node):
    if not isinstance(node, dict):
        return False
    return 'element_name' in node

def validate_endogenous_retrovirus(node):
    if not isinstance(node, dict):
        return False
    return 'locus' in node or 'activity' in node

def validate_mitochondrial_gene(node):
    if not isinstance(node, dict):
        return False
    return 'gene' in node or 'function' in node
        elif node_type == 'piRNA':
            if not validate_piRNA(data):
                print("❌ piRNA: error de validación.")
                return False
            print("✅ piRNA: validación semántica superada.")

        elif node_type == 'transposon':
            if not validate_transposon(data):
                print("❌ transposon: error de validación.")
                return False
            print("✅ transposon: validación semántica superada.")

        elif node_type == 'endogenous_retrovirus':
            if not validate_endogenous_retrovirus(data):
                print("❌ endogenous_retrovirus: error de validación.")
                return False
            print("✅ endogenous_retrovirus: validación semántica superada.")

        elif node_type == 'mitochondrial_gene':
            if not validate_mitochondrial_gene(data):
                print("❌ mitochondrial_gene: error de validación.")
                return False
            print("✅ mitochondrial_gene: validación semántica superada.")
