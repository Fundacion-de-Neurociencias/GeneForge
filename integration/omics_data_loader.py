# integration/omics_data_loader.py

"""
Omics Data Loader
------------------
Utility functions for loading and mapping external multi-omics datasets (e.g., GTEx, gnomAD, TCGA, Ensembl)
into formats compatible with GeneForgeLang validation and prediction workflows.
"""

import pandas as pd
from typing import Optional

class OmicsDataLoader:
    def __init__(self, gtex_path=None, gnomad_path=None, tcga_path=None):
        self.gtex_path = gtex_path or "data/gtex_expression.tsv"
        self.gnomad_path = gnomad_path or "data/gnomad_variants.tsv"
        self.tcga_path = tcga_path or "data/tcga_phenotypes.tsv"

    def load_gtex_expression(self) -> pd.DataFrame:
        """Load GTEx gene expression data."""
        return pd.read_csv(self.gtex_path, sep='\t')

    def load_gnomad_variants(self) -> pd.DataFrame:
        """Load gnomAD variant annotations."""
        return pd.read_csv(self.gnomad_path, sep='\t')

    def load_tcga_phenotypes(self) -> pd.DataFrame:
        """Load phenotype-level data from TCGA."""
        return pd.read_csv(self.tcga_path, sep='\t')

    def get_expression_for_gene(self, gene: str, tissue: Optional[str] = None) -> pd.Series:
        df = self.load_gtex_expression()
        if tissue:
            df = df[df["Tissue"] == tissue]
        return df[df["Gene"] == gene].set_index("Tissue").iloc[:, 1:]

    def get_variant_annotation(self, variant_id: str) -> Optional[dict]:
        df = self.load_gnomad_variants()
        row = df[df["Variant"] == variant_id]
        return row.iloc[0].to_dict() if not row.empty else None

    def get_tcga_phenotype_by_sample(self, sample_id: str) -> Optional[dict]:
        df = self.load_tcga_phenotypes()
        row = df[df["SampleID"] == sample_id]
        return row.iloc[0].to_dict() if not row.empty else None


# Example usage:
if __name__ == "__main__":
    loader = OmicsDataLoader()
    print("--- GTEx: Expression of TP53 in Brain ---")
    print(loader.get_expression_for_gene("TP53", tissue="Brain"))

    print("--- gnomAD: Variant rs1042522 ---")
    print(loader.get_variant_annotation("rs1042522"))

    print("--- TCGA: Sample TCGA-AB-1234 ---")
    print(loader.get_tcga_phenotype_by_sample("TCGA-AB-1234"))
