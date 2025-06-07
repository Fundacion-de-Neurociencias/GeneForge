def build_ast(tokens):
    ast = []
    subnode_buffer = {}

    for token in tokens:
        if not isinstance(token, dict):
            continue

        node_type = token.get("type")
        attrs = token.get("attrs", {})

        # 🔸 Si es subnodo tipo "clave: tipo"
        if node_type and ":" in node_type:
            key, sub_type = [x.strip() for x in node_type.split(":", 1)]
            subnode_buffer[key] = {
                "type": sub_type,
                "attrs": attrs
            }

        # 🔸 Si es nodo principal
        elif node_type:
            node = {
                "type": node_type,
                "attrs": attrs
            }
            # 💡 Insertamos subnodos guardados
            for key, sub in subnode_buffer.items():
                node["attrs"][key] = sub
            subnode_buffer = {}  # limpiamos

            ast.append(node)

        # 🔸 Ignorar basura
        else:
            continue

    if subnode_buffer:
        raise ValueError("Subnode(s) declared but no parent node found.")

    return ast
