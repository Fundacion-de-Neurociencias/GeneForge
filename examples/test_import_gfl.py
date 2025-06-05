from gf.gfl_import.gfl_importer import load_gfl_file

# Ruta al archivo GFL de ejemplo
path = 'examples/test_extended_semantics.gfl'

try:
    ast = load_gfl_file(path)
    print('✅ Nodes parsed and validated:\n')
    for node in ast:
        print(f'🔹 {node.type} - {node.attrs}')
except Exception as e:
    print(f'❌ Error: {e}')
