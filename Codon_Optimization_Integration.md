# GeneForge

**GeneForge** is a powerful multimodal transformer-based model designed for the generation and editing of genetic sequences. Initially focused on **DNA**, **GeneForge** now supports **DNA**, **RNA**, and **protein** sequence design, providing tools for creating **personalized gene therapies** across multiple biological levels.

With the integration of **codon optimization**, **GeneForge** is now capable of designing optimized **DNA, RNA**, and **protein sequences** that ensure **more efficient gene expression**, **stability**, and **therapeutic outcomes**.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

**GeneForge** enables the **in silico** design and generation of **DNA**, **RNA**, and **protein sequences**. This multimodal framework helps in:

- Predicting the functional impact of variants (SNVs, InDels) at **DNA**, **RNA**, and **protein** levels.
- Modeling splicing and regulatory alterations.
- Designing **CRISPR guides**, **AAV payloads**, **therapeutic oligos**, and **RNA-based therapies**.
- Personalizing gene therapy for individual genomes across all molecular levels.
- **Codon optimization** to improve the efficiency and stability of the gene sequences, ensuring better **protein synthesis** and **therapeutic outcomes**.

---

## 📦 Installation

To set up the environment and install **GenoML** and the codon optimization model, follow these steps:

```bash
git clone https://github.com/Fundacion-de-Neurociencias/GeneForge.git
cd GeneForge
pip install -r requirements.txt
pip install genoML
pip install codon-optimizer
```

---

## 🧬 Example Usage

Example: Predict functional impact of a mutation and generate optimized therapeutic sequence:

```python
from gene_tokenizer.tokenizer import tokenize_sequence
from model.gene_transformer import GeneTransformer
import codon_optimizer

# Example DNA sequence
seq = "ATGCGTACGTTAGC..."

# Preprocess the sequence using GenoML for improved input
preprocessed_data = genoML.preprocess(seq)

# Tokenize the sequence for GeneForge
tokens = tokenize_sequence(preprocessed_data)
model = GeneTransformer()

# Generate therapeutic sequence
generated_sequence = model(tokens)

# Optimize codon usage for the generated sequence
optimized_sequence = codon_optimizer.optimize(generated_sequence)

print("Optimized Gene Sequence:", optimized_sequence)
```

Explore `examples/inference_predict_variant_effect.ipynb` for more examples.

---

## 🏗️ Repository Structure

- `gene_tokenizer/`: K-mer and codon tokenizers for **DNA** and **RNA** sequences.
- `model/`: Transformer architecture for generating **DNA**, **RNA**, and **protein** sequences.
- `training/`: Scripts for pretraining and fine-tuning the multimodal model.
- `examples/`: Notebooks with real-world use cases, including RNA and protein generation.
- `docs/`: Model documentation, architectural overview, and specifications.
- `codon_optimizer/`: Codon optimization library for improving gene expression and protein synthesis.

---

## 📚 Documentation

See [`docs/architecture.md`](docs/architecture.md) for detailed technical explanations and multimodal framework insights.

---

## **Model Version 0.3**

This is the enhanced version (0.3) of **GeneForge**, now supporting **DNA**, **RNA**, and **protein** sequence generation and editing with **codon optimization** for better gene expression and therapy outcomes.

You can download the latest model version from **Hugging Face**:

[Download GeneForge Model (version 0.3)](https://huggingface.co/fneurociencias/GeneForge)

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

---

## 🚀 Codon Optimization Integration

We have integrated **codon optimization** into **GeneForge** to enhance the efficiency and stability of the gene sequences it generates. Codon optimization is an essential step in ensuring that **RNA** and **protein sequences** are efficiently translated in therapeutic applications.

### **What Codon Optimization Adds to GeneForge**:

1. **Improved Gene Expression**: Codon optimization ensures that the generated **RNA** and **protein sequences** are more efficiently expressed in biological systems, which is essential for therapeutic purposes.
2. **Protein Synthesis Efficiency**: It optimizes **codon usage** to match the preferred codon usage of highly expressed genes in the target organism.
3. **Enhanced Protein Stability**: Optimized sequences lead to **more stable proteins**, reducing the risk of misfolding or degradation in therapeutic applications.
4. **Customizing Therapies**: With **codon optimization**, **GeneForge** can design therapies that ensure high **protein production rates** and improved **functional outcomes**.

### **How to Use Codon Optimization with GeneForge**:

1. **Install Codon Optimization**:
   ```bash
   pip install codon-optimizer
   ```

2. **Preprocess Data**:
   Use **GenoML’s preprocessing functions** to clean and format genomic sequences before passing them into **GeneForge** for further analysis.

   ```python
   import genoML

   # Example RNA sequence
   seq = "AUGCGUAUCGAU..."

   # Preprocess using GenoML
   preprocessed_data = genoML.preprocess(seq)
   ```

3. **Generate Sequences**:
   After preprocessing, use **GeneForge's models** to generate **DNA**, **RNA**, or **protein** sequences.

   ```python
   from gene_tokenizer.tokenizer import tokenize_sequence
   from model.gene_transformer import GeneTransformer

   tokens = tokenize_sequence(preprocessed_data)
   model = GeneTransformer()

   # Generate therapeutic sequence
   generated_sequence = model(tokens)
   ```

4. **Optimize and Evaluate**:
   **Codon optimization** will help tune the sequence for better **protein synthesis** and **stability**.

   ```python
   import codon_optimizer

   # Optimize the generated sequence
   optimized_sequence = codon_optimizer.optimize(generated_sequence)

   print("Optimized Gene Sequence:", optimized_sequence)
   ```

### **Documentation**:
Refer to the **codon optimizer** documentation for more details on how to use the tool and integrate it into your workflows.

This integration allows **GeneForge** to become more **user-friendly** and **powerful**, enabling the design and editing of **DNA**, **RNA**, and **protein sequences** for more personalized and effective gene therapies.
```

---

### **What This Documentation Includes**:
1. **Codon Optimization**: The section explains how **codon optimization** enhances **GeneForge**'s ability to generate **efficient RNA** and **protein sequences** for therapeutic use.
2. **Installation**: It includes instructions on how to install the **codon optimization package** and how to integrate it into the **GeneForge** workflow.
3. **Example Code**: Provides clear examples of how to use the optimization feature with **GeneForge**.
4. **Enhanced Functionality**: Highlights the importance of optimizing codons for **gene expression** and **protein stability**, improving therapeutic outcomes.
