# GeneForge

**GeneForge** is a powerful multimodal transformer-based model designed for the **generation, editing, and regulation of genetic sequences**. Originally focused on DNA, GeneForge now supports **DNA, RNA, protein, and enhancer sequence design**, making it a versatile tool for engineering **personalized gene therapies** and **cellular programming** across multiple biological levels.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

GeneForge enables the **in silico design and manipulation** of genetic material, integrating advanced language models, structural biology tools, and regulatory logic. Current capabilities include:

- Prediction of functional impact of SNVs, InDels across DNA, RNA, and protein.
- Splicing and regulatory modeling.
- Design of:
  - **CRISPR guides**, **AAV payloads**, **antisense oligos**, **siRNA**, **mRNA vaccines**.
  - **Protein sequences** and **enzymes** via integration with **ProGen3** and **RFdiffusion2**.
  - **Enhancers** (regulatory DNA) with support for **transcription factor logic** and **cell-specific control**.
- Integration with proteomics tools (e.g., **CHIMERYS**) for experimental validation of expression and function.
- Codon optimization and translation-aware modeling for therapeutic contexts.
- Planning synthetic pathways for aptamers, PNAs, and engineered gene constructs.
- Compatibility with single-cell simulation tools (e.g., **scMultiSim**) for multi-omics and spatial expression analysis.

---

## 📦 Installation

```bash
git clone https://github.com/Fundacion-de-Neurociencias/GeneForge.git
cd GeneForge
pip install -r requirements.txt
````

---

## 🧬 Example Usage

### Generate a therapeutic protein sequence:

```python
from gene_tokenizer.tokenizer import tokenize_sequence
from model.gene_transformer import GeneTransformer

seq = "ATGCGTACGTTAGC..."  # DNA sequence
tokens = tokenize_sequence(seq)
model = GeneTransformer()

prediction = model(tokens)
```

### Design an enhancer targeting EPO in mouse hematopoietic cells:

```yaml
- enhancer:
    name: "Epo_Upregulator"
    target_gene: "EPO"
    cell_type: "hematopoietic_progenitor"
    species: "Mus musculus"
    factors: ["GATA1", "KLF1", "TAL1"]
    goal: "upregulate"
    model: "GeneForgeEnhancerGen-v1"
```

---

## 🏗️ Repository Structure

* `gene_tokenizer/`: Tokenization for DNA, RNA, and protein inputs.
* `model/`: Transformer-based architectures.
* `training/`: Pretraining and fine-tuning workflows.
* `examples/`: Notebooks covering DNA/RNA/protein/enhancer generation and validation.
* `docs/`: Architectural docs and module specifications.
* `enhancer_design/`: Modules and templates for synthetic regulatory element generation.

---

## 📚 Documentation

* `docs/architecture.md`: Core technical documentation.
* `Codon_Optimization_Integration.md`: Codon usage integration.
* `Integration_with_RFdiffusion2.md`: Protein structure-based generation.
* `GeneForge_Harvard_AI_Model_Integration.md`: Integration with Harvard's AI for structural and functional prediction.
* `ProGen3_and_CHIMERYS.md`: Integration for generation + proteomic validation.
* `Enhancer_Module_Spec.md`: Design and deployment of synthetic enhancers.
* `Ensembl_API_Usage.md`: REST-based annotation integration from Ensembl.
* `Integration_with_scMultiSim.md`: Multimodal and spatial simulation workflows.
* `Integration_with_ATOMICA.md`: Protein property prediction with universal representations.

---

## 🧪 Model Version 0.3

This version introduces:

* Full support for enhancer design and regulatory control.
* Protein generation using ProGen3-46B (optional external).
* CHIMERYS integration for PSM quantification.
* Compatibility with GeneForgeLang: a YAML-based language to describe and execute genetic programming workflows.
* Extended functionality for PNA and aptamer modeling.

👉 [Download GeneForge Model v0.3 from Hugging Face](https://huggingface.co/fneurociencias/GeneForge)

---

## 🤝 Contributing

We welcome collaboration from researchers, bioinformaticians, and computational biologists. You can:

* Open issues with suggestions or bug reports.
* Submit pull requests.
* Propose new use cases (e.g., aptamer design, mRNA vaccines, gene circuit simulation).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧠 Project Lead

**GeneForge** is developed by **Fundación de Neurociencias**
Lead Investigator: [Manuel Menéndez González](https://github.com/manuelmenendezg)

