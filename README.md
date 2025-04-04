### **1. Actualización del Nombre:**

El nombre **GeneForge** sigue siendo adecuado para este tipo de enfoque **multimodal**, ya que refleja la idea de **"forjar"** secuencias genéticas. Sin embargo, si queremos reflejar de forma más explícita el hecho de que estamos trabajando con **DNA**, **RNA**, y **proteínas**, podríamos considerar nombres como:

- **GeneForge-X** (donde "X" puede hacer referencia a la inclusión de RNA y proteínas)
- **GeneFusion** (enfatizando la **fusión** de diferentes modalidades: DNA, RNA y proteínas)
- **MultiGeneForge** (enfatizando el enfoque **multimodal**)
- **GeneMeld** (resaltando la **integración** de niveles genéticos, transcriptómicos y proteómicos)

**Recomendación**: Si no consideras que el cambio de nombre sea necesario para la fase actual, lo ideal sería mantener **GeneForge** y hacer énfasis en la **actualización multimodal** en la documentación.

---

### **2. Documentación Actualizada del README:**

Una vez hayas decidido si mantienes el nombre o no, podemos **actualizar el archivo README** con toda la información sobre las nuevas capacidades de **GeneForge**. A continuación, te proporciono una **estructura sugerida** para el archivo README en **Markdown**:

---

```markdown
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

```

---

### **3. Other Documentation Updates:**

1. **Update `docs/architecture.md`**: Expand the document to include details about how **GeneForge** has expanded from a **DNA-only model** to a **multimodal model** supporting **RNA** and **proteins**.
2. **Add Examples**: Include example notebooks and code for **RNA** and **protein sequence generation** alongside the existing **DNA** examples.

---

### **4. Other Considerations:**

- If you are using **RNA** and **protein sequences**, you might need additional datasets and models to train these components effectively. Consider referencing or integrating existing **public datasets** such as **RNA-seq** data or **protein structure databases**.
  
- **Future Steps**: As you plan for **commercial versions** (after the open-source release), you might want to add more **advanced features** related to **RNA-editing technologies**, **protein folding prediction**, or **real-time clinical application testing**.
