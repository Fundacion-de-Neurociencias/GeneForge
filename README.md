# GeneForge

**GeneForge** is a powerful multimodal transformer-based model designed for the generation and editing of genetic sequences. Originally focused on DNA, **GeneForge** now supports DNA, RNA, and protein sequence design, providing the tools for designing **personalized gene therapies** across multiple biological levels.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

**GeneForge** enables the **in silico** design and generation of **DNA, RNA**, and **protein sequences**. This multimodal framework helps in:

- Predicting the functional impact of variants (SNVs, InDels) at **DNA**, **RNA**, and **protein** levels.
- Modeling splicing and regulatory alterations.
- Designing **CRISPR guides**, **AAV payloads**, **therapeutic oligos**, and **RNA-based therapies**.
- Personalizing gene therapy for individual genomes across all molecular levels.

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

Example: Predict functional impact of a mutation and generate therapeutic sequence:

```python
from gene_tokenizer.tokenizer import tokenize_sequence
from model.gene_transformer import GeneTransformer

seq = "ATGCGTACGTTAGC..."  # Example DNA sequence
tokens = tokenize_sequence(seq)
model = GeneTransformer()

# Generate therapeutic sequence
prediction = model(tokens)
```

You can also explore `examples/inference_predict_variant_effect.ipynb` for more examples.

---

## 🏗️ Repository Structure

- `gene_tokenizer/`: K-mer and codon tokenizers for **DNA** and **RNA** sequences.
- `model/`: Transformer architecture for generating **DNA**, **RNA**, and **protein** sequences.
- `training/`: Scripts for pretraining and fine-tuning the multimodal model.
- `examples/`: Notebooks with real-world use cases, including RNA and protein generation.
- `docs/`: Model documentation, architectural overview, and specifications.

---

## 📚 Documentation

See [`docs/architecture.md`](docs/architecture.md) for detailed technical explanations and multimodal framework insights.

---

## Model Version 0.2

This is the enhanced version (0.2) of **GeneForge**, now supporting **DNA**, **RNA**, and **protein** sequence generation and editing.

You can download the latest model version from **Hugging Face**:

[Download GeneForge Model (version 0.2)](https://huggingface.co/fneurociencias/GeneForge)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues
- Submit pull requests
- Suggest improvements for model design, training pipeline, or multimodal integration

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧠 Project Lead

**GeneForge** is a project by **Fundación de Neurociencias**.  
Lead Investigator: [Manuel Menéndez González](https://github.com/manuelmenendezg)
