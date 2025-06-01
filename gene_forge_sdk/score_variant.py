# gene_forge_sdk/score_variant.py
"""
High-level helper: score a single variant and store/update a gfDB JSON entry.
"""

from pathlib import Path
from typing import Dict
import json

from gfl.parser import GFLParser
from gfl.inference_engine import InferenceEngine
from model.transformer_multimodal import GeneForgeModel

# -- gfDB minimal I/O -------------------------------------------------------
_GFDB_DIR = Path("gfdb/entries")
_GFDB_DIR.mkdir(parents=True, exist_ok=True)


def _entry_path(variant_id: str) -> Path:
    return _GFDB_DIR / f"{variant_id}.json"


def _save_entry(entry: Dict):
    _entry_path(entry["variant"]).write_text(json.dumps(entry, indent=2))
# ---------------------------------------------------------------------------


def score_variant(variant_id: str, gene: str) -> Dict:
    """
    Returns dict:
      variant, gene, confidence, gfdb_entry, gfl_block, explanation
    """
    gfl_block = (
        f"edit(SNP:{variant_id})\n"
        f"target(gene:{gene})\n"
        "effect(function:unknown)\n"
        "simulate(unspecified)\n"
        "link(edit->target)\n"
        "link(target->effect)\n"
        "link(effect->simulate)"
    )

    ast = GFLParser().parse(gfl_block)

    engine = InferenceEngine(GeneForgeModel())
    pred   = engine.predict_effect(ast.to_dict())
    conf   = float(pred.get("confidence", 0.50))

    entry = {
        "variant": variant_id,
        "gene": gene,
        "confidence": conf,
        "gfl": gfl_block.splitlines(),
        "explanation": pred.get("explanation", "Inferred by GeneForge")
    }
    _save_entry(entry)

    return {
        "variant": variant_id,
        "gene": gene,
        "confidence": conf,
        "gfdb_entry": entry,
        "gfl_block": gfl_block,
        "explanation": entry["explanation"]
    }


if __name__ == "__main__":
    print(score_variant("rs1042522", "TP53"))
