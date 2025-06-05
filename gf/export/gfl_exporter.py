def format_value(val):
    if isinstance(val, str):
        return f'"{val}"'
    elif isinstance(val, list):
        return "[" + ", ".join(format_value(v) for v in val) + "]"
    elif isinstance(val, bool):
        return "true" if val else "false"
    elif val is None:
        return "null"
    else:
        return str(val)

def export_node_to_gfl(node, indent=0):
    lines = []
    indent_str = " " * (indent * 4)
    lines.append(f"{indent_str}{node.type} {{")
    for key, value in node.attrs.items():
        lines.append(f"{indent_str}    {key} = {format_value(value)}")
    lines.append(f"{indent_str}}}")
    return "\n".join(lines)

def export_to_gfl(ast):
    if isinstance(ast, list):
        return "\n\n".join(export_node_to_gfl(n) for n in ast)
    else:
        return export_node_to_gfl(ast)
