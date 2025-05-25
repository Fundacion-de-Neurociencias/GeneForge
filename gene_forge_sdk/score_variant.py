# gene_forge_sdk/score_variant.py
"""
High-level helper to score a single variant with GeneForge.
"""

from typing import Dict
from pathlib import Path
import json                                # ✅ importa aquí, no dentro de la llamada

from gfl.parser import GFLParser
from gfl.inference_engine import InferenceEngine
from model.transformer_multimodal import GeneForgeModel

# ---------- minimal gfDB client ------------------------------------------
_GFDB_DIR = Path("gfdb/entries")
_GFDB_DIR.mkdir(parents=True, exist_ok=True)


def _entry_path(variant_id: str) -> Path:
    return _GFDB_DIR / f"{variant_id}.json"


def _save_entry(entry: Dict):
    _entry_path(entry["variant"]).write_text(
        json.dumps(entry, indent=2)        # ✅ ahora es sintaxis correcta
    )


# -------------------------------------------------------------------------


def score_variant(variant_id: str, gene: str) -> Dict:
    """
    Returns pathogenicity/confidence and gfDB linkage for *variant_id*.
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
    conf   = float(pred.get("confidence", 0.5))

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
