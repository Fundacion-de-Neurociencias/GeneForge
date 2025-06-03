from gfl.nodes_extended import RetroviralElement, MitochondrialGene, piRNA, Transposon

print("✅ Test de clases extendidas de GFL\n")

# Retrovirus endógeno
erv = RetroviralElement(locus="chr1:123456-123789", activity="silenced")
print("🔬 RetroviralElement:", erv)

# Gen mitocondrial
mt_gene = MitochondrialGene(name="MT-ND1", function="oxidative_phosphorylation")
print("🔬 MitochondrialGene:", mt_gene)

# piRNA funcional
pi = piRNA(origin_locus="chr2:998877-999999", target="LINE1", mode="silencing")
print("🔬 piRNA:", pi)

# Transposón activo
tp = Transposon(family="Tc1/mariner", insertion_site="chrX:555000", mobility=True)
print("🔬 Transposon:", tp)
