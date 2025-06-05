from gf.core import Node

def _convert_value(val):
    if isinstance(val, str):
        if val.isdigit():
            return int(val)
        try:
            return float(val)
        except ValueError:
            return val
    elif isinstance(val, list):
        return [_convert_value(item) for item in val]
    elif isinstance(val, dict):
        return {k: _convert_value(v) for k, v in val.items()}
    return val

def build_ast(parsed_tokens):
    nodes = []
    for token in parsed_tokens:
        node_type = token['type']
        raw_attrs = token.get('attrs', {})
        converted_attrs = {k: _convert_value(v) for k, v in raw_attrs.items()}
        nodes.append(Node(type=node_type, attrs=converted_attrs))
    return nodes
