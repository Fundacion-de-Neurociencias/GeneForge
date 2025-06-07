import sys
from gf.utils.gfl_fix import fix_gfl_file
from gf.parser import parse_tokens
from gfl.inference_engine import run

if __name__ == "__main__":
    filename = sys.argv[1]
    fixed_lines = fix_gfl_file(filename)
    ast = parse_tokens(fixed_lines)
    print("✅ AST listo. Ejecutando...\n")
    result = run(ast)
    print("🎯 Resultado:", result)
