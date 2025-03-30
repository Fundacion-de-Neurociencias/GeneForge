# GeneForge

**GeneForge** is a foundational transformer-based model for genomic sequences. Inspired by large language models (LLMs), it learns the structure and function of genetic code to enable predictive analysis and the in silico design of therapeutic gene sequences.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

GeneForge brings deep learning to the world of genomic medicine. It is trained on DNA/RNA/protein sequences and supports tasks like:

- Predicting functional impact of variants (SNVs, InDels)
- Modeling splicing and regulatory alterations
- Designing CRISPR guides, AAV payloads, and therapeutic oligos
- Personalizing gene therapy to individual genomes

---

## 📦 Installation

To set up the environment:

```bash
git clone https://github.com/Fundacion-de-Neurociencias/GeneForge.git
cd GeneForge
pip install -r requirements.txt
```

---

## 🧬 Example Usage

Example: Predict functional impact of a mutation:

```python
from gene_tokenizer.tokenizer import tokenize_sequence
from model.gene_transformer import GeneTransformer

seq = "ATGCGTACGTTAGC..."
tokens = tokenize_sequence(seq)
model = GeneTransformer()
prediction = model(tokens)
```

You can also explore `examples/inference_predict_variant_effect.ipynb`.

---

## 🏗️ Repository Structure

- `gene_tokenizer/`: k-mer and codon tokenizers
- `model/`: transformer architecture
- `training/`: scripts for pretraining and fine-tuning
- `examples/`: notebooks for real-world use cases
- `docs/`: model documentation and specifications

---

## 📚 Documentation

See [`docs/architecture.md`](docs/architecture.md) for detailed technical explanation.

---

## Model Version 0.1

This is the initial version of GeneForge. The model has been trained on genetic sequences, and you can download it from Hugging Face:

[Download GeneForge model (version 0.1)](https://huggingface.co/fneurociencias/GeneForge)

---

## 🤝 Contributing

Contributions welcome! Feel free to:
- Open issues
- Submit pull requests
- Suggest improvements to model design or training pipeline

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧠 Project Lead

GeneForge is a project by **Fundación de Neurociencias**.  
Lead Investigator: [Manuel Menéndez González](https://github.com/manuelmenendezg)

