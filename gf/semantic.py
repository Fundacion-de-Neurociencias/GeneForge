from gf.schema import SCHEMAS

def _validate_node(node):
    node_type = node.type
    attrs = node.attrs

    # Buscar esquema base si no está definido directamente
    schema = SCHEMAS.get(node_type)
    if not schema:
        # Buscar herencia: por ahora, 'enhanced_construct' hereda de 'construct'
        if node_type == "enhanced_construct":
            base_schema = SCHEMAS.get("construct", {})
            extra_schema = SCHEMAS.get("enhanced_construct", {})
            schema = {
                "required": base_schema.get("required", []) + extra_schema.get("required", []),
                "optional": base_schema.get("optional", []) + extra_schema.get("optional", []),
            }
        else:
            raise ValueError(f"Invalid node: {node_type} {{")

    # Validar atributos requeridos
    for key in schema["required"]:
        if key not in attrs:
            raise ValueError(f"Missing required attribute '{key}' in {node_type}")

    # Validar claves no permitidas
    allowed = set(schema["required"] + schema["optional"])
    for key in attrs:
        if key not in allowed:
            raise ValueError(f"Unexpected attribute '{key}' in {node_type}")

def validate_ast(ast):
    for node in ast:
        _validate_node(node)
