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
Se añade motor bayesiano y nuevas construcciones (ector, 
epeat_edit, 
isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, 
epeat_edit, 
isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, 
epeat_edit, 
isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, 
epeat_edit, 
isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, 
epeat_edit, 
isk, …).
### ✨ Mayo 2025
Se añade motor bayesiano y nuevas construcciones (ector, 
epeat_edit, 
isk, …).

---

## ?? Integraci�n de Edici�n Gen�tica

GeneForge ahora reconoce nodos avanzados del lenguaje GFL como:

- `prime_edit(...)`
- `base_edit(...)`
- `prime_del(...)`

Esto permite representar t�cnicas modernas de edici�n gen�tica como prime editing o base editing.

### ?? Cambios relevantes

- `inference_engine.py`: compatibilidad con los nuevos nodos.
- `translate_lstm.py`: modelo stub para eficiencia de traducci�n.
- Documentaci�n: ver `docs/variant_effects_integration.md`.

## ?? GFL Exporter Test Example

You can test the export of genetic nodes to GFL format using the following example:

### Example usage:

`bash
python examples/test_export_gfl.py
`

### Output example:

`
genetic_technique {
    name = \"CRISPR\"
    components = [\"Cas9\", \"sgRNA\"]
    mechanism = \"DSB repair\"
}
`

## ?? GFL Exporter Test Example

You can test the export of genetic nodes to GFL format using the following example:

### Example usage:

``bash
python examples/test_export_gfl.py
``

### Output example:

``
genetic_technique {
    name = "CRISPR"
    components = ["Cas9", "sgRNA"]
    mechanism = "DSB repair"
}
``

## ?? GFL Parser Edge Case Test

This script checks how the GFL parser handles edge cases such as missing attributes, booleans, null values, and syntax errors.

### Example usage:

```bash
python examples/test_edge_cases_gfl.py
Sample output:
pgsql
Copiar
Editar
?? Case 1:
empty_node { }
----------------------------------------

?? Case 2:
incomplete_node { key = }
----------------------------------------

?? Case 3:
logic_node { flag = true, debug = false, fallback = null }
----------------------------------------

?? Case 4:
list_node { items = [] }
----------------------------------------

?? Case 5:
bad_syntax_node { key == "value" }
----------------------------------------

## ?? GFL Custom Node Test

This script demonstrates how to define and roundtrip a custom node class using the GFL format.

### Example usage:

```bash
python examples/test_custom_nodes_gfl.py
Sample output:
csharp
Copiar
Editar
?? Exported GFL:

my_custom_node {
    label = "test_node"
    params = {"x": 1, "y": 2}
}

?? Re-importing...

? Parsed node:

?? my_custom_node - {'label': 'test_node', 'params': {'x': 1, 'y': 2}}

## ?? GFL Custom Node Test

This script demonstrates how to define and roundtrip a custom node class using the GFL format.

### Example usage:

```bash
python examples/test_custom_nodes_gfl.py
Sample output:
csharp
Copiar
Editar
?? Exported GFL:

my_custom_node {
    label = "test_node"
    params = {"x": 1, "y": 2}
}

?? Re-importing...

? Parsed node:

?? my_custom_node - {'label': 'test_node', 'params': {'x': 1, 'y': 2}}

## ?? GFL Custom Node Test

This script demonstrates how to define and roundtrip a custom node class using the GFL format.

### Example usage:

python examples/test_custom_nodes_gfl.py

### Sample output:

?? Exported GFL:

my_custom_node {
    label = "test_node"
    params = {"x": 1, "y": 2}
}

?? Re-importing...

? Parsed node:

?? my_custom_node - {'label': 'test_node', 'params': {'x': 1, 'y': 2}}

## [2025-06-07] Recent Updates

- All code and documentation are maintained strictly in English.
- Latest pipeline includes ASCII-cleaning for GFL input files, structured parsing, and probabilistic reasoning steps.
- Parsing and reasoning scripts are provided in Python, with clear input/output conventions.
- Repository synchronization scripts are available for automated version control.
- For any questions, please refer to the /docs directory or contact the project maintainer.

---

**Update Policy:**  
All further documentation, code comments, and docstrings must be written in English.  
Do not use Spanish or any other language for internal documentation under any circumstances.
## [2025-06-07] Recent Updates

- All code and documentation are maintained strictly in English.
- Latest pipeline includes ASCII-cleaning for GFL input files, structured parsing, and probabilistic reasoning steps.
- Parsing and reasoning scripts are provided in Python, with clear input/output conventions.
- Repository synchronization scripts are available for automated version control.
- For any questions, please refer to the /docs directory or contact the project maintainer.

---

**Update Policy:**  
All further documentation, code comments, and docstrings must be written in English.  
Do not use Spanish or any other language for internal documentation under any circumstances.
