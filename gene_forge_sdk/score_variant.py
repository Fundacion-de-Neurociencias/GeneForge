# gene_forge_sdk/score_variant.py
"""
High-level helper: given a variant ID and its gene symbol, it
  • builds a minimal GFL block
  • parses it to an AST
  • runs GeneForge inference
  • stores / updates a gfDB JSON entry
  • returns a dictionary ready for API / UI use
"""

from pathlib import Path
from typing import Dict
import json

from gfl.parser import GFLParser
from gfl.inference_engine import InferenceEngine
from model.transformer_multimodal import GeneForgeModel

# ---------------------------------------------------------------------- #
# Minimal on-disk gfDB client (writes JSON files into gfdb/entries/)
# ---------------------------------------------------------------------- #
_GFDB_DIR = Path("gfdb/entries")
_GFDB_DIR.mkdir(parents=True, exist_ok=True)


def _entry_path(variant_id: str) -> Path:
    """Return path where the JSON entry will be stored."""
    return _GFDB_DIR / f"{variant_id}.json"


def _save_entry(entry: Dict):
    """Write the entry as pretty-printed JSON."""
    _entry_path(entry["variant"]).write_text(json.dumps(entry, indent=2))


# ---------------------------------------------------------------------- #
# Main scoring helper
# ---------------------------------------------------------------------- #
def score_variant(variant_id: str, gene: str) -> Dict:
    """
    Args:
        variant_id: e.g. 'rs1042522'
        gene:       e.g. 'TP53'
    Returns:
        dict with keys:
          - variant, gene
          - confidence  (float)
          - gfdb_entry  (dict)
          - gfl_block   (str)
          - explanation (str)
    """
    # 1 ─ Compose a minimal GFL description
    gfl_block = (
        f"edit(SNP:{variant_id})\n"
        f"target(gene:{gene})\n"
        "effect(function:unknown)\n"
        "simulate(unspecified)\n"
        "link(edit->target)\n"
        "lin
