def validate_ast(ast):
    if not isinstance(ast, list):
        print("❌ AST is not a list.")
        return False

    for node in ast:
        if not isinstance(node, tuple) or len(node) != 2:
            print(f"❌ Invalid node format: {node}")
            return False

        node_type, attributes = node
        if not isinstance(attributes, dict):
            print(f"❌ Attributes must be a dict in node: {node}")
            return False

        if node_type == 'pirna':
            if 'target' not in attributes or 'cluster' not in attributes:
                print(f"❌ Missing fields in pirna node: {attributes}")
                return False

        elif node_type == 'transposon':
            if 'element_name' not in attributes:
                print(f"❌ Missing 'element_name' in transposon node: {attributes}")
                return False

        elif node_type == 'endogenous_retrovirus':
            if 'locus' not in attributes or 'activity' not in attributes:
                print(f"❌ Missing fields in endogenous_retrovirus node: {attributes}")
                return False

        elif node_type == 'mitochondrial_gene':
            if 'gene' not in attributes or 'function' not in attributes:
                print(f"❌ Missing fields in mitochondrial_gene node: {attributes}")
                return False

        else:
            print(f"❌ Unknown node type: {node_type}")
            return False

    return True
