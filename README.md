# GeneForge

**GeneForge** is a multimodal transformer platform for the **generation, editing and regulation of genetic sequences**. Originally DNA-centric, it now supports **DNA, RNA, protein and enhancer design**, enabling everything from personalised gene therapies to large-scale cellular programming.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview  *(v0.3)*

| Capability | Details |
|------------|---------|
| **Variant impact** | SNVs / InDels across DNA, RNA, protein |
| **Regulatory modelling** | Splicing, TF-logic, enhancer design |
| **Design modules** | CRISPR guides, AAV payloads, antisense, siRNA, mRNA vaccines |
| **Protein / enzyme generation** | ProGen3-46B + RFdiffusion2 integration |
| **Enhancer synthesis** | Cell-type-specific TF logic; codon-aware optimisation |
| **Omics integration** | scMultiSim (single-cell multi-omics & spatial), CHIMERYS proteomics |
| **Pathway planning** | Aptamers, PNAs, synthetic gene constructs |
| **Simulation** | Single-cell & tissue-scale expression dynamics |

---

## 🧬 GeneForgeLang (GFL)

A concise, symbolic language that drives the GeneForge inference engine.

```gfl
edit(SNP:rs1042522)
target(gene:TP53)
effect(function:loss_of_function)
pathway(p53:apoptosis)
link(edit->target)
link(target->effect)
simulate(tumorigenesis)
```

### Quick-start

1. Place `.gfl` files in `gfl/examples/`.
2. `python gfl/parser.py my_example.gfl` → AST.
3. `gfl/inference_engine.py` → effect / off-target prediction.
4. `gfl/validation_pipeline.py` → benchmark with GTEx, TCGA, gnomAD.

### Developer Tools
- AST parser with JSON export
- Unit tests in `tests/test_parser.py`
- GFL-aware interface layer in `model/transformer_multimodal.py`

For full syntax see [`gfl/grammar.md`](./gfl/grammar.md) and [`gfl/syntax.md`](./gfl/syntax.md).

---

## 🧠 gfDB – GeneForge Inferential Knowledge-base

`gfDB` is a **24 / 7 self-updating, probabilistic database** built by reasoning over public omics resources with GFL.

| Key trait | Why it matters |
|-----------|---------------|
| **Inferential** | Generates *new* variant→function→phenotype links |
| **Probabilistic** | Every entry carries a confidence score & traceable evidence |
| **Auto-updating** | Continuously monitors gnomAD, ClinVar, TCGA, GTEx … and re-annotates itself |
| **Semantic** | All facts stored as GFL sentences → instantly usable by the engine |

Example gfDB record:

```json
{
  "id": "gfdb:rs987654",
  "confidence_score": 0.83,
  "gfl": [
    "edit(SNP:rs987654)",
    "target(gene:BRCA2)",
    "effect(function:likely_loss_of_function)",
    "simulate(probable_breast_cancer)"
  ],
  "explanation": "Inferred by similarity to BRCA1 rs1042522 pathogenic variant."
}
```

Daemon script: `gfdb/inference_daemon.py` writes new JSON entries in `gfdb/entries/`.

---

## 📦 Installation

```bash
git clone https://github.com/Fundacion-de-Neurociencias/GeneForge.git
cd GeneForge
pip install -r requirements.txt
```

---

## 🧪 Example Usage

```python
from gfl.parser import GFLParser
from model.transformer_multimodal import GeneForgeModel
from gfl.inference_engine import InferenceEngine

gfl_text = """
edit(SNP:rs1042522)
target(gene:TP53)
effect(function:loss_of_function)
simulate(tumorigenesis)
"""

ast   = GFLParser().parse(gfl_text)
model = GeneForgeModel()
engine = InferenceEngine(model)

print(engine.predict_effect(ast.to_dict()))
```

Interactive exploration: **`notebooks/GFL_sandbox.ipynb`**.

---

## 🏗️ Repository Structure

```
gene_tokenizer/        tokenisers for DNA-RNA-protein
model/                 transformer architectures (GFL-aware)
gfl/                   parser, syntax, examples, validation
gfdb/                  inference daemon + generated entries
integration/           HEVisum connector, omics data loaders
notebooks/             Jupyter sandboxes and tutorials
enhancer_design/       synthetic enhancer module
tests/                 unit tests (e.g., test_parser.py)
docs/                  deep-dive architecture & specs
```

---

## 📚 Key Documentation

* `docs/architecture.md` – core design
* `gfl/grammar.md`, `gfl/syntax.md` – language spec
* `docs/GFL_Manual.md` – user & developer manual
* `Integration_with_RFdiffusion2.md`, `ProGen3_and_CHIMERYS.md` – protein pipelines
* `Integration_with_scMultiSim.md`, `Integration_with_ATOMICA.md` – multi-omics simulations

---

## 🤝 Contributing

We welcome PRs, issues and new use-case proposals (aptamer design, mRNA vaccines, gene-circuit simulation, …).

---

## 📄 License

Released under the [MIT License](LICENSE).

---

## 🧠 Project Lead

**Fundación de Neurociencias**  
Lead Investigator – [Manuel Menéndez González](https://github.com/manuelmenendezg)
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, epeat_edit, isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, epeat_edit, isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, epeat_edit, isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, epeat_edit, isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, epeat_edit, isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, epeat_edit, isk, …).
