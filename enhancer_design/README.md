# Enhancer Design Module

This module allows the generation of synthetic or optimized enhancer sequences to regulate gene expression, using transformer-based architectures and motif-informed models.

## Features

- Generate synthetic DNA enhancers
- Target specific promoters or cell types
- Support transcription factor annotation
- Output ready for integration into GeneForge pipelines

## Example

```python
from enhancer_design.enhancer_generator import generate_enhancer

output = generate_enhancer("MYC", "neuron", ["REST", "SP1"])
print(output)
