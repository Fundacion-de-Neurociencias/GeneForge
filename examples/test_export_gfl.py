from gf.genetics.nodes_genetics import GeneticTechnique
from gf.export.gfl_exporter import export_to_gfl

obj = GeneticTechnique(name="CRISPR", components=["Cas9", "sgRNA"], mechanism="DSB repair")
print(export_to_gfl(obj))
