import sys
from gf.gfl_import.gfl_importer import load_gfl_string

def main():
    if len(sys.argv) < 2:
        print("❌ Debes proporcionar el nombre del archivo GFL como argumento.")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        sys.exit(1)

    try:
        print("🔍 Splitting code...")
        lines = code.splitlines()
        print(f"🔍 Lines: {lines}")

        from gf.parser import parse_tokens
        ast = parse_tokens(lines)

        print("✅ AST generado:\n")
        import pprint
        pprint.pprint(ast, sort_dicts=False)

    except Exception as e:
        print(f"❌ Error al parsear: {e}")

if __name__ == "__main__":
    main()
