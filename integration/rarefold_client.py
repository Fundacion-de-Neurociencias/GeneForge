"""Lightweight client for RareFold API (non-canonical amino acids design).
Usage:
    from integration.rarefold_client import rarefold_predict
    pdb_or_fasta = rarefold_predict(sequence)
"""
import requests, json
RAREFOLD_EP = "https://rarefold.ai/api/v1/predict"  # placeholder

def rarefold_predict(seq: str, timeout: int = 60):
    payload = {"sequence": seq}
    r = requests.post(RAREFOLD_EP, json=payload, timeout=timeout)
    r.raise_for_status()
    return r.json()  # expects {"pdb": "...", "score": 0.87}
