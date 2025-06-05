from gf.genetics.nodes_genetics import GeneticTechnique
from gf.export.gfl_exporter import export_to_gfl
from gf.gfl_import.gfl_importer import load_gfl_string

# Crear nodo original
original = GeneticTechnique(name="CRISPR", components=["Cas9", "sgRNA"], mechanism="DSB repair")

# Exportar a string GFL
gfl_string = export_to_gfl(original)
print("🔁 Exported GFL:\n")
print(gfl_string)

# Reimportar desde string
print("\n🔁 Re-importing...\n")
reimported = load_gfl_string(gfl_string)

# Mostrar comparación
print("✅ Roundtrip comparison:\n")
for node in reimported:
    print(f"🔹 {node.type} - {node.attrs}")
