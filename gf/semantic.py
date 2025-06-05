def validate_ast(ast):
    # Validación mínima: asegura que cada nodo tenga tipo y attrs
    if not isinstance(ast, list):
        ast = [ast]
    for node in ast:
        if not hasattr(node, 'type') or not hasattr(node, 'attrs'):
            raise ValueError(f"Invalid node: {node}")
    return ast
