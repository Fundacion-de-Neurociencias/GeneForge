from gf.core import Node

def parse_tokens(tokens):
    ast = []
    current_node = None

    for line in tokens:
        if line.endswith('{'):
            node_type = line[:-1].strip()
            current_node = Node(node_type)
        elif line == '}':
            if current_node:
                ast.append(current_node)
                current_node = None
        elif '=' in line and current_node:
            key, val = [part.strip() for part in line.split('=', 1)]

            # Detectar tipo de valor
            if val.startswith('[') and val.endswith(']'):
                val = [v.strip().strip('\"') for v in val[1:-1].split(',')]
            elif val.startswith('\"') and val.endswith('\"'):
                val = val[1:-1]
            elif val == "true":
                val = True
            elif val == "false":
                val = False
            elif val == "null":
                val = None

            current_node.attrs[key] = val

    return ast
