# gfdb/inference_daemon.py
"""
Continuous daemon that:
  1. Monitors external variant databases (e.g., gnomAD).
  2. Builds GFL representations for new variants.
  3. Runs GeneForge inference to predict functional impact.
  4. Writes probabilistic entries into gfDB (JSON files).
"""

import time, json
from datetime import datetime
from pathlib import Path

from gfl.parser import GFLParser
from gfl.inference_engine import InferenceEngine
from integration.omics_data_loader import OmicsDataLoader
from model.transformer_multimodal import GeneForgeModel


class GFDBDaemon:
    def __init__(self, check_interval=3600):
        self.parser = GFLParser()
        self.model = GeneForgeModel()
        self.engine = InferenceEngine(self.model)
        self.loader = OmicsDataLoader()
        self.check_interval = check_interval          # seconds
        self.out_dir = Path("gfdb/entries")
        self.out_dir.mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------
    def monitor_and_infer(self):
        while True:
            print("[gfDB] Cycle start:", datetime.utcnow().isoformat())
            # For demo: sample 5 variants from gnomAD TSV
            sample = self.loader.load_gnomad_variants().sample(5)

            for _, row in sample.iterrows():
                var_id = row["Variant"]
                gene   = row.get("Gene", "UNKNOWN")

                gfl_text = f"""
                edit(SNP:{var_id})
                target(gene:{gene})
                effect(function:unknown)
                simulate(unspecified)
                link(edit->target)
                link(target->effect)
                link(effect->simulate)
                """

                ast = self.parser.parse(gfl_text)
                prediction = self.engine.predict_effect(ast.to_dict())

                entry = {
                    "id": f"gfdb:{var_id}",
                    "source": "gnomAD",
                    "inferred_by": "GeneForgeLang_v1.3",
                    "confidence_score": prediction.get("confidence", 0.50),
                    "status": "inferred",
                    "created_at": datetime.utcnow().isoformat() + "Z",
                    "last_updated": datetime.utcnow().isoformat() + "Z",
                    "gfl": [l.strip() for l in gfl_text.strip().splitlines() if l.strip()],
                    "links": [
                        {"from": "edit",   "to": "target"},
                        {"from": "target", "to": "effect"},
                        {"from": "effect", "to": "simulate"}
                    ],
                    "evidence": [],
                    "explanation": f"Auto-inferred using similarity patterns for gene {gene}.",
                    "tags": ["auto_generated"]
                }

                out_file = self.out_dir / f"{var_id}.json"
                with out_file.open("w") as f:
                    json.dump(entry, f, indent=2)

            print("[gfDB] Cycle complete. Sleeping", self.check_interval, "s")
            time.sleep(self.check_interval)


if __name__ == "__main__":
    GFDBDaemon().monitor_and_infer()
