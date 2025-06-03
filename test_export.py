from gfl import parser
from gfl.semantic_validator import validate_ast
from gfl.exporters import ast_to_vcf, ast_to_json, ast_to_gff, ast_to_yaml

code = """
prime_edit(
  target = HBB,
  edit = c20AtoT
)
"""

print("🧪 Generando AST...")
ast = parser.parser.parse(code)

if not ast:
    print("❌ AST nulo.")
    exit(1)

print("✅ AST generado.")

if not validate_ast(ast):
    print("❌ Validación semántica fallida.")
    exit(1)

print("✅ Validación semántica OK.")

vcf = ast_to_vcf(ast)
with open("test_output.vcf", "w", encoding="utf-8") as f:
    f.write(vcf)
print("📤 Exportado a test_output.vcf")

json_str = ast_to_json(ast)
with open("test_output.json", "w", encoding="utf-8") as f:
    f.write(json_str)
print("📤 Exportado a test_output.json")

gff = ast_to_gff(ast)
with open("test_output.gff", "w", encoding="utf-8") as f:
    f.write(gff)
print("📤 Exportado a test_output.gff")

yaml_str = ast_to_yaml(ast)
with open("test_output.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_str)
print("📤 Exportado a test_output.yaml")
