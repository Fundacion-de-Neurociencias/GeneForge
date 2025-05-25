# gene_forge_sdk/score_variant.py
"""High‑level helper to score a single variant using GeneForge.

Usage:
    from gene_forge_sdk.score_variant import score_variant
    result = score_variant(variant_id="rs1042522", gene="TP53")
    print(result["confidence"], result["gfdb_entry"])  
"""

from typing import Dict
from pathlib import Path

from gfl.parser import GFLParser
from gfl.inference_engine import InferenceEngine
from model.transformer_multimodal import GeneForgeModel

# --- minimal gfDB client ----------------------------------------------

_GFDB_DIR = Path("gfdb/entries")
_GFDB_DIR.mkdir(parents=True, exist_ok=True)


def _entry_path(variant_id: str) -> Path:
    return _GFDB_DIR / f"{variant_id}.json"


def _save_entry(entry: Dict):
    _entry_path(entry["variant"]).write_text(
        import json as _j; _j.dumps(entry, indent=2)
    )


# -----------------------------------------------------------------------

def score_variant(variant_id: str, gene: str) -> Dict:
    """Return pathogenicity/confidence and gfDB linkage for *variant_id*.
    Args:
        variant_id: e.g. "rs1042522" or "chr17:41276045G>A".
        gene: HGNC gene symbol.
    Returns:
        dict with keys: variant, gene, confidence, gfdb_entry, gfl_block, explanation.
    """
    # 1. Build minimal GFL block
    gfl_block = (
        f"edit(SNP:{variant_id})\n"
        f"target(gene:{gene})\n"
        "effect(function:unknown)\n"
        "simulate(unspecified)\n"
        "link(edit->target)\n"
        "link(target->effect)\n"
        "link(effect->simulate)"
    )

    # 2. Parse to AST
    ast = GFLParser().parse(gfl_block)

    # 3. Predict effect
    engine = InferenceEngine(GeneForgeModel())
    pred   = engine.predict_effect(ast.to_dict())
    conf   = float(pred.get("confidence", 0.5))

    # 4. Create / update gfDB entry
    entry = {
        "variant": variant_id,
        "gene": gene,
        "confidence": conf,
        "gfl": gfl_block.split("\n"),
        "explanation": pred.get("explanation", "Inferred by GeneForge"),
    }
    _save_entry(entry)

    # 5. Assemble response
    return {
        "variant": variant_id,
        "gene": gene,
        "confidence": conf,
        "gfdb_entry": entry,
        "gfl_block": gfl_block,
        "explanation": entry["explanation"],
    }


if __name__ == "__main__":
    test = score_variant("rs1042522", "TP53")
    print(test)
