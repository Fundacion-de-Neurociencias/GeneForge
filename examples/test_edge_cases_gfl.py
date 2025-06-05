from gf.gfl_import.gfl_importer import load_gfl_string

cases = [
    # Caso 1: Nodo sin atributos
    'empty_node { }',

    # Caso 2: Atributo sin valor
    'incomplete_node { key = }',

    # Caso 3: Booleanos y nulos
    'logic_node { flag = true, debug = false, fallback = null }',

    # Caso 4: Lista vacía
    'list_node { items = [] }',

    # Caso 5: Error de sintaxis
    'bad_syntax_node { key == "value" }'
]

for i, case in enumerate(cases, start=1):
    print(f"\n🔍 Case {i}:\n{case}\n{'-'*40}")
    try:
        result = load_gfl_string(case)
        for node in result:
            print(f"✅ Parsed: {node.type} - {node.attrs}")
    except Exception as e:
        print(f"❌ Error: {e}")
